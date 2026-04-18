# Error Handling and Logging Skill

Use this skill for resilient backend and AI systems.

## Error Handling Principles
- fail loudly in development
- fail gracefully in production
- classify errors as:
  - validation
  - auth
  - business logic
  - dependency/integration
  - unexpected internal

## Logging Principles
- structured logs preferred
- include request/task correlation IDs
- log enough to debug, not enough to leak secrets
- log external dependency failures with context

## Deliverables
- error taxonomy
- error response format
- logging fields
- monitoring/alert suggestions