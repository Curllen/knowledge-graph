# Graph Report - /workspace/examples/deepresearch  (2026-05-13)

## Corpus Check
- Corpus is ~2,053 words - fits in a single context window. You may not need a graph.

## Summary
- 19 nodes · 21 edges · 4 communities (0 shown, 4 thin omitted)
- Extraction: 95% EXTRACTED · 5% INFERRED · 0% AMBIGUOUS · INFERRED: 1 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_DeepResearch Agent|DeepResearch Agent]]
- [[_COMMUNITY_Static Loader|Static Loader]]
- [[_COMMUNITY_Application|Application]]
- [[_COMMUNITY_Prompts|Prompts]]

## God Nodes (most connected - your core abstractions)
1. `DeepResearchAgent` - 6 edges
2. `AgentStaticLoader` - 5 edges
3. `Application` - 4 edges
4. `Prompts` - 1 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Communities (4 total, 4 thin omitted)

## Knowledge Gaps
- **1 isolated node(s):** `Prompts`
  These have ≤1 connection - possible missing edges or undocumented components.
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `DeepResearchAgent` connect `DeepResearch Agent` to `Prompts`?**
  _High betweenness centrality (0.258) - this node is a cross-community bridge._
- **What connects `Prompts` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._