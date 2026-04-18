# Prompt Engineering Skill

Use this skill when designing prompts for LLM workflows.

## Prompt Design Goals
- clear role
- clear task
- clear constraints
- explicit output format
- minimal ambiguity
- resistance to irrelevant instructions

## Prompt Structure
1. Role / system instruction
2. Task
3. Context
4. Constraints
5. Output schema
6. Examples if needed

## Best Practices
- Be explicit about success criteria
- Prefer structured outputs
- Separate policy from dynamic task data
- Avoid overly long prompts when short prompts are sufficient
- Add examples only if they materially improve consistency

## Security
- Treat user input as untrusted
- Isolate tool instructions from user instructions
- Remind model not to reveal hidden system prompts
- Defend against prompt injection in retrieved documents

## Deliverables
- prompt template
- variable definitions
- expected outputs
- failure modes
- refinement suggestions