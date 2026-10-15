![agent-stack — 三个代理，共享一套基础规则](assets/agent-stack-cover.jpg)

# agent-stack

**切换代理时，保留你的工作规则。**

面向 **Hermes、OMP 和 Codex** 的已审核指令、技能与模板。共享经过选择的行为规范；凭据、运行时设置和实时会话仍由各自的所有者管理。

[English](README.md) · [Русский](README.ru.md) · [简体中文](README.zh-CN.md)

[快速开始](#先预览再安装) · [组件](#选择组件) · [设计](design/README.md) · [Codex Cloud（俄语）](docs/codex-cloud.md) · [兼容性](docs/compatibility.md) · [安全](docs/security.md)

每个组件的目标运行时和限制都在 [manifest.yaml](manifest.yaml) 中明确列出。共享 targets 表示可以将同一份技能文本安装到不同运行时。模型行为是否一致、所需工具是否可用，需要另行验证。

## 哪些内容可以迁移

| 共享材料 | 保留在运行时和宿主中 |
| --- | --- |
| 结果验证指令 | 凭据、OAuth 数据和服务商密钥 |
| 明确指定 targets 的技能 | 模型及服务商设置、MCP 注册信息 |
| 空白工作交接模板 | 实时会话、日志、计划任务和数据库 |
| 已审核的工作规则 | 配置档案、机器设置和私人知识 |

本仓库分发行为规范材料，不会升级 Hermes、OMP、Codex 或 Jev，不会替换其配置或同步会话，也不会自动执行 pull、push 或部署。

## 先预览再安装

需要 **Python 3.12+**。在仓库根目录运行以下命令，只列出基础组件，不写入文件：

```sh
python installers/install.py hermes --dry-run
# 也可以将 hermes 替换为 omp 或 codex
```

平台原生入口：`./installers/install.sh codex`，或在 PowerShell 中运行 `./installers/install.ps1 codex`。

检查所选技能时，请指定目标运行时或配置档案已存在的绝对根路径。运行下面的示例前，先设置 `HERMES_HOME`：

```sh
./installers/install.sh hermes \
  --component proof-gated-coding-delivery \
  --destination "$HERMES_HOME" \
  --no-clobber \
  --dry-run
```

审核计划并授权安装后，将 `--dry-run` 替换为 `--apply`。

- 写入操作必须同时提供 `--component` 和 `--destination`。
- Destination 是所选运行时或配置档案的根目录，必须位于本仓库及运行时源代码目录之外。
- `--no-clobber` 会拒绝覆盖已有目标。不提供 destination 时，无法检查本地文件冲突。
- 有意替换且未使用 `--no-clobber` 时，旧版本会保存到备份中；需要恢复时请手动操作。
- `optional` 组件必须显式选择。`manual` 片段需要手动合并到现有指令中，安装器不会应用它们。

更多示例和恢复说明：[可移植性](docs/portability.md)。

## 选择组件

| 组件 | Targets | 使用方式 |
| --- | --- | --- |
| `verification` | Hermes / OMP / Codex | 已审核的验证指令；复制文件不会自动加载指令 |
| `proof-gated-coding-delivery` | Hermes / OMP / Codex | 区分实现完成、运行时验证和发布就绪 |
| `knowledge-combine` | Hermes / OMP / Codex | 可选的知识整理流程；由用户选择存储位置 |
| `handoff-template` | Hermes / OMP / Codex | 空白工作交接模板 |
| `ecc-context-budget` / `ecc-workflow-eval` | Hermes / OMP | 经过选择性改编的 ECC 技能，有独立的离线检查记录 |
| `personal-operator-baseline` | 仅 Hermes | Hermes 专用工作规则 |
| `hermes-soul-fragment` / `codex-agents-fragment` | 各自对应的运行时 | 手动合并到现有指令中 |
| `design-reference-loop` | Hermes / OMP / Codex | 需求 → 参考 → 方案 → 用户选择 → 实现 → 验证 |
| 29 个[设计技能](design/README.md) | Hermes / OMP / Codex | Taste、Emil 和 Impeccable 的共享静态改编版，按需选择 |
| `design-routing-fragment` | Hermes / OMP / Codex | 手动合并设计技能选择规则 |

全部 **30 个设计技能** 均位于 `shared/skills`，状态为 `optional`。可以为三个运行时分别预览同一个组件：

```sh
python installers/install.py hermes --component impeccable-design --dry-run
python installers/install.py omp --component impeccable-design --dry-run
python installers/install.py codex --component impeccable-design --dry-run
```

图像生成、浏览器、子代理等能力由宿主提供。如果缺少必要工具，技能必须明确报告限制。`prototype`、`pick-ui-library` 和 `review-animations` 在所有运行时中仍然只能显式调用。Impeccable 仅包含静态指导，不包含其引擎或 hooks。

[Manifest](manifest.yaml) 定义组件状态、目标路径、依赖和 `tested_on`。`reviewed` 表示材料已审核；`optional` 要求显式选择；`manual` 要求手动合并。空的 `tested_on` 不代表已完成运行时验证。

## 文件安装与代理行为需要分别验证

测试会在临时目录中执行选择性安装，并比较文件哈希。这不能证明已打开的聊天能够发现技能、模型会遵循指令或输出质量有所提高。

ECC 另有通过 OMP 和 Windows Hermes 执行的技能发现与读取检查：[结果及限制](docs/portability.md#selective-ecc-adaptations)。新的 OMP 进程能够发现资源，而已有会话未加载新目录。文件安装与运行中会话的技能目录刷新是不同事件。

可选的 [OMP 原生 ECC 实验](runtimes/omp/README.md#native-ecc-trial-ecc-safe) 在独立配置档案中使用固定版本的 Pi adapter。其 PowerShell 启动器保持额外规则和生命周期脚本禁用。该实验独立于常规 OMP 配置，不会替换后者。

## 在 Codex Cloud 中继续工作

为 `typakon4/agent-stack` 创建云环境，使用当前 `master`，并通过 [Codex Cloud 指南（俄语）](docs/codex-cloud.md) 传递上下文。指南包含验证命令、选择性安装技能的示例和可直接复制的任务交接文本。本机的个人技能和进程不会自动迁移到 Cloud。

## 安全与配置归属

预览和安装会检查源文件名及明显的凭据特征，不会输出匹配到的值。这项保护无法保证检测到所有秘密信息；仍需人工审核源文件和 diff。

不要将密钥、浏览器配置档案、私人知识、原始聊天记录或运行时状态加入仓库。工具已登录并不意味着获得发布、发送消息、购买、删除或部署的权限。详见[安全边界](docs/security.md)。

Jev 仍是**外部依赖**，固定在提交 `08473a5496864e8c97ee6f8f58980131ae16aed2`。本仓库不包含其源代码、MCP 配置、凭据或 replay。设计检查器离线运行，尚未连接实时设计方案选择适配器。详见 [Jev 集成](integrations/jev/README.md)。

## 验证

```sh
python -B tests/validate_manifest.py
python -B -m unittest discover -s tests -v
python -B -m unittest discover -s design/tests -v
```

GitHub Actions 在 Linux 和 Windows 上使用 Python 3.12、3.14 执行检查，并预览平台原生安装器。检查涵盖 manifest、设计技能哈希、选择性安装、路径边界，以及文件和 Git 历史中的明显秘密信息。测试使用临时运行时目录。模型行为、视觉质量及真实 Jev 调用需要另行评估。

## 添加技能或运行时

检查工具需求、来源、许可证以及访问和发布边界。在 manifest 中添加 source、明确的 targets 和状态，然后针对约定的 destination 执行预览。保留原生策略，避免替换整个配置。详见[架构](docs/architecture.md)。

五个基础提交保留在历史中；当前文件树已移除过时的 Hermes-only 文件。

<sub>封面由用户生成，描绘第三方虚构角色绫波丽。这是非官方插画，与《新世纪福音战士》或所列运行时项目无关联。插画不构成运行时验证证据。</sub>
