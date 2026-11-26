"""Reproduce the switch game figure by exactly enumerating the rollout actions."""

from itertools import product
from math import prod
from pathlib import Path
from statistics import pvariance

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def gradient_variances(n, epsilon):
    actions = list(product((-1, 1), repeat=n))
    return [
        pvariance(
            prod(1 + epsilon * a for a in action[:i]) * (sum(action) / n) * action[i] / 2
            for action in actions
        )
        for i in range(n)
    ]


def main():
    n, epsilon = 8, 0.5
    variances = gradient_variances(n, epsilon)
    blue = "#365B88"
    ink = "#23313F"
    plt.rcParams.update({"font.family": "serif", "font.size": 9, "pdf.fonttype": 42})
    fig, (game, curve) = plt.subplots(
        1, 2, figsize=(5.5, 1.85), width_ratios=(1, 1.4), layout="constrained"
    )

    game.set_title("(a) Example round", loc="left", fontweight="bold")
    game.set_axis_off()
    game.text(0.5, 0.88, "Eight agents act simultaneously", ha="center", color=ink)
    switches = (1, -1, 1, 1, -1, 1, -1, 1)
    for i, value in enumerate(switches):
        row, col = divmod(i, 4)
        x, y = 0.055 + 0.23 * col, 0.59 - 0.23 * row
        game.add_patch(
            FancyBboxPatch(
                (x, y), 0.20, 0.16, boxstyle="round,pad=0.005,rounding_size=0.02",
                edgecolor=blue if value > 0 else "#6C7884",
                facecolor="#EAF1F8" if value > 0 else "#F3F4F5", linewidth=0.8,
            )
        )
        game.text(x + 0.10, y + 0.08, f"{value:+d}".replace("-", "−"),
                  ha="center", va="center", color=ink)
    game.text(0.5, 0.13, r"Shared reward $R=(5-3)/8=0.25$", ha="center", color=ink)

    curve.set_title("(b) Variance across updates", loc="left", fontweight="bold")
    curve.plot(range(1, n + 1), variances, color=blue, marker="o", markersize=4, linewidth=1.5)
    curve.set(xlabel="Update position $i$", ylabel="Gradient variance",
              xticks=range(1, n + 1), yticks=(0, 0.2, 0.4, 0.6),
              xlim=(0.65, 8.35), ylim=(0, 0.73))
    curve.set_axisbelow(True)
    curve.grid(axis="y", color="#DCE2E8", linewidth=0.6)
    curve.spines[["right", "top"]].set_visible(False)
    curve.annotate(f"{variances[0]:.4f}", (1, variances[0]), textcoords="offset points",
                   xytext=(1, 7), ha="left", color=ink)
    curve.annotate(f"{variances[-1]:.3f}", (n, variances[-1]), textcoords="offset points",
                   xytext=(-7, -1), ha="right", va="center", color=ink)

    fig.savefig(Path(__file__).with_suffix(".pdf"), metadata={"CreationDate": None})
    plt.close(fig)


if __name__ == "__main__":
    main()
