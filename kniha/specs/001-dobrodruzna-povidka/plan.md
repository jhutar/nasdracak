# Plán implementace: 001-dobrodruzna-povidka

**Větev**: `001-dobrodruzna-povidka` | **Datum**: 16. 5. 2026 | **Specifikace**: [spec.md](./spec.md)
**Vstup**: Specifikace funkce ze `specs/001-dobrodruzna-povidka/spec.md`

## Souhrn

Tento plán nastiňuje strukturu a potřebný výzkum pro sepsání fantasy dobrodružného příběhu „Ohrožená vesnice“. Příběh bude napsán v Markdownu podle pětiactové struktury, z pohledu první osoby čtrnáctileté protagonistky Páji. Propojuje tři odlišné dějové linky (záchrana Rypáčka, záchrana Bělky a porážka Vratislavova Běsa) do uceleného vyprávění, které ukazuje, že porozumění přírodě je mocnější než hrubá síla. Ústřední konflikt se týká Vratislava, který byl najat jen proto, aby vyhrál jednu pastvinu pro jednu vesnici, ale rozhodne se zcela ovládnout dvě vesnice. Využívá svou kontrolu nad Běsem k vydírání vesničanů, aby získal peníze na vybudování vlastního zločineckého gangu.

## Technický kontext

**Jazyk/Verze**: Čeština.
**Úložiště**: Textové soubory v adresáři `kniha/`.
**Testování**: Manuální kontrola podle Constitution v2.0.0 a kritérií úspěchu v `spec.md`.
**Cílová platforma**: Dokument Markdown.
**Typ projektu**: Návrh kapitoly knihy / příběhu.
**Výkonnostní cíle**: Cílový počet slov: 45 000 – 50 000 znaků.
**Omezení**: NESMÍ obsahovat explicitní RPG mechaniky nebo terminologii (Constitution v2.0.0). MUSÍ používat tykání v jakémkoli instruktážním/interaktivním textu, pokud je to relevantní, ačkoli hlavní příběh je v první osobě.

## Kontrola ústavy (Constitution Check)

*BRÁNA: Musí projít před výzkumem ve Fázi 0. Znovu zkontrolovat po návrhu ve Fázi 1.*

- [x] **Historická věrnost**: Je děj zasazen do konce 14. století na Moravě a využívá slovanskou mytologii? (Ano, Blansko, Těchov, Polevik, Běs).
- [x] **RPG Mechaniky**: Jsou herní prvky zjednodušeny a *nejsou* explicitně zmiňovány v textu? (Ano, ověřeno v spec.md).
- [x] **Jazyk a Styl**: Je použit fantasy sloh srozumitelný dětem? (Ano).
- [x] **Technické Standardy**: Dodržuje dokumentace Markdown? (Ano).
- [x] **Git Workflow**: Bude commit obsahovat trailer Generated-by:Gemini a sumář promptu? (Ano).

## Struktura projektu

### Dokumentace (tato funkce)

```text
specs/001-dobrodruzna-povidka/
├── spec.md              # Specifikace funkce
├── plan.md              # Tento soubor
├── research.md          # Výzkum struktury a postav
├── themes.md            # Tematické zaměření
└── subplots.md          # Dějové linky
```

### Výstupní data

Pracujeme v adresáři `kniha/` většího gitového repozitáře, ale není třeba z tohoto adresáře odcházet.

```text
└── povidka.md
```

**Rozhodnutí o struktuře**: Příběh bude vypracován jako textový dokument v rámci stávající struktury `kniha/` jako `povidka.md`.

## Sledování složitosti

> **Vyplňte POUZE v případě, že kontrola ústavy vykazuje porušení, která musí být odůvodněna**

| Porušení | Proč je potřeba | Jednodušší alternativa zamítnuta, protože |
|-----------|------------|-------------------------------------|
| N/A | | |
