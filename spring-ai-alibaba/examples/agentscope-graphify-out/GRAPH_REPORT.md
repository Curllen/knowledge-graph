# Graph Report - /workspace/examples/agentscope  (2026-05-13)

## Corpus Check
- Corpus is ~3,323 words - fits in a single context window. You may not need a graph.

## Summary
- 48 nodes · 44 edges · 9 communities (1 shown, 8 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Config & Tools|Config & Tools]]
- [[_COMMUNITY_Routing Actions|Routing Actions]]
- [[_COMMUNITY_Core Application|Core Application]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]

## God Nodes (most connected - your core abstractions)
1. `AgentScopeHandoffsConfig` - 5 edges
2. `UpdateExtraStateTool` - 5 edges
3. `AgentScopeHandoffsRunner` - 4 edges
4. `TransferToSalesTool` - 4 edges
5. `TransferToSupportTool` - 4 edges
6. `AgentScopeApplication` - 3 edges
7. `AgentScopeHandoffsService` - 3 edges
8. `RouteAfterSupportAction` - 3 edges
9. `RouteInitialAction` - 3 edges
10. `RouteAfterSalesAction` - 3 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Communities (9 total, 8 thin omitted)

### Community 0 - "Config & Tools"
Cohesion: 0.27
Nodes (4): AsyncCommandAction, RouteAfterSalesAction, RouteAfterSupportAction, RouteInitialAction

## Knowledge Gaps
- **8 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Not enough signal to generate questions. This usually means the corpus has no AMBIGUOUS edges, no bridge nodes, no INFERRED relationships, and all communities are tightly cohesive. Add more files or run with --mode deep to extract richer edges._