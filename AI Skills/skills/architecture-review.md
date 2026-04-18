# Architecture Review Skill

Use this skill when evaluating or proposing architecture.

## Review Dimensions
- modularity
- separation of concerns
- scalability
- testability
- reliability
- observability
- performance
- security
- maintainability

## Review Process
1. Identify system boundaries
2. List major modules/services
3. Map data flow
4. Identify coupling hotspots
5. Check failure points
6. Check logging and monitoring coverage
7. Evaluate scaling bottlenecks
8. Suggest improvements incrementally

## Output Format
- Current architecture summary
- Strengths
- Risks / bottlenecks
- Recommended changes
- Priority order
- Migration notes

## Guidance
- Avoid overengineering
- Match architecture to expected scale and team size
- Prefer explicit interfaces between modules
- For AI systems, include evaluation and observability in architecture