# LangChain Patterns Skill

Use this skill when building with LangChain.

## Preferred Patterns
- clearly separated prompt/template logic
- isolated tool definitions
- structured output parsing
- retriever abstraction
- callback/tracing support
- testable chain composition

## Guidance
- Prefer structured outputs over loose text when possible
- Keep prompts versionable
- Avoid coupling business logic tightly to prompt text
- Wrap external dependencies behind service layers
- Use runnable composition where it improves clarity

## Chain Design Checklist
- What is the input?
- What is the output schema?
- What external context is injected?
- Is retrieval needed?
- Are tools needed?
- How is failure handled?
- How is response quality evaluated?

## Deliverables
- chain purpose
- prompt strategy
- tool usage
- output schema
- code structure
- test strategy