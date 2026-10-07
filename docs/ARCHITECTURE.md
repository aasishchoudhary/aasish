# Architecture

~~~text
MODEL
  |
  | proposes
  v
ORCHESTRATOR
  |
  +-- POLICY ---- deterministic authorization
  |
  +-- TOOLS ----- controlled actions
  |
  +-- TELEMETRY - evidence
~~~

The model adapter is deliberately small so the surrounding system can be tested without network calls.

This is a foundation for experiments, not a claim that one agent architecture solves every problem.
