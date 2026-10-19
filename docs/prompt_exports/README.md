# 双智能体完整 LLM 输入

每个 `.txt` 文件从 `SYSTEM MESSAGE` 和 `USER MESSAGE` 两段组成；段标题只是阅读标记，标题后的内容是完整的实际消息文本，没有省略样本行、指导手册或运行时插值内容。采样 LLM 与经验总结 LLM 共用正式 system message，但 user prompt 不同。

| 文件 | 状态 | 正式 user prompt 的样本数 |
| --- | --- | ---: |
| `parquet_40_sampling.txt` | 新运行第一轮，先导入 40 条初始样本 | TOP-20 |
| `parquet_40_experience.txt` | 第一轮两条真实 HFSS 曲线入池后 | TOP-40 |
| `zero_start_sampling.txt` | 新运行第一轮，从空样本池启动 | 0 |
| `zero_start_experience.txt` | 两条真实 HFSS 曲线入池后的零样本模式示例 | TOP-2 |
| `preflight.txt` | 每个 LLM 模块正式请求前的独立连接预检 | 不含样本 |

两个 `parquet_40` 文件的 user prompt 已与 `O_2026_10_14_1630_ds_two_candidate` 中第一轮采样、经验总结交互日志逐字符比对一致。零样本采样文件由当前代码离线渲染。零样本经验文件使用该历史运行的两条第一轮真实 HFSS 曲线构造一个**示例状态**；这两条曲线是真实测量结果，但不表示曾进行过零样本模式的远程运行，也不预言零样本模式实际会产生这两条设计。

采样提示词会随 TOP-K 样本和当前变量指导手册变化；经验提示词会随 TOP-Q 样本变化。真实响应若不符合格式，程序会根据具体错误生成短纠错消息，并在同一轮请求中附带先前的 user/assistant 对话；因此纠错请求不存在一个独立于响应内容的固定全文。采样纠错逻辑位于 `llmo/agents.py` 的 `_sampling_correction_prompt`，经验格式纠错位于 `_format_correction_prompt`，规则校验纠错位于 `repair_invalid_rules`。

`manifest.json` 记录每份完整文件的字符数、样本数与 SHA-256。使用单智能体项目的 `docs/prompt_exports/export_examples.py` 可以离线重新生成这些文件。
