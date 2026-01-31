## About this Repo

我对这个中文翻译版本做了一些修改，初心是在当前 Age of AI，学习新技术的效率已经有了巨大的提升，本文档的学习方法完全可以在 Claude Code、Codex 等 coding agent 的协助下快速学习并写一些 demo 来深刻理解比特币, 以太坊和智能合约的原理，具体做了如下优化：

- 将原始 `.asciidoc` 格式转换为更易阅读的 **Markdown (`.md`)** 格式
- 优化了文档结构，添加了章节目录导航
- 保留了原书的图片和代码示例
- todo : 我会在我学习的过程中将最新的bitcoin区块链技术同步更新, 因为原书也是很久之前发版的, 技术不断的在迭代, 我只能在当下的时间尽量追踪最新bitcoin 开发团队的技术 
- todo：我会在学习过程中将最新的以太坊技术同步更新，因为原书发版较早，技术不断迭代，我会尽量追踪最新的技术发展


## 转换工具

本仓库包含 `convert_to_md.py` 脚本，用于将 AsciiDoc 格式转换为 Markdown。

**用法：**
```bash
python3 convert_to_md.py
```

**转换原理：**
- 标题：`=` ~ `=====` → `#` ~ `#####`
- 图片：`image::path[alt]` → `![alt](path)`
- 代码块：`----` → ` ``` `
- 提示框：`[TIP]/[WARNING]/[NOTE]` → blockquote
- 链接：`<<file#,text>>` → `[text](file.md)`
- LaTeX 公式：`[latexmath]` + `++++` → `$$...$$`
- 移除索引标记 `((("...")))`