# Graph Report - /workspace/examples/chatbot  (2026-05-13)

## Corpus Check
- Corpus is ~1,579 words - fits in a single context window. You may not need a graph.

## Summary
- 24 nodes · 21 edges · 4 communities (0 shown, 4 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Chatbot Agent|Chatbot Agent]]
- [[_COMMUNITY_Tools & Loader|Tools & Loader]]
- [[_COMMUNITY_Application|Application]]
- [[_COMMUNITY_Request Objects|Request Objects]]

## God Nodes (most connected - your core abstractions)
1. `ChatbotAgent` - 6 edges
2. `AgentStaticLoader` - 5 edges
3. `PythonTool` - 4 edges
4. `ChatbotApplication` - 3 edges
5. `PythonRequest` - 2 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Communities (4 total, 4 thin omitted)

## Knowledge Gaps
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Not enough signal to generate questions. This usually means the corpus has no AMBIGUOUS edges, no bridge nodes, no INFERRED relationships, and all communities are tightly cohesive. Add more files or run with --mode deep to extract richer edges._