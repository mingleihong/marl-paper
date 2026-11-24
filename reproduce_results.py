"""Recompute the manuscript's descriptive comparisons from saved HARL runs."""

import argparse
import csv
import json
import math
import statistics as stats
from collections import defaultdict
from pathlib import Path


BUDGET = 10_000_000
LATE_START = 9_000_000
TASKS = {
    "Ant-v2-4x2": ("Ant 4x2", 4),
    "HalfCheetah-v2-2x3": ("HalfCheetah 2x3", 2),
    "HalfCheetah-v2-6x1": ("HalfCheetah 6x1", 6),
    "Humanoid-v2-17x1": ("Humanoid 17x1", 17),
    "Walker2d-v2-6x1": ("Walker2d 6x1", 6),
    "manyagent_swimmer-10x2": ("ManyAgentSwimmer 10x2", 10),
    "simple_reference_v2-continuous": ("Simple Reference", 2),
    "simple_spread_v2-continuous": ("Simple Spread", 10),
    "25m": ("25m", 25),
    "27m_vs_30m": ("27m vs 30m", 27),
    "6h_vs_8z": ("6h vs 8z", 6),
    "corridor": ("Corridor", 6),
}


def load_runs(root):
    groups = defaultdict(list)
    for config_path in sorted(root.glob("*/*/happo/*/*/config.json")):
        config = json.loads(config_path.read_text())
        metadata = config.pop("main_args")
        args = config["algo_args"]
        beta = args["algo"].pop("prefix_reg_coef", 0)
        seed = args["seed"].pop("seed")
        suite, task, _ = config_path.relative_to(root).parts[:3]
        if metadata["algo"] != "happo" or metadata["env"] != suite:
            raise ValueError(f"Unexpected run metadata: {config_path}")
        if task not in TASKS or args["train"]["num_env_steps"] != BUDGET:
            continue
        progress_path = config_path.with_name("progress.txt")
        if not progress_path.is_file():
            continue
        with progress_path.open() as handle:
            progress = [tuple(map(float, row)) for row in csv.reader(handle) if row]
        if not progress:
            continue
        key = (suite, task, json.dumps(config, sort_keys=True))
        groups[key].append((beta, seed, progress, config_path))
    return groups


def verified_curve(run, suite):
    _, _, progress, config_path = run
    summary = json.loads((config_path.parent / "logs" / "summary.json").read_text())
    metric = "eval_win_rate" if suite == "smac" else "eval_average_episode_rewards"
    curves = [records for key, records in summary.items() if key.endswith(f"/{metric}/{metric}")]
    if len(curves) != 1 or len(curves[0]) != len(progress):
        raise ValueError(f"Evaluation series mismatch: {config_path}")
    step_values = [(int(row[0]), row[2] if suite == "smac" else row[1]) for row in progress]
    for (step, value), (_, logged_step, logged_value) in zip(step_values, curves[0]):
        if step != logged_step or not math.isclose(value, logged_value, rel_tol=2e-6, abs_tol=1e-7):
            raise ValueError(f"Evaluation value mismatch at {step}: {config_path}")
    if any(right <= left for (left, _), (right, _) in zip(step_values, step_values[1:])):
        raise ValueError(f"Nonincreasing evaluation steps: {config_path}")
    return [(step, value * (100 if suite == "smac" else 1)) for step, value in step_values]


def summarize(curve):
    late = stats.mean(value for step, value in curve if step > LATE_START)
    area = sum((right - left) * (y0 + y1) / 2 for (left, y0), (right, y1) in zip(curve, curve[1:]))
    return late, area / (curve[-1][0] - curve[0][0])


def comparisons(groups, root):
    for (suite, task, encoded), runs in sorted(groups.items()):
        algo = json.loads(encoded)["algo_args"]
        if algo["algo"]["action_aggregation"] != "prod" or algo["algo"]["share_param"]:
            continue
        complete = defaultdict(dict)
        for run in runs:
            beta, seed, progress, _ = run
            if progress[-1][0] != BUDGET:
                continue
            if seed in complete[beta]:
                complete[beta][seed] = None
            else:
                complete[beta][seed] = run
        for beta, regularized in sorted(complete.items()):
            if beta == 0:
                continue
            pairs = sorted(set(regularized) & set(complete[0]))
            pairs = [seed for seed in pairs if regularized[seed] and complete[0][seed]]
            if not pairs:
                continue
            curves = {0: [], beta: []}
            for seed in pairs:
                baseline, candidate = complete[0][seed], regularized[seed]
                left, right = verified_curve(baseline, suite), verified_curve(candidate, suite)
                if [step for step, _ in left] != [step for step, _ in right]:
                    raise ValueError(f"Evaluation grid mismatch: {task}, {seed}, {beta}")
                curves[0].append(left)
                curves[beta].append(right)
                print(task, beta, seed, baseline[3].relative_to(root), candidate[3].relative_to(root), sep="\t")
            yield suite, task, algo, beta, pairs, curves


def write_curve_panel(output, name, curves, ticks, ylabel):
    """Write one TikZ panel with thin seed curves and thick group means."""
    if any([step for step, _ in c] != [step for step, _ in curves[0][0]]
           for series in curves.values() for c in series):
        raise ValueError(f"Cannot average different evaluation grids in {name}")
    commands = [
        rf"\begin{{tikzpicture}}[x=0.225in,y=1.25in,font=\scriptsize]",
        r"\path[use as bounding box] (-1.6,-.28) rectangle (10.25,1.08);",
    ]
    ymin, ymax = ticks[0], ticks[-1]

    def scaled(value):
        return (value - ymin) / (ymax - ymin)

    for tick in ticks:
        height = scaled(tick)
        commands.append(rf"\draw[gray!26] (0,{height:.5f}) -- (10,{height:.5f});")
        commands.append(rf"\node[left] at (0,{height:.5f}) {{{tick}}};")
    for tick in range(0, 11, 2):
        commands.append(rf"\node[below] at ({tick},0) {{{tick}}};")
    commands.extend([
        r"\draw[thin] (0,1) -- (0,0) -- (10,0);",
        r"\node at (5,-.2) {Environment steps (millions)};",
        rf"\node[rotate=90] at (-1.38,.5) {{{ylabel}}};",
        r"\begin{scope}\clip (0,0) rectangle (10,1);",
    ])

    def draw(curve, style):
        points = " ".join(f"({step / 1_000_000:.4f},{scaled(value):.5f})"
                          for step, value in curve)
        commands.append(rf"\draw[{style}] plot coordinates {{{points}}};")

    means = []
    for color, series in zip(("baselinecurve", "regcurve"), curves.values()):
        for curve in series:
            draw(curve, f"{color}!20,very thin")
        mean = [(points[0][0], stats.mean(value for _, value in points))
                for points in zip(*series)]
        means.append((color, mean))
    for color, mean in means:
        style = "densely dashed" if color == "baselinecurve" else "solid"
        draw(mean, f"{color},thick,{style}")
    commands.extend([r"\end{scope}", r"\end{tikzpicture}"])
    (output / f"{name}_curves.tex").write_text("\n".join(commands) + "\n")


def write_outputs(groups, root, output):
    rows, paired, hyperparameters = [], [], {}
    output.mkdir(exist_ok=True, parents=True)
    for suite, task, algo, beta, seeds, curves in comparisons(groups, root):
        entropy = algo["algo"]["entropy_coef"]
        if task == "Humanoid-v2-17x1" and entropy == 0.001 and beta == 0.01 and len(seeds) == 5:
            write_curve_panel(output, "humanoid", curves, [-2000, 0, 2000, 4000, 6000, 8000], "Evaluation return")
        if task == "27m_vs_30m" and beta == 0.1 and len(seeds) == 5:
            write_curve_panel(output, "smac", curves, [0, 20, 40, 60, 80, 100], r"Evaluation win rate (\%)")
        label, agents = TASKS[task]
        baseline = [summarize(c) for c in curves[0]]
        candidate = [summarize(c) for c in curves[beta]]
        bl, ba = map(list, zip(*baseline))
        rl, ra = map(list, zip(*candidate))
        delta = [right - left for left, right in zip(bl, rl)]
        cells = [label, f"{entropy:g}", f"{beta:g}", str(len(seeds))]
        decimals = 1 if suite == "smac" or "mpe" in suite or "swimmer" in task else 0
        def fmt(values):
            mean = f"{stats.mean(values):.{decimals}f}"
            return mean if len(values) == 1 else f"{mean} $\\pm$ {stats.stdev(values):.{decimals}f}"
        cells += [fmt(bl), fmt(rl), f"{stats.mean(delta):+.{decimals}f}",
                  f"{stats.mean(ba):.{decimals}f} / {stats.mean(ra):.{decimals}f}"]
        row = " & ".join(cells) + r" \\"
        paired_row = " & ".join([label, f"{entropy:g}", f"{beta:g}",
                                *[f"{delta[seeds.index(s)]:+.{decimals}f}" if s in seeds else "--"
                                  for s in range(1, 6)]]) + r" \\"
        rows.append((suite, task, entropy, beta, row))
        paired.append((suite, task, entropy, beta, paired_row))
        hyperparameters[(suite, task, entropy)] = " & ".join(str(value) for value in [
            label, agents, f"{entropy:g}", algo["algo"]["clip_param"], algo["algo"]["ppo_epoch"],
            algo["model"]["lr"], algo["train"]["n_rollout_threads"], algo["train"]["episode_length"],
            algo["eval"]["eval_episodes"],
        ]) + r" \\"
        print("RESULT", row)
    for filename, records in [("results_rows.tex", rows), ("paired_rows.tex", paired)]:
        lines = []
        for suite in sorted({record[0] for record in records}):
            header = {"mamujoco": "Multi-Agent MuJoCo", "pettingzoo_mpe": "Particle environments", "smac": "SMAC"}[suite]
            lines.append(r"\multicolumn{8}{l}{\emph{" + header + r"}} \\")
            lines.extend(record[-1] for record in sorted(records) if record[0] == suite)
        (output / filename).write_text("\n".join(lines) + "\n")
    (output / "hyperparameter_rows.tex").write_text("\n".join(hyperparameters[k] for k in sorted(hyperparameters)) + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    paper_dir = Path(__file__).resolve().parent
    parser.add_argument("--results", type=Path, default=paper_dir.parent / "HARL/examples/results")
    parser.add_argument("--output", type=Path, default=paper_dir / "tables")
    options = parser.parse_args()
    write_outputs(load_runs(options.results), options.results, options.output)
