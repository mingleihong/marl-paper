# Reg-HAPPO 相关工作检索记录

检索日期为 2026-11-25。查询词为 `HAPPO sequential policy updates` 和 `policy optimization importance sampling Renyi divergence`，时间范围为 2015–2026 年。以顺序更新、联合重要性权重的方差、以及用分布差异约束策略更新为相关性标准。结果用于撰写稿件第 2 节。

各索引返回数：Semantic Scholar 4，OpenAlex 8，arXiv 8，OpenReview 0，Crossref 8，DBLP 0。共 28 条不同记录（0 条跨库重复合并），筛除 17 条明显不相关的记录。下表保留 8 篇相关或邻近研究，以及 3 条摘要不可用的待核记录。原始记录和摘要见 [search-results.json](ref/search-results.json)。排序和引用量取自检索快照，年份及会议以正式出版信息优先。

| 检索排名 | 题名 | 日期 | 会议或期刊 | 引用量 | 相关性分 | 来源 |
|---:|---|---|---|---:|---:|---|
| 1 | [Low Variance Trust Region Optimization with Independent Actors and Sequential Updates in Cooperative Multi-Agent Reinforcement Learning](https://doi.org/10.1007/s10458-025-09695-8) | 2025-02 | Autonomous Agents and Multi-Agent Systems | 4 | 6 | Semantic Scholar |
| 3 | [Trust Region Policy Optimisation in Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2109.11251) | 2022 | ICLR | 488 | 4 | Semantic Scholar |
| 4 | [Policy Optimization via Importance Sampling](https://proceedings.neurips.cc/paper/2018/hash/6aed000af86a084f9cb0264161e29dd3-Abstract.html) | 2018-12 | NeurIPS | 63 | 4 | OpenAlex |
| 5 | [Order Matters: Agent-by-agent Policy Optimization](https://discovery.ucl.ac.uk/id/eprint/10206861/) | 2023 | ICLR | 36 | 4 | OpenAlex |
| 6 | [Offline Multi-Agent Reinforcement Learning via In-Sample Sequential Policy Optimization](https://ojs.aaai.org/index.php/AAAI/article/download/34099/36254) | 2025 | AAAI | 24 | 4 | Semantic Scholar |
| 8 | [Breaking the Curse of Horizon: Infinite-Horizon Off-Policy Estimation](https://arxiv.org/abs/1810.12429) | 2018-12 | NeurIPS | 358 | 3 | OpenAlex |
| 9 | [Towards Optimal Off-Policy Evaluation for Reinforcement Learning with Marginalized Importance Sampling](https://arxiv.org/abs/1906.03393) | 2019-12 | NeurIPS | 127 | 3 | OpenAlex |
| 10 | [Importance Sampling Policy Evaluation with an Estimated Behavior Policy](https://proceedings.mlr.press/v97/hanna19a.html) | 2019 | ICML | 68 | 3 | OpenAlex |
| 13 | [HAPPO: Heuristic Assisted Proximal Policy Optimization for Dynamic Microservice Placement in Vehicular Edge Computing](https://doi.org/10.1109/vtc2026-spring68026.2026.11757824)（待核） | 2026-06 | IEEE VTC Spring | 0 | 3 | Crossref |
| 25 | [Symmetric Renyi-Permutation Divergence and Conflict Management for Random Permutation Set](https://doi.org/10.2139/ssrn.4550974)（待核） | — | SSRN | 0 | 2 | Crossref |
| 28 | [Reliability of Standing Ability, Hypo albuminemia and Sequential Organ Failure Assessment Score in Predicting ICU Readmission](https://doi.org/10.21608/muj.2026.459550.1306)（待核） | 2026-02 | Medicine Updates | 0 | 1 | Crossref |

DBLP 对两次查询均返回 `Expecting value: line 1 column 1 (char 0)`。Semantic Scholar 的第二个查询返回 `429 Client Error`。OpenReview 的独立检索在 `Getting V2 Notes` 阶段超时，退出码 124，未返回可用记录。安装版检索脚本没有 `--json` 参数，使用其内置的各索引检索程序保存结构化结果。检索范围内的缺失记录通过论文参考文献追踪和出版社、会议或 arXiv 原文补充。

## 补充核对后纳入正文的文献

| 论文 | 年份 | 来源 | 用于第 2 节的论点 |
|---|---:|---|---|
| [Trust Region Policy Optimization](https://proceedings.mlr.press/v37/schulman15.html) | 2015 | ICML | 用 KL 约束限制策略更新 |
| [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347) | 2017 | arXiv | PPO 的裁剪代理目标 |
| [Coordinated Proximal Policy Optimization](https://proceedings.neurips.cc/paper/2021/hash/de73998802680548b916f1947ffbad76-Abstract.html) | 2021 | NeurIPS | 裁剪其他智能体概率比率的乘积以及组合后的比率 |
| [Settling the Variance of Multi-Agent Policy Gradients](https://proceedings.neurips.cc/paper/2021/hash/6fe6a8a6e6cb710584efc4af0c34ce50-Abstract.html) | 2021 | NeurIPS | 基线对队友探索所引入梯度方差的作用 |
| [The Surprising Effectiveness of PPO in Cooperative Multi-Agent Games](https://proceedings.neurips.cc/paper_files/paper/2022/hash/9c1535a02f0ce079433344e14d910597-Abstract.html) | 2022 | NeurIPS | MAPPO 的集中式价值函数与单体 PPO 比率 |
| [Multi-Agent Reinforcement Learning is a Sequence Modeling Problem](https://proceedings.neurips.cc/paper_files/paper/2022/hash/69413f87e5a34897cd010ca698097d0a-Abstract-Conference.html) | 2022 | NeurIPS | 自回归动作建模与独立执行下的顺序参数更新 |
| [Heterogeneous-Agent Reinforcement Learning](https://jmlr.org/papers/v25/23-0488.html) | 2024 | JMLR | 异质智能体镜像学习框架 |
| [Multi-Agent Trust Region Policy Optimisation: A Joint Constraint Approach](https://doi.org/10.65109/ZOYC2112) | 2026 | AAMAS | HATRPO 的联合 KL 预算分配 |
| [Aggregate in the Advantage, Not the Ratio](https://arxiv.org/abs/2607.17924) | 2026 | arXiv | 联合求导目标中聚合多个智能体比率的方差 |
| [Importance Sampling Techniques for Policy Optimization](https://jmlr.org/papers/v21/20-124.html) | 2020 | JMLR | 二阶 Rényi 散度与重要性权重的方差 |

## 检索概览

索引检索保留的研究覆盖 HAPPO 类顺序更新和单智能体离策略重要性采样。正文引用检索表中的第 1、3、4、5 篇，并纳入上表的 10 篇补充文献。

## 时间与方法趋势

2018–2019 年的 NeurIPS 文献主要讨论单智能体轨迹复用和时序乘积方差。2022–2023 年的 ICLR 文献研究多智能体顺序更新和前序策略的校正。2025–2026 年的邻近研究进一步分析前缀裁剪、联合散度预算和跨智能体的比率聚合。检索样本的范围有限，年份分布用于说明技术脉络。

## 研究主题

- **顺序策略优化**。HAPPO、A2PO 和离线 InSPO 分别处理顺序改进、前序校正和离线联合动作分布偏移（第 3、5、6 篇）。
- **重要性权重的方差**。clip-HAPPO 裁剪智能体前缀权重，POIS 则把重要性采样的不确定性纳入优化目标（第 1、4 篇）。
- **时序重要性采样**。边际化状态分布或估计行为策略可以改变离策略评估的方差与偏差（第 8、9、10 篇）。

## 高频标题术语

按已读摘要且保留的 8 条记录统计，合并英美拼写和连字符变体。

| 术语 | 篇数 |
|---|---:|
| Policy optimization / optimisation | 4 |
| Multi-agent | 3 |
| Importance sampling | 3 |
| Trust region | 2 |
| Sequential | 2 |

## 引用量最高的已录用论文

| 排名 | 论文 | 年份 | 引用量 |
|---:|---|---:|---:|
| 1 | Trust Region Policy Optimisation in Multi-Agent Reinforcement Learning | 2022 | 488 |
| 2 | Breaking the Curse of Horizon: Infinite-Horizon Off-Policy Estimation | 2018 | 358 |
| 3 | Towards Optimal Off-Policy Evaluation for Reinforcement Learning with Marginalized Importance Sampling | 2019 | 127 |
| 4 | Importance Sampling Policy Evaluation with an Estimated Behavior Policy | 2019 | 68 |
| 5 | Policy Optimization via Importance Sampling | 2018 | 63 |

## 按第一作者汇总的引用量

| 排名 | 作者 | 篇数 | 引用量 |
|---:|---|---:|---:|
| 1 | Jakub Grudzien Kuba | 1 | 488 |
| 2 | Qiang Liu | 1 | 358 |
| 3 | Tengyang Xie | 1 | 127 |
| 4 | Josiah P. Hanna | 1 | 68 |
| 5 | Alberto Maria Metelli | 1 | 63 |

## 阅读顺序

1. **Metelli 等（2020）**。从重要性权重的二阶矩理解方差项的来源。
2. **Kuba 等（2022）**。从优势分解和 HAPPO 目标理解前序比率乘积的用途。
3. **Wang 等（2023）**。比较通过估计器修正处理前序策略变化的方法。
4. **Le 和 Ta（2025）**。比较前缀裁剪和当前策略更新正则的作用点。正文引用期刊版本，`ref/` 内保存的是作者公开版本 arXiv:2606.25526v1。

## 第 3.1 节 · 合作式多智能体建模

2026-11-26 使用查询 `Decentralized Control of Markov Decision Processes` 检索 1994–2026 年的记录。Semantic Scholar 0、OpenAlex 3、arXiv 0、OpenReview 0、Crossref 3、DBLP 0。去除 1 条跨库重复后有 5 条独立记录。根据摘要筛除 1 篇关于无人机编队形状控制的应用论文，保留 4 条。第 5 条缺少索引摘要，保留待核。完整记录、摘要和索引错误见 [search-results-3.1.json](ref/search-results-3.1.json)。

| 检索排名 | 题名 | 日期 | 会议或期刊 | 引用量 | 相关性分 | 来源 |
|---:|---|---|---|---:|---:|---|
| 1 | [The Complexity of Decentralized Control of Markov Decision Processes](https://doi.org/10.1287/moor.27.4.819.297) | 2002-11 | Mathematics of Operations Research | 1652 | 5 | OpenAlex |
| 2 | [Decentralized Control of Partially Observable Markov Decision Processes](https://doi.org/10.1109/cdc.2013.6760239) | 2013-12 | IEEE CDC | 189 | 5 | OpenAlex、Crossref |
| 4 | [Decentralized Stochastic Control with Partial History Sharing: A Common Information Approach](https://doi.org/10.1109/tac.2013.2239000) | 2013-06 | IEEE Transactions on Automatic Control | 361 | 4 | OpenAlex |
| 5 | [A Dynamic Programming Algorithm for Decentralized Markov Decision Processes with a Broadcast Structure](https://doi.org/10.1109/cdc.2010.5718187)（摘要待核） | 2010-12 | IEEE CDC | 16 | 4 | Crossref |

安装版 `search_papers.py` 返回 `unrecognized arguments: --json`，因此使用其检索程序保存结构化记录。arXiv 返回 `Read timed out. (read timeout=5.0)`，DBLP 返回 `Expecting value: line 1 column 1 (char 0)`，OpenReview 和 Semantic Scholar 返回 HTTP 429。各索引的原始错误保存在上面的 JSON 中。

### 补充核对的原文

| 文献 | 与第 3.1 节的关系 |
|---|---|
| [Littman（1994）](https://aima.eecs.berkeley.edu/~russell/classes/cs294/f21/papers/Littman_ICML94_Markov_Games.pdf) | 马尔可夫博弈建模的来源 |
| [Wen 等（2022）](https://proceedings.neurips.cc/paper_files/paper/2022/file/69413f87e5a34897cd010ca698097d0a-Paper-Conference.pdf) | 第 2.1 节提供共享奖励、同时执行及折扣分布的组织方式 |
| [Kuba 等（2022）](https://arxiv.org/html/2109.11251) | 合作策略的乘积分解及 HAPPO 的独立参数化 |

### 概览

索引结果主要来自分散式控制领域。正文引用 Bernstein 等人的建模论文，以及上表三篇核对过的原文。正文使用 Bernstein 等人论文的期刊书目信息，`ref/` 保存马萨诸塞大学公开的[四作者版本](https://cics.umass.edu/~immerman/pub/bgiz.pdf)。

### 时间与方法趋势

2002 年的记录从模型定义出发，2010–2013 年的记录进一步讨论不同信息结构下的控制和规划。这个样本较小，无法据此判断整个领域的发表趋势。

### 研究主题

- **分散式部分可观测模型**。第 1、2 篇区分环境状态、局部观测和共享目标。
- **控制者的信息结构**。第 4、5 篇关注部分历史共享或广播所形成的信息结构。
- **合作学习与策略参数化**。Wen 等和 Kuba 等分别提供问题建模和独立策略因子，与正文的分析设定直接相关。

### 高频标题术语

| 术语 | 篇数 |
|---|---:|
| Decentralized | 4 |
| Markov | 3 |
| Decision process | 3 |
| Control | 3 |
| Partial / partially | 2 |

### 引用量最高的已发表记录

| 排名 | 题名 | 年份 | 引用量 |
|---:|---|---:|---:|
| 1 | The Complexity of Decentralized Control of Markov Decision Processes | 2002 | 1652 |
| 2 | Decentralized Stochastic Control with Partial History Sharing: A Common Information Approach | 2013 | 361 |
| 3 | Decentralized Control of Partially Observable Markov Decision Processes | 2013 | 189 |
| 4 | A Dynamic Programming Algorithm for Decentralized Markov Decision Processes with a Broadcast Structure | 2010 | 16 |

### 按首作者统计

| 排名 | 作者 | 篇数 | 引用量 |
|---:|---|---:|---:|
| 1 | Daniel S. Bernstein | 1 | 1652 |
| 2 | Ashutosh Nayyar | 1 | 361 |
| 3 | Christopher Amato | 1 | 189 |
| 4 | Jeff Wu | 1 | 16 |

### 阅读顺序

1. Littman（1994）给出马尔可夫博弈建模和联合动作的基本记号。
2. Bernstein 等（2002）描述共享目标下的局部信息与分散决策。
3. Wen 等（2022）第 2.1 节展示合作式多智能体强化学习建模在论文中的写法。
4. Kuba 等（2022）第 2 节和第 4 节把联合策略分解接到 HAPPO 的顺序更新。
