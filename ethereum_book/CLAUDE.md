# Ethereum Book 项目指南

## 项目概述

这是《Mastering Ethereum》的中文翻译版，原书写于2017-2018年，部分内容可能已过时。

## 命令

### `update Chapter_X.md`

当用户输入 `update Chapter_X.md` (如 `update Chapter_1.md`) 时，执行以下验证+检查+更新流程：

#### 1. 读取章节内容
- 读取指定的 .md 文件

#### 2. 技术内容验证
检查以下关键技术点是否与最新以太坊技术吻合：

| 检查项 | 过时内容 | 正确内容 |
|--------|----------|----------|
| 共识机制 | PoW/Ethash/工作量证明 | PoS/权益证明 (2022年9月 The Merge 后) |
| Casper | "计划中"/"未来" | 已通过 The Merge 实现 |
| 开发阶段 | Frontier/Homestead/Metropolis/Serenity 四阶段 | 已完成 The Merge，当前路线图为 Surge/Scourge/Verge/Purge/Splurge |
| 客户端 | Parity | Parity 已停止维护，现主流：Geth、Nethermind、Besu、Erigon |
| P2P消息 | Whisper | Whisper 已弃用，被 Waku 取代 |
| 存储 | Swarm (作为以太坊核心组件) | Swarm 已独立于以太坊 |
| Gas 模型 | 传统 Gas 拍卖 | EIP-1559 (2021年 London 升级后引入 Base Fee + Priority Fee) |

#### 3. 链接验证
检查所有外部链接是否可访问：
- 使用 WebFetch 工具验证每个 http/https 链接
- 记录失效链接 (404、证书错误等)
- 提供替代链接建议

**已知失效链接及替代：**

| 失效链接 | 替代链接 |
|----------|----------|
| `https://github.com/ethereum/wiki/wiki/*` | `https://ethereum.org/developers/docs/` |
| `http://leveldb.org` | `https://github.com/google/leveldb` |
| `https://parity.io/` (以太坊客户端) | `https://nethermind.io/` 或移除 |
| `https://vitalik.ca/*` (如不稳定) | `https://vitalik.eth.limo/*` |

#### 4. 更新内容
- 修正过时的技术描述
- 替换失效链接
- 保持原文风格和结构
- 添加必要的历史背景说明（如"注：原书写于2018年，以下内容已更新至2026年"）

#### 5. 输出报告
完成后输出：
- 技术内容修改摘要
- 链接修复列表
- 仍需人工确认的问题

## 以太坊重要里程碑 (供参考)

| 时间 | 事件 | 影响 |
|------|------|------|
| 2015年7月 | Frontier 启动 | 以太坊主网上线 |
| 2016年3月 | Homestead | 第二阶段 |
| 2016年7月 | DAO 硬分叉 | ETH/ETC 分裂 |
| 2017年10月 | Byzantium | Metropolis 第一部分 |
| 2019年2月 | Constantinople | Metropolis 第二部分 |
| 2019年12月 | Istanbul | |
| 2021年4月 | Berlin | |
| 2021年8月 | London | EIP-1559 引入 |
| 2022年9月15日 | **The Merge** | PoW → PoS |
| 2023年4月 | Shanghai/Capella | 质押提款启用 |
| 2024年3月 | Cancun/Deneb | Proto-Danksharding (EIP-4844) |

## 当前以太坊客户端生态

**执行层客户端：**
- Geth (Go) - 最广泛使用
- Nethermind (C#)
- Besu (Java)
- Erigon (Go) - 存档节点优化

**共识层客户端：**
- Prysm (Go)
- Lighthouse (Rust)
- Teku (Java)
- Nimbus (Nim)
- Lodestar (TypeScript)
