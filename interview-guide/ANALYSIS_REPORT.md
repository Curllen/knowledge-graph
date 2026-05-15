# Interview Guide - 完整知识图谱分析报告

---

## 📋 文档信息

| 属性 | 值 |
|------|-----|
| **项目名称** | Interview Guide (面试指南平台) |
| **分析日期** | 2026-05-15 |
| **分析路径** | /workspace |
| **技术栈** | Java / Spring Boot / Spring AI / PostgreSQL (pgvector) / Redis / MinIO / Docker |
| **分析工具** | Graphify |
| **报告版本** | v1.0 |

---

## 一、项目概述

### 1.1 项目定位

Interview Guide 是一个基于 Spring Boot 的 AI 驱动面试平台，集成了文字面试、语音面试、简历分析、知识库 RAG 查询等核心功能，通过 LLM（大语言模型）实现智能出题、评估和反馈，支持多种 LLM Provider（DashScope/DeepSeek/Kimi/GLM/LMStudio）动态切换。

### 1.2 代码库规模

| 指标 | 数值 |
|------|------|
| **文件总数** | 252 |
| **代码量** | ~121,104 words |
| **图谱节点** | 2,104 |
| **图谱边** | 3,942 |
| **社区数量** | 197 |
| **提取置信度** | 72% EXTRACTED · 28% INFERRED |
| **Token 消耗** | AST 结构提取 + Agent 语义分析 |

**按文件类型统计：**

| 文件类型 | 文件数 | 说明 |
|----------|--------|------|
| Java | 199 | 后端核心代码（Controller/Service/Repository/Model/Config） |
| Markdown/YAML/XML | 53 | 项目文档、Prompt 模板、技能定义、配置文件 |
| SQL | 1 | PostgreSQL 初始化脚本（pgvector） |
| Lua | 1 | Redis 限流脚本 |

---

## 二、架构分析

### 2.1 核心架构层次

```
┌────────────────────────────────────────────────────────────────┐
│                      控制器层 (Controllers)                     │
│   InterviewController  │  VoiceInterviewController  │          │
│   ResumeController     │  KnowledgeBaseController   │          │
│   RagChatController    │  LlmProviderController     │          │
│   InterviewScheduleController  │  InterviewSkillController     │
├────────────────────────────────────────────────────────────────┤
│                      服务层 (Services)                          │
│   InterviewQuestionService  │  VoiceInterviewService  │        │
│   AnswerEvaluationService   │  ResumeParseService     │        │
│   KnowledgeBaseQueryService │  LlmProviderConfigService│       │
│   DashscopeLlmService      │  QwenAsrService          │       │
│   QwenTtsService           │  UnifiedEvaluationService │      │
├────────────────────────────────────────────────────────────────┤
│                      异步流处理层 (Stream Pipeline)              │
│   EvaluateStreamProducer/Consumer  │  AnalyzeStreamProducer/Consumer │
│   VectorizeStreamProducer/Consumer │  VoiceEvaluateStreamProducer/Consumer │
│   AbstractStreamProducer/Consumer  │  RedisService              │
├────────────────────────────────────────────────────────────────┤
│                      基础设施层 (Infrastructure)                │
│   RedisService  │  FileStorageService  │  DocumentParseService  │
│   PdfExportService  │  LlmProviderRegistry  │  PromptSanitizer  │
│   S3Config  │  CorsConfig  │  JacksonConfig  │  OpenApiConfig   │
└────────────────────────────────────────────────────────────────┘
```

### 2.2 核心组件关系图

```
                    ┌──────────────┐
                    │ LlmProvider  │  ← LLM 提供商注册与切换 (51 edges)
                    │ ConfigService│
                    └──────┬───────┘
                           │ 配置管理
              ┌────────────┼────────────┐
              │            │            │
              ▼            ▼            ▼
    ┌──────────────┐ ┌──────────┐ ┌──────────┐
    │ QwenAsrService│ │Dashscope │ │QwenTts   │  ← 语音 AI 服务
    │ 语音识别      │ │LlmService│ │Service   │
    └──────────────┘ └────┬─────┘ └──────────┘
                          │ LLM 调用
                          ▼
                ┌──────────────────┐
                │VoiceInterview    │  ← WebSocket 实时语音面试 (53 edges)
                │WebSocketHandler  │
                └────────┬─────────┘
                         │ 会话管理
              ┌──────────┼──────────┐
              │          │          │
              ▼          ▼          ▼
    ┌──────────┐  ┌──────────┐  ┌──────────┐
    │Interview │  │Knowledge │  │Resume    │  ← 业务模块
    │Session   │  │Base RAG  │  │Analysis  │
    │Entity    │  │Query     │  │Pipeline  │
    └──────────┘  └──────────┘  └──────────┘
```

### 2.3 主要组件说明

#### 面试模块 (Interview Module)
- **Interview Session REST API**: 面试会话的创建、答题、完成、导出全流程
- **Interview Question Generation**: 基于 Skill/简历的智能出题，含追问机制
- **Interview Evaluation & History**: 异步评估流水线 + 历史记录查询

#### 语音面试模块 (Voice Interview Module)
- **WebSocket Realtime Handler**: 实时音频流处理，ASR→LLM→TTS 全链路
- **Voice Interview Session Management**: 多阶段面试（INTRO→TECH→PROJECT→HR→COMPLETED）
- **Qwen ASR/TTS Speech**: 阿里云通义千问语音识别与合成

#### 简历模块 (Resume Module)
- **Resume Analysis Pipeline**: 上传→解析→AI分析→评分的异步流水线
- **Resume Controller API**: 简历上传、分析、删除、PDF导出

#### 知识库模块 (Knowledge Base Module)
- **Knowledge Base Vector Search**: 基于 pgvector 的向量相似度搜索
- **Knowledge Base Query & Counting**: RAG 查询（重写→检索→生成）
- **RAG Chat Session API**: 多轮对话式知识库问答

#### LLM 提供商模块 (LLM Provider Module)
- **LLM Provider Registry**: 多 LLM 提供商注册、切换、缓存
- **LLM Provider Configuration**: API Key 加密、ASR/TTS 配置动态更新
- **Structured LLM Output Processing**: 结构化输出 + JSON 修复重试

---

## 三、God Nodes（核心枢纽）

### 3.1 最重要的节点

| 排名 | 节点 | 连接数 | 说明 |
|------|------|--------|------|
| 1 | **VoiceInterviewWebSocketHandler** | 53 | 语音面试 WebSocket 核心处理器，协调 ASR/LLM/TTS |
| 2 | **LlmProviderConfigService** | 51 | LLM 提供商配置中心，跨模块桥接 |
| 3 | **InterviewSessionEntity** | 44 | 面试会话实体，数据模型核心 |
| 4 | **ErrorCode** | 40 | 错误码枚举，跨模块错误处理枢纽 |
| 5 | **KnowledgeBaseEntity** | 36 | 知识库实体，向量搜索与 RAG 核心 |
| 6 | **RedisService** | 31 | Redis 服务，异步流与缓存基础设施 |
| 7 | **VoiceInterviewService** | 30 | 语音面试业务逻辑核心 |
| 8 | **ResumeEntity** | 29 | 简历实体，分析流水线数据核心 |
| 9 | **InterviewSkillService** | 28 | 面试技能服务，出题与评估参考 |
| 10 | **QwenAsrService** | 27 | 语音识别服务，实时音频转文字 |

### 3.2 核心抽象分析

**VoiceInterviewWebSocketHandler**：作为语音面试的实时处理中枢，该节点连接了 ASR 语音识别、LLM 对话生成、TTS 语音合成三大 AI 服务，同时管理 WebSocket 会话状态、音频流控制、字幕推送等。它是整个语音面试功能的核心编排器。

**LlmProviderConfigService**：作为跨模块的配置桥梁，该节点连接了 LLM Provider 注册中心、ASR/TTS 配置、API Key 加密等关键服务。它使得语音面试模块能够动态切换 LLM 提供商，是系统灵活性的关键保障。

**InterviewSessionEntity**：作为面试数据模型的核心，承载了面试会话的完整生命周期数据——从创建、出题、答题到评估完成。它被 InterviewController、AnswerEvaluationService、InterviewPersistenceService 等多个服务依赖。

---

## 四、关键连接与发现

### 4.1 核心发现

- **异步流处理架构一致性**：项目在面试评估、简历分析、知识库向量化、语音评估四个场景中统一使用 Redis Stream 的 Producer-Consumer 模式，通过 `AbstractStreamProducer/AbstractStreamConsumer` 抽象基类实现代码复用，架构设计高度一致。
- **LLM Provider 动态切换机制**：`LlmProviderConfigService` 作为跨模块桥接节点，连接了 6 个不同社区，使得 ASR/TTS/LLM 服务可以在运行时动态切换提供商，无需重启应用。
- **多阶段语音面试状态机**：`VoiceInterviewService` 实现了 INTRO→TECH→PROJECT→HR→COMPLETED 的阶段状态机，配合 Redis 缓存和 WebSocket 实时通信，实现了流畅的语音面试体验。
- **Prompt 安全防护体系**：`PromptSanitizer` + `PromptSecurityConstants` + `StructuredOutputInvoker` 构成了三层 Prompt 注入防御体系，从输入清洗、安全常量注入到输出结构化验证，全方位保障 LLM 交互安全。
- **RAG 查询流水线**：知识库查询采用"重写→检索→生成"三阶段流水线，配合 pgvector 的 HNSW/COSINE 索引，实现了高质量的知识库问答。

### 4.2 意外连接（Surprising Connections）

| 源节点 | 关系 | 目标节点 | 置信度 | 说明 |
|--------|------|----------|--------|------|
| `QwenAsrServiceTest` | implements | `Qwen3 ASR (架构文档概念)` | INFERRED | 测试代码与架构文档中的概念实现对应 |
| `QwenTtsServiceTest` | implements | `Qwen3 TTS (架构文档概念)` | INFERRED | 测试代码验证了架构文档中描述的 TTS 实现 |
| `RustFS Service (dev)` | semantically_similar_to | `MinIO Service (prod)` | INFERRED | 开发/生产环境使用不同的 S3 兼容存储 |
| `PostgreSQL Init Script` | conceptually_related_to | `LlmProviderRegistry` | INFERRED | pgvector 扩展使 LLM Embedding 存储成为可能 |

### 4.3 跨社区桥接节点

**LlmProviderConfigService**（介数中心性 0.056）连接了 **6 个不同社区**，是整个系统的配置管理枢纽。它直接管理 QwenAsrService、QwenTtsService 的配置更新，同时与 LlmProviderRegistry 交互获取提供商信息，使得语音面试模块与 LLM Provider 模块解耦但又能动态协作。

**ErrorCode**（介数中心性 0.051）连接了 **8 个不同社区**，作为全局错误处理的统一出口，从 Rate Limiting 到 Knowledge Base、从 Resume Analysis 到 AI Agent Configuration，所有模块的错误都通过 ErrorCode 枚举统一管理。

**RedisService**（介数中心性 0.022）连接了 **6 个不同社区**，是异步流处理和缓存的基础设施枢纽，支撑了面试评估、简历分析、知识库向量化、语音评估四大异步流水线。

---

## 五、设计模式识别

### 5.1 已识别的设计模式

| 模式名称 | 涉及组件 | 置信度 |
|----------|----------|--------|
| **模板方法模式** | AbstractStreamProducer/Consumer → Evaluate/Analyze/Vectorize/VoiceEvaluate | 0.95 |
| **策略模式** | LlmProviderRegistry → 多 LLM Provider 切换 | 0.90 |
| **观察者模式** | Redis Stream Producer-Consumer 异步通知 | 0.85 |
| **工厂模式** | LlmProviderRegistry.createChatClient/createEmbeddingModel | 0.90 |
| **DTO/Entity 分离** | 各模块 Model 层 DTO 与 Entity 分离 | 0.95 |
| **Repository 模式** | Spring Data JPA Repository 统一数据访问 | 0.95 |
| **Builder 模式** | InterviewQuestionService 构建 Prompt 上下文 | 0.80 |

### 5.2 关键类层次结构

```
AbstractStreamProducer (抽象基类 - Redis Stream 生产者)
    ├── EvaluateStreamProducer     ← 面试评估任务发送
    ├── AnalyzeStreamProducer      ← 简历分析任务发送
    ├── VectorizeStreamProducer    ← 知识库向量化任务发送
    └── VoiceEvaluateStreamProducer ← 语音评估任务发送

AbstractStreamConsumer (抽象基类 - Redis Stream 消费者)
    ├── EvaluateStreamConsumer     ← 面试评估任务消费
    ├── AnalyzeStreamConsumer      ← 简历分析任务消费
    ├── VectorizeStreamConsumer    ← 知识库向量化任务消费
    └── VoiceEvaluateStreamConsumer ← 语音评估任务消费
```

---

## 六、社区分析

### 6.1 主要社区分布（Top 10）

| 社区ID | 名称 | 内聚度 | 节点数 | 说明 |
|--------|------|--------|--------|------|
| 0 | Core Infrastructure & Service Registry | 0.06 | 88 | 核心基础设施，包含 LLM 注册、Redis、加密等 |
| 1 | Session Cache & Rate Limiting | 0.06 | 73 | 会话缓存与限流，跨模块共享 |
| 2 | Document Parsing & Text Cleaning | 0.05 | 60 | 文档解析与文本清洗服务 |
| 3 | Structured LLM Output Processing | 0.06 | 57 | 结构化 LLM 输出处理与 JSON 修复 |
| 4 | Redis Stream Consumer Framework | 0.06 | 51 | Redis Stream 消费者抽象框架 |
| 5 | Qwen ASR Speech Recognition | 0.09 | 49 | 通义千问语音识别服务 |
| 6 | Knowledge Base Vector Search | 0.09 | 43 | 知识库向量搜索（pgvector） |
| 8 | Resume Analysis Pipeline | 0.05 | 40 | 简历分析异步流水线 |
| 7 | Knowledge Base Management API | 0.11 | 40 | 知识库管理 REST API |
| 9 | Cross-Cutting Error Handling & DTOs | 0.09 | 34 | 跨模块错误处理与 DTO |

### 6.2 低内聚度社区（需关注）

| 社区ID | 内聚度 | 问题描述 |
|--------|--------|----------|
| 0 | 0.06 | Core Infrastructure 社区过于庞大（88节点），建议拆分为 LLM Registry、Redis Infrastructure、Encryption 等更聚焦的子模块 |
| 1 | 0.06 | Session Cache & Rate Limiting 混合了缓存和限流两个关注点，建议分离 |
| 2 | 0.05 | Document Parsing 社区内聚度最低，解析服务与测试代码混合 |
| 3 | 0.06 | Structured Output Processing 可进一步拆分输出处理与重试逻辑 |
| 8 | 0.05 | Resume Analysis Pipeline 节点间连接松散，流水线各环节耦合度可提升 |

---

## 七、知识缺口（Knowledge Gaps）

### 7.1 孤立节点

发现 **642 个低连接节点**（degree ≤ 1），这些组件与其他部分的连接较少：

- `settings.gradle` / `build.gradle` - 构建配置文件，无代码依赖
- `App.java` - Spring Boot 启动类，仅被 main() 引用
- `ParseResponse` / `ParseRequest` - 面试调度 DTO，连接稀疏
- 各种 Properties 配置类 - 仅被对应的 Config 类引用

**建议**：检查这些组件是否需要与其他模块建立更多连接，或补充文档说明其用途。

### 7.2 薄弱社区

存在 **35 个节点数 < 3 的社区**，主要是：
- 单节点 DTO/Enum 类（如 `InterviewStatus`、`VectorStatus`、`ErrorCode`）
- 单节点配置 Bean（如 `JacksonConfig`、`OpenApiConfig`、`WebSocketConfig`）
- 单节点测试类（如 `TextCleaningServiceTest`、`AppTest`）

这些薄弱社区反映了 AST 提取的粒度特性——每个 Java 文件被拆分为类节点、方法节点和文件节点，导致小型类形成独立社区。

---

## 八、关键问题与建议

### 8.1 架构优化建议

| 优先级 | 建议 | 理由 |
|--------|------|------|
| 🔴 高 | 拆分 Core Infrastructure 社区 | 88个节点的超大社区（内聚度0.06）表明职责过于集中，建议按 LLM Registry、Redis Infrastructure、Security 拆分 |
| 🔴 高 | 统一异步流错误处理 | 四条 Redis Stream 流水线的错误处理逻辑高度相似但各自实现，建议抽取统一的重试与死信队列机制 |
| 🟡 中 | 增强 DTO 与 Entity 的映射文档 | 642个低连接节点中大量是 DTO/Properties，建议补充映射关系文档 |
| 🟡 中 | 抽取 Prompt 模板管理服务 | 当前 Prompt 模板分散在 .st 文件中，建议统一管理并支持动态加载 |
| 🟢 低 | 考虑引入事件驱动架构 | 当前 Redis Stream 模式可升级为 Spring Event + Redis Stream 的混合模式，提升可测试性 |

### 8.2 具体改进方案

1. **拆分 Core Infrastructure**：将 `LlmProviderRegistry`、`ApiKeyEncryptionService`、`LlmEmbeddingConfig` 抽取为独立的 `llm-registry` 子模块；将 `RedisService`、`InterviewSessionCache` 抽取为 `redis-infrastructure` 子模块；将 `PromptSanitizer`、`PromptSecurityConstants` 保留在 `ai-security` 子模块。

2. **统一异步流错误处理**：在 `AbstractStreamConsumer` 中增加统一的重试策略配置（最大重试次数、退避策略）、死信队列写入逻辑、以及可观测性埋点（Metrics/Tracing）。

---

## 九、推荐深度探索问题

1. **LlmProviderConfigService 如何实现跨模块的 LLM 动态切换？**：该节点连接了 6 个不同社区，是理解系统灵活性的关键入口。探索其如何管理 ASR/TTS/LLM 的配置更新流程。

2. **Redis Stream 四条流水线的容错机制是否一致？**：面试评估、简历分析、知识库向量化、语音评估四条流水线都基于 AbstractStreamProducer/Consumer，但各自的错误处理和重试策略可能存在差异。

3. **VoiceInterviewWebSocketHandler 如何协调 ASR→LLM→TTS 的实时流？**：53 条连接的 WebSocket 处理器是系统最复杂的节点，理解其音频流控制、状态管理和错误恢复机制对系统稳定性至关重要。

4. **Prompt 注入防御体系的三层防护如何协作？**：PromptSanitizer（输入清洗）+ PromptSecurityConstants（安全常量）+ StructuredOutputInvoker（输出验证）构成了防御纵深，但层间协作逻辑需要深入分析。

5. **pgvector 向量搜索的回退策略如何工作？**：KnowledgeBaseVectorService 同时实现了 similaritySearch 和 similaritySearchFallback，理解其降级策略对 RAG 查询质量有重要影响。

---

## 十、输出文件清单

| 文件 | 大小 | 用途 |
|------|------|------|
| `graph.html` | 2.2 MB | 交互式知识图谱可视化（浏览器打开） |
| `graph.json` | 2.6 MB | 原始图谱数据（JSON 格式） |
| `GRAPH_REPORT.md` | 36 KB | 自动生成的审计报告 |
| `ANALYSIS_REPORT.md` | - | 标准化分析报告（本文件） |
| `manifest.json` | 60 KB | 分析文件清单 |
| `cost.json` | 4 KB | Token 消耗记录 |

---

## 📁 文件引用

- [graph.html](file:///workspace/graphify-out/graph.html) - 交互式图谱
- [graph.json](file:///workspace/graphify-out/graph.json) - 图谱数据
- [GRAPH_REPORT.md](file:///workspace/graphify-out/GRAPH_REPORT.md) - 原始报告
- [manifest.json](file:///workspace/graphify-out/manifest.json) - 文件清单

---

*Generated by Graphify - Knowledge Graph Analysis Tool*
*报告生成模式: AST 结构提取 + Agent 语义分析*
