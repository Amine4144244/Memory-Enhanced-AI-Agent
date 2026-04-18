# Frontend State Management Skill

Use this skill when deciding or implementing frontend state patterns.

## State Categories
- local UI state
- server state
- shared app state
- form state
- URL state

## Guidance
- local state: use component state
- server state: use dedicated fetching/caching strategy
- shared state: use context/store only when needed
- form state: use form-focused patterns/libraries if complexity justifies it
- URL state: use query params when state should be shareable/bookmarkable

## Avoid
- putting everything in global state
- duplicating server state in many places
- mixing transient UI state with domain state unnecessarily

## Deliverables
- state ownership map
- chosen pattern and why
- synchronization concerns
- edge cases