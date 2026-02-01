# Ethereum Book 翻译项目指南

## 项目概述

《Mastering Ethereum》中文翻译版。英文原版位于 `en_origion/ethereumbook/src/`。

**翻译原则**：信（准确）、达（通顺）、雅（优美）

---

## 命令

### `translate-Chapter_X`

输入 `translate-Chapter_1` 或 `translate-Chapter_2` 等，执行对照翻译+技术更新：

#### 执行流程

1. **读取文件**
   - 英文原版：`en_origion/ethereumbook/src/chapter_X.md`
   - 中文译文：`Chapter_X.md`

2. **搜索最新技术**
   - `Ethereum roadmap [当前年份] latest updates`
   - `Ethereum Pectra Fusaka [当前年份]`

3. **逐段对照改进**
   - 修正偏离原意的翻译
   - 补充遗漏内容
   - 优化中文表达，避免翻译腔
   - 首次出现的术语给出中英对照

4. **技术更新**
   - 更新过时描述（见下方速查表）
   - 替换失效链接
   - 添加译注标注更新时间

5. **输出摘要**
   - 准确性修正
   - 内容补充
   - 技术更新
   - 信息来源 (Sources)

---

## 过时内容速查表

翻译时检查以下内容是否需要更新：

| 检查项 | 过时内容 | 正确内容 |
|--------|----------|----------|
| 共识机制 | PoW / Ethash | PoS（2022年9月 The Merge） |
| Casper | "计划中" / "未来" | 已实现 |
| 开发阶段 | 仅 Frontier→Serenity | 补充 Surge/Verge/Purge/Splurge |
| 客户端 | Parity | 已停维，用 Nethermind 替代 |
| P2P 消息 | Whisper | 已弃用，被 Waku 取代 |
| 存储 | Swarm（核心组件） | 已独立，非以太坊核心 |
| Gas 模型 | 传统拍卖 | EIP-1559（Base Fee + Priority Fee） |

## 失效链接替代

| 失效链接 | 替代 |
|----------|------|
| `github.com/ethereum/wiki/wiki/*` | `ethereum.org/developers/docs/` |
| `leveldb.org` | `github.com/google/leveldb` |
| `parity.io` | `nethermind.io` |
| `vitalik.ca/*` | `vitalik.eth.limo/*` |

---

## 以太坊升级里程碑

| 时间 | 升级 | 要点 |
|------|------|------|
| 2015-07 | Frontier | 主网上线 |
| 2016-03 | Homestead | 第二阶段 |
| 2016-07 | DAO 硬分叉 | ETH/ETC 分裂 |
| 2017-10 | Byzantium | Metropolis 第一部分 |
| 2019-02 | Constantinople | Metropolis 第二部分 |
| 2019-12 | Istanbul | |
| 2021-04 | Berlin | |
| 2021-08 | London | EIP-1559 |
| **2022-09-15** | **The Merge** | **PoW → PoS** |
| 2023-04 | Shanghai/Capella | 质押提款 |
| 2024-03 | Cancun/Deneb | EIP-4844 Proto-Danksharding |
| **2025-05-07** | **Pectra** | 11 EIPs, blob 翻倍, EIP-7702 |
| **2025-12-03** | **Fusaka** | PeerDAS, Gas 上限 60M |
| 2026 H1 (计划) | Glamsterdam | 并行处理, ZK 验证 |
| 2026 H2 (计划) | Hegota | Verkle 树 |

---

## 客户端生态

**执行层**：Geth (Go)、Nethermind (C#)、Besu (Java)、Erigon (Go)

**共识层**：Prysm (Go)、Lighthouse (Rust)、Teku (Java)、Nimbus (Nim)、Lodestar (TS)

---

## 参考来源

| 资源 | URL |
|------|-----|
| 官方路线图 | https://ethereum.org/roadmap/ |
| 开发者文档 | https://ethereum.org/developers/docs/ |
| 黄皮书 | https://ethereum.github.io/yellowpaper/paper.pdf |
| 共识规范 | https://github.com/ethereum/consensus-specs |
| 执行规范 | https://github.com/ethereum/execution-specs |
| Vitalik 博客 | https://vitalik.eth.limo/ |

---

## 术语对照表

| English | 中文 | 备注 |
|---------|------|------|
| State Machine | 状态机 | |
| Smart Contract | 智能合约 | |
| Turing Complete | 图灵完备 | |
| Proof of Stake | 权益证明 | PoS |
| Proof of Work | 工作量证明 | PoW |
| Validator | 验证者 | |
| Execution Layer | 执行层 | |
| Consensus Layer | 共识层 | |
| Gas | Gas | 不译 |
| EVM | 以太坊虚拟机 | |
| DApp | 去中心化应用 | |
| Rollup | Rollup | 不译 |
| Blob | Blob | 不译 |
| Sharding | 分片 | |
| Verkle Tree | Verkle 树 | |
| Finality | 最终性 | |
| Halting Problem | 停机问题 | |
| Singleton | 单例 | |
