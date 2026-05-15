# Graph Report - /workspace/examples/multimodal  (2026-05-13)

## Corpus Check
- Corpus is ~15,734 words - fits in a single context window. You may not need a graph.

## Summary
- 47 nodes · 46 edges · 10 communities (0 shown, 10 thin omitted)
- Extraction: 85% EXTRACTED · 15% INFERRED · 0% AMBIGUOUS · INFERRED: 7 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Multimodal Controller|Multimodal Controller]]
- [[_COMMUNITY_Image Service|Image Service]]
- [[_COMMUNITY_Audio Service|Audio Service]]
- [[_COMMUNITY_Creative Service|Creative Service]]
- [[_COMMUNITY_Tools|Tools]]
- [[_COMMUNITY_Config|Config]]
- [[_COMMUNITY_Exception Handler|Exception Handler]]
- [[_COMMUNITY_Application|Application]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]

## God Nodes (most connected - your core abstractions)
1. `MultimodalController` - 9 edges
2. `ImageService` - 6 edges
3. `AudioService` - 5 edges
4. `MultimodalExceptionHandler` - 4 edges
5. `GenerateImageTool` - 3 edges
6. `CreativeService` - 3 edges
7. `MultimodalApplication` - 2 edges
8. `ImageConfig` - 2 edges
9. `CreativeConfig` - 2 edges
10. `AudioConfig` - 1 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Communities (10 total, 10 thin omitted)

## Knowledge Gaps
- **1 isolated node(s):** `AudioConfig`
  These have ≤1 connection - possible missing edges or undocumented components.
- **10 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `MultimodalController` connect `Image Service` to `Multimodal Controller`, `Audio Service`, `Tools`?**
  _High betweenness centrality (0.240) - this node is a cross-community bridge._
- **Why does `ImageService` connect `Multimodal Controller` to `Image Service`?**
  _High betweenness centrality (0.076) - this node is a cross-community bridge._
- **What connects `AudioConfig` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._