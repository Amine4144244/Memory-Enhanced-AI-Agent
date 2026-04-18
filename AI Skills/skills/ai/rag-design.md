# RAG Design Skill

Use this skill when building retrieval-augmented generation systems.

## RAG Design Process
1. Define retrieval goal
2. Define corpus/source of truth
3. Define chunking strategy
4. Define embedding/index approach
5. Define retrieval method
6. Define ranking/filtering
7. Define answer generation constraints
8. Define citation/grounding requirements
9. Define evaluation metrics

## Design Questions
- What documents are authoritative?
- What freshness requirements exist?
- Is metadata filtering needed?
- What chunk size and overlap fit the corpus?
- Is hybrid search needed?
- Should results be cited?
- What should happen when retrieval is weak?

## Quality Guidance
- Ground answers in retrieved evidence
- Prefer “I don’t know” over hallucination
- Include provenance when useful
- Measure retrieval quality separately from generation quality

## Output
- corpus definition
- indexing strategy
- retrieval flow
- answer policy
- evaluation plan
- risks