<!--
Sync Impact Report:
- Version change: [CONSTITUTION_VERSION] (placeholder) → 1.0.0
- List of modified principles:
  - [PRINCIPLE_1_NAME] → I. Historická věrnost a mýty
  - [PRINCIPLE_2_NAME] → II. RPG Mechaniky a Magie
  - [PRINCIPLE_3_NAME] → III. Jazyk a Styl
  - [PRINCIPLE_4_NAME] → IV. Konzistentní Terminologie
  - [PRINCIPLE_5_NAME] → V. Technická Integrita
- Added sections:
  - Technické a Formátovací Standardy
  - Proces Vývoje a Validace
- Templates requiring updates:
  - ✅ updated: .specify/templates/plan-template.md
  - ✅ updated: .specify/templates/spec-template.md
  - ✅ updated: .specify/templates/tasks-template.md
- Follow-up TODOs: none
-->

# Nasdracak RPG & Povídka Constitution

## Core Principles

### I. Historická věrnost a mýty
Děj a pravidla jsou pevně zasazeny do konce 14. století na středověké Moravě. Historické reálie jsou organicky propojeny s prvky slovanské mytologie (běsové, vodníci, víly). Racionální středověký svět je obohacen o magické prvky, které však nesmí narušit atmosféru doby.

### II. RPG Mechaniky a Magie
Projekt integruje magii a herní systémy inspirované D&D a Dračím doupětem. Tyto systémy MUST být zjednodušeny tak, aby byly přístupné dětem od 6 let. Magie je vzácná a nebezpečná, herní mechanismy musí být vysvětlitelné během několika minut.

### III. Jazyk a Styl
Veškeré texty (pravidla i povídky) jsou psány v češtině. Ke čtenáři/hráči se MUST přistupovat s úctou pomocí "tykání" (např. "Vytvoř si postavu"). Jazyk musí být bohatý, ve fantasy stylu, ale srozumitelný dětskému publiku bez zbytečných archaismů, které by bránily pochopení.

### IV. Konzistentní Terminologie
Ve všech částech projektu se MUST dodržovat jednotná terminologie:
- Síla postavy = SÍL
- Magická energie = magenergie
- Zdraví/Body výdrže = životy
Nedodržení této terminologie je považováno za chybu v integritě systému.

### V. Technická Integrita
Pravidla jsou spravována ve formátu reStructuredText pro zajištění kvalitního exportu (Sphinx). Pomocné skripty v adresáři `tools/` MUST dodržovat standardy `black` (formátování), `flake8` (linting) a MUST být pokryty testy `pytest`.

## Technické a Formátovací Standardy

### Dokumentace (Sphinx/reST)
- Pravidla jsou psána srozumitelně a přímo k věci.
- Příklady v pravidlech MUST být formátovány pomocí `.. admonition:: Příklad:` s odsazeným textem.
- Hlavní vstupní bod pravidel je `docs/source/pravidla/index.rst`.

### Git a Gemini Workflow
- Používáme "Conventional commits" (v češtině, bez diakritiky).
- Změny generované AI MUST obsahovat trailer `Generated-by:Gemini`.
- Commit message MUST obsahovat zesumarizovaný prompt poskytnutý operátorem.

## Proces Vývoje a Validace

### Kvalita Kódu
Všechny skripty v `tools/` jsou spouštěny ve virtuálním prostředí `venv/`. Před commitem je doporučeno spustit:
- `venv/bin/black tools/`
- `venv/bin/flake8 tools/`
- `venv/bin/pytest tools/tests/`

### Validace Dat
Jakákoliv data (např. bestiář, gamebook uzly) MUST být validována pomocí:
- `venv/bin/python tools/doit.py --data data/ lint`

## Governance

Tato ústava je nejvyšším dokumentem projektu. Veškeré změny v kódu, textech nebo procesech musí být v souladu s jejími principy.

### Změny a Revize
- Jakákoliv změna v ústavě vyžaduje zvýšení verze (Semantic Versioning).
- Změna principu = MAJOR bump.
- Přidání standardu = MINOR bump.
- Oprava překlepů = PATCH bump.

### Soulad (Compliance)
Všechny Pull Requesty a automatické generování textu musí být kontrolovány proti sekci "Constitution Check" v plánech implementace.

**Version**: 1.0.0 | **Ratified**: 2026-05-16 | **Last Amended**: 2026-05-16
