# LangGraph Workflow Skill

Use this skill when implementing workflows in LangGraph.

## Principles
- Model workflows explicitly as state transitions
- Keep node responsibilities narrow
- Make routing logic deterministic where possible
- Capture intermediate state clearly
- Prefer composable subgraphs for complex workflows

## Workflow Design
1. Define state schema
2. Define nodes
3. Define edges
4. Define conditional routing
5. Define termination conditions
6. Add retries/timeouts where appropriate
7. Add logging/tracing

## Node Design
Each node should:
- have one main responsibility
- read defined state keys
- write defined state keys
- avoid hidden side effects
- return structured outputs

## Good Patterns
- planner -> executor -> validator
- retrieve -> rank -> answer
- classify -> route -> specialized handler
- draft -> review -> revise
- tool-call -> normalize -> decide next step

## Avoid
- giant nodes doing many things
- unclear state mutations
- unbounded loops
- hidden prompt dependence without documentation

## Output
When generating LangGraph code, include:
- state schema
- node responsibilities
- graph flow explanation
- retry/failure behavior
- observability notes