# Implementation Plan: 001-dobrodruzna-povidka

**Branch**: `001-dobrodruzna-povidka` | **Date**: 2026-05-16 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `specs/001-dobrodruzna-povidka/spec.md`

## Summary

This plan outlines the structure and required research to draft the fantasy adventure story "Rosný lán". The story will be written in Markdown/reST, following a 5-Act structure, from the first-person perspective of the 14-year-old protagonist, Pája. It weaves three distinct narrative arcs (rescuing Rypáček, saving Bělka, and defeating Vratislav's Běs) into a cohesive narrative demonstrating that understanding nature is more powerful than brute force.

## Technical Context

**Language/Version**: Čeština (Czech), Markdown with reStructuredText (`reST`) admonitions.
**Primary Dependencies**: Sphinx (for final documentation/book generation).
**Storage**: Text files in the `docs/` and `gamebook/` directories.
**Testing**: Manual review against Constitution v2.0.0 and `spec.md` Success Criteria.
**Target Platform**: PDF/HTML book formats via Sphinx.
**Project Type**: Book Chapter/Story Draft.
**Performance Goals**: Target word count: 45,000 - 50,000 characters.
**Constraints**: MUST NOT contain explicit RPG mechanics or terminology (Constitution v2.0.0). MUST use "tykání" in any instructional/interactive text if applicable, though the main story is first-person limited.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] **Historická věrnost**: Je děj zasazen do konce 14. století na Moravě a využívá slovanskou mytologii? (Yes, Blansko, Těchov, Polevik, Běs).
- [x] **RPG Mechaniky**: Jsou herní prvky zjednodušeny a *nejsou* explicitně zmiňovány v textu? (Yes, validated in spec.md).
- [x] **Jazyk a Styl**: Je použit fantasy sloh srozumitelný dětem? (Yes).
- [x] **Technické Standardy**: Dodržuje dokumentace reST? (Yes, markdown with reST hints).
- [x] **Git Workflow**: Bude commit obsahovat trailer Generated-by:Gemini a sumář promptu? (Yes).

## Project Structure

### Documentation (this feature)

```text
specs/001-dobrodruzna-povidka/
├── spec.md              # Feature specification
├── plan.md              # This file
├── research.md          # Structural and character research
├── themes.md            # Thematic focus
└── subplots.md          # Narrative arcs
```

### Source Code (repository root)

```text
docs/source/
└── dobrodruzstvi/
    └── zlaty_rypacek/
        └── povidka.md   # Or .rst, the main output file
```

**Structure Decision**: The story will be drafted as a text document within the existing `docs/source/` structure, likely as `povidka.md` or `povidka.rst` depending on the exact build pipeline requirements.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| N/A | | |
