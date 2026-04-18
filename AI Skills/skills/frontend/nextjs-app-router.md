# Next.js App Router Skill

Use this skill for Next.js App Router projects.

## Principles
- use server components by default when appropriate
- use client components only when interactivity is needed
- keep data fetching close to where data is used
- respect caching and revalidation semantics

## Checklist
- Is this server or client code?
- What can be rendered on the server?
- What requires browser APIs or client state?
- Is route loading handled?
- Are error boundaries provided?
- Are metadata and SEO considered?

## Good Practices
- use route groups for organization
- use server actions carefully
- keep API contracts explicit
- avoid unnecessary client-side fetching

## Deliverables
- route structure
- component boundary decisions
- data fetching strategy
- caching/revalidation notes
- error/loading handling