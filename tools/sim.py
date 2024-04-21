#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import copy
import random


class Postava:

    def __init__(self):
        self.jmeno = None
        self.zivoty = None
        self.magenergie = None

        self.sila = None
        self.obratnost = None
        self.odolnost = None
        self.inteligence = None
        self.charisma = None

        self.sila_zbrane = None
        self.kvalita_zbroje = None

    def popis(self):
        print(f"Jmeno: {self.jmeno}")
        print(f"Zivoty: {0 if self.zivoty < 0 else self.zivoty}")

    @property
    def zivy(self):
        return self.zivoty > 0

    @property
    def utok(self):
        return self.sila + self.sila_zbrane + k6()

    @property
    def obrana(self):
        return self.obratnost + self.kvalita_zbroje + k6()

    def utok_na(self, souper):
        utok = self.utok
        obrana = souper.obrana
        zraneni = utok - obrana
        if zraneni > 0:
            ###print(f"DEBUG: {self.jmeno} zranil {souper.jmeno} za {zraneni} zivotu (utok byl {utok} a obrana {obrana})")
            souper.zivoty -= zraneni


class Skupina(list):

    def __init__(self, clenove):
        super().__init__(clenove)

    def __len__(self):
        return len(self.zivy)

    @property
    def zivy(self):
        return [i for i in self if i.zivy]


def k6():
    return random.randint(1, 6)


def souboj(jedni, druzi):
    while len(jedni) > 0 and len(druzi) > 0:
        for prvni in jedni.zivy:
            druhy = random.choice(druzi.zivy)
            prvni.utok_na(druhy)
        for druhy in druzi.zivy:
            prvni = random.choice(jedni.zivy)
            druhy.utok_na(prvni)

    ###for postava in jedni + druzi:
    ###    postava.popis()

    if len(jedni) > 0:
        return 1
    else:
        return -1

a = Postava()
a.jmeno = "Aaa"
a.zivoty = 10
a.sila = 1
a.obratnost = 1
a.sila_zbrane = 1
a.kvalita_zbroje = 1

z = Postava()
z.jmeno = "Bbb"
z.zivoty = 10
z.sila = 1
z.obratnost = 1
z.sila_zbrane = 1
z.kvalita_zbroje = 1

jedni = Skupina([a])
druzi = Skupina([z])

loops = 10000
summary = 0
for i in range(loops):
    jedni_loop = copy.deepcopy(jedni)
    druzi_loop = copy.deepcopy(druzi)
    summary += souboj(jedni_loop, druzi_loop)
print(f"Prvni druzinka vyhrala v {summary/loops*100}%")
