# Feature Specification: Dobrodružná povídka "Ohrožená vesnice"

**Feature Branch**: `001-dobrodruzna-povidka`
**Created**: 2026-05-16
**Status**: Draft
**Input**: User description: "Dobrodružná fantasy povídka v češtině zasazená na středověkou Moravu ke konci 14-tého století, křížená s magií RPG hry D&D a slovanskou mytologií. Budeme tvořit povídku nastíněnou v @text.md"

## Clarifications

### Session 2026-05-16
- Q: Which specific negative trait should be used to provide consistent character depth throughout the story? → A: Tvrdohlavost (Stubbornness)

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Čtení úvodní expozice (Priority: P1)

Jako čtenář (dítě 6+) si chci přečíst úvod příběhu, abych se seznámil s Pájou, s prostředím Blanska a několika lidmi v něm a prožil první malou zápletkou s prasátkem Rypáčkem.

**Why this priority**: Úvodní dobrodružství příběhu, představuje hrdinku a svět. Bez expozice nelze věrně popsat proč se Pája o svůj svět (Blansko a lidé v něm) bojí.

**Independent Test**: Čtenář dokáže popsat, kdo je Pája, čím se zabývá a co se stalo babičce Chrastě a jak Pája přišla k dráčkovi.

**Acceptance Scenarios**:

1. **Given** text povídky, **When** čtenář dočte scénu s babičkou Chrastou, **Then** musí rozumět motivaci Páji (stát se chovatelkou koní) a tušit tajemství Rypáčka (hledání lanýžů).
2. **Given** popis Rosného lánu, **When** čtenář čte o pastvině, **Then** musí cítit atmosféru středověké Moravy (vůně bylinek, děti pasoucí dobytek).

---

### User Story 2 - Magický střet a pouto s přírodou (Priority: P2)

Jako čtenář chci sledovat, jak Pája využívá své znalosti bylinek a magii (dráček, lektvary) k řešení konfliktů a jak si vytváří pouto s vlkem a duchem pole Jarmilem.

**Why this priority**: Rozvíjí magické prvky a slovanskou mytologii, které jsou klíčové pro unikátnost příběhu, aniž by je explicitně pojmenovávaly herní terminologií. Poprvé zaznívají problémy způsobené Vratislavem a jeho kumpány, na Blansko padá první náznak stínu.

**Independent Test**: Příběh obsahuje napínavé scény léčení dráčka, setkání s polevikem Jarmilem a postupné ochočení vlka, vše popsáno plynulým vyprávěním.

**Acceptance Scenarios**:

1. **Given** scénu u Vlčího žleb, **When** Pája zachraňuje dráčka, **Then** musí být jasně popsáno použití lektvaru nebo bylinky jako přirozená součást děje, nikoliv jako herní mechanika.
2. **Given** setkání s Jarmilem, **When** Pája slíbí zalévat meduňku, **Then** interakce musí působit jako setkání s nadpřirozenou, ale reálnou přírodní bytostí.

---

### User Story 3 - Finální konfrontace a rozuzlení (Priority: P3)

Jako čtenář chci zažít vrcholné napětí při boji s monstrem a Vratislavem, aby příběh skončil uspokojivým vítězstvím a hrdinským uznáním Páji.

**Why this priority**: Uzavírá všechny dějové linky a přináší emocionální odměnu. Vratislavova snaha vydírat vesnice a vybudovat si gang je zastavena.

**Independent Test**: Čtenář dočte až k epilogu, kde Pája dostává zbroj a meč a stává se váženou osobou.

**Acceptance Scenarios**:

1. **Given** boj s monstrem, **When** Pája roztříští magickou píšťalku, **Then** zlo musí být poraženo plynulým literárním popisem akce.
2. **Given** konec příběhu, **When** Pája mluví s biřicem a Jarmilem, **Then** čtenář musí mít pocit uzavřeného a harmonického dobrodružství.

## Language & Tone *(mandatory)*

- **Jazyk**: Čeština.
- **Styl**: Fantasy, bohatý jazyk, ale srozumitelný pro děti (6+), stylizovaný do konce 14. století na Moravě (Blansko, Těchov, Brno). Bez zbytečných archaismů.
- **Tone Restriction**: MUST NOT explicitně zmiňovat herní systémy (D&D, Dračí doupě) ani jejich mechaniky v textu knihy. Popisuje se čistě děj.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Text povídky musí dodržet dějovou strukturu nastíněnou v `text.md` (Úvod -> Kolize -> Krize -> Klimax -> Peripetie).
- **FR-002**: Příběh je rozdělen do 3 pod-příběhů: 1. dobrodružství prasátka Rypáčka, 2. dobrodružství kozy Bělky a 3. dobrodružství s Vratislavem.
- **FR-003**: Hlavní hrdinka Pája (14 let) musí být vykreslena jako bylinkářka s ambicí chovat koně, starající se o své okolí, ale musí být tvrdohlavá.
- **FR-004**: Prostředí musí odpovídat reáliím okolí Blanska na konci 14. století.
- **FR-005**: Nadpřirozené bytosti musí vycházet ze slovanské mytologie (polevik Jarmil, běsové v pozadí).
- **FR-006**: Magie a z ní plynoucí konflikty (monstrum, dráček) jsou organickou součástí děje, NESMÍ používat tabulky, explicitní body zdraví nebo jinou přímo herní terminologii.

### Key Entities

- **Pája**: Hlavní hrdinka, bylinkářka, znalkyně zvířat, 14 let. Má ráda dobré smlouvání. Dobrosrdečná, starostlivá, ale tvrdohlavá.
- **Radmila**: Mentorka, bylinkářka, bývalá dobrodružka (lukostřelkyně), ale nikdo ve vesnici to o ní neví.
- **Jarmil**: Polevik, duch Rosného lánu. Mrzutý, ale ne zlý. Miluje hádanky, obchodování (věci s příběhem) a stará se o trávu.
- **Rypáček**: Babiččino prasátko s fenomenálním čichem na lanýže (což je tajemství). Statečný obránce.
- **Babička Chrasta**: Zděnkovitá babička, tajná sběratelka lanýžů pro bohaté měšťany.
- **Lesní dráček**: Malé okřídlené stvoření s telepatickými schopnostmi, které Pája zachrání a ochočí si ho. Vylučuje uspávací jed.
- **Koza Bělka**: Neuvěřitelně šťastná, ale problematická koza, která přitahuje maléry. Má ráda meduňku.
- **Vratislav**: Hlavní antagonista. Bývalý psovod a hajný, vyhozený za pytláctví a krutost. Nenávidí vesničany. Původně najat k zastrašení Blanska, nyní chce pomocí vydírání (s využitím Běsa) získat peníze na vlastní gang. Ovládá Běsa pomocí kostěné píšťalky.
- **Hrom a Křivák**: Vratislavovi poskoci. Hrom je obrovský, hloupý rváč. Křivák je malý, záludný zloděj.
- **Pytlák Pivec**: Zarostlý hromotluk s kuší, který se pokusí ukrást Rypáčka.
- **Běs (Monstrum)**: Lesní démon vázaný do zvířecí podoby (velikost telete, drátovité štětiny, žhnoucí oči). Ovládán Vratislavem.
- **Ochočený vlk**: Pájův zvířecí spojenec, kterého si postupně získá.
- **Rychtářka Vítka**: Rychtářka z Blanska, zodpovědná, bývalá dobrodružka (zná se s Radmilou).
- **Rosný lán**: Klíčová lokalita, zázračná pastvina provoněná bylinkami, ležící mezi Blanskem a Těchovem.
- **Vlčí žleb**: Zalesněné údolí, kde Rypáček najde dráčka.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Celkový rozsah povídky se pohybuje kolem 45 000 - 50 000 znaků.
- **SC-002**: Text neobsahuje ani jednu explicitní zmínku o "bodech", "životě", "magenergii" jakožto herní statistice.
- **SC-003**: Všechny historické názvy lokalit (Blansko, Těchov, Soběšice) jsou použity správně v geografickém kontextu.

## Assumptions

- **Cílová skupina**: Děti od 6 let, text je vhodný pro předčítání i samostatné čtení.
- **Formát**: Primárně textový soubor (Markdown).
