# Graph Report - /workspace/spring-boot-starters/spring-ai-alibaba-starter-graph-observation  (2026-05-13)

## Corpus Check
- Corpus is ~1,987 words - fits in a single context window. You may not need a graph.

## Summary
- 38 nodes · 39 edges · 6 communities (0 shown, 6 thin omitted)
- Extraction: 95% EXTRACTED · 5% INFERRED · 0% AMBIGUOUS · INFERRED: 2 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Test Cases|Test Cases]]
- [[_COMMUNITY_Auto Configuration|Auto Configuration]]
- [[_COMMUNITY_Observation Handlers|Observation Handlers]]
- [[_COMMUNITY_Properties Configuration|Properties Configuration]]
- [[_COMMUNITY_Observation Convention|Observation Convention]]
- [[_COMMUNITY_Test Configurations|Test Configurations]]

## God Nodes (most connected - your core abstractions)
1. `GraphObservationAutoConfigurationTest` - 13 edges
2. `GraphObservationAutoConfiguration` - 5 edges
3. `ObservationHandlersConfiguration` - 4 edges
4. `SpringAiAlibabaChatModelObservationConvention` - 4 edges
5. `GraphObservationProperties` - 3 edges
6. `TestConfiguration` - 3 edges
7. `TestConfigurationWithMeterRegistry` - 3 edges
8. `ObservationThreadLocalAccessorRegistrar` - 1 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Communities (6 total, 6 thin omitted)

## Knowledge Gaps
- **1 isolated node(s):** `ObservationThreadLocalAccessorRegistrar`
  These have ≤1 connection - possible missing edges or undocumented components.
- **6 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `GraphObservationAutoConfigurationTest` connect `Test Cases` to `Properties Configuration`, `Test Configurations`?**
  _High betweenness centrality (0.550) - this node is a cross-community bridge._
- **Why does `TestConfiguration` connect `Test Configurations` to `Auto Configuration`?**
  _High betweenness centrality (0.360) - this node is a cross-community bridge._
- **Why does `GraphObservationAutoConfiguration` connect `Auto Configuration` to `Observation Handlers`?**
  _High betweenness centrality (0.342) - this node is a cross-community bridge._
- **What connects `ObservationThreadLocalAccessorRegistrar` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._