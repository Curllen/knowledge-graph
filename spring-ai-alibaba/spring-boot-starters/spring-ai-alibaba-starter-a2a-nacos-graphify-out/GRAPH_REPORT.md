# Graph Report - /workspace/spring-boot-starters/spring-ai-alibaba-starter-a2a-nacos  (2026-05-13)

## Corpus Check
- Corpus is ~10,847 words - fits in a single context window. You may not need a graph.

## Summary
- 298 nodes · 436 edges · 19 communities (9 shown, 10 thin omitted)
- Extraction: 79% EXTRACTED · 21% INFERRED · 0% AMBIGUOUS · INFERRED: 92 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
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

## God Nodes (most connected - your core abstractions)
1. `A2aAgentCardProperties` - 29 edges
2. `NacosA2aProperties` - 22 edges
3. `A2aServerProperties` - 16 edges
4. `AgentCardConverterUtil` - 16 edges
5. `A2aServerMultiAgentAutoConfiguration` - 14 edges
6. `A2aServerAgentCardAutoConfiguration` - 11 edges
7. `GraphAgentExecutor` - 11 edges
8. `A2aClientAgentCardProperties` - 10 edges
9. `A2aServerHandlerAutoConfiguration` - 10 edges
10. `JsonRpcA2aRequestHandler` - 10 edges

## Surprising Connections (you probably didn't know these)
- `A2aServerProperties` --implements--> `EnvironmentAware`  [EXTRACTED]
  main/java/com/alibaba/cloud/ai/a2a/autoconfigure/A2aServerProperties.java →   _Bridges community 4 → community 1_
- `A2aClientAgentCardProperties` --extends--> `A2aAgentCardProperties`  [EXTRACTED]
  main/java/com/alibaba/cloud/ai/a2a/autoconfigure/A2aClientAgentCardProperties.java →   _Bridges community 12 → community 3_

## Communities (19 total, 10 thin omitted)

### Community 1 - "Community 1"
Cohesion: 0.06
Nodes (7): A2aClientAgentCardWellKnownCondition, OnMultiAgentModeCondition, EnvironmentAware, NacosA2aDiscoveryAutoConfiguration, NacosA2aRegistryAutoConfiguration, NacosA2aProperties, SpringBootCondition

### Community 2 - "Community 2"
Cohesion: 0.08
Nodes (4): A2aMultiAgentProperties, MultiAgentRequestRouter, A2aServerMultiAgentAutoConfiguration, A2aServerMultiAgentAutoConfigurationTest

### Community 3 - "Community 3"
Cohesion: 0.11
Nodes (7): A2aAgentCardProperties, A2aServerExecutorProvider, AgentExecutor, A2aServerAgentCardProperties, DefaultA2aServerExecutorProvider, GraphAgentExecutor, ReactAgentNodeOutputConsumer

### Community 4 - "Community 4"
Cohesion: 0.12
Nodes (3): A2aServerProperties, A2aServerAutoConfiguration, InetUtils

### Community 6 - "Community 6"
Cohesion: 0.11
Nodes (5): AgentRegistry, NacosA2aRegistryProperties, NacosAgentRegistry, A2aServerRegistryAutoConfiguration, NacosA2aOperationService

### Community 7 - "Community 7"
Cohesion: 0.22
Nodes (3): A2aRequestHandler, A2aRouterProvider, JsonRpcA2aRequestHandler

### Community 8 - "Community 8"
Cohesion: 0.2
Nodes (5): AgentCardProvider, AgentCardWrapper, A2aClientAgentCardProviderAutoConfiguration, NacosAgentCardProvider, NacosAgentCardWrapper

### Community 9 - "Community 9"
Cohesion: 0.19
Nodes (3): MultiAgentCardHandler, MultiAgentJsonRpcRouterProvider, MultiAgentMessageHandler

### Community 10 - "Community 10"
Cohesion: 0.2
Nodes (3): AgentCardHandler, JsonRpcA2aRouterProvider, MessageHandler

## Knowledge Gaps
- **1 isolated node(s):** `A2aConstants`
  These have ≤1 connection - possible missing edges or undocumented components.
- **10 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `NacosA2aProperties` connect `Community 1` to `Community 6`?**
  _High betweenness centrality (0.187) - this node is a cross-community bridge._
- **Why does `A2aServerMultiAgentAutoConfiguration` connect `Community 2` to `Community 3`, `Community 5`?**
  _High betweenness centrality (0.172) - this node is a cross-community bridge._
- **Why does `A2aServerProperties` connect `Community 4` to `Community 1`?**
  _High betweenness centrality (0.114) - this node is a cross-community bridge._
- **What connects `A2aConstants` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.08 - nodes in this community are weakly interconnected._
- **Should `Community 1` be split into smaller, more focused modules?**
  _Cohesion score 0.06 - nodes in this community are weakly interconnected._
- **Should `Community 2` be split into smaller, more focused modules?**
  _Cohesion score 0.08 - nodes in this community are weakly interconnected._