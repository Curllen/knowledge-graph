# Graph Report - /workspace/examples/voice-agent  (2026-05-13)

## Corpus Check
- Corpus is ~6,426 words - fits in a single context window. You may not need a graph.

## Summary
- 95 nodes · 154 edges · 13 communities (5 shown, 8 thin omitted)
- Extraction: 92% EXTRACTED · 8% INFERRED · 0% AMBIGUOUS · INFERRED: 12 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_WebSocket Handlers|WebSocket Handlers]]
- [[_COMMUNITY_Stream Services|Stream Services]]
- [[_COMMUNITY_Voice Agent Core|Voice Agent Core]]
- [[_COMMUNITY_JavaScript Client|JavaScript Client]]
- [[_COMMUNITY_Realtime Services|Realtime Services]]
- [[_COMMUNITY_Events|Events]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]

## God Nodes (most connected - your core abstractions)
1. `VoiceAgentAudioWebSocketHandler` - 13 edges
2. `VoiceAgentStreamService` - 12 edges
3. `VoiceAgentWebSocketHandler` - 12 edges
4. `handleEvent()` - 8 edges
5. `addLog()` - 6 edges
6. `start()` - 6 edges
7. `RealtimeVoiceAgentStreamService` - 6 edges
8. `create()` - 6 edges
9. `addActivity()` - 5 edges
10. `stop()` - 5 edges

## Surprising Connections (you probably didn't know these)
- `start()` --calls--> `setStatus()`  [EXTRACTED]
  resources/static/js/voice.js → resources/static/js/voice.js  _Bridges community 4 → community 3_
- `handleEvent()` --calls--> `addActivity()`  [EXTRACTED]
  resources/static/js/voice.js → resources/static/js/voice.js  _Bridges community 7 → community 4_
- `sendText()` --calls--> `addActivity()`  [EXTRACTED]
  resources/static/js/voice.js → resources/static/js/voice.js  _Bridges community 7 → community 3_
- `stop()` --calls--> `addLog()`  [EXTRACTED]
  resources/static/js/voice.js → resources/static/js/voice.js  _Bridges community 7 → community 9_
- `start()` --calls--> `stopTtsPlayback()`  [EXTRACTED]
  resources/static/js/voice.js → resources/static/js/voice.js  _Bridges community 9 → community 3_

## Communities (13 total, 8 thin omitted)

### Community 0 - "WebSocket Handlers"
Cohesion: 0.18
Nodes (3): AbstractWebSocketHandler, VoiceAgentAudioWebSocketHandler, VoiceAgentEvent

### Community 3 - "JavaScript Client"
Cohesion: 0.27
Nodes (9): clearActivity(), clearLogs(), el, resetPipeline(), sendText(), start(), startTurn(), ttsBuffer (+1 more)

### Community 4 - "Realtime Services"
Cohesion: 0.38
Nodes (7): finalizeStop(), finishTurn(), flushTtsToQueue(), handleEvent(), playNextTtsInQueue(), pushTtsChunk(), setStatus()

### Community 7 - "Community 7"
Cohesion: 0.67
Nodes (4): addActivity(), addLog(), escapeHtml(), formatTime()

### Community 9 - "Community 9"
Cohesion: 0.67
Nodes (3): stop(), stopAudioCapture(), stopTtsPlayback()

## Knowledge Gaps
- **3 isolated node(s):** `el`, `ttsBuffer`, `ttsPlayQueue`
  These have ≤1 connection - possible missing edges or undocumented components.
- **8 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `create()` connect `Voice Agent Core` to `WebSocket Handlers`, `Events`?**
  _High betweenness centrality (0.099) - this node is a cross-community bridge._
- **What connects `el`, `ttsBuffer`, `ttsPlayQueue` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._