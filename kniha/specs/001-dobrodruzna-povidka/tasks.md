# Tasks: 001-dobrodruzna-povidka

**Input**: Design documents from specs/001-dobrodruzna-povidka/
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, subplots.md, pov-structure.md

**Organization**: Tasks are grouped by user story (Act/Phase in this narrative context) to enable independent implementation and testing of each story arc.

## Format: [ID] [P?] [Story] Description
- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)

## Phase 1: Setup
**Purpose**: Project initialization and basic structure
- [ ] T001 Create the output file povidka.md with a main heading and metadata placeholder in the root directory.

## Phase 2: Foundational
**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented
- [ ] T002 Outline the 5-Act structure with empty headings inside povidka.md based on research.md. Ensure format follows Markdown with reST admonition syntax for examples.

## Phase 3: User Story 1 - Čtení úvodní expozice (Priority: P1)
**Goal**: Představit Páju, prostředí Blanska a zápletku s Rypáčkem. (Act I)
**Independent Test**: Čtenář dokáže popsat, kdo je Pája, čím se zabývá, co se stalo babičce Chrastě a jak Pája přišla k dráčkovi.

### Implementation for User Story 1
- [ ] T003 [US1] Napsat úvodní scénu s Pájou na Rosném lánu do povidka.md.
- [ ] T004 [US1] Napsat scénu, kde babička Chrasta naříká nad ztrátou Rypáčka do povidka.md.
- [ ] T005 [US1] Napsat scénu u Vlčího žlebu: záchrana dráčka před krysami do povidka.md.
- [ ] T006 [US1] Napsat útěk před pytlákem a návrat k babičce do povidka.md.
- [ ] T006b [US1] Napsat scénu hádky starostů na Rosném lánu, představení žoldáků a zpozorování kostěné píšťalky do povidka.md.

## Phase 4: User Story 2 - Magický střet a pouto s přírodou (Priority: P2)
**Goal**: Vyřešit problém s kozou Bělkou, rozzlobit a usmířit si Polevika Jarmila a začít si ochočovat vlka. (Act II)
**Independent Test**: Příběh obsahuje scény s Bělkou, setkání s Jarmilem a postupné ochočení vlka.

### Implementation for User Story 2
- [ ] T007 [US2] Napsat scénu hledání kozy Bělky u útesu do povidka.md.
- [ ] T008 [US2] Napsat pokus o použití dráčkova jedu na vlka, který selže do povidka.md.
- [ ] T009 [US2] Napsat nález rezavé dýky a rozhněvání Polevika Jarmila do povidka.md.
- [ ] T010 [US2] Napsat večerní scénu budování důvěry s vlkem do povidka.md.

## Phase 5: User Story 3 - Finální konfrontace a rozuzlení (Priority: P3)
**Goal**: Odhalit Vratislavovo vydírání a porazit jeho zotročeného Běsa. (Act III-V)
**Independent Test**: Čtenář zažije odhalení spiknutí, záchranu vesnice bez použití magie/síly Páji a uvidí její uznání.

### Implementation for User Story 3
- [ ] T011 [US3] Napsat scénu vyšetřování zkaženého mléka a odhalení Křiváka do povidka.md.
- [ ] T012 [US3] Napsat Křivákovo přiznání o Vratislavově plánu do povidka.md.
- [ ] T013 [US3] Napsat útok zotročeného Běsa, kterého zadrží Jarmil do povidka.md.
- [ ] T014 [US3] Napsat finální boj: Pája roztříští rezavou dýkou Kostěnou píšťalku do povidka.md.
- [ ] T015 [US3] Napsat rozuzlení: Vratislav utíká, Jarmil odvede Běsa do povidka.md.
- [ ] T016 [US3] Napsat epilog: Pája se probouzí po vyčerpání, je oslavována jako hrdinka do povidka.md.

## Phase N: Polish & Cross-Cutting Concerns
**Purpose**: Improvements that affect the whole story
- [ ] T017 Review the entire povidka.md to ensure STRICT ADHERENCE to the Single POV rule.
- [ ] T018 Review the entire povidka.md to ensure NO EXPLICIT RPG TERMINOLOGY is used.
- [ ] T019 Review narrative flow and verify word count is roughly on track towards the 45,000 character goal.
- [ ] T020 Review geographic and historical accuracy (Blansko, Těchov, Soběšice) per SC-003.
