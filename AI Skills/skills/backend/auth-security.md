# Auth and Security Skill

Use this skill when implementing authentication, authorization, or security-sensitive behavior.

## Security Principles
- least privilege
- secure defaults
- explicit authorization checks
- input validation everywhere
- secrets via environment/config
- careful session/token handling

## Checklist
- Who is the user?
- How is identity verified?
- What actions are allowed?
- What resources are protected?
- What happens on expired/invalid auth?
- Are rate limits needed?
- Are logs safe and non-sensitive?

## AI-Specific Security
- protect tool execution
- sanitize retrieved content
- defend against prompt injection
- gate side-effectful actions
- require confirmation for risky operations

## Deliverables
- auth flow
- protected resources
- authorization model
- failure cases
- security risks