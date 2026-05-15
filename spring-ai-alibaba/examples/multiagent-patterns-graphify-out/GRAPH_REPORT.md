# Graph Report - /workspace/examples/multiagent-patterns  (2026-05-13)

## Corpus Check
- Corpus is ~25,550 words - fits in a single context window. You may not need a graph.

## Summary
- 321 nodes · 329 edges · 46 communities (8 shown, 38 thin omitted)
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 14 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Tools (Support & SQL)|Tools (Support & SQL)]]
- [[_COMMUNITY_Simple Routing Pattern|Simple Routing Pattern]]
- [[_COMMUNITY_Graph Routing Pattern|Graph Routing Pattern]]
- [[_COMMUNITY_Supervisor Pattern|Supervisor Pattern]]
- [[_COMMUNITY_RAG Agent Pattern|RAG Agent Pattern]]
- [[_COMMUNITY_Handoffs Pattern|Handoffs Pattern]]
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

## God Nodes (most connected - your core abstractions)
1. `SupportTools` - 12 edges
2. `SqlTools` - 11 edges
3. `RouterService` - 8 edges
4. `RoutingGraphConfig` - 7 edges
5. `SupervisorConfig` - 7 edges
6. `RoutingConfig` - 6 edges
7. `RagAgentConfig` - 6 edges
8. `HandoffsSupportHook` - 6 edges
9. `StepConfigInterceptor` - 6 edges
10. `AgentStaticLoader` - 5 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Communities (46 total, 38 thin omitted)

### Community 0 - "Tools (Support & SQL)"
Cohesion: 0.06
Nodes (9): AgentLoader, AgentStaticLoader, PipelineAgentLoaderConfig, AgentStaticLoader, AgentStaticLoader, AgentStaticLoader, AgentStaticLoader, AgentStaticLoader (+1 more)

### Community 1 - "Simple Routing Pattern"
Cohesion: 0.09
Nodes (8): ApplicationRunner, RoutingGraphRunner, MultiAgentHandoffsRunner, RoutingRunner, HandoffsRunner, SkillsRunner, SubagentRunner, SupervisorRunner

### Community 2 - "Graph Routing Pattern"
Cohesion: 0.11
Nodes (8): CallGetSchemaNode, ListTablesNode, PostprocessNode, PrepareAgentNode, PreprocessNode, RetrieveNode, RewriteNode, NodeAction

### Community 5 - "Handoffs Pattern"
Cohesion: 0.19
Nodes (4): ModelHook, ModelInterceptor, HandoffsSupportHook, StepConfigInterceptor

### Community 6 - "Community 6"
Cohesion: 0.27
Nodes (4): AsyncCommandAction, RouteAfterSalesAction, RouteAfterSupportAction, RouteInitialAction

## Knowledge Gaps
- **38 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `CallGetSchemaNode` connect `Graph Routing Pattern` to `Supervisor Pattern`?**
  _High betweenness centrality (0.008) - this node is a cross-community bridge._
- **Why does `PrepareAgentNode` connect `Graph Routing Pattern` to `Community 9`?**
  _High betweenness centrality (0.007) - this node is a cross-community bridge._
- **Should `Tools (Support & SQL)` be split into smaller, more focused modules?**
  _Cohesion score 0.06 - nodes in this community are weakly interconnected._
- **Should `Simple Routing Pattern` be split into smaller, more focused modules?**
  _Cohesion score 0.09 - nodes in this community are weakly interconnected._
- **Should `Graph Routing Pattern` be split into smaller, more focused modules?**
  _Cohesion score 0.11 - nodes in this community are weakly interconnected._
- **Should `Supervisor Pattern` be split into smaller, more focused modules?**
  _Cohesion score 0.14 - nodes in this community are weakly interconnected._