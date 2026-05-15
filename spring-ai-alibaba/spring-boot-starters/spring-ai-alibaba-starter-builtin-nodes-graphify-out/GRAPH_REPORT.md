# Graph Report - /workspace/spring-boot-starters/spring-ai-alibaba-starter-builtin-nodes  (2026-05-13)

## Corpus Check
- Corpus is ~34,603 words - fits in a single context window. You may not need a graph.

## Summary
- 603 nodes · 1047 edges · 34 communities (20 shown, 14 thin omitted)
- Extraction: 70% EXTRACTED · 30% INFERRED · 0% AMBIGUOUS · INFERRED: 309 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Code Execution|Code Execution]]
- [[_COMMUNITY_Template Transform Tests|Template Transform Tests]]
- [[_COMMUNITY_LLM & Message Utils|LLM & Message Utils]]
- [[_COMMUNITY_Template & Variable Nodes|Template & Variable Nodes]]
- [[_COMMUNITY_Agent & List Nodes|Agent & List Nodes]]
- [[_COMMUNITY_Knowledge Retrieval|Knowledge Retrieval]]
- [[_COMMUNITY_Iteration Node|Iteration Node]]
- [[_COMMUNITY_HTTP Node|HTTP Node]]
- [[_COMMUNITY_File Storage|File Storage]]
- [[_COMMUNITY_Condition Node|Condition Node]]
- [[_COMMUNITY_Summary Node|Summary Node]]
- [[_COMMUNITY_HTTP Body Data|HTTP Body Data]]
- [[_COMMUNITY_Built-in Nodes|Built-in Nodes]]
- [[_COMMUNITY_Switch Node|Switch Node]]
- [[_COMMUNITY_Action Node|Action Node]]
- [[_COMMUNITY_Reflection Node|Reflection Node]]
- [[_COMMUNITY_Embedding Node|Embedding Node]]
- [[_COMMUNITY_Multi-modal|Multi-modal]]
- [[_COMMUNITY_Document Node|Document Node]]
- [[_COMMUNITY_Prompt Template|Prompt Template]]
- [[_COMMUNITY_Text Splitter|Text Splitter]]
- [[_COMMUNITY_Function Call|Function Call]]
- [[_COMMUNITY_Search Node|Search Node]]
- [[_COMMUNITY_Math Node|Math Node]]
- [[_COMMUNITY_Logic Node|Logic Node]]
- [[_COMMUNITY_Filter Node|Filter Node]]
- [[_COMMUNITY_Sort Node|Sort Node]]
- [[_COMMUNITY_Aggregation Node|Aggregation Node]]

## God Nodes (most connected - your core abstractions)
1. `TemplateTransformNodeTest` - 38 edges
2. `Builder` - 26 edges
3. `CodeExecutionConfig` - 21 edges
4. `Group` - 17 edges
5. `Builder` - 16 edges
6. `BodyData` - 15 edges
7. `Converter` - 14 edges
8. `Builder` - 13 edges
9. `HttpNodeTest` - 13 edges
10. `HttpNode` - 12 edges

## Surprising Connections (you probably didn't know these)
- `HttpNode` --implements--> `NodeAction`  [EXTRACTED]
  main/java/com/alibaba/cloud/ai/graph/node/HttpNode.java →   _Bridges community 4 → community 23_
- `QuestionClassifierNode` --implements--> `NodeAction`  [EXTRACTED]
  main/java/com/alibaba/cloud/ai/graph/node/QuestionClassifierNode.java →   _Bridges community 4 → community 2_
- `ToolNode` --implements--> `NodeAction`  [EXTRACTED]
  main/java/com/alibaba/cloud/ai/graph/node/ToolNode.java →   _Bridges community 4 → community 7_
- `VariableAggregatorNode` --implements--> `NodeAction`  [EXTRACTED]
  main/java/com/alibaba/cloud/ai/graph/node/VariableAggregatorNode.java →   _Bridges community 4 → community 3_
- `McpNode` --implements--> `NodeAction`  [EXTRACTED]
  main/java/com/alibaba/cloud/ai/graph/node/McpNode.java →   _Bridges community 4 → community 13_

## Communities (34 total, 14 thin omitted)

### Community 0 - "Code Execution"
Cohesion: 0.06
Nodes (8): DockerCodeExecutor, LogContainerResultCallback, DockerCodeExecutorTest, LocalCommandlineCodeExecutor, CodeExecutor, CodeExecutionConfig, CodeUtils, FileUtils

### Community 1 - "Template Transform Tests"
Cohesion: 0.1
Nodes (3): TemplateTransformNodeIntegrationTest, TemplateTransformNodeTest, VariableAggregatorNodeTest

### Community 2 - "LLM & Message Utils"
Cohesion: 0.07
Nodes (4): Builder, LlmNode, QuestionClassifierNode, Messageutils

### Community 3 - "Template & Variable Nodes"
Cohesion: 0.07
Nodes (6): Builder, TemplateTransformNode, AdvancedSettings, Builder, Group, VariableAggregatorNode

### Community 4 - "Agent & List Nodes"
Cohesion: 0.05
Nodes (9): AgentNode, Builder, AnswerNode, Builder, AssignerNode, End, ListOperatorNode, ParameterParsingNode (+1 more)

### Community 5 - "Knowledge Retrieval"
Cohesion: 0.07
Nodes (4): DocumentPostProcessor, Builder, KnowledgeRetrievalDocumentRanker, KnowledgeRetrievalNode

### Community 6 - "Iteration Node"
Cohesion: 0.12
Nodes (4): Builder, Converter, IterationNode, IterationNodeTest

### Community 7 - "HTTP Node"
Cohesion: 0.13
Nodes (3): Builder, ToolNode, FileUtilsTest

### Community 8 - "File Storage"
Cohesion: 0.14
Nodes (4): CodeExecutorNodeAction, TemplateTransformer, fromValue(), getValue()

### Community 9 - "Condition Node"
Cohesion: 0.19
Nodes (4): Builder, withKey(), withValue(), CodeActionTest

### Community 12 - "Built-in Nodes"
Cohesion: 0.22
Nodes (4): Builder, excludeExtension(), ListOperatorNodeTest, sizeNoLessThan()

### Community 13 - "Switch Node"
Cohesion: 0.14
Nodes (4): Builder, McpNode, McpNodeException, RuntimeException

### Community 16 - "Embedding Node"
Cohesion: 0.13
Nodes (3): Start, FileRecord, InMemoryFileStorage

### Community 22 - "Search Node"
Cohesion: 0.27
Nodes (4): JavaTemplateTransformer, NodeJsTemplateTransformer, Python3TemplateTransformer, TemplateTransformer

## Knowledge Gaps
- **14 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `HttpNode` connect `Math Node` to `HTTP Body Data`, `Agent & List Nodes`, `Function Call`?**
  _High betweenness centrality (0.041) - this node is a cross-community bridge._
- **Are the 8 inferred relationships involving `Group` (e.g. with `.replaceVariables()` and `.renderTemplate()`) actually correct?**
  _`Group` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Should `Code Execution` be split into smaller, more focused modules?**
  _Cohesion score 0.06 - nodes in this community are weakly interconnected._
- **Should `Template Transform Tests` be split into smaller, more focused modules?**
  _Cohesion score 0.1 - nodes in this community are weakly interconnected._
- **Should `LLM & Message Utils` be split into smaller, more focused modules?**
  _Cohesion score 0.07 - nodes in this community are weakly interconnected._
- **Should `Template & Variable Nodes` be split into smaller, more focused modules?**
  _Cohesion score 0.07 - nodes in this community are weakly interconnected._
- **Should `Agent & List Nodes` be split into smaller, more focused modules?**
  _Cohesion score 0.05 - nodes in this community are weakly interconnected._