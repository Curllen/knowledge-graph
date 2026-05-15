# Graph Report - /workspace/spring-boot-starters/spring-ai-alibaba-starter-agentscope  (2026-05-13)

## Corpus Check
- Corpus is ~8,982 words - fits in a single context window. You may not need a graph.

## Summary
- 128 nodes · 268 edges · 11 communities (5 shown, 6 thin omitted)
- Extraction: 57% EXTRACTED · 43% INFERRED · 0% AMBIGUOUS · INFERRED: 114 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Agent Tests & Routing|Agent Tests & Routing]]
- [[_COMMUNITY_Agent Builder & Action|Agent Builder & Action]]
- [[_COMMUNITY_Agent Core & Tests|Agent Core & Tests]]
- [[_COMMUNITY_Graph Building Strategy|Graph Building Strategy]]
- [[_COMMUNITY_Routing Agent & Builder|Routing Agent & Builder]]
- [[_COMMUNITY_Message Utils|Message Utils]]
- [[_COMMUNITY_Routing Merge Node|Routing Merge Node]]
- [[_COMMUNITY_Routing Node Logic|Routing Node Logic]]
- [[_COMMUNITY_Routing Schema|Routing Schema]]
- [[_COMMUNITY_Auto Configuration|Auto Configuration]]
- [[_COMMUNITY_Update Extra State Tool|Update Extra State Tool]]

## God Nodes (most connected - your core abstractions)
1. `AgentScopeAgentBuilder` - 13 edges
2. `AgentScopeMessageUtils` - 11 edges
3. `AgentScopeAgent` - 9 edges
4. `AgentScopeRoutingNode` - 9 edges
5. `AgentScopeRoutingGraphBuildingStrategy` - 9 edges
6. `AgentScopeRoutingAgent` - 9 edges
7. `AgentScopeRoutingAgentBuilder` - 8 edges
8. `AgentScopeRoutingMergeNode` - 8 edges
9. `ReActAgentNodeAction` - 7 edges
10. `StandaloneTests` - 5 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Communities (11 total, 6 thin omitted)

### Community 0 - "Agent Tests & Routing"
Cohesion: 0.23
Nodes (3): GraphAgentScopeToolContextTests, SequentialIntegrationTests, AgentScopeRoutingAgentTest

### Community 1 - "Agent Builder & Action"
Cohesion: 0.15
Nodes (3): AgentScopeAgentBuilder, ReActAgentNodeAction, NodeActionWithConfig

### Community 2 - "Agent Core & Tests"
Cohesion: 0.29
Nodes (3): AgentScopeAgentTest, AsNodeTests, StandaloneTests

### Community 3 - "Graph Building Strategy"
Cohesion: 0.16
Nodes (4): AbstractFlowGraphBuildingStrategy, AgentScopeAgent, BaseAgent, AgentScopeRoutingGraphBuildingStrategy

### Community 4 - "Routing Agent & Builder"
Cohesion: 0.15
Nodes (3): AgentScopeRoutingAgent, AgentScopeRoutingAgentBuilder, FlowAgent

## Knowledge Gaps
- **6 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `AgentScopeAgentBuilder` connect `Agent Builder & Action` to `Agent Tests & Routing`, `Agent Core & Tests`?**
  _High betweenness centrality (0.116) - this node is a cross-community bridge._
- **Why does `AgentScopeRoutingAgent` connect `Routing Agent & Builder` to `Agent Tests & Routing`, `Graph Building Strategy`?**
  _High betweenness centrality (0.099) - this node is a cross-community bridge._
- **Why does `AgentScopeRoutingAgentBuilder` connect `Routing Agent & Builder` to `Agent Tests & Routing`?**
  _High betweenness centrality (0.085) - this node is a cross-community bridge._