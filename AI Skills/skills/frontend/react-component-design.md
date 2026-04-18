# React Component Design Skill

Use this skill when creating or refactoring React components.

## Principles
- components should do one thing well
- separate presentation from complex logic where useful
- prefer reusable composition over duplication
- keep props APIs simple and explicit

## Component Design Checklist
- What is the component’s responsibility?
- What props are required vs optional?
- Is state local or should it be lifted?
- Are side effects isolated?
- Is accessibility addressed?
- Are loading/error/empty states handled?

## Good Patterns
- container + presentational split when complexity grows
- custom hooks for reusable stateful logic
- derived state instead of duplicated state
- memoization only when justified

## Avoid
- giant components
- prop drilling when context/store is more appropriate
- hidden side effects in render paths
- mixing unrelated concerns

## Deliverables
- component API
- state/props design
- edge states
- accessibility notes
- test suggestions