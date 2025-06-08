---
title: Opuštěná mágova věž
author: Jan Hutař
lang: cs-CZ
csquotes: true
gamebook-gap: 5
papersize: a5
geometry: margin=2cm
---

![Opuštěná mágova věž](docs/source/dobrodruzstvi/opustena_magova_vez/img/vez.svg "Opuštěná mágova věž")

\newpage

Dobrodružství je zamýšleno pro skupinku 3 dobrodruhů na první úrovni. Co se týče pravidel a způsobu popisu příšer či předmětů, vycházíme z prastarého Dračího doupěte. Myslím ale, že to půjde převést na libovolný systém.

Text psaný skoloněným písmem (tzv. *italikou*) jsou instrukce pro hráče. Zbytek je popis příběhu - toho co se děje postavám za které hraješ (nebo hrajete).

# Jak hrát
Toto dobrodružství je zamýšleno pro skupinku tří postav na první úrovni. Můžeš hrát sám za všechny postavy, nebo vás může hrát několik, každý za svou postavu. Pokud si chceš hru ztížit, hraj s méně postavami, pokud zjednodušit, přizvy kamarády a vaši skupinku dobrodruhů rozšiřte. Je to jen na tobě (nebo na vás).

Co budeš potřebovat? Jednu nebo lépe 2 šestistěnné kostky, tužku, papír a bude se hodit guma. Na kreslení mapy se bude hodit papír čtverečkovaný.

## Pravidla

### Souboj
Útok zbraní při boji tváří v tvář: síla postavy (SÍL) + síla zbraně = útočné číslo (ÚČ).

Útok zbraní na dálku: obratnost postavy (OBR) + síla zbraně = útočné číslo (ÚČ).

Obrana proti útoku: bonusu za obratnost (OBR) + kvalita zbroje + štít = obranné číslo (OČ).

Pokud je ÚČ větší než OČ, cíl útoku přichází o ÚČ - OČ životů.

Další možnosti při boji:

* Útok na nehybného protivníka (například spoutaného nějakým kouzlem): +4
* Útok ze zálohy, překvapení protivníka: +2 na první útok
* Útok na plocho: Při použití jiných než střelných a vrhacích zbraní můžeš útočit tzv. "na plocho". Při tomto útoku se oběti neubírají opravdové životy, ale tzv. "stínové". Pokud útoky na plocho oběti ubereš tolik stínových životů kolik má opravdových, oběť omdlí. Za 10 minut se probere a ztrácí ¼ svých opravdových životů.
* Pokud se některá strana rozhodne utéct z boje, druhá strana na ni bude ještě dvě kola útočit. Utíkající strana tato dvě kola neútočí, jen se brání.

### Pasti
Příklad zápisu pro past kde se rozhoduje jestli postava najde skryté tlačítko:

    INT 5, nic/tlačítko nalezeno

a znamená to, že pokud hod hráče desetistěnou kostkou plus jeho bonus na inteligenci je ve výsledku 1 až 4, postava tlačítko nenašla. Pokud je ale výsledek 5 a více, postava tlačítko našla.

Past ale může být složitější. Tady se třeba určuje, jestli postava přes kluzký starý kmen vedoucí přes zpěněnou řeku dokáže přejít na druhou stranu:

    OBR 2/4/8, pád do vody a zranění za 2 životy/pád do vody a vypalování zpět na původním břehu/pád do vody a vyplavání na cílovém břehu/přejde

Pokud tedy hráč s postavou s odolností +1 hodí 1k10 kostkou 3, jeho výsledek je 4 (hod plus +1 za ODO). To znamená že postava z klády do vody spadla, ale vynořila se na cílovém břehu (t.j. třetí možnost v popisu pasti). Bylo to však těsně. Hod o jedna menší (2 na kostce plus +1 za ODO) by znamenal, že postava spadla do vody a proud ji vyvrhl na břehu z něhož vycházela (t.j. druhá možnost v popisu pasti).

## Tvorba postay
Pravděpodobně budeš vytvářet několik postav, takže prostě tento postup zopakuješ pro každou z nich. Pokud vás hraje víc, můžete postupovat společně a každý si tvořit svou postavu.

Vytváření postavy se skládá z těchto kroků:

1. Vymysli si jméno.
2. Vyber si její rasu.
3. Urči její vlastnosti (síla, obratnost, odolnost, inteligence a charisma).
4. Z vlastností vyplyne počet životů a množství magické energie.
5. Vyber 2 startovací dovednosti.
6. Nakup si vybavení do začátku.

### Deník postavy
Pro každou postavu budete potřebovat její deník. Záznam jejich vlastností a majetku. Stačí tužka a obyčejný papír jam to všechno zapíšeš, ale můžeš použít tuto předpřipravenou šablonu:

TODO denik postavy

### Jméno postavy
*Zapiš si jak se postava jmenuje.*

Dál se můžeš zamyslet nad tím jaká je, jaký je její životní příběh, odkud pochází. Prostě si o ní udělat představu. Strávíš s ní teď nějaký čas, tak ať se trochu poznáte.

### Výběr rasy
Vyber si rasu, v jaké se tvá postava narodila. Na výběr máš tyto:

* **Hobit** - TODO
* **Kudůk**
* **Trpaslík**
* **Elf**
* **Člověk**
* **Barbar**
* **Krol**

### Vlastnosti
*Urči vlastností tvé postavy podle tabulky za pomocí kostek.*

V naší hře zjednodušíme vlastnosti každé postavy (či netvora) na těchto pět vlastnosí:

* Síla (budeme zkracovat `SÍL`) - TODO
* Obratnost (`OBR`) - 
* Odolnost (`ODO`) - 
* Inteligence (`INT`) - 
* Charisma (`CHR`) - 

Pro rasu vybranou v předchozím kroku, pro každou vlastnost si hodíš kostkou (jednou nebo víckrát, podle tabulky) a přičteš nebo odečteš číslo (opět podle tabulky). Dostaneš číslo, které udává jak dobrá (nebo špatná) je tvá postava v dané schopnosti.

Hodnoty v tabulce jsou zakódovány zápisem jako `1k3 - 4`. Tento zápis znamená "hoď jednou trojstěnnou kostkou a odečti čtyřku". Protože trojstěnnou kostku má málokdo, hod trojstěnnou kostkou provedeme tak, že hodíme obyčejnou šestistěnnou a když padne 1 nebo 2, bereme to za 1, když 3 nebo 4 je to 2 a když 5 nebo 6, je to 3.

_Příklad:_ Áďa právě určuje charisma pro svou elfku Jasmínu. Má tedy házet podle `2k3 - 3`. Prvním hodem hodila 5 (tedy 3 po převodu) a druhým 4 (tedy 2). Jasmína má tedy charismu 3 + 2 - 3, takže "+2". Je to tedy nebývalá krasavice.

Takže, pro určení pěti základních vlastností tvé postavy si připrav kostku a házej podle této tabulky:

|  | Síla (SÍL) | Obratnost (OBR) | Odolnost (ODO) | Inteligence (INT) | Charisma (CHR) |
|---|---|---|---|---|---|
| Hobit | `1k3 - 5` | `1k3 - 1` | `1k3 - 2` | `1k3 - 1` | `1k3 - 1` |
| Kudůk | `1k3 - 4` | `1k3 - 1` | `1k3 - 1` | `1k3 - 2` | `1k3 - 3` |
| Trpaslík | `1k3 - 3` | `1k3 - 3` | `1k3 + 0` | `1k3 - 2` | `1k3 - 3` |
| Elf | `1k3 - 3` | `1k3 - 1` | `1k3 - 3` | `1k3 + 0` | `2k3 - 3` |
| Člověk | `2k3 - 4` | `1k3 - 2` | `1k3 - 2` | `1k3 - 1` | `3k3 - 6` |
| Barbar | `1k3 - 1` | `1k3 - 2` | `1k3 - 1` | `1k3 - 3` | `3k3 - 8` |
| Krol | `1k3 - 1` | `2k3 - 4` | `1k3 + 0` | `1k3 - 4` | `2k6 - 6` |

**Pozor:** Po naházení si ještě přidej 3 body do alespoň dvou vlastností jak je libo.

_Příklad:_ Ádina elfka Jasmína má po určení vlastností podle tabulky sílu -1, obratnost +1, odolnost -2, inteligenci +2 a charisma +2. Áďa nyní rozděluje 3 body podle svého uvážení, ale tak aby nedala vše na jednu vlastnost. Na konec se rozhodla že vylepší tyto tři vlastnosti, každou o jedna: síla, odolnost a inteligence. Finální vlastnosti Jasmíny jsou tedy sílu 0, obratnost +1, odolnost -1, inteligenci +3 a charisma +2.

Co si pod čísly představit?

Tak třeba pokud se elf se silou "-3" pokusí vyrazit chatrné dveře v dlouho opuštěné rybářské chýši, nepodaří se mu to a bude muset najít pomoc nebo si poradit jinak (třeba vlést oknem). Naproti tomu barbar se silou "+3" bude široko daleko vyhlášeným silákem a vyrazit i pevné dubové dveře na solidních železných pantech se mu jistě brzo povede (v našem světě bys ho asi našel jak vzpírá na olympiádě). Síla "0" potom představuje běžnou hodnotu, něco co čekat u průměrného obyvatele.

### Životy
*Maximální počet životů postavy: 8 + ODO (čili tvoje odolnost).*

_Příklad:_ Pájina postava, trpaslice Grafita má oolnost +1. Grafita má tedy 9 životů.

O životy můžeš přijít v boji či jako důsledek různých akcí. Rozhodně s nimi ale neplýtvej. Nula životů znamená smrt tvojí postavy.

Jak ztracené životy získat zpět? Každý den ráno, po kvalitním spánku (8 hodin, v suchu a teple) se ti vyléčí až 2 životy (vždy ale jen do maximálního množství). Pokud spánek takto kvalitní nebyl (například tvá postava měla hlídku, nebo celou noc pršelo a vy neměli žádný úkryt), vyléčí se jen 1 život.

Také existují kouzla, lektvary či magické předměty které ti můžou životy vyléčit, mají ale své vlastní pravidla.

### Magenergie
*Maximální množství magenergie tvé postavy: 8 + INT (čili tvoje inteligence).*

I když se se svou postavou neplánuješ věnovat magii, hodnotu si zapiš. Třeba někdy názor změníš.

### Dovednosti
*Pro novou postavu si ze seznamu dovedností vyber 2 různé.*


Jak je to s penězi? Jeden "zlatý" (značíme "zl") se dá rozměnit na 10 "stříbrných" (značíme "st") a jeden stříbrný pak na 10 "měďáků" (značíme "md").

Při vytváření postavy dostáváte TODO zlatých, za které si za tabulkovu cenu (viz. kapitola "Běžné ceny") nakup svůj počáteční inventář. Co ti zbyde si nechej v penězích.
Zkušenosti
Vaše postava bude s tím jak prochází životem získávat zkušenosti. Jakmile jich nastřádá dané množství, může se naučit novou dovednost.

Na rozdíl od reálného světa kdy zkušenosti získáváte i když (nebo dokonce "hlavně když") nějakou tu denní zkoušku pokazíme, tady bude tvoje postava zkušenosti získávat jen když se jí něco nezanedbatelného povede. Ber to jako jakési ocenění toho, že tvoje postava vyřešila úkol či něco podobného.

Ale pozor, zkušenosti se nerovnají počtu zabitých nepřátel. Stejně jako v životě, i tady je diplomatické či nenásilné řešení situace cennější!

První novou dovednost se tvá postava bude moci naučit jakmile dosáhne 50ti bodů zkušeností, za dalších 100 to bude další a tak dále:

### Vybavení do začátku
*Z tabulek níže si nakup libovolné vybavení za 20 zlatých.*

Jednoruční zbraně pro boj tváří v tvář

| Název | Síla zbraně | Cena | Poznámka |
|---|---|---|---|
| žádná | 0 | 0 |  |
| dýka | 2 | 1 zl |  |
| obušek | 2 | 2 st |  |
| tesák | 3 | 4 zl |  |
| čakan | 3 | 1 zl |  |
| krátký meč | 4 | 16 zl |  |
| kyj | 3 | 8 st | Jen pro postavy s SÍL +1 a větší |
| sekera | 3 | 1 zl  | Jen pro postavy s SÍL +1 a větší |
| řemdih | 4 | 2 zl | Jen pro postavy s SÍL +2 a větší |
| válečné kladivo | 5 | 3 zl | Jen pro postavy s SÍL +2 a větší |

Obouruční zbraně pro boj tváří v tvář

| Název | Síla zbraně | Cena | Poznámka |
|---|---|---|---|
| kovaná hůl | 5 | 7 st |  |
| vidle | 4 | 1 zl |  |
| kopí | 5 | 1 zl |  |
| válečná sekera | 4 | 4 zl | Jen pro postavy s SÍL +1 a větším |
| sudlice | 5 | 1 zl | Jen pro postavy s SÍL +1 a větším |
| píka | 5 | 1,5 zl | Jen pro postavy s SÍL +1 a větším |
| tesák a dýka | 4 | - | Jen pro postavy s SÍL +1 a větším |
| krátký meč a dýka | 5 | - | Jen pro postavy s SÍL +1 a větším |
| cep | 5 | 8 st | Jen pro postavy s SÍL +2 a větším |
| halapartna | 4 | 4 zl | Jen pro postavy s SÍL +2 a větším |
| těžký kyj | 5 | 2 zl | Jen pro postavy s SÍL +2 a větším |

Střelné zbraně

| Název | Síla zbraně | Cena | Poznámka |
|---|---|---|---|
| prak | 3 | 1 st |  |
| krátký luk | 4 | 4 zl |  |
| lehká kuše | 4 | 32 zl |  |

Vrhací zbraně

| Název | Síla zbraně | Cena | Poznámka |
|---|---|---|---|
| oštěp | 3 | 4 st |  |
| sekera | 3 | 1 zl |  |
| dýka | 2 | 1 zl |  |
| kámen | 0 | 0 |  |
| flakónek (svěcená voda...) | 0 | 1 zl |  |
| láhev (olej, voda...) | 0 | ? |  |
| pochodeň | 0 | 1 md |  |

Obrana

| Název | Obrana | Cena | Poznámka |
|---|---|---|---|
| žádné brnění | 0 | 0 |  |
| vycpávané | 1 | 16 zl |  |
| kožené | 2 | 40 zl |  |
| šupinové | 3 | 120 zl | Jen pro postavy s SÍL +1 a větší |
| Kroužkové | 4 | 240 zl | Jen pro postavy s SÍL +1 a větší |
| plátové | 5 | 160 zl | Jen pro postavy s SÍL +2 a větší |
| rytířská zbroj | 6 | 800 zl | Jen pro postavy s SÍL +2 a větší |
| štít | 1 | 5 zl |  |

Vybavení

| Název | Cena |
|---|---|
| pochodně 6 ks | 6 md |
| křesadlo | 1 st |
| zrcátko kovové | 1 st |
| olej do lucerny | 3 st |
| lano 10m | 1 zl |
| lucerna | 2 zl |
| batoh | 4 zl |
| kožešiny pro spaní venku | 6 zl |

Oblečení

| Název | Cena |
|---|---|
| nuzné oblečení (odebírá -2 od CHAR) | 2 zl |
| obyčejné oblečení | 8 zl |
| zdobné oblečení (přidává +1 k CHAR) | 70 zl |
| luxusní oblečení, zdobené zlatem a drahými kameny (přidává +2 k CHAR) | 350 zl |

Jídlo

| Název | Cena |
|---|---|
| večeře v hostinci | 1 st |
| jídlo na den | 1 st |



# 1
Na trhu k vám přistoupí cizí muž. Na hlavě má bílý baret, moukou zaprášenou kostkovanou košili a přes větší břicho bílou zástěru.

Nesměle vás osloví: "Jmenuji se Žemlička, jsem tady radním a pekařem. Vypadáte jako zkušení dobrodruhové, tak jsem se na vás dovolil obrátit. Měl bych pro vás jistou prácičku."

Vybídnete ho ať pokračuje: "Za městem stojí stará opuštěná věž. Jistě jste si jí všimli, nedá se přehlédnout. Rád bych ji využil jako sklad obilí. Skladiště ve městě jsou strašně drahá. Lidi ale blekotají něco o tom že tam straší." Chvilku se odmlčel a se sklopenými zraky rychle dodal: "Já ale samozřejmě myslím že to je nesmysl. Pro někoho jako vy", poplácá jednoho z vás po silném rameni, "to nebude nejmenší problém. Pomůžete mi?"

Nějaké peníze by se vám hodily a on nabízí 30 zlatých. Doptáte se na podrobnosti a pochopíte že prostě potřebuje abyste se do věže podívali a ujistili se že tam nestraší - případně to strašidlo vyhnali nebo, nó, zlikvidovali.

Chcete s ním smlouvat o výši odměny? Pak jděte na [zemlicka_smlouvani].

Nebo vám Žemlička připadá podezřelý a raději se na věž ještě poptáte dalších lidí ve městě? Jděte na [patrani_vyptavani].

# zemlicka_smlouvani
Žemlička je zjevně zkušený obchodník a na nějaké to handrkování je zvyklý a jen tak někdo ho k něčemu co nechce nepřesvědčí.

"Cože? Třicet zlatých je vám málo?" ptá se se zděšeným pohledem když ho požádáte o navýšení odměny. "Víte že za to bych tu mohl najmout tucet takových jako jste vy?".

Vy na to: "No ale co všechno to riziko? Straší tam a takový duch nebo jiná magická havěť, to může být pěkně nepříjemné střetnutí, to my známe".

"Ale nic takového tam nehrozí, to jen pověrčiví lidi se bojí a představují si kde co" odráží vaše argumenty Žemlička. "Prostě to tam občíhnete a vyženete nějakou tu kunu co se tam usídlila a dělá tam randál."

"Kdyby to bylo tak jednoduchý, uděláte to sám otče. Nebo pošlete svoje učedníky." hádáte. "Ale ty jste tam asi ani za zlatý prase nedostal a vy se tam taky bojíte a o nás si myslíte že jsme tu cizí, tak že klidně nastavíme svoje krky za ubohých třicet zlaťáků."

...a tak to pokračuje pěkných pár minut. Obě strany zkouší různé argumenty, zkouší toho druhého přesvědčit.

*Vyberte postavu která bude s Žemličkou smlouvat. Hoďte za ni na charisma (pokud má postava dovednost "smlouvání" TODO, nezapomeňte za ni přičíst bonus).*

Pokud je výsledek hodu 2, jděte na [zemlicka_smlouvani_dolu]. Pokud jste dostali 3 až 8, jděte na [zemlicka_smlouvani_stejne]. Pokud ale máte 9 a víc, jděte na [zemlicka_smlouvani_nahoru].

# zemlicka_smlouvani_dolu
Postava která za vaši družinu smlouvala se snažila jak mohla, ale v jednu chvíli Žemlička povídá "Víte co? Mě tohle už nebaví, najdu si někoho jiného, zapomeňte na to." Otočí se na podpatku a odchází.

Skočíte za ním a popadnete ho za rameno. "Počkejte, pane Žemlička. My jsme to tak nemysleli. Nám by se ty peníze opravdu hodily" vychrlíte na něj. "My to teda bereme."

Otočí se na vás s vítězoslavným úsměvem. "A helemese. No dobře, ale teď už je odměna jen 25 zlatých. Berte, nebo odcházím!"

Zkroušeně kývnete na souhlas, raději rychle než odměnu ještě sníží: "Tak teda jo, dojednáno."

Žemlička se usměje, vesele na vás mávne a odchází.

Teď když máte dojednáno, jděte na [zemlicka_smlouvani_hotovo].

# zemlicka_smlouvani_stejne
Smlouvání pokračovalo poměrně dlouho a žádná strana nedokázala přenést nic co by tu druhou přesvědčilo. Nakonec to vás i Žemličku přestalo bavit a tak povídáte: "Tohle nikam nevede. Máte pravdu, 30 zlatých vypadá jako dobrá cena. Nebudeme se tu zdržovat nějakým handrkováním. My jdeme na to, brzo na shledanou."

Žemlička na vás kývne a přitaká: "Moje řeč. Snad to rychle vyřešíte. Pak se na mě doptejte, peníze budu mít připravené."

Mávnete na sebe a rozcházíte se v dobrém. Nyní jděte na [zemlicka_smlouvani_hotovo].

# zemlicka_smlouvani_nahoru
Smlouvání pokračovalo několik dlouhých minut a v jednu chvíli se Žemlička usměje a uznale se na vás podívá. "No, vidím že nejednám s žádnými začátečníky. A taky se mi zamlouváte. Připomínáte mi mně když jsem býval mladý. No co s váma nadělám, tak tedy 40 zlatých. Souhlasíte?"

Spokojeně kývnete a poděkujete mu "Děkujeme, pane Žemlička. A nemusíte se bát. Té záhadě přijdeme na kloub a pokud tam opravdu straší, tak se s tím pořádně popereme."

Žemlička si s vámi potřese rukou, prohodíte ještě několik frází a potom odejde za svými povinnostmi. Nyní jděte na [zemlicka_smlouvani_hotovo].

# zemlicka_smlouvani_hotovo
Jak budete pokračovat? Jste nedůvěřiví nebo snad jen opatrní a pokusíte se o věži získat další informace od někoho jiného? Pak jděte na [patrani_vyptavani].

Pokud se nechcete zdržovat nějakým povídáním a chcete vyrazit rovnou k věži, jděte na [vez_prichod].

# patrani_vyptavani
![Co se děje na náměstí](gamebook/image_mesto_namesti.svg "Co se děje na náměstí"){ width=100% }

Koho se ale zeptat? Prodejci na trhu vypadají velmi zaměstnaně. Usmívají se, ale jak zjistí že se s nimi nechcete bavit o jejich zboží a vašem nákupu, brzo se vám přestanou věnovat. Stejně tak většina nakupujících. Nejsou tu za zábavou, ale pracovně. Učni a učnice vyřizují pochůzky pro své mistry a mistrové, co nejrychleji neboť příliš často zakusili jejich hbitou rákosku. Kuchařky pečlivě vybírají, smlouvají a nakupují aby ještě stihly uvařit. Městská hlídka sice postává, ale dává pozor na kapsáře a výtržníky a zakecat se nenechá.

Po chvíli hledání si všimnete několika lidí kteří by se s vámi snad bavili. U jednoho domku sedí na velkém poleně stařeček. Sedí, opírá se o zeď svého domu, bafá z fajfky a pozoruje šrumec na tržišti. Pokud to chcete zkusit a zajít za ním, jděte na [patrani_starecek].

Také jste si všimli babičky která se asi vrací od pekaře. Z košíku jí čouhá pecen chleba, opírá se o hůlčičku a po každých pár krocích se zastaví aby si oddechla. Pokud se jí chcete zkusit na něco zeptat, teď je na to dobrá příležitost. Zkuste to na [patrani_babicka].

U kašny zase naplnila dvě vědra děvečka z nějakého měšťanského domu a teď tam postává a očividně se jí ještě nechce domů. Rozhlíží se a možná čeká na nějaké kamarádky, ale nikdo se neblíží. Pokud se jí chcete poptat na to co vás zajímá, zkuste to na [patrani_sluzka].

Pokud už máte vyptávání dost, nebo jste změnili názor a další informace nepotřebujete, jděte na [vez_prichod].

# patrani_starecek
Stařeček vypadá poměrně překvapeně když k němu napochodujete. Na takové zjevy jako jste vy asi není zvyklý. Tázavě se na vás zahledí.

*Vyberte si postavu z vaší družinky která s ním bude mluvit a teprve potom pokračujte.*

Pokud je postava která ho osloví muž, jdi na [patrani_starecek_muz]. Pokud je to žena, jdi na [patrani_starecek_zena].

# patrani_starecek_zena
Jako zvolená žena ze tvé družinky přijdeš ke stařečkovi, usměješ se abys prolomila ledy a zeptáš se: "Dobrý den dědečku. Mohl byste mi povědět něco o té velké věži co stojí před hradbami?"

Asi ho tvůj zájem potěšil, protože se chystá odpovědět. Jdi na [patrani_starecek_uspech] aby ses dozvěděla co se vám chystá říct.

# patrani_starecek_muz
Jako zvolený muž z tvé družiny se vydáš promluvit si se stařečkem: "Dobré ráno starý pane!", snažíš se být co nejslušnější. "Mohl bych se vás na něco zeptat?"

"Tož co nadělám chlapče. Co potřebuješ? Ale rovnou říkám, že nic nekoupím" říká děda.

"Ne ne, nic neprodávám" usměješ se. "Rád bych se vás jen zeptal na tu věž co stojí před hradbami. Víte o ní něco?"

*Hoď si na charisma. Pokud to padlo 5 a víc, jdi na [patrani_starecek_uspech], pokud ti padlo míň, jdi na [patrani_starecek_neuspech]*.

# patrani_starecek_neuspech
Děda se zamračí. "Hele, já mám spoustu práce a nemám čas se tady s váma vybavovat. Běžte si otravovat někoho jinýho."

To bylo poměrně jasné odmítnutí a zřejmě nemá smysl se ho dál vyptávat, běž tedy na [patrani_vyptavani].

# patrani_starecek_uspech
Starý muž se se usměje a povídá:

"To je věž ve které před dávnými věky bydlel jeden mocný čaroděj.", řekl stařeček. "Jednoho dne se ztratil a už se nikdy neobjevil. Prý je zakletá, ale já tomu samozřejmě nevěřím!", rychlý nervózní pohled ve směru kde věž stojí ale svědčí o opaku.

"Děkuji, moc jste nám pomohl" poděkuješ a všichni odcházíte.

"Ba ba, klidně zase přijďte. Vím třeba jak se stavěla naše radnice a kdo z toho co měl. To byste se divili..." volá za vámi ještě děda. Teď se vraťte na [patrani_vyptavani].

# patrani_babicka
Prijdete k oddechující babičce a zeptáte se jí na věž před hradbami.

"No být váma, tam bych rozhodně nechodila. Strašilo tam už když jsem byla malá a teď se to prý ještě zhoršilo. Lidi tam prý viděli zářící duchy a slyšeli pekelný rejdy."

Teď se vraťte na [patrani_vyptavani].

# patrani_sluzka
Přijdete ke kašně a povídáte: "Krásná slečno", snažíte se pochlebovat a nevšímat si uhrovité tváře. "Chtěli jsme se vás zeptat na tu věž před hradbama. Prý tam straší?"

"Já bych řekla, že ty řeči o strašení jsou nesmysl. To jen nás naše mámy tak dlouho tou věží strašily, že tu už nikdo neví co je vlastně pravda. Když se tam potom ňákej opilec zatoulá, klidně uvidí i ďábla jak tancuje na střeše jestli víte jak to myslím, hahaha."

Teď se vraťte na [patrani_vyptavani].



# vez_prichod
Kamenná čtvercová věž stojí na rovince, asi sto metrů od městských hradeb. Tři patra z velkých kamenných bloků se zvedají vysoko nad malou městskou palisádu a v rovné krajině poseté poli, sady a pastvinami na sebe zlověstně stahují pozornost. Obklopená je houštinou křoví a mladých stromků, které jsou oblíbenými odpočívadly černých havranů. Jediné dveře jsou zavřené a vypadají funkčně, otvory těch několika malých oken v přízemí jsou zahrazené deskami.

Pokud se chceš prodrat houštinou kolem věže a pokusit se najít nějakou jinou cestu dovnitř než hlavní dveře, jdi na [vez_pruzkum].

Pokud se odvážíš jít přímo k hlavnímu vchodu, jdi na [vez_dvere].

# vez_pruzkum
Okolí věže je zarostlé pichlavými šípky a mladými stromky jejichž větvě rády šlehají do obličeje. Ze špiček stromů na vás hladově zírá několik havranů. Nevypadají že by se vaší hlučnou přítomností nechali vyrušit ze své zádumčivé hlídky. Po hodné chvíli plné trnů a šlahounů se vám podařilo celou věž obejít. Dle očekávání má jen jedny dveře, a to ty které jste viděli už na začátku. Dále má tři malá okénka. Jen jedno vypadá, že by se jím dalo prolézt - je sice poměrně vysoko, ale jako jediné není zahrazené silnými deskami.

Pokud se chceš pokusit prolézt tím otevřeným okénkem na zadní straně věže, jdi na [vez_pruzkum_zachodove_okno].

Pokud se raději vrátíš k hlavním dveřím které jsi viděl při příchodu k věži, jdi na [vez_dvere].

# vez_pruzkum_zachodove_okno
Okénko je výšce mírně přesahující dospělého člověka. Je čtvercové, o straně asi tří čtvrtin metru. Pokud máte v družince vysokého barbara, bez větších obtíží dokáže nahlédnout dovnitř, ale nic užitečného nevidí. Okénko ústí do malé místnůstky s jedněmi zavřenými dveřmi.

Věž je postavená z dobře opracovaných kamenů, přesto se vám zdá že by se po ní vylézt dalo. Není to ani příliš vysoko, takže se domníváte že nic moc neriskujete.

Družinka se chce pokusit nepozorovaně se protáhnout okénkem do věže. Vypadá to, že jakmile se to podaří jednomu z vás, ten či ta už ostatním pomůže dostat se nahoru.. Chvíli se šeptem dohadujete a nakonec vyberete postavu která poleze jako první.

*Vyber jednu postavu z družinky která poleze jako první. Za vybranou postavu si hoďte na obratnost a nezapomeňte na bonus za dovednost akrobacie TODO pokud ji postava má.*

Pokud jste dostali číslo 4 a menší, jděte na [vez_pruzkum_zachodove_okno_selhani]. Pokud 5 a více, jděte na [vez_pruzkum_zachodove_okno_prolezeni].

# vez_pruzkum_zachodove_okno_selhani
Možná to bylo tím jak je kámen stěny vlhký, nebo je to prostě příliš vysoko, každopádně se vylézt nepodařilo a pokus dokonce skončil odřeným kolenem. Přesto nemusíte zoufat. Protože zrovna nikam nespěcháte, o vylezení se můžete pokusit s jinou postavou. S každým členem družinky však jenom jednou.

Pokud to chcete zkusit s jinou postavou, jděte na [vez_pruzkum_zachodove_okno]. Pokud přijmete tuto nepodstatnou porážku, vraťte se na místo kudy jste k věži přišli na [vez_prichod].

# vez_pruzkum_zachodove_okno_prolezeni
Vybraný člen družinky povyskočil, natáhl se a zachytil okraje okna, ze spodu jste pomohli najít solidní stupy pro nohy když stěna věže je porostlá mechem na kterém to pěkně klouže. Pak už jen pár šikovných pohybů a šup, první člen družinky se vyšvihl do místnůstky za oknem. Vyklonil se z okna a podal ruce dalšímu lezoucímu. Ostatní to tímto měli mnohem jednodušší a tak se v malé místnosti za chvílí tísnila celá skupinka. Nyní pokračuj na [vez_prizemi_zachod].

# vez_dvere
Konečně jste došli až k patě věže k solidním železem pobitým dveřím. Pro jistotu našlapujete potichu, aby jste na sebe neupozornili její obyvatele. Dveře mají velkou zahnutou kliku, pod ní klíčovou dírku a uprostřed od pohledu těžké klepadlo. Klepadlo je stylizované do tvaru liščí hlavy s mírně potměšilým či tajemným výrazem - nemůžete se rozhodnout.

Pokud chcete prostě vzít za kliku a otevřít, jděte na [vez_dvere_otevrit]. Pokud o sobě raději dáte vědět a před vstupem spořádaně zaklepete klepadlem, jděte na [vez_dvere_klepadlo]. Pokud se chcete pokusit dveře vyrazit, jděte na [vez_dvere_vyrazit]. Pokud se pokusíte dveře odemknout či vypáčit, jděte na [vez_dvere_odemknout].

# vez_dvere_vyrazit
Rozhodli jste se jít do toho naplno. Všichni v družince jste se do sebe zaklesli, ke dveřím se natočili ramenem a chystáte se do nich pěkně s rozběhem vrazit.

*Urči postavu která bude v čele a hoď za ni na sílu.*

Pokud jste dostali číslo 5 a méně, jděte na [vez_dvere_vyrazit_nic]. Pokud 6 a více, jděte na [vez_dvere_vyrazit_zraneni].

# vez_dvere_vyrazit_nic
Zdá se že dveře, ač na to nevypadaly, vůbec nebyly zamčené. Dokonce ani moc nedržely. Dlouhé roky a působení deště a rzi se k zavíracímu mechanismu nezachovaly nejlépe. A tak se váš vyrážecí klín rozběhl, o dveře se téměř ani nezpomalil a za hlasitého prásknutí ramenem otevíraných dveří jste vběhli do chodby za dveřmi kde jste popadali všichni na jednu hromadu.

Naštěstí se nikomu nic nestalo, a tak se mírně zahanbeně zvedáte zase na nohy a jste rádi že vás nikdo cizí neviděl. Tohle by pověsti drsných dobrodruhů jistě neprospělo.

No, nebudeme to rozmazávat a družinka se tímto ocitá na [vez_prizemi_chodba].

# vez_dvere_vyrazit_zraneni
Zdá se že dveře, ač na to nevypadaly, vůbec nebyly zamčené. Dokonce ani moc nedržely. Dlouhé roky a působení deště a rzi se k zavíracímu mechanismu nezachovaly nejlépe. A tak se váš vyrážecí klín rozběhl, o dveře se téměř ani nezpomalil a za hlasitého prásknutí ramenem otevíraných dveří jste vběhli do chodby za dveřmi kde jste popadali všichni na jednu hromadu.

Protože se vám podařilo vyvinout opravdu pořádnou rychlost a sílu nárazu, přistání nebylo vůbec příjemné. Člen družinky v jejím čele se pořádně narazil o těžké okovaná dveře a potom na něj ještě těmi nejnepříjemnějšími způsoby popadala celá družinka. Rameno je jistě naražené a v žebrech něco snad i křuplo.

*Postava která byla v čele ztrácí jeden bod života.*

Otřepete se, postavíte se a ocitáte se v chodbičce za dveřmi na [vez_prizemi_chodba].

# vez_dvere_otevrit
Opatrně vezmete za kliku a připravujete se na nutnost pořádně zabrat, ale ukázalo se, že klika se celkem snadno pohybuje a bez problémů plní svůj úkol. Panty snad zázrakem nevržou a dveře se téměř neslyšně otevřely. Procházíte do chodbičky na [vez_prizemi_chodba].

# vez_dvere_odemknout
Pokud máte šperhák a umíte s ním zacházet, samozřejmě si tohoto luxusu můžete dopřát. S větší pravděpodobností se ale chystáte použít špičku nějaké tenké dýky, nebo možná máte kus drátu. Ať už jste jen nadšení amatéři či profesionálové nočních řemesel, stačilo se o dveře trošku opřít a ty se začaly rovnou otevírat.

Překvapeně pohodíte hlavou a mírně překvapeně do dveří strčíte aby se otevřely úplně. Nekonalo se žádné vrzání stoletých pantů a závoje pavučin, dveře se prostě otevřely a vy tak vstupujete do věže na [vez_prizemi_chodba].

# vez_dvere_klepadlo
Zvednete klepadlo abyste upozornili obyvatele věže na svůj příchod a pořádně s ním třísknete do dveří. Ozval se hlasitý třesk. Půlka družinky čekala že se nic nestane, půlka že na vás vyrazí armáda nemrtvých příšer. Nestalo se ani jedno toho. Místo toho se dveře, asi po nárazu mohutného klepadla, sami pootevřeli. Tohle jste nečekali a hledíte na to s pootevřenou pusou a chvíli tam jen tak stojíte. Pak se otřepete, pokrčíte rameny, otevřete dveře a vstoupíte do chodby za dveřmi na [vez_prizemi_chodba].

# vez_prizemi_chodba
Stojíte v dlouhé přímé chodbě vedoucí severo-jižně, od dveří ke dveřím. Třetí dveře, dřevěné a bez zámku, jsou potom ve východní stěně. Čistě dřevěné jsou i ty jižní, severní dveře jsou těžké, pobité plechem a opatřené zamykacím mechanismem. V chodbě toho moc k vidění není, takže co teď?

Můžete se pokusit tiše naslouchat, jestli odněkud neuslyšíte podezřelé zvuky. Pokud to chcete zkusit, jděte na [vez_prizemi_chodba_naslouchat]. Pokud chcete vejít do dveří ve východní stěně, jděte na [vez_prizemi_straznice], pokud zkusíte jižní dveře, jděte na [vez_prizemi_hlavni], pokud chcete projít těžkými severními dveřmi, jděte na [vez_dvere].

# vez_prizemi_chodba_naslouchat
Dorozumíváte se posunky abyste netropili žádný hluk. Všichni v družince se přestanou pohybovat a zaposloucháte se do zvuků okolí. Moc jich není. Věž je tichá a vy se soustředíte čím dál tím víc.

*Vyber postavu podle které se bude rozhodovat o úspěchu či neúspěchu a hoď si za ni na inteligenci.*

Pokud jsi dostal číslo 1 nebo 2, jdi na [vez_prizemi_chodba_naslouchat_halucinace]. Pokud byl výsledek 3 a více, jdi na [vez_prizemi_chodba_naslouchat_nic].

# vez_prizemi_chodba_naslouchat_halucinace
Napjatě posloucháš, noříš hlouběji a hlouběji do ticha, snažíš se vytěsnit zvuk vašeho dechu a zachytit cokoli podezřelého. V tom to přijde. Zcela zřetelně slyšíš jak za některými dveřmi, nedokážeš určit za kterými, bručí medvěd! Jsi si jistý že pokud se neprozradíte a rovnou se na něj vrhnete, můžete v nerovném boji zvítězit. Začneš rychle gestikulovat na ostatní členy družinky, snažíš se naznačit velké chlupaté zvíře a jeho kolébavou chůzi. Nejdřív na tebe nechápavě koukají, ale pak se jeden z nic zatváří ublíženě a normálně nahlas povídá "No tak mi trošku kručí v břiše, co má jako bejt?". Naslouchající postava je tím zvukem tak překvapená že jí chvíli trvá než pochopí svůj omyl. Žádný medvěd, jen mohutné kručení v břiše to bylo. Uchechtnete se té situaci a rychle se od představy bručícího medvěda vrátíte do reality úzké chodbičky na [vez_prizemi_chodba].

# vez_prizemi_chodba_naslouchat_nic
Napjatě posloucháš, noříš hlouběji a hlouběji do ticha, snažíš se vytěsnit zvuk vašeho dechu a zachytit cokoli podezřelého, ale ať se snažíš sebevíc, nic neslyšíš. Pokračuj na [vez_prizemi_chodba].

# vez_prizemi_straznice
Malá místnost s oknem zatlučeným deskami přes které prosvítá nějaké to světlo. Vidíte tři rozbité postele se slamníky prolezlými plísní, trosky malých kamínek, stolu a tří židlí. Takhle na první pohled tu není nic zvláštního. Tady asi bydlelo čarodějovo služebnictvo.

Pokud to tu chceš trochu prohledat, jdi na [vez_prizemi_straznice_prohledani].

Pokud se chcete vrátit chodbu před místností, jděte na [vez_prizemi_chodba].

# vez_prizemi_straznice_prohledani
Obrátili jste naruby celou místnost, ale kromě spousty nepořádku a plesnivého sena ze slamníků jste narazili jen na jednu zajímavou věc. Malou rozbitou a prázdnou truhličku.

Pokud se chcete vrátit na chodbu, jděte na [vez_prizemi_chodba].

Pokud chcete zbytky truhličky pečlivě prohlédnout, vyberte jednoho z družiny a *hoďte si na inteligenci*. Pokud jste dostali méně než 3, jděte na [vez_prizemi_straznice_prohledani_neuspech]. Pokud více, jděte na [vez_prizemi_straznice_prohledani_uspech]

# vez_prizemi_straznice_prohledani_uspech
Žádný poklad jste nenašli pokud jste v něj doufali, ale alespoň malý střípek informace: všimli jste si, že truhlička byla asi rozbitá teprve nedávno. Na zlomech má dřevo jinou barvu než všude jinde v místnosti kdy bylo vystavené rokům samoty a chybí na něm jinak všude přítomný prach. Doufáte že vám ta informace zapadne do nějakého většího obrazu tohoto místa později, protože právě teď vám to nijak nepomáhá. Vracíte se na chodbu na [vez_prizemi_chodba].

# vez_prizemi_straznice_prohledani_neuspech
Při prohlížení zbytku truhličky jste si ničeho zvláštního nevšimli. Nyní se vraťte na chodbu na [vez_prizemi_chodba].

# vez_prizemi_hlavni
Vstupujete do velké místnosti.

Tato místnost asi měla zapůsobit na různé žadatele kteří asi kdysi přicházeli za majitelem věže. Nejvíc pozornosti na sebe strhává půlkruhové vyvýšené pódium se třemi schody uprostřed jižní zdi. Přímo proti hlavnímu vstupu na něm stojí sice zaprášené, ale krásné a zjevně pohodlné křeslo (pokud tě zajímá, jdi na [vez_prizemi_podium]). Podél stěn občas vidíte trosky polic a jiné harampádí.

Z místnosti vedou celkem 4 dveře. Jedny uprostřed severní zdi (jdi na [vez_prizemi_chodba]), druhé v jiho-východním rohu (jdi na [vez_prizemi_zachod]), třetí v jiho-západním rohu (jdi na [vez_prizemi_nahoru]) a poslední v severo-západním rohu. Všechny vypadají použitelně, až na ty poslední. Tyto dveře jsou zatlučené, jen se hemží hřebíky a halabala přitlučenými deskami (jdi na [vez_prizemi_spizirna_dvere]).

Uprostřed západní zdi je jediné okno v místnosti. Pokud se tam chceš podívat, jdi na [vez_prizemi_okno].

# vez_prizemi_okno
Okno je a půli zatlučené, ale velkými škvírami je vidět že je otočené přímo na město. Na jeho parapetu leží mírně začouzená olejová lucerna. Zvednete ji a zatřesete s ní. Podle šplouchání usoudíte, že je v ní asi polovina oleje, což podle vašeho odhadu vystačí na dvě hodiny střízlivého svícení.

*Pokud se rozhodnete lucernu si vzít, napište ji do inventáře jedné z postav.*

Nyní se vraťte na [vez_prizemi_hlavni].

# vez_prizemi_podium
Na vyvýšeném půlkruhovém "pódiu" stojí krásné velké křeslo. Má čalouněný sedák a opěrku a područky složitě vyřezávané rostlinnými motivy. Je sice notně zaprášené, ale vypadá pohodlně a přímo vybízí k sednutí.

Pokud ho budete ignorovat, vraťte se na [vez_prizemi_hlavni]. Pokud ho chcete prozkoumat, jděte na [vez_prizemi_podium_pruzkum]. Pokud si chcete vyzkoušet jaké to je seďet v tomto trůnu, jděte na [vez_prizemi_podium_sednout].

# vez_prizemi_podium_pruzkum
*Vyber postavu která chce křeslo prozkoumat a hoď za ni na inteligenci.*

Pokud jste dostali 9 a méně, jděte na [vez_prizemi_podium_pruzkum_nic]. Pokud 10 nebo dokonce ještě více, jděte na [vez_prizemi_podium_pruzkum_ano].

# vez_prizemi_podium_pruzkum_nic
Pečlivě jsi celé křeslo prozkoumal. Dokonce jsi i vlezl pod něj. Klepal jsi na různých místech a hledal skryté pasti a kdo ví co ještě, každopádně nic zajímavého tam není. Vrať se na [vez_prizemi_podium].

# vez_prizemi_podium_pruzkum_ano
Tvá postava to už už chtěla vzdát, ale potom jí myslí proběhl poslední nápad. Ty područky. Celé jsou pečlivě drobně vyřezávané a tak ty malé kruhové hladké části působí podezřele. A opravdu. Po dalším dlouhém zkoumání přijdeš na to, že při dosednutí křeslo z opěrky na záda vystřeluje dva ostré bodce. Kdysi byly pravděpodobně napuštěny i nějakým jedem. Každopádně vyklopení těch bodců se dá zabránit právě zmáčknutím těch dvou kruhových tlačítek.

Teď už se můžeš na křeslo posadit když víš jak vyřadit past, ale žádné příjemné posezení to není když víš že jen kousek od svých zad máš smrtící bodce. Raději toho necháš a vracíš se na [vez_prizemi_hlavni].

# vez_prizemi_podium_sednout
*Vyber postavu která se chce do křesla posadit.*

Stoupneš si zády ke křeslu, rukama se opatrně dotkneš područek a pomalu si sedáš. Představuješ si jaké to je být mocným čarodějem a shlížet odsud na zástupy které tě přišli žádat o nejrůznější rady a přinášejí bohaté dary aby si tě naklonili.

Když dosedneš tvé snění ale přeruší nečekané cvaknutí. Z opěradla vyskočí dva bodce přímo proti tvým zádům. Před nepříjemným poraněním či snad smrtí tě můžou zachránit jen kočičí reflexy.

*Hoď si na obratnost.* Pokud jsi dostal(a) 7 a méně, jdi na [vez_prizemi_podium_sednout_auvajs]. Pokud 8 a více, jdi na [vez_prizemi_podium_sednout_ok].

# vez_prizemi_podium_sednout_auvajs
V křeslu cvaklo a do zad tvé postavy se zaryly dva ostré bodce. Ze zad ti stéká krev. Toto křeslo se o sebe asi umí postarat a sednou si na něj zjevně smí jen jeho právoplatný majitel.

*Hoď si šesti-stěnou kostkou a pokud ti padne 1 nebo 2, tvá postava přišla o 1 život, pokud padne 3 nebo 4 pak ztrácí 2 životy a pokud 5 nebo 6, přichází dokonce o 3 životy.*

Vrať se na [vez_prizemi_podium].

# vez_prizemi_podium_sednout_ok
Tvé skvělé reflexy a každodenní tréning se vyplatily. Hned jak tvá postava zaslechla ono cvaknutí, téměř instinktivně z křesla vyskočila a vyhnula se tím dvěma nebezpečně vyhlížejícím bodcům. Zhluboka si oddechla a o sedání si do křesla ztratila zájem. Nyní jdi na [vez_prizemi_podium].

# vez_prizemi_zachod
Je to opravdu malinká místnost s oknem a dveřmi. Kupodivu to tu dost páchne i když okénko není ničím zatarasené a skvěle větrá. V jednom rohu místnůstky je něco jako velká dřevěná truhla s okrouhlým otvorem v její horní části. K čemu to asi sloužilo?

Pokud chcete tu bednu prozkoumat, jděte na [vez_prizemi_zachod_pruzkum].

Pokud chcete zkusit prolézt oknem ven, jděte na [vez_prizemi_zachod_vylezeni].

Pokud chcete projít jedinými dveřmi v místnůstce, jděte na [vez_prizemi_hlavni].

# vez_prizemi_zachod_pruzkum
*Urči která postava z družinky provádí průzkum.*

Bedna se nedá posunout, sedí pevně na zemi. Zdá se vám že puch příchází přímo z ní. Protože nic jiného se na ní nedá zkoumat, postava prohmatává vnitřek oné okrouhlé díry na horní straně bedny. "Ale tak to snad ne, že mě to nenapadlo hned" naráz zakleje a zhnuseně vytahuje ruku na které ulpělo něco hnědého a páchnoucího. Že on to je prevét?

*Postava která prohledávala si zmenší stupeň charisma o 2. Na původní velikost si jej může vrátit až po pořádné koupeli.*

> Prevét (z latinského locus privatus – soukromé místo) je typ středověkého záchodu.
> Objevuje se na hradech, zámcích i jiných stavbách. ...
> Žádný splachovací systém nebyl potřebný, neboť o patřičný odvod výkalů se zpravidla postarala sama gravitace.
> Tento výraz, respektive jeho počeštěná forma "prevít", se stal nadávkou a synonymem pro nečestného člověka.
>
> -- [Wikipedie: Prevét]( https://cs.wikipedia.org/wiki/Prev%C3%A9t)

Pokud chcete zkusit prolézt oknem ven, jděte na [vez_prizemi_zachod_vylezeni].

Pokud chcete projít jedinými dveřmi v místnůstce, jděte na [vez_prizemi_hlavni].

# vez_prizemi_zachod_vylezeni
Prolézáte úzkým okénkem. Spěcháte, protože v malé místnůstce odkud vede to právě nevoní abychom tak řekli. Venku je ale okno poměrně výš nad zemí a je potřeba šikovně seskočit. Podaří se seskočit beze zranění?

*Za každou postavu si hoď na obratnost. Pokud je výsledná hodnota menší než 3, postava špatně doskočila a ztrácí jeden život.*

Pokračuj na [vez_pruzkum].

# vez_prizemi_spizirna_dvere
Dveře do této místnosti jsou zatlučené, jen se hemží hřebíky a halabala přitlučenými deskami. Někdo asi hodně spěchal, aby je zavřel a aby zavřené i zůstaly.

Můžeš se vrátit na [vez_prizemi_hlavni], nebo se pokusit dveře otevřít na [vez_prizemi_spizirna_dvere_otevrit], nebo pokud je družinka už v minulosti otevřela, můžeš vejít do místnosti za nimi na [vez_prizemi_spizirna].

# vez_prizemi_spizirna_dvere_otevrit
*Vyber postavu (klidně můžeš postupně zkoušet více postav ze své družinky) a hoď za ni na obratnost.*

Pokud je výsledná hodnota menší než 3, postava se zranila za jeden život. Pokud je výsledek menší než 5, nepodařilo se dveře otevřít a musíš to zkusit s jiným členem družiny či jinou postavou. Pokud je hodnota 5 a větší, desky zapraskaly a dveře se začaly pomalu otevírat. Nyní dveřmi můžeš projít na [vez_prizemi_spizirna].

Pokud chcete otevírání vzdát, nebo se jen chcete vrátit, jděte na [vez_prizemi_hlavni].

# vez_prizemi_spizirna
Místnost, kam jste právě vstoupili, je poměrně temná, neboť nemá žádné okno a jediné světlo do ní proniká z otevřených dveří. Z místnosti vedou schody dolů, asi do sklepa. Ty jsou ale halabala zaházené zbytky trámů a desek, jako by se někdo snažil rychle zabarikádovat průchod. Místnost asi sloužila jako nějaký sklad nebo spižírna – stojí v ní dvojice dlouhých, prázdných polic. Počkat, nepohlo se něco támhle pod jednou z nich?

Pokud se chcete obrátit na útěk, vyběhnout z místnosti a zabouchnout za sebou dveře, jděte na [vez_prizemi_spizirna_boj_uprk]. Pokud chcete skočit na schody a pokusit se protáhnout dolů, jděte na [vez_prizemi_spizirna_boj_schody]. Pokud se na to cítíte a chcete se nebezpečí postavit čelem, jděte na [vez_prizemi_spizirna_boj_priprava].

Pokud jste se už s tím nebezpečím vypořádali v nějakém předchozím průchodu touto místností, můžete se tu v klidu porozhlédnout. Na policích, pod nimi či za nimi není opravdu nic, ale pokud byste odtahali nepořádek ze schodiště vedoucího asi do sklepa, dalo by se tudy projít. Pokud se tím chcete zaobírat, jděte na [vez_prizemi_spizirna_schody]. Pokud se tím nechcete unavovat, můžete se vrátit do hlavní místnosti v přízemí věže na [vez_prizemi_hlavni].

Pokud jste už schody dříve vyčistili, můžete po nich sejít do sklepa na [vez_sklep_vstup].

# vez_prizemi_spizirna_schody
Protože v celé místnosti je poměrně solidní přítmí, rozmyslete si, jestli použijete nějaký zdroj světla.

Zabralo vám to dobrou půlhodinu. Schodiště bylo zavaleno zmetí trámků, starých desek a různého nepořádku. Na některých rostly jakési slizké houby a některé byly potřísněné holuby či jinými ptáky. To vám připadlo divné, protože sem se přes ty zavřené dveře žádní ptáci rozhodně nemohli dostat. Pokud máte nějakou teorii, jak se na trámy holubí trus dostal, jděte na [vez_prizemi_spizirna_schody_teorie]. Pokud nad tím ale jen pokrčíte rameny, nic se neděje a můžete jít dál. Každopádně to byla práce špinavá a úmorná, ale nakonec jste průchod uvolnili natolik, aby se tamtudy dalo projít dolů do sklepa.

Pokud jste si u práce svítili, ať už pochodní nebo lucernou, jděte na [vez_prizemi_spizirna_schody_sviceni]. Pokud nic z toho nemáte, nebo jste tím nechtěli plýtvat, jděte na [vez_prizemi_spizirna_schody_potme].

# vez_prizemi_spizirna_schody_teorie
Tak co, jak myslíte, že se do zavřené místnosti bez oken dostaly trámy a desky potřísněné holuby? Pokud vás hraje více, klidně se o tom poraďte a zkuste přijít s nějakou teorií. Máte to? Shodli jste se? Pokud ano, ověřte si ji na [vez_prizemi_spizirna_schody_teorie_overeni].

# vez_prizemi_spizirna_schody_teorie_overeni
Takže bylo to takhle:

> Ty trámy a desky pokryté tu a tam holubím trusem jsou ve skutečnosti z hlavní místnosti v přízemí věže. Někdo je sem přenesl předtím, než dveře zatloukl. Buď tu tehdy ještě ty dvě ploštice zelené nebyly, nebo byly zrovna někde zalezlé, nebo je sem jen házeli otevřenými dveřmi. Asi se pokoušeli zjistit, zda co je ve sklepě zůstane ve sklepě. Kdo a proč to udělal se snad ještě ukáže.

Pokud jste to trefili a odhadli jste, že trámy byly ze sousední místnosti, můžete každé postavě přidat jeden bod zkušenosti. Pokud ne, nic se neděje. Teď se vraťte na [vez_prizemi_spizirna_schody] a pokračujte, kde jste přestali.

# vez_prizemi_spizirna_schody_sviceni
Moudře jste použili světlo a vyvarovali jste se možných zranění a schody jsou teď volné. Odepište si jednu pochodeň nebo jeden díl lampového oleje a jděte buď dolů po schodech na [vez_sklep_vstup], nebo se vraťte do hlavní místnosti věže na [vez_prizemi_hlavni].

# vez_prizemi_spizirna_schody_potme
Pracujete potmě a v této místnosti není zrovna moc světla, takže vám všechno, i ty nejjednodušší činnosti, zaberou spoustu času. Je to namáhavá práce a brzo se potřebujete najíst.

Pokud máte alespoň třetinu denní dávky jídla, škrtněte si ji. Pokud ne, dočasně si snižte sílu, a to až do doby, než se zase pořádně najíte. Pak si sílu můžete obnovit na původní úroveň.

Práce se nakonec podařila a vy můžete pokračovat na [vez_sklep_vstup].

# vez_prizemi_spizirna_boj_uprk
Po zahlédnutí pohybu ve stínu pod jednou policí jste na nic nečekali a vyhrnuli se z místnosti. Zabouchli jste dveře a spěšně je zaklínili několika deskami, které jste z nich před malou chvílí vypáčili. Chvíli u dveří nasloucháte a zaznamenali jste rychlé klapání, co znělo, jako by se po kamenné podlaze pohybovalo několik nohou z velmi tvrdého dřeva, potom drobný náraz do dveří a chvilka jakéhosi chřestění. Potom zase ty divné klapavé kroky, které se vzdálily ode dveří a pak už byl klid.

Pokud máte v družině někoho se schopností *znalost živých tvorů* TODO, jděte na [vez_prizemi_spizirna_boj_uprk_znalost], jinak se vraťte na [vez_prizemi_hlavni].

# vez_prizemi_spizirna_boj_uprk_znalost
Postava, která má schopnost *znalost živých tvorů* TODO, se otočí na vystrašenou družinku a povídá: "Poslouchejte, já myslím, že jsem to poznal. Možná se pletu, ale ty kroky a to chřestění, to znělo jako ploštice. Ne ty malé, co se v létě rojí třeba na vyhřátých zídkách, ale její větší příbuzná. Je to štíhlý, nízký a asi metr dlouhý obří hmyz. Je zelená, šestinohá a chráněná pevným krunýřem. Má velká kusadla, a pokud se zakousne třeba do nohy, dokáže vystříknout jed, který celou nohu na nějaký čas ochromí. Většina lidí se z toho sice vzpamatuje, ale nic příjemného to není."

Teď, když asi víte, čemu jste se za dveřmi vyhnuli, můžete se vrátit do hlavní místnosti v přízemí na [vez_prizemi_hlavni].

# vez_prizemi_spizirna_boj_schody
Doufali jste, že se kolem barikády na schodech protáhnete a těm podivným stvořením se ztratíte. No a nebo aspoň na schodech najdete výhodnou pozici k boji. Ale nic nemohlo být dál od pravdy. Schody jsou kluzké, je na nich poházeno spousta nepořádku o který se snadno zakopává a tak jste si jenom přitížili.

*Zpanikařili jste a váš nepřítel tak získal výhodu. V nadcházejícím boji si každý jeden nepřítel při prvním útoku přičte 2 body k hodu na útok.*

Se schodů už nemáte kam ustoupit, takže se připravte na boj na [vez_prizemi_spizirna_boj].

# vez_prizemi_spizirna_boj_priprava
Zachovali jste klidnou hlavu a k nebezpečí se otočili čelem. Ostatně, v téhle zatuchlé tajemné věži jste nějakou tu nebezpečnou potvoru už dlouho čekali. Stoupnete si tak jak je to pro nás výhodné a připravte se na boj.

*Díky tomu že jste se na boj připravili, získáváte východu. Budete začínat a k prvnímu hodu tohoto zápasu si přečtěte jedničku.*

Střetnutí začíná na [vez_prizemi_spizirna_boj]

# vez_prizemi_spizirna_boj
TODO Boj se dvěma plošticemi zelenými.

> * životaschopnost - 1/2
> * útok - 0 (SÍL) +1 (kusadla) +ochromení (ODO 7)
> * obrana - 0 (OBR) +3 (krunýř)
> * síla - 11 (0)
> * obratnost - 12 (0)
> * odolnost - 14 (+1)
> * inteligence - 1 (-5)
> * charisma - -- (--)
> * bojovnost - 9
> * poklady - 0/0
> * zkušenosti - 5
> * velikost - C
> 
> Ploštice zelená je štíhlý, asi metr dlouhý obří hmyz. Je nízká (do 20 centimetrů), zelená, šestinohá a chráněná pevným chytinovým pancířem. Schovává se ve stínech a k boji používá svá silná kusadla. Zvukově se projevuje výrazným třeskavým zvukem vydávaným do sebe narážejícími tvrdými kusadly.
> 
> Doma je na savaně, kde se schovává v trávě či řídkých křovinách a loví králíky a jiné malé hlodavce. Je-li hladová nebo jich je víc, troufne si ale i na mnohem větší kořist.
> 
> Při jejím útoku kusadly je možnost, že při zakousnutí vystříkne svůj jed (*ODO 7: zasažení jedem/nic*). Pokud k tomu dojde, jejímu soupeři ochrne jedna končetina a kromě toho že ji potom půl hodiny nemůže pohnout (takže třeba při zasažení nohy nemůže nijak extra chodit), snižuje se postavě po dobu trvání účinků jedu bonus obratnosti o jedna. Během dne může jed použít až třikrát.

Pokud stále žijete, své dobrodružství pokračujte na [vez_prizemi_spizirna].

# vez_prizemi_nahoru
Dveře jsou zavřené, ale vypadají plně funkčně. Když vezmete za kliku a zatáhnete, otevřou se jen s tichým zavrzáním. Za dveřmi zatáčí úzká, asi metr široká, chodba se schody vedoucími směrem kamsi nahoru.

Můžeš bud pokračovat po schodech nahoru [vez_prvni_vstup], nebo se vrátit na [vez_prizemi_hlavni].



# vez_sklep_vstup
Jste na rozcestí tvaru písmene "T". Na západ vede chodba se stoupajícími schody. Vyjít po nich znamená jít na [vez_prizemi_spizirna].

Na východ vede temná chodba na [vez_sklep_mistnost].

Na sever se chodba rozšiřuje a jít tam znamená jít na [vez_sklep_pruchod]. Jsou odtamtud slyšet tiché zvuky pomalé vody, nebo, pokud dobře čicháte, něčeho trošku horšího.

# vez_sklep_mistnost
Prošli jste asi tři metry dlouhou chodbou s otevřela se před vámi větší místnost. Už na první pohled tu není nic zajímavého, na zemi jen zbytky dřeva a prach. Možná to tady sloužilo jako sklad, ale není tu nic co by vás zaujalo a tak se raději co nejrychleji vracíte na rozcestí na [vez_sklep_vstup].

# vez_sklep_pruchod
Prošli jste úzkým průchodem a zjistili že chodba se tady zatáčí na západ a notně rozšiřuje. U její západní stěny ústí chodba která vede na jih, u východní stěny je druhý průchod. V místnosti si všimnete nějakého naplaveného nepořádku: písek a větvičky, ale nijak vás to nezaujalo. Pokud si vyberete cestu u západní stěny odkud je poměrně zřetelně slyšet tekoucí voda, jděte na [vez_sklep_prechod]. Pokud raději cestu u východní stěny, jděte na [vez_sklep_vstup].

# vez_sklep_prechod
Asi tři metry procházíte chodbou plnou pavučin a když se na chvíli zastavíte abyste se zaposlouchali, zvuky vody jsou teď úplně jasné. Došli jste do místa kde chodbu kříží široká stoka s tekoucím odpadem z celého města. Podle zbytků sloupků vidíte že tu kdysi byl mostek, ten je ale dávno pryč. Na přebrodění ani nemyslíte, ale možná by se dalo na druhou stranu dostat díky naplavené kládě která se zaklínila z jednoho na druhý břeh. Vypadá pevně, ale poměrně kluzce.

Pokud se chcete vrátit, jděte na [vez_sklep_prechod], můžete se ale pokusit přejít na druhý břeh na [vez_sklep_prechod_pokus].

# vez_sklep_prechod_pokus
Pokud nemáte žádné světlo (nebo s ním nehodláte plýtvat), přechod bude téměř nemožný (pokud jsou všichni v družince trpaslíci, díky jejich schopnosti vidění ve tmě můžeš tento odstaveček ignorovat) a jdi na [vez_sklep_prechod_bez_svetla].

Pokud světlo máte, spotřebujte jednu louč nebo jeden díl lampového oleje a vyberte postavu, která se o přechod pokusí jako první.

*Za vybranou postavu hoďte na obratnost a má-li postava dovednost "akrobacie", nezapomeňte připočítat bonus.*

Pokud jste dostali číslo 3 a méně, jděte na [vez_sklep_prechod_neuspech]. Pokud 4 a více, jděte na [vez_sklep_prechod_uspech].

# vez_sklep_prechod_bez_svetla
Vybraný člen družinky nohou nahmatal kládu a začal se po ní krůček po krůčku sunout přes nevábně vonící stoku. Netrvalo ale dlouho a stalo se co se muselo stát. Uklouznutí, ztráta rovnováhy a pád do stoky.

*Charisma postavy klesá o 3 body a zůstane tak, dokud se postava někde pořádně nevykoupe.*

Stoje v slabém proudu stoky teď může pomoci převést ostatní po kládě. Ocitáte se tak na druhé straně a můžete pokračovat na [vez_sklep_hnizdo].

Nebo se na to chcete vykašlat a vrátit se ke schodům do sklepa? Pak jděte na [vez_sklep_vstup].

# vez_sklep_prechod_neuspech
Postava uklouzla a zřítila se do smrduté stoky. Sice se jí na poslední chvíli podařilo zachytit nějaké trčící větve, ale stoka si i tak vybrala svou daň.

*Charisma postavy klesá o 2 body a zůstane tak, dokud se postava někde pořádně nevykoupe.*

Stoje v slabém proudu stoky teď může pomoci převést ostatní po kládě. Ocitáte se tak na druhé straně a můžete pokračovat na [vez_sklep_hnizdo].

Nebo se na to chcete vykašlat a vrátit se ke schodům do sklepa? Pak jděte na [vez_sklep_vstup].

# vez_sklep_prechod_uspech
Dobrovolníkovi se podařilo neuklouznout a bezpečně přejít nad smradlavou stokou. Nyní se může z druhé strany natáhnou a podat ruku dalším členům družinky kteří teď přecházejí. Přechod je tak mnohem bezpečnější a všem se to bez problémů podaří. Pokračujte dál chodbou na [vez_sklep_hnizdo].

# vez_sklep_hnizdo
Krátkou chodbou od přechodu přes stoku přicházíte do středně velké čtvercové místnosti. Podlaha místnosti je plná větviček, hadrů a malých kostí. Nemáte ale čas si ji prohlížet, protože s podrážděným pištěním se na vás vrhnou krysí obyvatelé této části sklepení.

Dřív než cokoli jiného si družina musí poradit s:

* 3 Krysy obří (životy 5 životy, 3 životy a 3 životy, ÚČ: +2, OČ: +1, zkušenosti: 5)
* 3 Krysy obyčejné (životy 2 životy, 2 životy a 1 život, ÚČ: 0, OČ: 0, zkušenosti: 1)

Pokud se vám ze zjevné přesily rozklepala kolena a chcete si zachránit život, můžete se pokusit uprchnout. Není to jistota, ale pokusit se o to můžete na [vez_sklep_hnizdo_uprk].

Pokud budete bojovat a nemáte světlo, každý váš hod na útok či obranu zmenšete o 3. Pokud světlo máte, odškrtněte si jednu louči či jeden díl lampového oleje. Nyní bojujte a pokud jste přežili, jděte na [vez_sklep_hnizdo_vytezstvi].

# vez_sklep_hnizdo_uprk
Hlava nehlava prcháte před smečkou krvežíznivých krys. Jak utíkáte, krysy na vás stihnou ještě dvakrát zaútočit. Vy na ně v těchto dvou kolech ale útočit nemůžete, protože utíkáte co vám síly stačí. Můžete se jen bránit.

*Za každou krysu budete dvakrát útočit. Členům družinky přiřaďte čísla (například v trojčlenné družince to budou 1, 2 a 3) a házejte kostkou tak dlouho až padne jedno z nich. Na toho pak krysa útočí jako obyčejně. Napadená postava se může bránit jako obyčejně, nemůže ale útočit.*

Pokud útěk někdo přežil, nechť pokračuje na [vez_sklep_prechod_zpet].

# vez_sklep_hnizdo_vytezstvi
Podařilo se vám to. Přežili jste boj s těmi krvežíznivými potvorami. Z místností ve které měly své doupě už žádná další cesta nevede, takže se můžete vrátit k přechodu přes stoku na [vez_sklep_prechod_zpet].

Pokud to tu chcete prohledat a prohrabovat se tím nepořádkem který vám křupe pod nohama, jděte na [vez_sklep_hnizdo_prohledavani].

# vez_sklep_hnizdo_prohledavani
Prohledat tenhle nepořádek rozhodně nebude jednoduchá a bezpečná záležitost. Zcela jistě je to koledování si o otravu krve, ale vidina nějakého ztraceného bohatství vás nenechá odejít bez toho abyste to zkusili.

*Vyberte postavu z družinky která povede pátrání a hoďte za ni na odolnost. Spíš než hledání se tu jedná o schopnost nezranit se, takže třeba dovednost "hledání skrytého" tu nepomůže.*

Pokud jste dostali číslo 1 a méně, jděte na [vez_sklep_hnizdo_prohledavani_otrava]. Pokud 2 nebo 3, jděte na [vez_sklep_hnizdo_prohledavani_nic]. Pokud 4 a více, jděte na [vez_sklep_hnizdo_prohledavani_uspech].

# vez_sklep_hnizdo_prohledavani_otrava
Při prohrabování obsahem krysího hnízda jste se snažili o nic nepoškrábat, protože všudypřítomná špína by ráně neprospěla. Používali ste proto hlavně nohy a rozhrabovali nánosy nohama. V jednu chvíli jste ale uklouzli na něčem co rozhodně zkoumat nechcete a jednu ostrou a špinavou větev si zapíchli přímo do hýždě.

*Zranění postavu stálo 3 životy.*

Vraťte se na [vez_sklep_hnizdo_vytezstvi].

# vez_sklep_hnizdo_prohledavani_nic
Prohrabovali jste se nepořádkem na zemi, ale moc se vám do toho nechtělo. Na nic jste nenarazili a tak jděte na [vez_sklep_hnizdo_vytezstvi].

# vez_sklep_hnizdo_prohledavani_uspech
Prohrabujete se nepořádkem a v rohu místnosti, v hnízdě z tenkých větviček a krysí srsti jste si všimli něčeho blýskavého. Opatrně jste to tam prohrabali a s tím co jste našli jste nad míru spokojeni. Ve vaší dlani se zaleskly 2 prsteny a jedna náušnice.

Jsou krásné a jistě budou i cenné. Pokud má některá postava v družince dovednost "odhadování ceny", jděte na [vez_sklep_hnizdo_prohledavani_uspech_odhadovani], jinak na [vez_sklep_hnizdo_prohledavani_uspech_neodhadovani].

# vez_sklep_hnizdo_prohledavani_uspech_neodhadovani
Nyní si dva prsteny a jednu náušnici s neznámou cenou zapište do osobního deníku. Poznačte si, že pochází z krysího pokladu. Později je můžete prodat ve městě u šperkaře na [mesto_sperkar_krysipoklad_neodhadnuty]. Teď si číslo jen zapište, na konci dobrodružství na něj můžete jít a šperky prodat.

Nyní se vraťte na [vez_sklep_prechod_zpet].

# vez_sklep_hnizdo_prohledavani_uspech_odhadovani
Člen z vaší družinky s dovedností "odhad ceny" se na ony dva prsteny a jednu náušnici vezme do ruky, omyje je vodou z čutory a pečlivě je prohlíží. "Řekl bych, že nám tu do klína spadlo malé bohatství. Tenhle prsten, ten bez kamene bych odhadl na 50 zlatých. Ten druhý, s tím malým kamínkem, asi rubínem, tak na 80. A ta náušnice, řekněme, 40 zlatých."

*Zapište si je všechny i s cenou, u šperkaře budete mít bonus při smlouváni o ceně.*

Později je můžete prodat ve městě u šperkaře na [mesto_sperkar_krysipoklad_odhadnuty]. Teď si číslo jen zapište, na konci dobrodružství na něj můžete jít a šperky prodat.

Nyní se vraťte na [vez_sklep_prechod_zpet].

# vez_sklep_prechod_zpet
Vrátili jste se zpět k přechodu přes podzemní stoku. Stále ještě oddechujete po setkání s hrozivými obřími krysami.

Jak vlastně myslíte že se sem do podzemí ty obří krysy dostaly? Čím se tady živí? Pokud si myslíte že máte odpověď aspoň na jednu z otázek a chcete si ověřit že je správná, jděte na [vez_sklep_hnizdo_vysvetleni].

Pokud chcete prostě přejít na druhou stranu, zase zvolte jednoho z družinky kdo se o to pokusí jako první a pomůže ostatním. S balancováním na naplavené kládě už máte jisté zkušenosti, přesto to nebude zadarmo.

*Za vybranou postavu hoďte na obratnost a má-li postava dovednost "akrobacie", nezapomeňte připočítat bonus.*

Pokud jste dostali číslo 2 a méně, jděte na [vez_sklep_prechod_zpet_neuspech]. Pokud 3 a více, jděte na [vez_sklep_prechod_zpet_uspech].

# vez_sklep_hnizdo_vysvetleni
Máte teorii ohledně těchto dvou otázek?

* Jak se sem do podzemí ty obří krysy dostaly?
* Čím se vlastně živí?

Klidně se o tom poraďte pokud vás hraje víc a zkuste přijít s nějakou teorií. Máte to? Shodli jste se? Ověřte si svou teorii na [vez_sklep_hnizdo_vysvetleni_overeni].

# vez_sklep_hnizdo_vysvetleni_overeni
Takže je to takhle:

> Stoka kterou jste překračovali teče z města. Když jste stoku přecházeli po kluzké kládě, všimli jste si velké mříže. Ta zabraňuje projít stokou z města do mágovy věže či naopak, ale pro krysy překážku nepředstavuje. Krysy se tedy chodí krmit do stok pod městem, kde je vždy hojnost různých čerstvých odpadků. Skrýš pod věží za pevnou mříží jim zase poskytuje klidné útočiště.
> Ve věži pak i dlouho po odchodu dávného mága asi zůstává nějaká zbytková magie a tak krysy které se tu rodily byly generaci od generace větší až vznikly ty příšery se kterými jste měli tu čest.

Pokud jste se alespoň s jednou odpovědí trefili, můžete každé postavě přidat jeden bod zkušenosti. Pokud ne, nevadí. Vraťte se na [vez_sklep_prechod_zpet] a pokračujte s přechodem klády.



# vez_sklep_prechod_zpet_neuspech
Postava uklouzla a zřítila se do smrduté stoky. Sice se jí na poslední chvíli podařilo zachytit nějaké trčící větve, ale stoka si i tak vybrala svou daň.

*Charisma postavy klesá o 2 body a zůstane tak, dokud se postava někde pořádně nevykoupe.*

Nešťastný člen družinky se přebrodil na druhou stranu a pomohl ostatním bezpečně přelézt na [vez_sklep_vstup].

# vez_sklep_prechod_zpet_uspech
S trochou balancování a opatrného našlapování se vybranému členu družinky podařilo přelézt druhou stranu a potom i pomoci ostatním dostat se tam. Pokračujte na [vez_sklep_vstup].



# vez_prvni_vstup
Po dlouhých kamenných schodech jste vystoupali na podestu prvního patra. Ve směru schodů ještě dva metry pokračuje chodbička nebo nějaký výklenek. Protože nahoru je už víceméně tma, spíše ho tušíte, než že byste tam viděli. Po levé ruce máte dveře, pod kterými prosvítá trocha světla.

Můžete se vrátit po schodech do přízemí na [vez_prizemi_hlavni], prozkoumat výklenek na [vez_prvni_vstup_vyklenek] nebo otevřít dveře a pokračovat v průzkumu na [vez_prvni_knihovna].

# vez_prvni_vstup_vyklenek
Družina se rozhodla tuto malou chodbičku prozkoumat. Kdo ví, co by se tady mohlo nacházet za poklady, že? Pokud chcete použít jednu pochodeň či jeden díl lampového oleje, jděte na [vez_prvni_vstup_vyklenek_svetlo]. Pokud nechcete plýtvat, nebo žádné světlo nemáte, zkuste to po tmě a jděte na [vez_prvni_vstup_vyklenek_tma].

# vez_prvni_vstup_vyklenek_svetlo
Poctivě jste hledali v obou rozích, nahoře i dole, vyzkoušeli jste zatlačit na všechny podezřelé kameny (i na několik nepodezřelých) jestli neskrývají nějaký tajný mechanismus. Nic jste ale nenašli. Škrtněte si jednu pochodeň či jeden díl lampového oleje (protože jste je použili při hledání) a vraťte se na [vez_prvni_vstup].

# vez_prvni_vstup_vyklenek_tma
Rozhodli jste se hledat po tmě. Pokud máte v družině trpaslíka, jděte na [vez_prvni_vstup_vyklenek_tma_trpaslik]. Pokud s vámi trpaslík není, jděte na [vez_prvni_vstup_vyklenek_tma_sami].

# vez_prvni_vstup_vyklenek_tma_trpaslik
Trpaslík je jistě velká pomoc v každé družině. Tentokrát vám pomohla jeho schopnost vidění ve tmě a poměrně rychle vám pomohl určit, že tady prostě nic k vidění ani není. Zklamaně se vracíte na [vez_prvni_vstup].

# vez_prvni_vstup_vyklenek_tma_sami
Velmi pomalu jste po tmě prohmatávali výklenek a snažili se najít nějakou tajnou chodbu, ukrytý poklad či cokoli jiného užitečného. Ztratili jste tím spoustu času a nakonec vás to přestalo bavit. Za tu dlouhou dobu vás ale dohnal hlavní nepřítel každého dobrodruha: hlad.

*Pokud máte zásobu jídla, každá postava musí sníst polovinu denní dávky (škrtněte si ji). Pokud nemáte co jíst, neustálé kručení v žaludku vás odteď bude rušit a tak si snížíte inteligenci o 1. Jakmile se pořádně najíte, můžete si inteligenci obnovit na původní úroveň.*

S prázdnými rukama se vracíte na [vez_prvni_vstup].

# vez_prvni_knihovna
Vstupujete do podlouhlé místnosti, která se u severní stěny zatáčí a někam pokračuje. Má dvě malá okna ve východní stěně, dveře v západní a další v jižní stěně. U stěn stojí zaprášené a místy poškozené regály, všechny do jednoho ale prázdné. Stěny jsou tu zdá se poněkud lépe opracované. Asi to byly místnosti, kde mág trávil nejvíce svého času. Ti z družiny, kteří již někdy navštívili nějakou knihovnu, si možná všimnou jisté podobnosti.

Chcete-li projít dveřmi v jižní stěně, potom jděte na [vez_prvni_vstup]. Pokud se rozhodnete pro dveře v západní stěně, jdete na [vez_prvni_nahoru]. Můžete také pokračovat místností jak zatáčí u své severní části, pak jděte na [vez_prvni_pracovna].

# vez_prvni_nahoru
Vstupujete do úzké točité chodby se schody vedoucími nahoru, asi do dalšího patra věže. Schody jsou kamenné a je na nich několik mokrých míst, ale vyjít po nich není žádný problém. Pokračujte na [vez_druhe_hlavni].

# vez_prvni_pracovna
Další podlouhlá místnost, která se dále zatáčí na jihovýchod a jihozápad. V severní stěně je velké, snad 4 metry široké okno, které ale po těch letech postrádá zasklení. Dříve ale muselo být tak velké okno zázrakem moderního stavitelství a sklářství. Pod velkým oknem stojí rozpadlý stůl zničený deštěm a sněhem z již nechráněného okna.

V severozápadním rohu stojí velká okovaná truhlice. Má poškozený zámek a dá se tedy předpokládat, že vše cenné z ní je dávno pryč. Pokud se do ní přesto chcete podívat, jděte na [vez_prvni_pracovna_truhlice].

Můžete odsud pokračovat na jihovýchod do [vez_prvni_knihovna], nebo na jihozápad na [vez_prvni_loznice].

# vez_prvni_pracovna_truhlice
Za vybranou postavu *hoď na inteligenci*.

Pokud je výsledek 3 a níže, jdi na [vez_prvni_pracovna_truhlice_nic], pokud je výsledné číslo vyšší, jdi na [vez_prvni_pracovna_truhlice_nalez].

# vez_prvni_pracovna_truhlice_nic
Postava se přehrabuje v zapáchajícím obsahu truhly poněkud neochotně, jaksi se nedokáže přemoct, aby se podívala pořádně do hloubky. Nakonec popadla kus desky a použila ho jako lopatu. Vybírala s ním obsah truhly a rozsypávala kolem ní s tím, že cokoli cenného by se jistě objevilo. A konečně: v další várce vytahované hmoty se zalesklo něco skleněného. Zahlédl to další člen družinky stojící opodál a vykřikl: "Pozor, je tam něco skleněného!", ale ještě než to dořekl, náklad na provizorní lopatě spadl na zem. Celá družina sledovala, jak na tvrdou kamennou zem kromě cárů látky padá malá buclatá lahvička s temně rudou kapalinou. Dopadla na zem, roztříštila se a červená kapalina se zčásti roztekla po špinavé zaprášené zemi a zčásti vsákla do smradlavých kusů látek. No tak s tímhle už nic nevymyslíte a ve zbytku obsahu truhličky už nic dalšího nenajdete. Můžete pokračovat v průzkumu věže zpět na [vez_prvni_pracovna].

# vez_prvni_pracovna_truhlice_nalez
S očividným přemáháním se postava přehrabuje v zapáchajícím obsahu staré truhly a ve chvíli, kdy to chce vzdát, konečně něco nahmatá. Ze změti hader a chlupů opatrně vytáhne malou baculatou skleněnou lahvičku. Asi do poloviny je naplněná temně rudou kapalinou.

*Pokud ji nepoznáváte, do deníku si ji zapište třeba jako "lektvar s temně rudou kapalinou".*

Pokud ji potřebujete určit a máte v družině někoho s dovedností "vaření lektvarů", jděte na [vez_prvni_pracovna_truhlice_nalez_poznani]. Pokud ne, vraťte se na [vez_prvni_pracovna].

# vez_prvni_pracovna_truhlice_nalez_poznani
Váš alchymista se na lahvičku podívá a s úsměvem se obrátí na nového majitele. "To je jistě lektvar Rudého kříže, skvělý lék na všemožná zranění," řekne. "Barvou a skupenstvím je to jistě ono, ale úplně jistý si být samozřejmě nemůžu. Dá se to ověřit lakmusovým papírkem, ale na to bych potřeboval čas." Nyní se vraťte na [vez_prvni_pracovna].

# vez_prvni_loznice
Dostáváte se do části zatočené místnosti, která asi dříve sloužila jako ložnice. Vévodí jí krb na její jižní stěně a velká a kdysi jistě pohodlná postel s nebesy u západní stěny. Naproti ní, na východní stěně, visí moly prolezlý velký a dříve asi i barevný gobelín, který asi kdysi prostor pěkně zůtulňoval.

Můžete se pokusit prohledat krb na [vez_prvni_loznice_krb]. Kdo ví jestli se v něm něco neskrývá? Nebo chcete propátrat gobelín a stěnu za ním? Je tam sice spousta pavučin, ale na [vez_prvni_loznice_gobelin] se můžete pokusit zjistit jestli se za nimi něco neschovává. No a poslední možnost je ta luxusní postel. Sláma v matraci je sice prolezlá myšmi takže na spaní zrovna neláká, ale třeba se v ní skrývá něco užitečného? Pro průzkum postele jděte na [vez_prvni_loznice_postel]. Pokud vás tu nic nezaujalo, můžete se samozřejmě vrátit na [vez_prvni_pracovna].

# vez_prvni_loznice_krb
Krb je zaprášený, dokonce do něj asi komínem napadalo pár suchých listů. Zkoumáte ho, ale nic zajímavého jste neobjevili. Očistíte si ruce umazané od popela a sazí a vrátíte se k průzkumu ložnice na [vez_prvni_loznice].

# vez_prvni_loznice_gobelin
Gobelín se při každém sebemenším doteku trhá a na zem v oblacích zvířeného prachu padají velké kusy látky. Ten se vám již jistě zachránit nepovede.

> Tapiserie neboli gobelín je označení pro zvláštní techniku převodu obrazových předloh nebo jejich motivů do tkané plošné textilie a pro výrobky vzniklé touto technikou. V češtině je ekvivalentním termínem *nástěnný koberec*.
>
> -- [Wikipedie: Tapiserie](https://cs.wikipedia.org/wiki/Tapiserie)

Ale co stěna za ním? Jako malé děti jste poslouchali spoustu příběhů o starých hradech a velkých jeskyních s tajnými místnosti napěchovanými poklady. Vždy jste si pak představovali jaké by to bylo, kdybyste taky takový tajný vchod někdy našli, takže se rozhodnete že to zkusíte tady. Proč ně, že?

*Vyberte postavu, která se pokusí domnělý tajný vchod najít a hoďte za ni na inteligenci a pokud máte dovednost "hledání skrytého" TODO, nezapomeňte na bonus.*

Pokud jste dostali číslo 7 a méně, jděte na [vez_prvni_loznice_gobelin_neuspech]. Pokud však máte 8 a více, jděte na  [vez_prvni_loznice_gobelin_uspech].

# vez_prvni_loznice_gobelin_neuspech
Hodnou chvíli prohledáváte dlouhou kamennou stěnu. Skáčete z jedno místa které vám připadá podezřelé na druhé ale nic na plat. Nic opravdu zajímavého neobjevujete. Navíc vám z toho dlouhého hledání a čekání všem vyhládlo.

Pokud s sebou máte nějaké jídlo, každá postava musí sníst polovinu denní dávky (škrtněte si ji). Pokud nemáte co jíst, svíravý hlad vás připraví o jeden bod obratnosti. Jakmile se ale zase pořádně najíte, můžete si obratnost obnovit na původní úroveň.

Teď se vraťte k prohledávání ložnice na [vez_prvni_loznice].

# vez_prvni_loznice_gobelin_uspech
Kámen po kameni, spáru po spáře prohledáváte dlouhou kamennou stěnu a doufáte v nějaký ten tajný výklenek který by ukrýval třeba pár dukátů. Zrovna přemýšlíte o tom, že všechny ty báchorky o tajných dveřích které jste poslouchali jako děti jsou jisto jistě nesmysl, když si všimnete podezřele dlouhé pukliny. Sledujete ji a zjistíte že se táhne od země nahoru, do boku a pak zase dolů, zhruba ve tvaru menších dveří. Rozbuší se vám srdce. To je mnohem víc než v co jste doufali!

Jak ale dveře otevřít? Škvírka je příliš úzká aby se tam dalo strčit nějaké páčidlo, takže hledáte otevírací mechanismus. Nakonec si všimnete jednoho uvolněného kamene. Zatlačíte na něj. O dobré tři centimetry se zanořil do stěny a ozvalo se tiché cvaknutí. Kamenné dveře se tiše pootevřely tak že je teď můžete otevřít rukou. Nyní otevřete dveře, dříve prostě část stěny, na [vez_prvni_tajna].

# vez_prvni_tajna
Se zatajeným dechem otevíráte dveře. Dveře odhalí asi tři metry dlouhou a metr širokou slepou chodbu. Ze stropu visí cáry pavučin, ale jinak vypadá netknutá zubem času. Má krásnou podlahu tvořenou leštěnými čtvercovými dlaždicemi. Dlaždice jsou velké a v šachovnicovém vzoru se střídají bílé a černé. Na konci chodby, nejdál od dveří stojí dřevěná kovaná truhla. Nevidíte na ní žádný zámek. Nemůžete se dočkat až zjistíte co skrývá.

Pokud chcete místnost prozkoumat než do ní vstoupíte, jděte na [vez_prvni_tajna_pruzkum]. Pokud se chcete jít rovnou podívat jaké poklady skrývá ona truhla, pokračujte na [vez_prvni_tajna_jdeme].

# vez_prvni_tajna_pruzkum
*Vyberte postavu, která bude místnost prozkoumávat a hoďte za ni na inteligenci. Pokud má dovednost "hledání skrytého" TODO, nezapomeňte přičíst bonus.*

Postava hledí do místnosti a chvíli přemýšlí. Potom pečlivě ohmatává stěny a naklání se dovnitř. Uvidíme jstli se povedlo něco najít. Pokud jste dostali 5 a méně, jděte na [vez_prvni_tajna_pruzkum_neuspech]. Pokud jste dostali 6 a více, jděte na [vez_prvni_tajna_pruzkum_uspech].

# vez_prvni_tajna_pruzkum_neuspech
Prohmatáváte stěny, odhrnuli jste nějaké ty pavučiny a dokonce prohlédli podlahu a hledali natažená lanka. Po chvilce si oddechnete. Všechno vypadá úplně normálně a tak se konečně vydáte podívat se na truhlu na konci chodbičky na [vez_prvni_tajna_jdeme_nevi].

# vez_prvni_tajna_pruzkum_uspech
Opatrně prohledáváte místnost. Prohmatáváte spáry mezi kameny a hledáte cokoliv podezřelého. Ve chvíli kdy už se to chystáte vzdát vás naráz něco upoutá. Když se podíváte ze správného úhlu ve stěnách ve stěně vidíte řadu malých kruhových otvorů. Vypadá to příliš pravidelně na to aby to tam bylo náhodou. Zaměříte na ně svou pozornost a napadlo vás že by to mohli být ústí pro nějaké střely. Kde je ale jejich spouštěcí mechanismus? Pečlivě zkoumáte podlahu a všimnete si že spáry mezi kachličkami jsou volné vypadá to jakoby nějaké kachličky po došlápnutí aktivovali past. Ale které to budou? Černé nebo bílé?

Ty kachličky vám připadají velmi podezřelé. Nakonec se rozhodnete že to prostě vyzkoušíte. Lehnete si, velmi opatrně se natáhnete a zkusíte zmáčknout bílou kachličku. Nic se nestane. Že by past spouštěli až kachličky dále v místnosti? Jen pro pořádek zkusíte zmáčknout ještě černou kachličku. Téměř se leknete když kachlička zajede asi centimetr níže. Ozve se tiché cvaknutí a ze všech otvorů vyletí černé šipky. Díky vaší opatrnosti a nic nezpůsobí jen neškodně narazí do protější zdi. Nyní se můžete vydat těch pár kroků místností a víte že musíte šlapat pouze na bílé kachličky. Učiňte tak [vez_prvni_tajna_jdeme].

# vez_prvni_tajna_jdeme
*Vyberte která postava půjde jako první.*

[vez_prvni_tajna_jdeme_bile]

# vez_prvni_tajna_jdeme_nevi
Cítíte v kostech že tohle nedopadne dobře ale už jste si vybrali. Žádnou past jste nenašli a tak vykročíte do místnosti.

*Vyberte která postava půjde jako první.*

Pokračujte na [vez_prvni_tajna_jdeme_cerne].

# vez_prvni_tajna_jdeme_bile
*Vyberte postavu která se vydá do místnosti.*

Procházíte místnosti a opatrně našlapujete pouze po bílých kachličkách. Jste tak opatrní až občas zavrávoráte. Podaří se vám dojít bez přešlápnutí? Hoďte si na odolnost (pokud má postava dovednost akrobacie připočítejte její bonus) a pokud dostanete méně než TODO tak [vez_prvni_tajna_jdeme_bile_preslapnuti] pokud dostanete TODO a více tak [vez_prvni_tajna_jdeme_bile_nepreslapnuti].

# vez_prvni_tajna_jdeme_bile_preslapnuti
Snažíte se našlapovat co nejpečlivěji a nejpomalej a možná právě proto mírně ztratili rovnováhu. Vaše tělo se naklonilo dozadu a museli jste tak posunout nohu a tím jste sotva o palec přešlápli bílou kachličku. Cítíte jak černá kachlička na které spočinula vaše váha mírně zajíždí do podlahy. Potom už jen slyšíte svistot šipek.

*Hoďte si na obratnost (připočítejte případný bonus za dovednost akrobacie).*

Pokud jste dostali číslo menší než TODO tak [vez_prvni_tajna_jdeme_cerne_neuhnuti], pokud TODO a větší tak [vez_prvni_tajna_jdeme_cerne_uhnuti].

# vez_prvni_tajna_jdeme_bile_nepreslapnuti
Stálo vás to spoustu Opatrného našlapování a pěkných pár kapek potu ale nakonec se dostáváte až truhle nakonec na konci místonosti na [vez_prvni_tajna_truhla].

# vez_prvni_tajna_jdeme_cerne
Stoupli jste na černou kachličku a ucítili jak klesá pod vaší váhou. Ozvalo se tiché lupnutí a ze stěn vystřelili šipky. Vaše postava má však výtečné reflexy a možná se jí podaří se šipkám vyhnout?

*Hoďte na obratnost a (pokud má postava dovednost akrobacie při počítejte si bonus)*.

Pokud vám padlo TODO a méně pokračujte na [vez_prvni_tajna_jdeme_cerne_neuhnuti].

Pokud padlo TODO a více jděte na [vez_prvni_tajna_jdeme_cerne_uhnuti].

# vez_prvni_tajna_jdeme_cerne_neuhnuti
Z otvorů ve stěnách vyletěly šipky. Většina jich neškodně narazila do protější zdi, ale dvě si našly svůj cíl. Jedna se vám zabodla hluboko do stehna a druhá škrábla na břiše. "Áaaaa" zavili jste bolestí, ale podařilo se vám zůstat stát a zabránit tak vystřelení dalších šipek.

*Vaše postava si odepíše TODO životů.*

Pokračujte dál k truhle na konci místnosti na [vez_prvni_tajna_truhla]. Pokud postava zemřela a chcete to zkusit s jinou, začněte znovu na TODO. (TODO Přidat tam i možnost osobně se rozhodnout jestli půjdeme po bílých nebo černých.)

# vez_prvni_tajna_jdeme_cerne_uhnuti
Z otvoru ve stěnách vyletěly šipky. Jejich rychlost však nedokázala překonat rychlost tvých reflexů. Všiml sis že většina šipek míří kamsi na nohy a podařilo se ti nadskočit tak že šipky neškodně prolétly. Jen jednu jsi si po této akrobatické eskapádě vytahoval z hrotem šipky roztržených kalhot, ale to je malá cena za zdraví. Pokračuj k truhle na [vez_prvni_tajna_truhla].

# vez_prvni_tajna_truhla
Konečně jsi se dostal k vytoužené truhle. Je dřevěná a pobitá železnými pruty. Připadá ti podezřelé, že na ní není žádný zámek. Když už si někdo dal tolik práce s tím, aby se k truhle žádný zloděj nedostal, proč ji potom nechal nezamčenou?

Pokud máš podezření na nějaké nepříjemné překvapení, můžeš truhlu opatrně prohledat na [vez_prvni_tajna_truhla_pruzkum].

Pokud má postava na průzkumu dovednost "vycítění magenergie" TODO, můžete ji zkusit využít na něco [vez_prvni_tajna_truhla_magenergie].

Pokud chcete truhlu prostě otevřít, učiňte tak na [vez_prvni_tajna_truhla_otevreni].

Můžete se samozřejmě také vrátit do ložnice na [vez_prvni_loznice] a na truhlu zapomenout.

# vez_prvni_tajna_truhla_pruzkum
Velmi opatrně prohlížíš truhlu. Nejdřív jen pohledem, potom přidáš opatrné doteky. Ať se snažíš jak se snažíš, nevypadá to že by truhla byla zapasťovaná. Vrať se na [vez_prvni_tajna_truhla].

# vez_prvni_tajna_truhla_magenergie
Opatrně položíš na truhlu ruce, zavřeš oči a soustředíš se přesně tak jak je to potřeba při pokusu vycítit magickou energii. Po chvilce se ti v mysli objeví obraz místnosti vybledlý do odstínů šedi. Vše je černé či šedé, jen místo truhly vidíš přelévat se slabě zářící uzlík duhové magie. Odhaduješ, že k truhle je připoutaný nějaký slabší duch. Jaké má ale rozkazy nevíš.

Pokračuj na [vez_prvni_tajna_truhla].

# vez_prvni_tajna_truhla_otevreni
Rozhodl jsi se truhlu otevřít. Opatrně k ní natahuješ ruku, chytáš víko a otevíráš ji. *Pokud máte v družině postavu s dovedností "vycítitění magie" TODO jdi na [vez_prvni_tajna_truhla_otevreni_zavanmagie].* Pokud ne, nic se neděje. Ničeho jste si nevšimli a truhlu jste bez problémů otevřeli.

Do truhly se podíváš na [vez_prvni_tajna_truhla_otevreni_obsah].

# vez_prvni_tajna_truhla_otevreni_zavanmagie
Při otevření truhli jsi pocítil že bylo splněno nějaké kouzlo. Připadalo ti, jako by se jednalo o nějaký poplach, ale slabý, jako by se rozbil už před mnoha lety. Nebo to mohlo být tím že byl kdysi zacílený na konkrétní osobu, ale ta už na tomto světě nemá, a tak se zbytky kouzla rozplynuly v magické dimenzi bez zamýšleného efektu?

Každopádně zdá se že je možné se teď v klidu podívat do truhly a tak pokračuj na [vez_prvni_tajna_truhla_otevreni_obsah].

# vez_prvni_tajna_truhla_otevreni_obsah
Truhla není nijak velká, přesto je naplněná jen skromně. Na dně leží kožený měšec, dvě malé skleněné lahvičky (takzvané "flakónky") a smotek papíru opatřený malou pečetí.

Tvé ruce jako první hmátly po lahvičkách. První má skleněný špunt po okrajích zalitý voskem. Kapalina je průhledná, zbarvená do světle žluta. Druhá potom obsahuje temně rudou kapalinu.

Pokud je v tvé družince postava s dovedností "Alchymie" TODO, o nalezených lektvarech se můžeš dozvědět něco více na [vez_prvni_tajna_truhla_otevreni_obsah_lektvary]. Pokud chcete místo toho pro určení lektvarů využít služeb městské kořenářky, zapište si číslo [mesto_korenarka_lektvary_truhla] a až ji navštívíte, zajděte i na to číslo a nechte si lektvary určit.

Dále jsi v ruce potěžkal měšec. Příjemně to v něm cinkalo a když jsi jeho obsah přepočítal, vyšlo ti krásných 55 zlatých.

Jako poslední jsi z truhly vytál do ruličky smotaný list papíru. Je zajištěný pečetí s nějakým složitým alchymistickým znakem. V rohu ale navíc vidíte uhlem psanou poznámku „ochr. p. nem. 9, pro Soreha, zaplaceno“. Pokud máš v družince někoho s dovedností "Svitky" TODO, můžeš se dozvědět více na [vez_prvni_tajna_truhla_otevreni_obsah_svitek]. Pokud chceš přelomit pečeť a podívat se jaká tajemství jsou napsána uvnitř, jdi na [vez_prvni_tajna_truhla_otevreni_obsah_svitek_aktivace].

Nic dalšího tu k vidění není, a tak se vracíš do ložnice na [vez_prvni_loznice].

# vez_prvni_tajna_truhla_otevreni_obsah_lektvary
Alchymista/ka družiny se na lektvary zahleděl: "Podívejte na tenhle, na ten pečlivě zajištěný skleněný špunt. A ta barva! Tohle vypadá na Megacloumák. Vdechuje se a rychle se odpařuje, takže nedoporučuji otevírat pokud nepotřebujete někoho probrat z mdlob nebo omráčení. Je i mírně léčivý, ale nemá se používat moc často, není to žádné ořezávátko." Potom vzal do ruky ten druhý, otevřel ho, přičichl a spokojeně pokýval hlavou: "A tady je zase zcela zachovalý Lektvar rudého kříže. Vynikající při léčení vážných zranění, ale nikdy by se neměli brát dva zároveň nebo krátce po sobě, to pak můžou mít účinek opačný."

Vrať se k prohlížení obsahu truhly na [vez_prvni_tajna_truhla_otevreni_obsah]

# vez_prvni_tajna_truhla_otevreni_obsah_svitek
Ten kdo se v družince vyzná ve svitcích se podívá na pečeť bez přemýšlení povídá: "No tak tohle je svitek pro ochranu před nemrtvými. To se pozná podle znaku na pečeti. Pokud ho chcete použít, stačí zlomit. A soudě podle té poznámky tady na boku, jak je tu ta devítka, tak myslím že to určuje jeho sílu a řeknu vám, devítka to je celkem jistota."

Vrať se k prohlížení obsahu truhly na [vez_prvni_tajna_truhla_otevreni_obsah]

# vez_prvni_tajna_truhla_otevreni_obsah_svitek_aktivace
Opatrně jsi zatlačil na plošku pečetě aby praskla a umožnila ti svitek rozbalit. Když praskla, přejela tebou vlna horkosti ale přičítal jsi to dlouhému napětí které několik posledních hodin zažíváš když se plížíš touhle zatracenou věží. Svitek jsi rychle rozbalil a ještě jsi stihl zahlédnout blednoucí písmena vyvedená neznámým písmem. Přímo před tvýma očima nápis zmizel a ať na svitek svítíš jak chceš, držíš v ruce jen kus prázdného papíru.

Vrať se k prohlížení obsahu truhly na [vez_prvni_tajna_truhla_otevreni_obsah]

# vez_prvni_loznice_postel
Široká postel má sloupky vyřezávané do spirály. Sloupky jsou vysoké a nahoře drží lehká nebesa která asi dříve nesla látku jako ochranu. V létě před hmyzem, v zimě před chladem. Po té látce ale nic nezbylo a je vidět přímo do postele na které je nevábně vypadající slamník a přes něj přehozená stará, místy rozežraná deka. Možná se vám to jenom zdálo, ale připadá vám, že pod dekou se něco pohnulo. Mohly by to být nějaké myši. Pokud vám to stojí za práci, můžete se přesvědčit na [vez_prvni_loznice_postel_poletuchy].

Postel jste ze všech stran okoukli, ale nevypadá to že by se v ní mohl schovávat nějaký úkryt nebo pod ní nějaké nebezpečí. Tak jste si jí přestali všímat a vrátili se k průzkumu té části patra které asi bylo ložnicí na [vez_prvni_loznice].

# vez_prvni_loznice_postel_poletuchy
Tasíte zbraně a jediným rychlým škubnutím přikrývku strhnete z postele. Čekali jste myši, krysy nebo tak něco, ale právě hledíte na dvě malinké podivné bytosti. Vypadají jako lidé, až na to že jsou asi jenom loket vysocí a, světe div se, na zádech mají křídla. Jedna z nich vypadá jako děvče, druhý jako kluk. Dívají se na vás překvapeně, ale rozhodně to nevypadá že by se vás báli.

Pokud má někdo ve vaší družince dovednost znalost tvorů TODO, jděte na [vez_prvni_loznice_postel_poletuchy_znalost].

Pokud nechcete váhat a chcete je zabít dřív než se jim povede seslat na vás nějaké prokletí, bodnout vás jedovatým špendlíkem nebo co jiného co tyhle potvory dělají, jděte na [vez_prvni_loznice_postel_poletuchy_utok].

Pokud se chcete pokusit promluvit si s nimi, jděte na [vez_prvni_loznice_postel_poletuchy_povidani].

# vez_prvni_loznice_postel_poletuchy_znalost
Ten z vaší družinky, kdo má znalost "znalost zvířat" TODO, se nenápadně nakloní k ostatním členům družinky, která ostražitě zírá na nově nalezené tvory, a šeptem se je bude snažit uklidnit: „Poslouchejte, já myslím, že toto jsou úplně jasně poletuchy. Většinou to bývala užitečná stvoření. Pokud se sedlákovi někde na vesnici usídlí ve stodole, a pokud je to chytrý hospodář..."

"Nebo pokud má chytrou ženu, to spíš," ozve se jedna z žen ve vaší družince (máte-li ji).

"...většinou s nimi dokáže navázat oboustranně výhodné přátelství. Bývají veselé, loajální a pro nás rozhodně nemůžou být nebezpečné, právě naopak, možná by nám mohly pomoct."

To jsou ale zajímavé informace. Nyní jdi zpět na [vez_prvni_loznice_postel_poletuchy].

# vez_prvni_loznice_postel_poletuchy_utok
Rozhodli jste se na ty divné tvorečky zaútočit. Vytasili jste zbraně ale nespouštíte z nich oči. Když ale tvorečci uviděli co máte v plánu dost je to poděsilo. Lehce vyskočili do vzduchu a zároveň roztáhli křídla. Vznesli se, jednou obkroužili postel a než jste se nadáli uletěli oknem v druhé části patra. Nevypadá to že by se chtěli vrátit, takže zase schováte zbraně. Připadáte si hloupě že jste chtěli sáhnout na život tak neškodným stvořením. Nyní se můžete vrátit na [vez_prvni_loznice].

# vez_prvni_loznice_postel_poletuchy_povidani
"Ahoj" ozvete se. "Nebojte se nás, my vám nechceme ublížit" snažíte se zapříst hovor s malými tvorečky.

Ti se po sobě podívají, nakloní se k sobě a něco si šuškají. Potom se ta, která vypadá jako děvče otočí k vám a povídá "My se vás přece nebojíme, takových habánů neohrabanejch." a založí si ruce v bok.

"Jak se jmenujete?"

"Já jsem Pepina a tohle je Tomík. To vy jste tu včera dělali ten rambajs?" ptá se Pepina.

"Včera jsme tu ani nebyli" odpovíte popravdě.

Chvilku si s nimi povídáte a dozvíte se že tihle malý tvorečci přiletěli do města se sedlákem, jakýmsi jejich přítelem kterému se pokoušely na trhu zajistit lepší ceny. Před návratem domů se zastavili tady ve věži aby si odpočinuli, ale včera je tu vyrušila nějaká dvojice habánů (zdá se že Pepina tak říká lidem) která ve spodním podlaží dělala strašný virvál.

"Pozorovali jsme je škvírou ve dveřích, ale pili pálenku a to mi nemáme rádi" přikyvuje Tomík.

Pokud máte nějaký kousek jídla a chcete ho tvorečkům nabídnout jako pozornost jděte na [vez_prvni_loznice_postel_poletuchy_povidani_jidlo].

Pokud se je raději pokusíte přímo z nich vytáhnout informace, jděte na [vez_prvni_loznice_postel_poletuchy_povidani_zhurta].

# vez_prvni_loznice_postel_poletuchy_povidani_zhurta
"Tak povězte nám ještě něco o těch co v přízemí dělali ten kravál. Jak vypadali?" ptáte se.

"Ale, vždyť sme vám říkali že se nám nelíbíli, nechceme o nich mluvit!" zatváří se Pepina kysele.

Vy se ale nedáte "No ale my to potřebujeme vědět, zamyslete se vy pidižvíci."

Pepina se na vás zamračí "Tak tohle né. Prostě se o nich nebavíme" "Tak tak" přikyvuje Tomík. "Celkem jste se nám ale líbili, měli bysme pro vás něco, co by se vám možná mohlo hodit." Pepina mrkla na Tomíka, ten se na chvíli zamyslel a pak spustil:

> Když se dobře rozhlédneš,\
> další dveře nalezneš.

Když to dopovídal, oba vyskočili do vzduchu, zamávali vám na pozdrav a v cuku-letu byli pryč.

Je jasné že se už nevrátí a tak se můžete vrátit zpátky k prozkoumávání ložnice na [vez_prvni_loznice].

# vez_prvni_loznice_postel_poletuchy_povidani_jidlo
Vaši nový známí rádi přijali nabízenou krmi.

*Odepište si jednu dávku jídla. Na to jak jsou malí toho spořádali opravdu hodně.*

"Mňam to je ale dobrota" pochvalovala si Pepina i Tomík. Koukáte na ně jak jim šmakuje. "Poslouchejte my už musíme letět ale máme pro vás něco co by se vám možná mohlo hodit" zatváří se Pepina prohnaně.

Potom kývne na Tomíka a ten se na chvíli zamyslí a začne recitovat krátkou básničku:

> Když se dobře rozhlédneš,\
> další dveře nalezneš.\
> Vevnitř ale pozor dej,\
> na jednu barvu nešlapej.

Když skončí, zamávají vám na pozdrav, rozpustile vás obletí a se smíchem vyletí děravým oknem. Chvíli za nimi zmateně koukáte, ale po chvíli je jasné že už se nevrátí a vy se můžete vrátit k prohledávání ložnice na [vez_prvni_loznice].



# vez_druhe_hlavni
Ocitáte se v jediné místnosti třetího podlaží. Je to vlhká místnost se čtyřmi okny, ze které v jihovýchodním rohu vedou nahoru jedny příkré schody a téměř uprostřed další schody sestupují dolů. V dalším rohu vidíte trosky nějakého přístroje. Jsou tam zbytky dřevěných nožek, pomačkané plechová trubka a skleněné střepy.

Pokud chcete prozkoumat hromádku zbytků, jděte na [vez_druhe_hlavni_dalekohled]. Pokud chcete sejít po schodech dolů, jděte na [vez_prvni_knihovna]. Pokud chcete vyjít po schodech nahoru, jděte na [vez_treti_hlavni].

# vez_druhe_hlavni_dalekohled
Chvilku se prohrabujete zbytky jakéhosi dávného přístroje. Vzdělanější členové vaší družiny v nich na konec možná poznají dalekohled. V hromádce nevidíte nic co by se vám mohlo hodit a tak se vracíte na [vez_druhe_hlavni].



# vez_treti_hlavni
Vyšli jste na rovnou střechu věže. Je z ní krásný výhled do okolí a na město. Ve spárech mezi kameny roste mech a ve větru se třepetají listy několika semenáčků břízy které se usídlily ve spárách. Zábradlí je ztrouchnivělé a na několika místech zničené, takže pozor. Pád dolů by byl dlouhý a asi smrtelný.

Rozhlížíte se po okolí. V dálce na východě vidíte mohutné horské štíty známé především pro trpasličí doly chrlící železnou rudu. Na severu se rozprostírají nízké kopce porostlé hlubokými lesy, město stojí na západě a jih před vás klade členitou zemědělskou krajinu s poli, pastvinami, remízky a rozesetými statky.

Stromy kolem věže z této výšky výhledu nebrání a tak vidíte i bezprostřední okolí věže a cestičku která k ní vede. V tom se zarazíte. Po cestičce k věži se pohybují dvě postavy. Na to že je to vyhlášená strašidelná věž je tu nějak moc živo zapřemýšlíte.

Pokud si myslíte že jsou to jen dva náhodní procházející a chcete na ně zamávat a zavolat by se vás nepolekali, jděte na [vez_konfrontace_mavani].

Pokud ty dva příchozí podezíráte z toho že by mohli mít něco společného s vaším hlavním úkolem od mlynáře Žemličky, možná se chcete rychle přikrčit aby si vás náhodou nevšimli a potom opatrně seběhnout na schody z přízemí a pozorovat, jděte na [vez_konfrontace_pozorovani].

Nebo možná chcete zvolit přímější metodu a prostě si na ně v přízemí počíhat a lapnout je? Pak jděte na [vez_konfrontace_cihani].

Můžete se také pokusit slézt dolů, ale bude to velký risk pokud nemáte dostatečně dlouhé lano. Pokud máte alespoň 10ti metrové lano a chcete slézt dolů a pokusit se příchozím odříznout útěkovou cestu a chytit je, jděte na [vez_konfrontace_slezani]. Pokud takto dlouhé lano nemáte a přesto se chcete pokusit slézt dolů, jděte na [vez_konfrontace_slezani_bezlana].



# vez_konfrontace_mavani
Stoupli jste si blíž k chatrnému zábradlí a začali na příchozí mávat a volat "Haló, tady jsme, nelekejte se!". Ještě chvíli šli dál po cestičce k věži a pak si vás asi konečně všimli. Viděli jste jak se na sebe podívali, potom znovu vaším směrem, pak něco vyjekli a pak se dali na útěk.

Jestli o tajemství ve věži něco věděli, rozhodně nemá cenu zkoušet je dohonit. Mají příliš velký náskok. Zdá se že prozradit se byla chyba. Zdá se vám že o záhadě strašení ve věži asi už nic dalšího nezjistíte.

Vše podstatné ve věži máte prozkoumané, takže se asi můžete vrátit k pekaři Žemličkovi a ohlásit mu co jste zjistili na [zemlicka_hlaseni_30p]. Snad to na slíbenou odměnu bude stačit.

Pokud se chcete ještě porozhlédnout po věži, vraťte se do ní na [vez_treti_hlavni], ale číslo [zemlicka_hlaseni_30p] si zapamatujte a kdykoli se za Žemličkou můžete vydat.

# vez_konfrontace_pozorovani
Přikrčíte se aby vás zdola nebylo vidět a dva příchozí chvíli pozorujete. Jsou to dva prostě oblečení hoši, v učňovském věku. Brzo bylo jisté že směřují do věže a tak co nejrychleji a zároveň co nejtišeji seběhnete na dlouhé schody které vedou z přízemí do prvního patra. Mírně pootevřete dveře a naskládáte se kolem škvíry tak, abyste všichni dobře slyšeli. Nemusíte ani dlouho čekat a uslyšíte kroky. To do hlavní místnosti s trůnem přichází ti dva. Zdá se že si vás nevšimli, což je dobré znamení.

Pokud budete chtít jen sedět a poslouchat co se bude dít, jděte na [vez_konfrontace_pozorovani_poslouchani]. Sice riskujete že vás odhalí, ale možná se dozvíte něco důležitého. Jen doufáte, že se nechystají vyvolávat nějaká nečistá stvoření - nevypadají na to, ale třeba se za neškodné mladíky jen maskují.

Pokud na ně raději chcete vlítnout a pokusit se je chytit než začnou tropit nějakou neplechu, jděte na [vez_konfrontace_pozorovani_chyceni]. Není jisté že se vám je podaří chytit, protože máte horší postavení a budete se muset všichni prodrat jedněmi dveřmi. Spoléháte ale na moment překvapení.

# vez_konfrontace_pozorovani_poslouchani
Napjatě posloucháte co se bude dít. Slyšíte jak rozsvěcí lucernu a povedlo se vám nahlédnout škvírkou ve dveřích, takže máte celkem dobrý přehled o tom co se děje.

Chlapci, jeden poměrně vysoký uhrovitý a druhý nižší s vlasy na ježka, chodí po místnosti s lucernou a vypadají poměrně nervózně. Vidíte jak zkoumají dveře které jste otevřeli a zapomněli zpátky zavřít a všimli si i několika dalších stop které po vás zbyly.

Pak slyšíte toho vyššího, který drží lucernu šeptat: "Franto, sem si fakt jistej, že tohle tu minule nebylo. Já bych se dneska rači vypařil." "To nemůžem", říká ten menší. "Mistr by nám zase namlátil. Poď, uděláme to ať to máme z krku. Kdes to minule nechal tu druhou lampu? No nic, máme aspoň tuhle."

Pak sledujete, jak ten nižší z pod košile vytahuje velkou, otřískanou a zprohýbanou plechovou poklici. "Tak můžem" kývne na toho vyššího s lampou. Ten dojde k oknu, vytočí knot lampy aby svítila co nejjasněji a začne s ní mávat. Z venku je jistě dobře vidět její tančící světlo. Ten menší zase začne mlátit to pokličky kusem dřeva. Dělá to randál který by mrtvého probudil. Do toho oba hulákají "Hůůů" a "Hééé" jako zběsilí.

Občas zastaví a odpočívají, ale vydrží to dělat dobrou čtvrthodinu. Jednou zaslechnete jak ten menší říká tomu většímu "Máš pravdu Jardo. Ještě dneska řeknem starýmu, že s tím končíme, protože pokud nás tu nic nesežere, o hlas přídem určitě." A pak zase randál, svícení a hulákání.

Nakonec toho přeci jenom nechají a ten menší, asi Franta, říká "Tak jo Cirdo, padla, deme. U Bubnu dneska naráželi novou várku, třeba ještě něco zbylo." Pak už jen ztlumili světlo lucerny a skoro vyběhli ven do noci.

No tak to bylo pěkně divné představení. Každopádně začínáte mít jakési tušení o co tady jde a tohle divadlo vám dalo další hromadu informací. Pokud chcete vyrazit k Žouželkovi povědět mu o tom co jste zjistili, jděte na [zemlicka_hlaseni_50p].

Pokud chcete ještě setrvat ve věži a porozhlédnout se tu ještě více, jděte na [vez_prizemi_hlavni], ale zapište si [zemlicka_hlaseni_50p] a za Žemličkou se můžete vydat kdykoli později.

# vez_konfrontace_pozorovani_chyceni
Kouknete na sebe a i beze slov je jasné co chcete udělat. Jeden z družinky zvedne ruku a když mu všichni začnou věnovat pozornost, chvíli počká a pak mávne. Na to znamení otevřete dveře a všichni se naráz pokusíte vřítit do hlavní místnosti.

Bohužel jste si ale nedomluvili pořadí, takže došlo k nějakým strkanicím které vás stály čas. Ti kluci se ale strašně lekli a pokud byste měli čas je pozorovat místo provozování strkanice ve dveřích, viděli byste, jak na hodnou chvíli ztuhli. Pak je dohnaly jejich instinkty a vzali nohy na ramena.

Ten větší byl o krapánek pomalejší a podařilo se vám ho obestoupit ještě v místnosti s křeslem. Ten menší byl sice pohotovější a s hlasitým křikem vyrazil ke dveřím, ale v tom spěchu si nevšiml že jsou zavřené a téměř do nich narazil.

Když zjistili kdo proti nim stojí, otrnulo jim a postavili se vám. Nechcete je zranit a tak si ostražitě odkládáte zbraně. Tohle bude pěstní souboj. Jděte na [vez_konfrontace_prizemi_pestni_souboj]

# vez_konfrontace_prizemi_pestni_souboj
*Pěstní souboj se hází stejně jako ten normální, jen se při něm nepočítá síla zbraně ani kvalita brnění. Útok je prostě jen hod + SÍL, obrana je jen hod + OBR. Účastníci souboje se střídají v kolech jako obvykle. Životy však ubývají jen jako. Jakmile někdo při pěstním souboji "zemře", neumírá ale prohrává v boji. Po ukončení souboje každá postava přichází jen o třetinu životů o které přišla při pěstním souboji.*

Pokud se vám podařilo ty dva přemoct, vyslechněte je na [vez_konfrontace_vyslech].

Pokud přemohli oni vás, je na čase zajít za Žemličkou a povědět mu aspoň to málo co zatím víte na [zemlicka_hlaseni_30p]. Pokud se chcete ve věži ještě porozhlédnout, jděte na [vez_prizemi_hlavni], ale zapište si číslo [zemlicka_hlaseni_30p] a za Žemličkou se můžete vydat kdykoli později.

# vez_konfrontace_cihani
Chvilku jste se tlumeně překřikovali ale nakonec zvítězila varianta "seběhneme do přízemí a počíháme si na ně". Co nejrychleji tedy vyrazíte po schodišti dolů - chcete tam být dřív než ti dva vetřelci. Schodiště ale není v nejlepším stavu a se svícením na neosvětlených částech se také neobtěžujete, takže by se mohlo stát že někdo uklouzne.

*Každá postava si v pořadí v jakém běží dolů hodí na obratnost. Pokud dostaneš 3 a méně, pak jsi na nepřehledné části schodiště uklouzl a po elegantním kotoulu přes několik schodů ses zastavil až o blízkou zeď. Bolí tě snad všude a můžeš se těšit na spoustu modřin. Na čele máš mírně krvácející odřeninu. Odepiš si jeden život. Pokud někdo takto uklouzl, ostatní postavy už nehází. Viděli co se stalo a jistě si budou dávat pozor.*

Konečně dobíháte do hlavní místnosti se zdobným křeslem v přízemí na [vez_konfrontace_cihani_dole].

# vez_konfrontace_cihani_dole
Konečně jste v hlavní místnosti přízemí věže. A bylo to jen o chloupek. Sotva se rozmístíte do jakýchs takýchs úkrytů, vrznou dveře a do místnosti vstupují ti dva které jste pozorovali z vršku věže.

Slyšíte jak se ve dveřích chvíli handrkují. "Já tam dneska nejdu." žadoní jeden hlas. "Šak si to slyšel ne? Něco tam určitě je." "Nebuď strašpytel, víš že tam musíme. A mistr říkal že už jenom třikrát." povzbuzuje ho druhý hlas. Pak je chvíli ticho a z dveří nejdřív vyleze ruka s lampou. Chvíli se nic neděje a pak s povzbuzujícím "No tak dělej, ať to máme za sebou." vejdou i ti dva.

Jsou to chlapci, jeden poměrně vysoký uhrovitý a druhý nižší s vlasy na ježka. Z toho co jste zaslechli víte že se jmenují Franta a Cyril.

Naštěstí se lucerna v roztřesené ruce houpe tak, že vás ve vašich chabých úkrytech nezpozorovali až bylo pozdě. Postoupili do středu místnosti a v tu ránu jste vystoupili ze svých úkrytů a zhurta na ně spustili: "Co tady děláte takhle pozdě holomci, nemáte bejt už dávno doma u maminky?"

Strašně se lekli, ale zdálo se vám že když poznali že jste jen lidé, odvaha se jim trochu vrátila. "Hele nechte nás, je to tady snad vaše? My už stejně musíme jít, tak ustupte." a hrnou se ke dveřím.

"Nacháme vás, ale nejdřív nám musíte pár věcí vysvětlit." nedáte se odbít.

*Vyberte někoho z družinky kdo se pokusí vymámit ty odpovědi a hoďte za něj na charisma. Pokud má postava dovednost smlouvání, tady se použije. Pokud jste dostali 9 a méně, nezadařilo se a jděte na [vez_konfrontace_cihani_dole_neuspech]. Pokud 10 a více, jděte na [vez_konfrontace_cihani_dole_uspech].*

# vez_konfrontace_cihani_dole_uspech
"No teda, vy tady tak talentovaně stojíte." spustíte na ně dokud jsou ještě trošku vyjukaní. Zmateně se na sebe podívají, ale vy hned pokračujete. "A to musíte být i hrozně stateční když takhle v noci dete sem do té opuštěné věže." mažete jim med kolem huby. "No a koukáme že ste pořádní chlapi! S takovýma svalovcema by sme se nechtěli dostat do křížku. Asi tu máte nějaký zařizování co?" pomalu se dostáváte k tomu co vás zajímá.

Konečně se zapojí do diskuse: "Noo, vlastně to je jenom takovej vtip." Podívají se na sebe, asi se očima domlouvají co řeknou. "My tu jen tak rámusíme. Mistr nás sem poslal. Narazili jsme tady sice na jakousi havěť, ale toho se nelekneme, že Cirdo?"

"Jé, vtipy, to my máme rádi. O co jde, třeba vám můžem pomoct" snažíte se z nich nenápadně vytáhnout další informace.

"No on totiž náš mistr" vložil se do toho Cirda, "chce zajistit aby se povídalo že tady straší a tak sem musíme každej večír tady s Frantou chodit a jako strašit."

"Jak jako strašit?"

"No prostě tu enom u okna co směřuje na město blbneme s lucernou a děláme randál" vysvětlí František. "No ale dneska už půjdem, mějte se." Otočí se a odejdou z věže.

Tato rozprava vám dala všechny informace které jste potřebovali a můžete se vydat za Žemličkou vylíčit mu co jste zjistili na [zemlicka_hlaseni_100p]. Pokud se chcete ve věži ještě porozhlédnout, [zemlicka_hlaseni_100p] si zapište a zajděte tam později a teď se můžete vrátit na [vez_prizemi_hlavni].

*Postava která ty dva přesvědčila, získává 10 zkušeností. TODO*

# vez_konfrontace_cihani_dole_neuspech
Pokoušeli jste se ty dva rozmluvit aby vám řekli co o téhle věži ví, ale nebyli jste úspěšní. Koukali se na vás jako pekař na někoho kdo mu sebral už dvě housky a přišel si pro třetí. Byli ostražití a dávali pozor kdy budou moct utéct.

Po chvíli vašeho přesvědčování jak to s nimi myslíte dobře to už asi nevydrželi a skočili vám do řeči: "No tak my už asi půjdeme, žejo" a kývli na sebe, jako že v tom jsou zajedno.

"No tak to prrrrr" vyhrkli jste, ale oni už se vydali ke dveřím. Když jste je chytili za rameno, ruku setřásli a dál se tlačili k východu. Vypadá to že jim budete muset ukázat, že to myslíte vážně. Pokračujte na [vez_konfrontace_prizemi_pestni_souboj].

# vez_konfrontace_slezani_bezlana
Věž je postavená z velkých otesaných kamenů a stojí tam už dlouho, takže mnohé spáry jsou hluboké a to vám dodalo odvahu pokusit se slézt i bez dostatečně dlouhého lana. Lezete jeden po druhém, na straně opačné k přicházejícím. Spěcháte.

*Postupně si na každého člena družinky hoď na obratnost. Pokud má postava dovednost Akrobacie, připočítej si za ni bonus. Pokud jsi dostal 10 a více, postavě se podařilo slézt. Pokud však 9 a méně, jdi na [vez_konfrontace_slezani_bezlana_pad].*

Pokud se všem členům družinky podařilo dostat se dolů, pokračuj na [vez_konfrontace_slezani_dole].

# vez_konfrontace_slezani_bezlana_pad
Při sestupu jsi využil stup který vypadal perfektně, akorát na špičku tvé škorně. Co jsi ale neviděl bylo, že byl porostlý vlhkým lišejníkem. Když jsi na něj přenesl váhu, noha znenadání uklouzla. Na zlomek sekundy jsi visel na jedné ruce, ale ta povolila a zřítil jsi se na zem. Při pádu jsi se potloukl o střechu spodního patra, odřel o větve stromu kterým jsi propadl, ale nejhorší bylo přistání na tvrdou zemi.

*Postava si odečte 5 životů.*

Vrať se na [vez_konfrontace_slezani_bezlana] a pokračuj ve slézání s ostatními postavami z družinky.

# vez_konfrontace_slezani
Někdo z družinky ze svých věcí vylovil lano. Je to velká pomoc pro váš plán. Slézat věž bez lana by bylo náročné.

Tak aby vás nebylo vidět od pěšiny po které ti dva přicházeli lano pečlivě uvážete a hodíte dolů. Potom postupně, všichni bez nehody, slaníte dolů.

Teď je na čase pokusit se chytit dvě postavy které jste shora viděli přicházet. Jděte na [vez_konfrontace_slezani_dole].

*Až bude po všem, pro lano se můžete nahoru na věž vrátit, takže si ho z batohu nemusíš škrtat.*

# vez_konfrontace_slezani_dole
Dostat se dolů vám nějaký čas zabralo a ti dva se mezitím dostali do věže. Obestoupíte tedy vstupní dveře a tiše se radíte jak to provedete.

Pokud vám ti dva které jste viděli vstupovat do věže připadají nebezpeční, můžete zkusit je z venku nenápadně pozorovat na [vez_konfrontace_slezani_poslouchani]. Někdo dohlédne na okno, někdo na dveře a získáte tak jistě dobrou představu o tom co se to tam vlastně děje.

Pokud si věříte a raději se je ve věži pokusíte chytit, jděte na [vez_konfrontace_slezani_chyceni].

# vez_konfrontace_slezani_poslouchani
Rychle utrhnete pár stébel trávy a použijete je na vylosování "šťastlivce", který zůstane hlídat dveře. Taháte a brzo e rozhodnuto. Jeden z vaší družinky s mírně nasupeným výrazem zůstává hlídat vchod do věže. Ostatní se nenápadně proplétají houštím k oknu. Tam se schováte za blízké stromy a keře a napjatě se díváte a posloucháte. Venku už před nějakou dobou padla tma a hordy cvrčků se snaží jeden přehlušit druhého.

Po chvíli se za oknem rozsvítí a nezřetelně slyšíte útržky hovoru: "...tak deme na to..." a "...neboj, prej už jen párkrát" a "...tak teď!" Na ten povel se z věže začal ozývat randál jak kdyby někdo bubnoval na velkou poklici a světlo lucerny se teď míhá přímo u polo-zatlučeného okna.

Kdybyste nevěděli že tohle mají na svědomí dva chuligáni, při pohledu od nedaleké palisády byste to taky jistě přisoudili sílám pekelným. Nemá smysl čekat na konec tohoto představení. Zvlášť když vám už začíná být jasné o co tady jde a tak se můžete vydat za Žemličkou a sdělit mu co jste zjistili na [zemlicka_hlaseni_50p].

Pokud chcete ještě počkat až ti dva odejdou a vrátit se do věže, můžete. Jen si číslo [zemlicka_hlaseni_50p] zapište a jděte tam až se za žemličkou budete chtít vydat. Nyní se můžete vrátit do hlavní místnosti v přízemí na [vez_prizemi_hlavni].

# vez_konfrontace_slezani_chyceni
[vez_konfrontace_slezani_chyceni_uspech]
[vez_konfrontace_slezani_chyceni_neuspech]

# vez_konfrontace_slezani_chyceni_uspech
[vez_konfrontace_vyslech]

# vez_konfrontace_slezani_chyceni_neuspech
[zemlicka_hlaseni_30p]
[vez_prichod]

# vez_konfrontace_vyslech
[vez_konfrontace_vyslech_uspech]
[vez_konfrontace_vyslech_neuspech]
[vez_konfrontace_vyslech_uspech_nasilim]

# vez_konfrontace_vyslech_uspech
[zemlicka_hlaseni_100p]
[vez_prizemi_hlavni]

# vez_konfrontace_vyslech_neuspech
[zemlicka_hlaseni_50p]
[vez_prizemi_hlavni]
[vez_konfrontace_vyslech_uspech_nasilim]

# vez_konfrontace_vyslech_uspech_nasilim
[zemlicka_hlaseni_100p_nasili]
[vez_prizemi_hlavni]



# zemlicka_hlaseni_30p

# zemlicka_hlaseni_50p

# zemlicka_hlaseni_100p

# zemlicka_hlaseni_100p_nasili



# mesto_rozcetnik
Do města jste si buď odskočili z věže něco zařídit nebo po skončení dobrodružství něco málo utratit.

Pokud si ale v městečku chcete něco dojednat, nabízí se vám tyto podniky:

Hledáte-li odpočinek či dobré jídlo, určitě navštivte hospodu U bubnu. Pokud budete mít štěstí, možná tam zastihnete i potulného barda. Hostinská Bětuš vás ráda obslouží jen několik kroků daleko, na náměstí na [mesto_hospoda].

Pokud potřebujete nakoupit zbraně, toto malé městečko žádným zbrojířem nemůže sloužit, ale místní kovář je prý šikovný a kde co opraví. Řekli vám o něm že kdysi býval vojákem a má slabost pro zbraně. Sbírá je a tak by se u něj nějaká ta palice snad našla. Dílnu má na ulici U spodní brány na [mesto_kovar].

Hledáte-li zdravotní pomoc, snad každý vás posílá k místní babce kořenářce. Je to sice mladá holka a "babka" si nechá jenom říkat, ale ve městě prý už pomohla spoustě lidem a v tom co dělá se vyzná. Žije mimo městské hradby ale na dohled od města u lesa na [mesto_korenarka].

Nějaké ty běžně dostupné zásoby pak určitě seženete v Koloniálu Pírko. "Rozličné zboží za rozumné ceny pro pána i kmána" jak hlásá cedule na druhé straně náměstí na [mesto_kolonial].

Pokud tu už nic nepotřebujete, buď se vraťte tam kde jste přestali, nebo se budeme těšit u nějakého dalšího gamebooku.

# mesto_hospoda
Hospoda se jmenuje "U ztracených nadějí" a vede ji vysoký štíhlý elf. Nebo je to možná elfka, těžko se to pozná. Z dlouhých blonďatých vlasů vykukují špičaté uši. Je tam čisto, ale cítíte jakousi ponurou (TODO něco jako spis ze se tam nic nehybe) atmosféru. Těch pár hostů co tu sedí buď jen tiše usrkávají ze svých vysokých sklenic, nebo se tiše a jaksi ospale baví. No a ten hospodský (nebo hospodská) jsou věrným obrazem své hospody. Když vejdete, ani si vás nevšimnout a tak se musíte ozvat sami.

"Pěkný den vespolek" zahulákáte na celou místnost a potom přímo k majiteli: "rádi bysme si něco nakoupili, šlo by to?"

"Jaký podivný vítr vás zavál do tohohle zapadákova? Pro mě za mě, vyberte si byste chtěli, ale za nic neručím." ospale odpoví.

"Jak to myslíte že za nic neručíte?"

"No jak to říkám. Včera mi dovezli maso co bych nejedl ani kdybych ho jedl a to víno co kupuju? To je spíš ocet. Ale jestli vám to nevadí, tak hurá do toho" ušklíbne se.

Vypadá to že nemá svůj den, tak se raději vyptáte na konkrétní sortiment a ceny a vypadá to že něco koupit by se tady dalo.

TODO sortiment

Kromě nákupu se tu můžete taky dobře najíst a vyspat. Pokud vás to zajímá, jděte na TODO.

*Pokud budete s hospodským smlouvat, hoďte si na charisma, přidejte případný bonus za dovednost smlouvání. Hospodského se vám podařilo přesvědčit, pokud jste dostali 9 a více. Zdá se vám, jako by ho vlastně nic moc nezajímalo, včetně vašich zlaťáků.*

Pokud jste tu skončili, vraťte se do města na [mesto_rozcetnik].

# mesto_kovar
Kovárna stojí nedaleko a jednoduše se hledá. Rozléhá se z ní bušení pravidelné bušení. Kovářku najdete venku, pod přístřeškem u kovadliny. Ženu kovářku jste ještě neviděli. Pracuje na něčem velkém, asi na pluhu. "Dobrý den kovář-ko" pozdravíte s malým zaváháním když si udělá malou pauzu.

Usměje se na vás veselýma očima a zpocený obličej umazaný od sazí si otře do hadry na opasku. "Tak co to bude, drobotino?" zeptá se. Oslovení "drobotino" by vás možná normálně urazilo, ale od ní to zní v pořádku. Je vysoká snad dva metry, ruce má silné jako stehna normálního chlapa a ramena široká že dveřmi normálně neprojde. Určitě má barbarské předky.

"No, mysleli jsme že by se u vás možná daly koupit nějaké zbraně madam, nebo možná nějaký kousek brnění?"

"Hahaha, to mi lichotíte" potěšeně se zasměje. "Já většinou dělám jenom takový obyčejný věci. Vidíte" a mávne k polici s rozdělanými zakázkami. Jsou tam podkovy, násady na rýče, sekery a taky jedny vidle. "Ale počkejte, něco vyhrabu vzadu v baráku."

Za chvíli se vrátí a v náručí přináší několik promaštěných kožešin které ukrývají železem chřestící náklad. Všechno to rozloží před vás a i když toho není moc, vybrat by si mohl každý.

TODO sortiment

*Pokud budete s kovářkou smlouvat, hoďte si na charisma, přidejte případný bonus za dovednost smlouvání. Slevu se vám podaří usmlouvat pokud jste dostali 11 a více.*

Pokud má někdo z vás zrezivělou zbraň, kovářka vám ho za desetinu jeho ceny přebrousí a opraví. Bude jako nový a síla útoku se jí zvedne na hodnotu podle tabulky výše.

Pokud jste tu skončili, vraťte se do města na [mesto_rozcetnik].

# mesto_korenarka
Kousek za městským opevněním stojí malá chatrč. Vypadá jako by byla uplácaná z bláta, velké kameny vidíte jen v základech. Má hrbolaté stěny které s velkou rezervou přesahuje střecha z rákosových došků. Z každého střešního trámu vysí několik svazečků různých bylin či plátěné pytlíky s neznámým obsahem. Na okně stojí malá klícka v ní krásně vybarvený stehlík který si vás prohlíží malýma černýma očkama.

Zabušíte na dveře a když se ozve přívětivé "No jen poťte, poťte", vejdete dovnitř.

V potemnělé komoře zády k vám sedí bába a cosi dělá na stole před sebou. Její šedé vlasy jsou svázané do ohonu. Vedle ní je opřená hůlka s do leskla ohmatanou vyřezávanou soví hlavou. Buď zapomněla že vás pozvala dovnitř, nebo si vás nevšímá. Vy sázíte na to druhé.

"Tak kdo se ujme rozhovoru s tou starou špachtlí?" ptá se jeden z vás. "Asi bude potřeba dost křičet, hádám."

Od babky se ozve jakési zahýkání, ale dál si vás nevšímá a věnuje se tomu co má před sebou.

"Dobrý den babičko" zavoláte. Žádná odezva.

"Ta je hluchá jak poleno. Co kdybysme si prostě vzali nějaký to léčivý kvítí tady" navrhuje jeden z družinky po nejbližším svazečku usušených bylin, "a půjdeme?"

V tom se od babky zcela zřetelně ozve "To bych ti nedoporučovala panáčku se tohohle snopku ani dotýkat. A děkuju za optání, slyším dobře." Otočí se na vás a i když je jistě hodně stará, hledí na vás pronikavýma očima. "Karty mi řekly že mám čekat nové zákazníky, ale že budou takhle nevychovaní se nezmínili."

Nastala chvilka trapného ticha. Tohle jste nečekali a když jste se vzpamatovali, pokusili jste se to urovnat jak nejlépe se dalo: "Promiňte madam, moc se omlouváme za ty řeči. My to tak nemysleli. Už se to nestane, opravdu."

Kořenářka teď vypadá spokojeně. "Tak copak ode mě potřebujete slovutní dobrodruhové?" ptá se s pobaveným výrazem.

*Smlouvání s babkou kořenářkou se povede, jen pokud hodem na charisma s případným bonusem za smlouvání dostanete 12 a více. Je to totiž velmi chytrá žena a zná cenu svých znalostí a své práce.*

TODO sortiment

Pokud jste vyřídili všechno co jste potřebovali, vraťte se do města na [mesto_rozcetnik].

# mesto_korenarka_lektvary_truhla
TODO Urceni lektvaru z pudy za penize - toto je jen kopie jineho textu ktery se da pouzit:

Alchymista/ka družiny se na lektvary zahleděl: "Podívejte na tenhle, na ten pečlivě zajištěný skleněný špunt. A ta barva! Tohle vypadá na Megacloumák. Vdechuje se a rychle se odpařuje, takže nedoporučuji otevírat pokud nepotřebujete někoho probrat z mdlob nebo omráčení. Je i mírně léčivý, ale nemá se používat moc často, není to žádné ořezávátko." Potom vzal do ruky ten druhý, otevřel ho, přičichl a spokojeně pokýval hlavou: "A tady je zase zcela zachovalý Lektvar rudého kříže. Vynikající při léčení vážných zranění, ale nikdy by se neměli brát dva zároveň nebo krátce po sobě, to pak můžou mít účinek opačný."

Pokud chcete u babky ještě něco zařídit, jděte na [mesto_korenarka], jinak se vraťte do města na [mesto_rozcetnik].

# mesto_kolonial
Přivítá vás velký vývěsní štít se zdobně vyvedeným nápisem "Zboží koloniální". Ač se obchod tváří jako něco extra, při pohledu na nabídku vidíte že jde prostě o prodej všeho možného. Všech těch běžných věcí které měšťan nebo sedlák potřebují a ve městě není nikdo jiný kdo by je prodával.

Máte štěstí. Dnes tu obsluhuje jen pomocník a ne majitel, takže pokud se pokusíte smlouvat, stačí vám přehodit 6-ku (*smlouvání se povede, pokud hodem na charisma s případným bonusem za smlouvání dostanete 7 a více*).

Sortiment: TODO

Pokud jste s nákupem skončili, vraťte se zpět do města na [mesto_rozcetnik].

# mesto_sperkar_krysipoklad_odhadnuty
Přicházíte do šperkařské dílny. Když zabušíte na dveře, musíte poměrně dlouho čekat než zevnitř něco uslyšíte, ale nakonec se dveře přeci jen opatrně pootevřou. Zevnitř vykoukne trpasličí tvář s dlouhým vousem svázaným provázkem kousek pod bradou. "Neznám vás, co chcete?"

"Přišli jsme prodat nějaké šperky, ale jestli nemáte zájem, půjdeme jinam." na oko se otáčíte a chystáte se odejít.

Majitel dílny ale hned otočí. "Počkejte, počkejte, přece se nic nestalo. Říkají mi Valounek. Pojďte dovnitř, podíváme se na to vaše zboží."

Dojdete do malé, ale dobře osvětlené místnosti. Valounek sedne za stůl uprostřed místnosti a rutinním pohybem shodí své vousy z pracovní plochy. Na stole stojí lampa a velká lupa na stojanu. Celá družinka se natěsná kolem stolu a podáte mu 2 prsteny a náušnici kterou jste našli v krysím doupěti pod věží.

Valounek je chvíli obrací v ruce a dívá se na ně přes lupu a pak se na vás podívá a ptá se: "No, vypadá to dobře. Tak kolik byste si za to představovali?"

Protože se vám podařilo odhadnout cenu šperků (na 50 a 80 za prsteny a 40 zlatých za náušnici), odpovíte "Mají cenu 170 zlatých, takže 20 procent dolů, to jsme na 136 zlatých."

*Pokud chcete zkusit usmlouvat vyšší cenu, vyberte člena družinky a hoďte za něj na charisma. Pokud má postava dovednost "smlouvání", nezapomeňte na bonus.*

Pokud jste dostali číslo 8 a menší, jdi na [mesto_sperkar_krysipoklad_odhadnuty_neuspech], pokud 9 a víc, pak jděte na [mesto_sperkar_krysipoklad_odhadnuty_uspech].

# mesto_sperkar_krysipoklad_odhadnuty_neuspech
S Valounkem jste se dlouho dohadovali, ale je vidět že to je zkušený obchodník. Neustoupil ani o píď a tak jste zkončili na těch 136 zlatých. To ale vám ale vůbec nepřipadá málo a tak odcházíte zcela spokojení. Vraťte se na městské náměstí na [mesto_rozcetnik].

# mesto_sperkar_krysipoklad_odhadnuty_uspech
S Valounkem jste se dlouho dohadovali a nakonec se vám podařilo usmlouvat cenu na 153 zlatých. Odcházíte nad míru spokojeni. Vraťte se na městské náměstí na [mesto_rozcetnik].

# mesto_sperkar_krysipoklad_neodhadnuty
Přicházíte do šperkařské dílny. Když zabušíte na dveře, musíte poměrně dlouho čekat než zevnitř něco uslyšíte, ale nakonec se dveře přeci jen opatrně pootevřou. Zevnitř vykoukne trpasličí tvář s dlouhým vousem svázaným provázkem kousek pod bradou. "Neznám vás, co chcete?"

"Přišli jsme prodat nějaké šperky, ale jestli nemáte zájem, půjdeme jinam." na oko se otáčíte a chystáte se odejít.

Majitel dílny ale hned otočí. "Počkejte, počkejte, přece se nic nestalo. Říkají mi Valounek. Pojďte dovnitř, podíváme se na to vaše zboží."

Dojdete do malé, ale dobře osvětlené místnosti. Valounek sedne za stůl uprostřed místnosti a rutinním pohybem shodí své vousy z pracovní plochy. Na stole stojí lampa a velká lupa na stojanu. Celá družinka se natěsná kolem stolu a podáte mu 2 prsteny a náušnici kterou jste našli v krysím doupěti pod věží.

Valounek je chvíli obrací v ruce a dívá se na ně přes lupu a pak se na vás podívá a ptá se: "No, vypadá to dobře. Tak kolik byste si za to představovali?"

Protože se vám nepodařilo odhadnout cenu šperků, tipnete si "Co kdyby jste nám dal 100 zlatých?"

*Pokud chcete zkusit usmlouvat vyšší cenu, vyberte člena družinky a hoďte za něj na charisma. Pokud má postava dovednost "smlouvání", nezapomeňte na bonus.*

Pokud jste dostali číslo 8 a menší, jdi na [mesto_sperkar_krysipoklad_neodhadnuty_neuspech], pokud 9 a víc, pak jděte na [mesto_sperkar_krysipoklad_neodhadnuty_uspech].

# mesto_sperkar_krysipoklad_odhadnuty_neuspech
S Valounkem jste se dlouho dohadovali, ale je vidět že to je zkušený obchodník. Neustoupil ani o píď a tak jste zkončili na těch 136 zlatých. To ale vám ale vůbec nepřipadá málo a tak odcházíte zcela spokojení. Vraťte se na městské náměstí na [mesto_rozcetnik].

# mesto_sperkar_krysipoklad_odhadnuty_uspech
S Valounkem jste se dlouho dohadovali a nakonec se vám podařilo usmlouvat cenu na 153 zlatých. Odcházíte nad míru spokojeni. Vraťte se na městské náměstí na [mesto_rozcetnik].


# Epilog
TODO
