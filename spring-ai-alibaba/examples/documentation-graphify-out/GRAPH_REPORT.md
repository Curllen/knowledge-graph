# Graph Report - /workspace/examples/documentation  (2026-05-13)

## Corpus Check
- Corpus is ~41,621 words - fits in a single context window. You may not need a graph.

## Summary
- 700 nodes · 1026 edges · 50 communities (14 shown, 36 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 34 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Messages & Tools Examples|Messages & Tools Examples]]
- [[_COMMUNITY_Agents Examples|Agents Examples]]
- [[_COMMUNITY_Hooks & Models|Hooks & Models]]
- [[_COMMUNITY_Workflow Examples|Workflow Examples]]
- [[_COMMUNITY_MultiAgent Examples|MultiAgent Examples]]
- [[_COMMUNITY_HumanInTheLoop Examples|HumanInTheLoop Examples]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 14|Community 14]]
- [[_COMMUNITY_Community 15|Community 15]]
- [[_COMMUNITY_Community 16|Community 16]]
- [[_COMMUNITY_Community 17|Community 17]]
- [[_COMMUNITY_Community 18|Community 18]]
- [[_COMMUNITY_Community 19|Community 19]]
- [[_COMMUNITY_Community 20|Community 20]]
- [[_COMMUNITY_Community 21|Community 21]]
- [[_COMMUNITY_Community 22|Community 22]]
- [[_COMMUNITY_Community 23|Community 23]]
- [[_COMMUNITY_Community 24|Community 24]]
- [[_COMMUNITY_Community 25|Community 25]]
- [[_COMMUNITY_Community 26|Community 26]]
- [[_COMMUNITY_Community 27|Community 27]]
- [[_COMMUNITY_Community 28|Community 28]]
- [[_COMMUNITY_Community 29|Community 29]]
- [[_COMMUNITY_Community 30|Community 30]]
- [[_COMMUNITY_Community 31|Community 31]]
- [[_COMMUNITY_Community 32|Community 32]]
- [[_COMMUNITY_Community 33|Community 33]]
- [[_COMMUNITY_Community 34|Community 34]]
- [[_COMMUNITY_Community 35|Community 35]]
- [[_COMMUNITY_Community 36|Community 36]]
- [[_COMMUNITY_Community 37|Community 37]]
- [[_COMMUNITY_Community 38|Community 38]]
- [[_COMMUNITY_Community 39|Community 39]]
- [[_COMMUNITY_Community 40|Community 40]]
- [[_COMMUNITY_Community 41|Community 41]]
- [[_COMMUNITY_Community 42|Community 42]]
- [[_COMMUNITY_Community 43|Community 43]]
- [[_COMMUNITY_Community 44|Community 44]]
- [[_COMMUNITY_Community 45|Community 45]]
- [[_COMMUNITY_Community 46|Community 46]]
- [[_COMMUNITY_Community 47|Community 47]]
- [[_COMMUNITY_Community 48|Community 48]]
- [[_COMMUNITY_Community 49|Community 49]]

## God Nodes (most connected - your core abstractions)
1. `MessagesExample` - 24 edges
2. `ToolsExample` - 20 edges
3. `AgentsExample` - 18 edges
4. `HooksExample` - 17 edges
5. `ModelsExample` - 15 edges
6. `WorkflowExample` - 15 edges
7. `MultiAgentExample` - 14 edges
8. `HumanInTheLoopExample` - 13 edges
9. `HumanInTheLoopExample` - 12 edges
10. `StructuredOutputExample` - 12 edges

## Surprising Connections (you probably didn't know these)
- `ReadEmailNode` --implements--> `NodeAction`  [EXTRACTED]
  graph/QuickStartExample.java →   _Bridges community 16 → community 0_
- `ClassifyIntentNode` --implements--> `NodeAction`  [EXTRACTED]
  graph/QuickStartExample.java →   _Bridges community 0 → community 4_
- `SupervisorNode` --implements--> `NodeAction`  [EXTRACTED]
  graph/examples/MultiAgentSupervisorExample.java →   _Bridges community 0 → community 5_
- `ParallelResultAggregatorNode` --implements--> `NodeAction`  [EXTRACTED]
  framework/advanced/WorkflowExample.java →   _Bridges community 0 → community 6_
- `ToolMonitoringInterceptor` --extends--> `ToolInterceptor`  [EXTRACTED]
  framework/tutorials/HooksExample.java →   _Bridges community 21 → community 18_

## Communities (50 total, 36 thin omitted)

### Community 0 - "Messages & Tools Examples"
Cohesion: 0.05
Nodes (14): ProcessStreamingNode, StreamingExample, StreamingNode, LlmStreamingSpringAiExample, StreamingAgentNode, McpNode, McpNodeExample, CompiledSubGraphNode (+6 more)

### Community 1 - "Agents Examples"
Cohesion: 0.05
Nodes (16): RemoteMcpToolsExample, RemoteMcpToolsExampleController, ToolCallbackProvider, AccountInfoTool, CalculatorFunction, CalculatorFunctionWithContext, CalculatorFunctionWithRequest, CalculatorRequest (+8 more)

### Community 2 - "Hooks & Models"
Cohesion: 0.08
Nodes (5): PersistenceExample, CheckpointRedisExample, PersistenceExample, TimeTravelExample, TimeTravelRedisExample

### Community 3 - "Workflow Examples"
Cohesion: 0.07
Nodes (10): MemoryExample, MessagesModelHook, MessageTrimmingHook, MessageTrimmingHook, ClearAllMessagesHook, CustomMemoryHook, MessageDeletionHook, MessageSummarizationHook (+2 more)

### Community 4 - "MultiAgent Examples"
Cohesion: 0.1
Nodes (8): BugTrackingNode, ClassifyIntentNode, DraftResponseNode, EmailClassification, HumanReviewNode, QuickStartExample, SearchDocumentationNode, SendReplyNode

### Community 5 - "HumanInTheLoop Examples"
Cohesion: 0.09
Nodes (8): CodeRequest, CoderNode, CoderTool, MultiAgentSupervisorExample, ResearcherNode, SearchRequest, SearchTool, SupervisorNode

### Community 6 - "Community 6"
Cohesion: 0.11
Nodes (4): A2AExample, ParallelResultAggregatorNode, WorkflowExample, WeatherFunction

### Community 10 - "Community 10"
Cohesion: 0.19
Nodes (4): AsyncNodeActionWithConfig, HumanInTheLoopExample, InterruptableNodeAction, InterruptableAction

### Community 13 - "Community 13"
Cohesion: 0.16
Nodes (3): ToolSelectionExample, TravelTools, UtilityTools

### Community 16 - "Community 16"
Cohesion: 0.17
Nodes (3): RAGExample, ReadEmailNode, CalculatorTools

### Community 18 - "Community 18"
Cohesion: 0.16
Nodes (4): ModelHook, CustomModelHook, LoggingModelHook, ToolMonitoringInterceptor

### Community 21 - "Community 21"
Cohesion: 0.23
Nodes (4): ToolInterceptor, SearchTool, ToolErrorInterceptor, ToolMonitoringInterceptor

### Community 22 - "Community 22"
Cohesion: 0.18
Nodes (4): ModelInterceptor, DynamicPromptInterceptor, GuardrailInterceptor, LoggingInterceptor

### Community 24 - "Community 24"
Cohesion: 0.2
Nodes (3): AgentHook, LoggingHook, CustomAgentHook

## Knowledge Gaps
- **36 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `CalculatorTools` connect `Community 16` to `Agents Examples`?**
  _High betweenness centrality (0.078) - this node is a cross-community bridge._
- **Should `Messages & Tools Examples` be split into smaller, more focused modules?**
  _Cohesion score 0.05 - nodes in this community are weakly interconnected._
- **Should `Agents Examples` be split into smaller, more focused modules?**
  _Cohesion score 0.05 - nodes in this community are weakly interconnected._
- **Should `Hooks & Models` be split into smaller, more focused modules?**
  _Cohesion score 0.08 - nodes in this community are weakly interconnected._
- **Should `Workflow Examples` be split into smaller, more focused modules?**
  _Cohesion score 0.07 - nodes in this community are weakly interconnected._
- **Should `MultiAgent Examples` be split into smaller, more focused modules?**
  _Cohesion score 0.1 - nodes in this community are weakly interconnected._
- **Should `HumanInTheLoop Examples` be split into smaller, more focused modules?**
  _Cohesion score 0.09 - nodes in this community are weakly interconnected._