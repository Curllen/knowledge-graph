# Graph Report - /workspace/spring-ai-alibaba-admin/spring-ai-alibaba-admin-server-runtime  (2026-05-13)

## Corpus Check
- Corpus is ~33,028 words - fits in a single context window. You may not need a graph.

## Summary
- 398 nodes · 499 edges · 116 communities (51 shown, 65 thin omitted)
- Extraction: 95% EXTRACTED · 5% INFERRED · 0% AMBIGUOUS · INFERRED: 26 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_LoginRequest|LoginRequest]]
- [[_COMMUNITY_Document.java|Document.java]]
- [[_COMMUNITY_ApiKey|ApiKey]]
- [[_COMMUNITY_CommonParam|CommonParam]]
- [[_COMMUNITY_AppQuery|AppQuery]]
- [[_COMMUNITY_Result.java|Result.java]]
- [[_COMMUNITY_JsonUtils.java|JsonUtils.java]]
- [[_COMMUNITY_AgentConfig|AgentConfig]]
- [[_COMMUNITY_NodeResult.java|NodeResult.java]]
- [[_COMMUNITY_ApiParameter.java|ApiParameter.java]]
- [[_COMMUNITY_AppComponentConfig|AppComponentConfig]]
- [[_COMMUNITY_WebUploadPolicy.java|WebUploadPolicy.java]]
- [[_COMMUNITY_isNumber()|isNumber()]]
- [[_COMMUNITY_BizException|BizException]]
- [[_COMMUNITY_ModelConfig.java|ModelConfig.java]]
- [[_COMMUNITY_Cloneable|Cloneable]]
- [[_COMMUNITY_Content|Content]]
- [[_COMMUNITY_McpTool.java|McpTool.java]]
- [[_COMMUNITY_Tool.java|Tool.java]]
- [[_COMMUNITY_Function|Function]]
- [[_COMMUNITY_TimeoutConfig.java|TimeoutConfig.java]]
- [[_COMMUNITY_WebUploadRequest.java|WebUploadRequest.java]]
- [[_COMMUNITY_WorkflowResponse|WorkflowResponse]]
- [[_COMMUNITY_AgentResponse|AgentResponse]]
- [[_COMMUNITY_AsyncResultResponse|AsyncResultResponse]]
- [[_COMMUNITY_CustomParam|CustomParam]]
- [[_COMMUNITY_ProcessGetResponse|ProcessGetResponse]]
- [[_COMMUNITY_ChatMessageContentDeserializer|ChatMessageContentDeserializer]]
- [[_COMMUNITY_ChatMessage|ChatMessage]]
- [[_COMMUNITY_ApiConstants|ApiConstants]]
- [[_COMMUNITY_McpQuery.java|McpQuery.java]]
- [[_COMMUNITY_ToolExecutionRequest.java|ToolExecutionRequest.java]]
- [[_COMMUNITY_McpServerDetail.java|McpServerDetail.java]]
- [[_COMMUNITY_Content.java|Content.java]]
- [[_COMMUNITY_McpServerDeployConfig.java|McpServerDeployConfig.java]]
- [[_COMMUNITY_ProcessConfig.java|ProcessConfig.java]]
- [[_COMMUNITY_ShortTermMemory.java|ShortTermMemory.java]]
- [[_COMMUNITY_TokenResponse|TokenResponse]]
- [[_COMMUNITY_Account|Account]]
- [[_COMMUNITY_TaskRunRequest|TaskRunRequest]]
- [[_COMMUNITY_WorkflowRequest|WorkflowRequest]]
- [[_COMMUNITY_RetryConfig.java|RetryConfig.java]]
- [[_COMMUNITY_ChangePasswordRequest|ChangePasswordRequest]]
- [[_COMMUNITY_DeleteChunkRequest.java|DeleteChunkRequest.java]]
- [[_COMMUNITY_ToolCallSchema.java|ToolCallSchema.java]]
- [[_COMMUNITY_DocumentChunk.java|DocumentChunk.java]]
- [[_COMMUNITY_CommonParam.java|CommonParam.java]]
- [[_COMMUNITY_File.java|File.java]]
- [[_COMMUNITY_DocumentRetrieverQuery.java|DocumentRetrieverQuery.java]]
- [[_COMMUNITY_Oauth2User|Oauth2User]]
- [[_COMMUNITY_TaskRunResponse|TaskRunResponse]]
- [[_COMMUNITY_DeleteDocumentRequest.java|DeleteDocumentRequest.java]]
- [[_COMMUNITY_AppComponent|AppComponent]]
- [[_COMMUNITY_IndexDocumentRequest.java|IndexDocumentRequest.java]]
- [[_COMMUNITY_UpdateChunkRequest.java|UpdateChunkRequest.java]]
- [[_COMMUNITY_Error|Error]]
- [[_COMMUNITY_KnowledgeBase.java|KnowledgeBase.java]]
- [[_COMMUNITY_InputSchema.java|InputSchema.java]]
- [[_COMMUNITY_ApplicationVersion|ApplicationVersion]]
- [[_COMMUNITY_RequestContext.java|RequestContext.java]]
- [[_COMMUNITY_TaskResumeResponse|TaskResumeResponse]]
- [[_COMMUNITY_PagingList.java|PagingList.java]]
- [[_COMMUNITY_UploadPolicy.java|UploadPolicy.java]]
- [[_COMMUNITY_AsyncResultRequest|AsyncResultRequest]]
- [[_COMMUNITY_McpServerCallToolRequest.java|McpServerCallToolRequest.java]]
- [[_COMMUNITY_TaskPartGraphResponse|TaskPartGraphResponse]]
- [[_COMMUNITY_Workspace|Workspace]]
- [[_COMMUNITY_AppConfig|AppConfig]]
- [[_COMMUNITY_ApiTaskRunRequest|ApiTaskRunRequest]]
- [[_COMMUNITY_InitRequest|InitRequest]]
- [[_COMMUNITY_Refer.java|Refer.java]]
- [[_COMMUNITY_UpdateProviderRequest.java|UpdateProviderRequest.java]]
- [[_COMMUNITY_AddModelRequest.java|AddModelRequest.java]]
- [[_COMMUNITY_UpdateModelRequest.java|UpdateModelRequest.java]]
- [[_COMMUNITY_AddProviderRequest.java|AddProviderRequest.java]]
- [[_COMMUNITY_QueryProviderRequest.java|QueryProviderRequest.java]]

## God Nodes (most connected - your core abstractions)
1. `ToolsExample` - 20 edges
2. `ApiKey` - 13 edges
3. `Model` - 12 edges
4. `JsonUtils` - 10 edges
5. `BizException` - 4 edges
6. `Result` - 4 edges
7. `CalculatorTools` - 4 edges
8. `CustomToolCallbackProvider` - 4 edges
9. `Edge` - 4 edges
10. `toError()` - 4 edges

## Surprising Connections (you probably didn't know these)
- `BizException` --implements--> `Serializable`  [EXTRACTED]
  exception/BizException.java →   _Bridges community 13 → community 0_
- `PagingList` --implements--> `Serializable`  [EXTRACTED]
  domain/PagingList.java →   _Bridges community 0 → community 67_
- `Error` --implements--> `Serializable`  [EXTRACTED]
  domain/Error.java →   _Bridges community 0 → community 61_
- `Result` --implements--> `Serializable`  [EXTRACTED]
  domain/Result.java →   _Bridges community 0 → community 5_
- `RequestContext` --implements--> `Serializable`  [EXTRACTED]
  domain/RequestContext.java →   _Bridges community 0 → community 65_

## Communities (116 total, 65 thin omitted)

### Community 0 - "LoginRequest"
Cohesion: 0.08
Nodes (21): LoginRequest, RefreshTokenRequest, AgentRequest, Application, FileSearchOptions, AudioOutput, MultimodalContent, Usage (+13 more)

### Community 1 - "Document.java"
Cohesion: 0.06
Nodes (17): Document, Metadata, AccountInfoTool, CalculatorFunction, CalculatorFunctionWithContext, CalculatorFunctionWithRequest, CalculatorRequest, ConversationSummaryTool (+9 more)

### Community 2 - "ApiKey"
Cohesion: 0.2
Nodes (4): ApiKey, Config, Model, ToolsExample

### Community 3 - "CommonParam"
Cohesion: 0.16
Nodes (9): CommonParam, TaskPartGraphRequest, TaskResumeRequest, TaskRunParam, TryCatchConfig, InputParam, Node, NodeCustomConfig (+1 more)

### Community 4 - "AppQuery"
Cohesion: 0.23
Nodes (7): AppQuery, KnowledgeBaseQuery, BaseQuery, AppComponentQuery, AppComponentRequest, DocumentQuery, ToolQuery

### Community 5 - "Result.java"
Cohesion: 0.2
Nodes (4): Result, getMessage(), toError(), ExceptionUtils

### Community 7 - "AgentConfig"
Cohesion: 0.22
Nodes (8): AgentConfig, McpServer, Memory, Parameter, Prologue, PromptVariable, Tool, AppConfig

### Community 8 - "NodeResult.java"
Cohesion: 0.29
Nodes (5): MultiBranchReference, NodeResult, Retry, ShortMemory, TryCatch

### Community 10 - "AppComponentConfig"
Cohesion: 0.4
Nodes (4): AppComponentConfig, Input, Params, UserParams

### Community 11 - "WebUploadPolicy.java"
Cohesion: 0.4
Nodes (3): WebUploadPolicy, CreateDocumentRequest, UploadPolicy

### Community 14 - "ModelConfig.java"
Cohesion: 0.5
Nodes (3): ModelConfig, ModelParam, SkillConfig

## Knowledge Gaps
- **17 isolated node(s):** `ApiConstants`, `McpQuery`, `Tool`, `ToolExecutionRequest`, `AppConfig` (+12 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **65 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ToolsExample` connect `ApiKey` to `Document.java`?**
  _High betweenness centrality (0.099) - this node is a cross-community bridge._
- **Why does `ApiKey` connect `ApiKey` to `LoginRequest`?**
  _High betweenness centrality (0.071) - this node is a cross-community bridge._
- **Why does `Model` connect `ApiKey` to `LoginRequest`?**
  _High betweenness centrality (0.064) - this node is a cross-community bridge._
- **Are the 11 inferred relationships involving `ApiKey` (e.g. with `.addToolToChatClient()` and `.accessingContext()`) actually correct?**
  _`ApiKey` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Are the 10 inferred relationships involving `Model` (e.g. with `.accessingContext()` and `.accessingMemoryStore()`) actually correct?**
  _`Model` has 10 INFERRED edges - model-reasoned connections that need verification._
- **What connects `ApiConstants`, `McpQuery`, `Tool` to the rest of the system?**
  _17 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `LoginRequest` be split into smaller, more focused modules?**
  _Cohesion score 0.08 - nodes in this community are weakly interconnected._