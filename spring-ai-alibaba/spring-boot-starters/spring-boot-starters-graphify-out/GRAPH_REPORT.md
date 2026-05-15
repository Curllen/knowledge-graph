# Graph Report - /workspace/spring-boot-starters  (2026-05-13)

## Corpus Check
- 130 files · ~69,511 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1418 nodes · 2407 edges · 93 communities (37 shown, 56 thin omitted)
- Extraction: 72% EXTRACTED · 28% INFERRED · 0% AMBIGUOUS · INFERRED: 665 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_TemplateTransform & Test|TemplateTransform & Test]]
- [[_COMMUNITY_CodeExecution|CodeExecution]]
- [[_COMMUNITY_AgentScope|AgentScope]]
- [[_COMMUNITY_Nacos Config|Nacos Config]]
- [[_COMMUNITY_Nacos Tests|Nacos Tests]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Builders|Builders]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_A2a Properties|A2a Properties]]
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
- [[_COMMUNITY_Community 50|Community 50]]
- [[_COMMUNITY_Community 51|Community 51]]
- [[_COMMUNITY_Community 52|Community 52]]
- [[_COMMUNITY_Community 53|Community 53]]
- [[_COMMUNITY_Community 54|Community 54]]
- [[_COMMUNITY_Community 55|Community 55]]
- [[_COMMUNITY_Community 56|Community 56]]
- [[_COMMUNITY_Community 58|Community 58]]
- [[_COMMUNITY_Community 59|Community 59]]
- [[_COMMUNITY_Community 60|Community 60]]
- [[_COMMUNITY_Community 61|Community 61]]
- [[_COMMUNITY_Community 62|Community 62]]
- [[_COMMUNITY_Community 63|Community 63]]
- [[_COMMUNITY_Community 64|Community 64]]
- [[_COMMUNITY_Community 65|Community 65]]
- [[_COMMUNITY_Community 66|Community 66]]
- [[_COMMUNITY_Community 67|Community 67]]
- [[_COMMUNITY_Community 68|Community 68]]
- [[_COMMUNITY_Community 69|Community 69]]
- [[_COMMUNITY_Community 70|Community 70]]
- [[_COMMUNITY_Community 71|Community 71]]
- [[_COMMUNITY_Community 72|Community 72]]
- [[_COMMUNITY_Community 73|Community 73]]
- [[_COMMUNITY_Community 74|Community 74]]
- [[_COMMUNITY_Community 75|Community 75]]
- [[_COMMUNITY_Community 76|Community 76]]
- [[_COMMUNITY_Community 77|Community 77]]
- [[_COMMUNITY_Community 78|Community 78]]
- [[_COMMUNITY_Community 79|Community 79]]
- [[_COMMUNITY_Community 80|Community 80]]
- [[_COMMUNITY_Community 81|Community 81]]
- [[_COMMUNITY_Community 82|Community 82]]
- [[_COMMUNITY_Community 83|Community 83]]
- [[_COMMUNITY_Community 84|Community 84]]
- [[_COMMUNITY_Community 85|Community 85]]
- [[_COMMUNITY_Community 86|Community 86]]

## God Nodes (most connected - your core abstractions)
1. `TemplateTransformNodeTest` - 38 edges
2. `A2aAgentCardProperties` - 29 edges
3. `NacosOptions` - 27 edges
4. `Builder` - 26 edges
5. `NacosReactAgentBuilderToolsTest` - 24 edges
6. `NacosMcpGatewayToolDefinition` - 23 edges
7. `NacosA2aProperties` - 22 edges
8. `CodeExecutionConfig` - 21 edges
9. `NacosReactAgentBuilderInterceptorTest` - 20 edges
10. `Group` - 20 edges

## Surprising Connections (you probably didn't know these)
- `NacosMcpGatewayToolCallback` --implements--> `ToolCallback`  [EXTRACTED]
  spring-ai-alibaba-starter-config-nacos/src/main/java/com/alibaba/cloud/ai/agent/nacos/tools/NacosMcpGatewayToolCallback.java →   _Bridges community 3 → community 75_
- `McpGatewayToolDefinition` --implements--> `ToolDefinition`  [EXTRACTED]
  spring-ai-alibaba-starter-config-nacos/src/main/java/com/alibaba/cloud/ai/agent/nacos/tools/McpGatewayToolDefinition.java →   _Bridges community 31 → community 75_
- `TestHookWithTools` --implements--> `Hook`  [EXTRACTED]
  spring-ai-alibaba-starter-config-nacos/src/test/java/com/alibaba/cloud/ai/agent/nacos/NacosReactAgentBuilderToolsTest.java →   _Bridges community 62 → community 61_
- `AgentScopeAgent` --extends--> `BaseAgent`  [EXTRACTED]
  spring-ai-alibaba-starter-agentscope/src/main/java/com/alibaba/cloud/ai/agent/agentscope/AgentScopeAgent.java →   _Bridges community 2 → community 9_
- `AgentScopeRoutingMergeNode` --implements--> `NodeAction`  [EXTRACTED]
  spring-ai-alibaba-starter-agentscope/src/main/java/com/alibaba/cloud/ai/agent/agentscope/flow/AgentScopeRoutingMergeNode.java →   _Bridges community 9 → community 38_

## Communities (93 total, 56 thin omitted)

### Community 0 - "TemplateTransform & Test"
Cohesion: 0.05
Nodes (7): GraphObservationAutoConfigurationTest, Builder, AssignerNodeTest, TemplateTransformNodeIntegrationTest, TemplateTransformNodeTest, VariableAggregatorNodeTest, Messageutils

### Community 1 - "CodeExecution"
Cohesion: 0.05
Nodes (9): DockerCodeExecutor, LogContainerResultCallback, DockerCodeExecutorTest, LocalCommandlineCodeExecutor, CodeExecutor, CodeExecutionConfig, CodeUtils, FileUtils (+1 more)

### Community 2 - "AgentScope"
Cohesion: 0.05
Nodes (10): AgentScopeAgent, AgentScopeAgentBuilder, ReActAgentNodeAction, AgentScopeAgentTest, AsNodeTests, GraphAgentScopeToolContextTests, SequentialIntegrationTests, StandaloneTests (+2 more)

### Community 3 - "Nacos Config"
Cohesion: 0.06
Nodes (7): Builder, TemplateTransformNode, AdvancedSettings, Builder, Group, VariableAggregatorNode, NacosMcpGatewayToolCallback

### Community 4 - "Nacos Tests"
Cohesion: 0.15
Nodes (3): NacosReactAgentBuilderInterceptorTest, NacosReactAgentBuilderToolsTest, MultiAgentRequestRouter

### Community 5 - "Community 5"
Cohesion: 0.06
Nodes (11): A2aAgentCardProperties, A2aServerExecutorProvider, AgentExecutor, AgentRegistry, A2aServerAgentCardProperties, NacosAgentRegistry, A2aServerHandlerAutoConfiguration, A2aServerRegistryAutoConfiguration (+3 more)

### Community 6 - "Community 6"
Cohesion: 0.08
Nodes (5): MethodInterceptor, CglibMethodInterceptor, ChatOptionsProxy, ModelVO, PromptVO

### Community 7 - "Builders"
Cohesion: 0.07
Nodes (4): DocumentPostProcessor, Builder, KnowledgeRetrievalDocumentRanker, KnowledgeRetrievalNode

### Community 8 - "Community 8"
Cohesion: 0.12
Nodes (4): Builder, Converter, IterationNode, IterationNodeTest

### Community 9 - "Community 9"
Cohesion: 0.07
Nodes (7): AbstractFlowGraphBuildingStrategy, BaseAgent, AgentScopeRoutingAgent, AgentScopeRoutingAgentBuilder, AgentScopeRoutingGraphBuildingStrategy, AgentScopeRoutingMergeNode, FlowAgent

### Community 10 - "Community 10"
Cohesion: 0.12
Nodes (6): AgentScopeRoutingNode, MultiCommandAction, Builder, excludeExtension(), ListOperatorNodeTest, sizeNoLessThan()

### Community 11 - "Community 11"
Cohesion: 0.12
Nodes (5): NacosAgentInjector, NacosPartnerAgentsInjector, NacosPromptInjector, NacosReactAgentBuilder, NacosAgentPromptBuilder

### Community 12 - "Community 12"
Cohesion: 0.12
Nodes (4): A2aRequestHandler, AgentScopeMessageUtils, A2aRouterProvider, JsonRpcA2aRequestHandler

### Community 14 - "Community 14"
Cohesion: 0.13
Nodes (3): Builder, ParameterParsingNode, ParameterParsingNodeTest

### Community 17 - "Community 17"
Cohesion: 0.18
Nodes (4): Builder, withKey(), withValue(), CodeActionTest

### Community 18 - "Community 18"
Cohesion: 0.13
Nodes (3): Builder, QuestionClassifierNode, QuestionClassifierNodeTest

### Community 24 - "Community 24"
Cohesion: 0.15
Nodes (4): CodeExecutorNodeAction, TemplateTransformer, fromValue(), getValue()

### Community 25 - "Community 25"
Cohesion: 0.15
Nodes (5): AgentCardProvider, AgentCardWrapper, A2aClientAgentCardProviderAutoConfiguration, NacosAgentCardProvider, NacosAgentCardWrapper

### Community 26 - "Community 26"
Cohesion: 0.13
Nodes (5): GraphObservationAutoConfiguration, ObservationHandlersConfiguration, ObservationThreadLocalAccessorRegistrar, TestConfiguration, TestConfigurationWithMeterRegistry

### Community 28 - "Community 28"
Cohesion: 0.13
Nodes (3): from(), HttpRequestNodeBody, RetryConfig

### Community 33 - "Community 33"
Cohesion: 0.16
Nodes (5): ModelInterceptor, EchoFunction, TestModelInterceptor, TestToolInterceptor, ToolInterceptor

### Community 36 - "Community 36"
Cohesion: 0.19
Nodes (3): MultiAgentCardHandler, MultiAgentJsonRpcRouterProvider, MultiAgentMessageHandler

### Community 37 - "Community 37"
Cohesion: 0.21
Nodes (3): AgentCardHandler, JsonRpcA2aRouterProvider, MessageHandler

### Community 38 - "Community 38"
Cohesion: 0.19
Nodes (4): End, Start, ListOperatorNode, NodeAction

### Community 41 - "Community 41"
Cohesion: 0.21
Nodes (5): AbstractListener, DefaultBuilder, NacosAgentPromptBuilder, AgentBaseListener, PromptListener

### Community 44 - "Community 44"
Cohesion: 0.17
Nodes (3): Builder, McpNodeException, RuntimeException

### Community 48 - "Community 48"
Cohesion: 0.22
Nodes (5): EchoFunction, SimpleToolCallbackResolver, TestToolClass, ToolCallbackProvider, ToolCallbackResolver

### Community 54 - "Community 54"
Cohesion: 0.27
Nodes (4): JavaTemplateTransformer, NodeJsTemplateTransformer, Python3TemplateTransformer, TemplateTransformer

### Community 56 - "Community 56"
Cohesion: 0.28
Nodes (3): AgentBuilderFactory, NacosAgentBuilderFactory, NacosAgentPromptBuilderFactory

### Community 63 - "Community 63"
Cohesion: 0.36
Nodes (3): A2aClientAgentCardWellKnownCondition, OnMultiAgentModeCondition, SpringBootCondition

## Knowledge Gaps
- **2 isolated node(s):** `ObservationThreadLocalAccessorRegistrar`, `A2aConstants`
  These have ≤1 connection - possible missing edges or undocumented components.
- **56 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `A2aServerMultiAgentAutoConfiguration` connect `Community 35` to `Community 57`, `Community 5`?**
  _High betweenness centrality (0.045) - this node is a cross-community bridge._
- **Why does `Group` connect `Nacos Config` to `Community 71`, `Community 14`, `Community 18`, `Community 53`, `Community 21`, `Community 24`, `Community 59`?**
  _High betweenness centrality (0.043) - this node is a cross-community bridge._
- **Why does `NacosA2aProperties` connect `Community 21` to `Community 49`, `Community 51`, `Community 5`?**
  _High betweenness centrality (0.043) - this node is a cross-community bridge._
- **What connects `ObservationThreadLocalAccessorRegistrar`, `A2aConstants` to the rest of the system?**
  _2 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `TemplateTransform & Test` be split into smaller, more focused modules?**
  _Cohesion score 0.05 - nodes in this community are weakly interconnected._
- **Should `CodeExecution` be split into smaller, more focused modules?**
  _Cohesion score 0.05 - nodes in this community are weakly interconnected._
- **Should `AgentScope` be split into smaller, more focused modules?**
  _Cohesion score 0.05 - nodes in this community are weakly interconnected._