# Tool Calling Skill

Use this skill when building LLM tool use.

## Tool Design
Each tool should have:
- clear name
- clear purpose
- strict input schema
- predictable output schema
- explicit failure responses

## Rules
- Expose only necessary tools
- Validate all tool inputs
- Log tool calls
- Normalize tool outputs before feeding back to the model
- Avoid tools with dangerous side effects unless strongly controlled

## Tool Selection Guidance
Use tools for:
- external data lookup
- deterministic computation
- side-effectful actions with guardrails
- internal service orchestration

Do not use tools when:
- plain reasoning is enough
- the tool is unreliable and unnecessary
- the action is unsafe without confirmation

## Output
- tool definitions
- input/output schema
- usage policy
- safety controls
- retry/fallback behavior