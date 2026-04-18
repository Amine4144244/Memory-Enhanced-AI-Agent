# Stitch UI Generation Skill

Use this skill when generating or iterating UI with Stitch MCP in Antigravity.

## Tools
- Stitch MCP in Antigravity
- Stitch skills from: https://github.com/google-labs-code/stitch-skills

## Purpose
Translate product requirements into high-quality UI generation requests and integrate the resulting UI into the application.

## Workflow
1. Identify screen or component to build
2. Summarize user goal
3. Define content hierarchy
4. Define actions and interaction points
5. Define state variations
6. Prepare concise but specific Stitch request
7. Review generated output
8. Refine if needed
9. Integrate into codebase
10. Connect to real data and behavior

## Required Spec
Every Stitch request should try to include:
- screen/component name
- business purpose
- user goal
- content sections
- CTA hierarchy
- state requirements
- responsive expectations
- accessibility requirements
- style direction
- reuse constraints from existing design system/components

## UI State Checklist
Always consider:
- loading
- success
- empty
- error
- disabled
- validation states for forms
- no-results state for search/filter experiences

## Integration Checklist
After Stitch generates UI, the AI should:
- identify reusable components
- separate static and dynamic pieces
- replace placeholder data
- define props/interfaces
- wire events/actions
- connect API or state sources
- ensure semantic structure
- ensure mobile responsiveness
- ensure visual consistency

## Output Format
- screen/component summary
- Stitch generation brief
- review findings
- integration steps
- follow-up improvements