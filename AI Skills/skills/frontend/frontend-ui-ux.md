# Frontend UI/UX Skill

Use this skill when implementing user-facing interfaces.

## Primary UI Generation Workflow
This project uses:
- Stitch MCP in Antigravity
- Stitch skills from: https://github.com/google-labs-code/stitch-skills

The AI should prefer using Stitch-based workflows for UI generation and iteration rather than manually inventing large UI implementations from scratch, unless explicitly requested.

## Role of the AI
The AI should act as:
- a UI task planner
- a requirements translator for Stitch
- a reviewer of generated UI output
- an integrator of generated UI into the app
- a quality checker for accessibility, responsiveness, and product consistency

## When to Use Stitch
Use Stitch when:
- creating new pages
- generating layout ideas
- scaffolding UI components
- iterating on visual structure
- converting product requirements into screens/components
- improving consistency of design patterns

## When Manual Implementation Is Fine
Manual implementation is acceptable when:
- fixing small UI bugs
- wiring data into an existing component
- adjusting styles incrementally
- improving accessibility
- handling state, loading, and error behavior
- integrating generated UI into the actual app architecture

## Workflow
1. Understand the user flow
2. Define the purpose of the screen/component
3. Identify required states:
   - loading
   - empty
   - success
   - error
   - disabled
4. Write a clear UI generation brief for Stitch
5. Generate or refine UI through Stitch MCP
6. Review the output for:
   - clarity
   - hierarchy
   - usability
   - accessibility
   - responsiveness
   - consistency with project patterns
7. Integrate the result into React/Next.js structure
8. Connect real data, actions, and state handling
9. Refine semantics and accessibility
10. Suggest polish and cleanup

## Required Input Before UI Generation
Before using Stitch, the AI should identify:
- target page or component
- user goal
- key actions
- required data to display
- constraints from product/business logic
- mobile/desktop expectations
- branding or style direction if provided
- existing design system or component library if any

If important UI context is missing, ask clarifying questions.

## Stitch Prompt/Spec Guidance
When preparing a request for Stitch, the AI should include:
- what screen/component is being built
- target user and user goal
- page purpose
- information hierarchy
- required sections
- key CTAs
- important states
- accessibility expectations
- responsive expectations
- tone/style direction
- constraints from existing product patterns

## Example Structure for a Stitch Brief
Use a structure like:

- Screen name
- Goal
- Primary user actions
- Required content sections
- Important states
- Layout expectations
- Style/tone direction
- Accessibility requirements
- Notes for integration

## Review Checklist for Stitch Output
The AI should review generated UI for:

### UX
- Is the main action obvious?
- Is the layout easy to scan?
- Are important actions prominent?
- Are forms and flows easy to understand?
- Are empty and error states useful?

### Accessibility
- semantic HTML opportunities
- keyboard accessibility
- label clarity
- contrast considerations
- screen-reader-friendly structure

### Responsiveness
- mobile layout behavior
- desktop spacing/layout balance
- overflow issues
- button/input usability on smaller screens

### Product Consistency
- matches app architecture
- compatible with existing components
- avoids unnecessary UI complexity
- aligns with real backend/frontend data flow

## Integration Rules
When integrating Stitch-generated UI:
- separate presentation from data fetching when useful
- avoid embedding fake/mock business logic into final components
- convert placeholder content into props/data-driven rendering
- align file structure with project conventions
- keep components modular
- connect loading/error/empty states to real app behavior

## Do Not
- treat generated UI as production-ready without review
- ignore accessibility issues
- leave fake data in integrated components unless explicitly requested
- mix UI generation with backend assumptions that are not confirmed
- overcomplicate visual design when product requirements are simple

## Deliverables
When doing UI/UX work, return:
1. user flow summary
2. Stitch brief or prompt
3. review of generated UI
4. integration plan
5. accessibility/responsiveness notes
6. any cleanup/refactor suggestions