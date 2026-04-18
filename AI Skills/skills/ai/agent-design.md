# Agent Design Skill

Use this skill when designing an AI agent or agentic workflow.

## Goals
Design agents that are:
- reliable
- observable
- constrained
- testable
- aligned to a clear task boundary

## Design Process
1. Define the user goal
2. Define the agent’s responsibilities
3. Define what the agent must NOT do
4. List required tools
5. Define memory needs
6. Define state transitions
7. Define stopping conditions
8. Define fallback behavior
9. Define human-in-the-loop points if needed

## Agent Design Questions
- Is a single agent enough?
- Does this need a graph/workflow instead of a loop?
- What tools are safe to expose?
- What context should be injected?
- What is transient state vs persistent memory?
- What are failure and retry policies?

## Output Format
- Goal
- Inputs
- Outputs
- Tools
- State definition
- Workflow steps
- Error handling
- Observability plan
- Evaluation approach

## Safety Guidance
- Minimize tool access
- Validate tool inputs
- Protect against prompt injection
- Bound retries and recursion
- Ensure deterministic escape paths