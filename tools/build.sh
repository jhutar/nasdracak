#!/bin/bash -eux

rm -rf docs/build/

sphinx-build -M latexpdf docs/source/ docs/build/
sphinx-build -M latexpdf docs/source/pravidla/ docs/build/
sphinx-build -M latexpdf docs/source/predmety/ docs/build/
sphinx-build -M latexpdf docs/source/bestiar/ docs/build/
sphinx-build -M latexpdf docs/source/dobrodruzstvi/ docs/build/
sphinx-build -M latexpdf docs/source/dobrodruzstvi/opustena_magova_vez/ docs/build/
sphinx-build -M latexpdf docs/source/dobrodruzstvi/duha_ve_meste/ docs/build/

sphinx-build -M html docs/source/ docs/build/
