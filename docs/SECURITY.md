# Security Architecture

## Rules

1. No secrets in source control.
2. External inputs are untrusted.
3. Model output is not automatically trusted.
4. High-risk actions require explicit approval.
5. Tool interfaces validate arguments.
6. Logs must not contain credentials or unnecessary private data.

Potential threats include prompt injection, unsafe tool selection, malformed arguments, privilege escalation, destructive actions and sensitive-data leakage.

The current implementation addresses the deterministic authorization boundary; production deployment would require additional controls.
