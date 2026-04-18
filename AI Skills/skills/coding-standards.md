# Coding Standards

## General Principles
- Prefer readability over cleverness
- Use descriptive names
- Avoid deeply nested logic where possible
- Keep functions small and focused
- Extract shared logic into utilities/services/hooks when reuse appears
- Document non-obvious decisions

## File Organization
- One file should have one primary responsibility
- Group related logic by feature/domain where possible
- Avoid dumping unrelated helpers into generic utility files

## Comments
- Do not over-comment obvious code
- Add comments for:
  - business rules
  - edge-case handling
  - architectural constraints
  - agent workflow rationale

## API / Contract Safety
- Validate external inputs
- Fail gracefully with actionable errors
- Preserve existing public contracts unless explicitly changing them

## Refactoring Rules
- Do not refactor unrelated code unless necessary
- If touching a fragile area, explain why
- Prefer incremental refactors over broad rewrites

## Security
- Never hardcode secrets
- Validate auth-sensitive operations
- Sanitize / validate user input
- Be careful with prompt injection, tool abuse, and untrusted context in AI systems

## Deliverables
When writing code, include:
- changed files
- why each change was made
- test suggestions
- known gaps or assumptions