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
- [ ] T002 Outline the 5-Act structure with empty headings inside povidka.md based on research.md.

## Phase 3: User Story 1 - Cteni uvodni expozice (Priority: P1)
**Goal**: Predstavit Paju, prostredi Blanska a zapletku s Rypackem. (Act I)
**Independent Test**: Ctenar dokaze popsat, kdo je Paja, cim se zabyva, co se stalo babicce Chraste a jak Paja prisla k drackovi.

### Implementation for User Story 1
- [ ] T003 [US1] Napsat uvodni scenu s Pajou na Rosnem lanu do povidka.md.
- [ ] T004 [US1] Napsat scenu, kde babicka Chrasta narika nad ztratou Rypacka do povidka.md.
- [ ] T005 [US1] Napsat scenu u Vlciho zlebu: zachrana dracka pred krysami do povidka.md.
- [ ] T006 [US1] Napsat utek pred pytlakem a navrat k babicce do povidka.md.

## Phase 4: User Story 2 - Magicky stret a pouto s prirodou (Priority: P2)
**Goal**: Vyresit problem s kozou Belkou, rozzlobit a usmirit si Polevika Jarmila a zacit si ococovat vlka. (Act II)
**Independent Test**: Pribeh obsahuje sceny s Belkou, setkani s Jarmilem a postupne ococeni vlka.

### Implementation for User Story 2
- [ ] T007 [US2] Napsat scenu hledani kozy Belky u utesu do povidka.md.
- [ ] T008 [US2] Napsat pokus o pouziti drackova jedu na vlka, ktery selze do povidka.md.
- [ ] T009 [US2] Napsat nalez rezave dyky a rozhneveni Polevika Jarmila do povidka.md.
- [ ] T010 [US2] Napsat vecerni scenu budovani duvery s vlkem do povidka.md.

## Phase 5: User Story 3 - Finalni konfrontace a rozuzleni (Priority: P3)
**Goal**: Odhalit Vratislavovo vydirani a porazit jeho zotroceneho Besa. (Act III-V)
**Independent Test**: Ctenar zazije odhaleni spiknuti, zachranu vesnice bez pouziti magie/sily Paji a uvidi jeji uznani.

### Implementation for User Story 3
- [ ] T011 [US3] Napsat scenu vysetrovani zkazeneho mleka a odhaleni Krivaka do povidka.md.
- [ ] T012 [US3] Napsat Krivakovo priznani o Vratislavove planu do povidka.md.
- [ ] T013 [US3] Napsat utok zotroceneho Besa, ktereho zadrzi Jarmil do povidka.md.
- [ ] T014 [US3] Napsat finalni boj: Paja roztrišti rezavou dykou Kostěnou pišťalku do povidka.md.
- [ ] T015 [US3] Napsat rozuzleni: Vratislav utika, Jarmil odvede Besa do povidka.md.
- [ ] T016 [US3] Napsat epilog: Paja se probouzi po vycerpani, je oslavovana jako hrdinka do povidka.md.

## Phase N: Polish & Cross-Cutting Concerns
**Purpose**: Improvements that affect the whole story
- [ ] T017 Review the entire povidka.md to ensure STRICT ADHERENCE to the Single POV rule.
- [ ] T018 Review the entire povidka.md to ensure NO EXPLICIT RPG TERMINOLOGY is used.
- [ ] T019 Review narrative flow and verify word count is roughly on track towards the 45,000 character goal.
