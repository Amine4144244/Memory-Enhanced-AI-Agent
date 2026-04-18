# Project Context

This project is built by an AI full-stack developer with the following stack:

## Core Stack
- AI / Agentic AI
- LangGraph
- LangChain
- Python
- React.js / Next.js
- Node.js / Express
- MongoDB

## Frontend UI Workflow
Frontend UI/UX generation may use:
- Stitch MCP in Antigravity
- Stitch skills from: https://github.com/google-labs-code/stitch-skills

When doing UI-heavy work, prefer Stitch-based generation and refinement workflows, then integrate the output into the real application architecture.

## Default Preferences
- Write maintainable, modular, production-minded code
- Prefer clear architecture over clever shortcuts
- Keep components and services focused and reusable
- Favor explicit typing / schemas where possible
- Build for observability, debuggability, and iteration
- Minimize hidden coupling between frontend, backend, and agent workflows

## Design Philosophy
- Small composable modules
- Clear separation of concerns
- Strong error handling
- Human-readable logs
- Measurable agent behavior
- API contracts should be stable and documented
- Frontend should handle loading, success, empty, and error states

## Preferred Output
When implementing features, the AI should:
- define assumptions
- propose folder/file changes
- implement incrementally
- note edge cases
- suggest tests
- point out risks

## If Context Is Missing
The AI should ask:
- What is the expected user flow?
- What are the input/output contracts?
- Are there existing patterns in the repo?
- Is backward compatibility required?
- What level of production-readiness is expected?