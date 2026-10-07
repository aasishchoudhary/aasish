# 05 — AWS Serverless Platform

**Status: Prototype**

A small-service cloud architecture focused on understandable deployment boundaries.

```
CLIENT → API → LAMBDA → BUSINESS LOGIC → STORAGE / EXTERNAL API
                         ↓
                    OBSERVABILITY
```

### Evidence targets
- infrastructure assumptions
- deployment procedure
- API contract
- least-privilege design
- failure handling
- logging
- cost assumptions

### Client use cases
Serverless APIs, lightweight backends, event-driven automation and cloud integrations.
