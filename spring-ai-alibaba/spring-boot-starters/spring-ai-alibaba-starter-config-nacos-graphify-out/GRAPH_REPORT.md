# Graph Report - /workspace/spring-boot-starters/spring-ai-alibaba-starter-config-nacos  (2026-05-13)

## Corpus Check
- Corpus is ~13,092 words - fits in a single context window. You may not need a graph.

## Summary
- 352 nodes · 589 edges · 16 communities (7 shown, 9 thin omitted)
- Extraction: 79% EXTRACTED · 21% INFERRED · 0% AMBIGUOUS · INFERRED: 126 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Core Builders & Context|Core Builders & Context]]
- [[_COMMUNITY_Nacos Options & Injectors|Nacos Options & Injectors]]
- [[_COMMUNITY_MCP Tools Injector|MCP Tools Injector]]
- [[_COMMUNITY_Utils & Value Objects|Utils & Value Objects]]
- [[_COMMUNITY_Tool Callbacks & Memory|Tool Callbacks & Memory]]
- [[_COMMUNITY_Tests & Hooks|Tests & Hooks]]
- [[_COMMUNITY_Encryption Utils|Encryption Utils]]
- [[_COMMUNITY_Config Refresh Listener|Config Refresh Listener]]
- [[_COMMUNITY_Configuration Properties|Configuration Properties]]
- [[_COMMUNITY_Auto Configuration|Auto Configuration]]
- [[_COMMUNITY_Interceptor Tests|Interceptor Tests]]
- [[_COMMUNITY_MCP Tool Definition|MCP Tool Definition]]
- [[_COMMUNITY_Agent Factories|Agent Factories]]
- [[_COMMUNITY_Agent Value Object|Agent Value Object]]
- [[_COMMUNITY_Model Injector|Model Injector]]
- [[_COMMUNITY_Agent Configuration|Agent Configuration]]

## God Nodes (most connected - your core abstractions)
1. `NacosOptions` - 27 edges
2. `NacosReactAgentBuilderToolsTest` - 24 edges
3. `NacosMcpGatewayToolDefinition` - 23 edges
4. `NacosReactAgentBuilderInterceptorTest` - 20 edges
5. `NacosContextHolder` - 15 edges
6. `McpGatewayToolDefinition` - 15 edges
7. `NacosMcpGatewayToolCallback` - 13 edges
8. `MemoryVO` - 11 edges
9. `ModelVO` - 11 edges
10. `McpServerVO` - 11 edges

## Surprising Connections (you probably didn't know these)
- `NacosMcpGatewayToolCallback` --implements--> `ToolCallback`  [EXTRACTED]
  main/java/com/alibaba/cloud/ai/agent/nacos/tools/NacosMcpGatewayToolCallback.java →   _Bridges community 4 → community 2_
- `TestHookWithTools` --implements--> `Hook`  [EXTRACTED]
  test/java/com/alibaba/cloud/ai/agent/nacos/NacosReactAgentBuilderToolsTest.java →   _Bridges community 5 → community 8_

## Communities (16 total, 9 thin omitted)

### Community 0 - "Core Builders & Context"
Cohesion: 0.06
Nodes (7): AbstractListener, DefaultBuilder, NacosAgentPromptBuilder, NacosContextHolder, AgentBaseListener, PromptListener, ObservationConfiguration

### Community 1 - "Nacos Options & Injectors"
Cohesion: 0.06
Nodes (6): NacosAgentInjector, NacosOptions, NacosPartnerAgentsInjector, NacosPromptInjector, NacosReactAgentBuilder, NacosAgentPromptBuilder

### Community 2 - "MCP Tools Injector"
Cohesion: 0.07
Nodes (6): NacosMcpToolsInjector, ToolCallback, Builder, NacosMcpGatewayToolsInitializer, McpServersVO, McpServerVO

### Community 3 - "Utils & Value Objects"
Cohesion: 0.09
Nodes (5): MethodInterceptor, CglibMethodInterceptor, ChatOptionsProxy, ModelVO, PromptVO

### Community 5 - "Tests & Hooks"
Cohesion: 0.1
Nodes (7): Hook, ModelInterceptor, EchoFunction, TestHookWithTools, TestModelInterceptor, TestToolInterceptor, ToolInterceptor

### Community 8 - "Configuration Properties"
Cohesion: 0.12
Nodes (6): EchoFunction, SimpleToolCallbackResolver, TestHookWithTools, TestToolClass, ToolCallbackProvider, ToolCallbackResolver

### Community 12 - "Agent Factories"
Cohesion: 0.28
Nodes (3): AgentBuilderFactory, NacosAgentBuilderFactory, NacosAgentPromptBuilderFactory

## Knowledge Gaps
- **9 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `NacosMcpGatewayToolCallback` connect `Tool Callbacks & Memory` to `Auto Configuration`, `MCP Tools Injector`, `Tests & Hooks`, `Config Refresh Listener`?**
  _High betweenness centrality (0.149) - this node is a cross-community bridge._
- **Why does `NacosOptions` connect `Nacos Options & Injectors` to `Core Builders & Context`, `Agent Configuration`?**
  _High betweenness centrality (0.129) - this node is a cross-community bridge._
- **Why does `NacosReactAgentBuilderInterceptorTest` connect `Interceptor Tests` to `Nacos Options & Injectors`, `Utils & Value Objects`, `Tool Callbacks & Memory`, `Tests & Hooks`?**
  _High betweenness centrality (0.112) - this node is a cross-community bridge._
- **Should `Core Builders & Context` be split into smaller, more focused modules?**
  _Cohesion score 0.06 - nodes in this community are weakly interconnected._
- **Should `Nacos Options & Injectors` be split into smaller, more focused modules?**
  _Cohesion score 0.06 - nodes in this community are weakly interconnected._
- **Should `MCP Tools Injector` be split into smaller, more focused modules?**
  _Cohesion score 0.07 - nodes in this community are weakly interconnected._
- **Should `Utils & Value Objects` be split into smaller, more focused modules?**
  _Cohesion score 0.09 - nodes in this community are weakly interconnected._