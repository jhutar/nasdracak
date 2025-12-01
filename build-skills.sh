#!/bin/bash

set -eu
###set -x

# In fors go over lines, not words
export IFS=$'\n'

# Cleanup
echo "Deleting previous build artefacts"
mkdir -p build/skill-rows/
rm build/skill-rows/row-*.svg
mkdir -p build/skill-rows/
rm build/skill-pages/page-*.svg
mkdir -p build/skill-pdfs/
rm build/skill-pdfs/page-*.pdf
rm build/skills.pdf

# Generate rows of 3 cards
counter=1
f1=""
f2=""
f3=""
for f in $( ls build/skill-cards/*.svg | sort ); do
    if [[ -z $f1 ]]; then
        f1="$f"
        continue
    fi
    if [[ -z $f2 ]]; then
        f2="$f"
        continue
    fi
    if [[ -z $f3 ]]; then
        f3="$f"
    fi

    echo "Creating (complete) row $counter from: $f1, $f2, $f3"
    uv --directory svg_stack/ run svg_stack.py --direction=h --margin=100 "../$f1" "../$f2" "../$f3" > build/skill-rows/row-$counter.svg
    f1=""
    f2=""
    f3=""
    (( counter += 1 ))
done

# Finish last incomplete row
if [[ -n $f1 ]]; then
    if [[ -n $f2 ]]; then
        echo "Creating (partial) row $counter from: $f1, $f2"
        uv --directory svg_stack/ run svg_stack.py --direction=h --margin=100 "../$f1" "../$f2" > build/skill-rows/row-$counter.svg
    else
        echo "Creating (partial) row $counter from: $f1"
        uv --directory svg_stack/ run svg_stack.py --direction=h --margin=100 "../$f1" > build/skill-rows/row-$counter.svg
    fi
fi

# Generate pages of 3 cards
counter=1
f1=""
f2=""
f3=""
for f in $( ls build/skill-rows/row-*.svg | sort ); do
    if [[ -z $f1 ]]; then
        f1="$f"
        continue
    fi
    if [[ -z $f2 ]]; then
        f2="$f"
        continue
    fi
    if [[ -z $f3 ]]; then
        f3="$f"
    fi

    echo "Creating (complete) page $counter from: $f1, $f2, $f3"
    uv --directory svg_stack/ run svg_stack.py --direction=v --margin=100 "../$f1" "../$f2" "../$f3" > build/skill-pages/page-$counter.svg
    f1=""
    f2=""
    f3=""
    (( counter += 1 ))
done

# Finish last incomplete page
if [[ -n $f1 ]]; then
    if [[ -n $f2 ]]; then
        echo "Creating (partial) page $counter from: $f1, $f2"
        uv --directory svg_stack/ run svg_stack.py --direction=v --margin=100 "../$f1" "../$f2" > build/skill-pages/page-$counter.svg
    else
        echo "Creating (partial) page $counter from: $f1"
        uv --directory svg_stack/ run svg_stack.py --direction=v --margin=100 "../$f1" > build/skill-pages/page-$counter.svg
    fi
fi

# Convert pages to PDF
for f in $( ls build/skill-pages/page-*.svg | sort ); do
    echo "Converting page $f to PDF"
    ff="$( basename $f .svg )"
    inkscape --export-filename="build/skill-pdfs/$ff.pdf" --export-overwrite "$f" 2>&1 | grep -v -e '^$' -e 'Unknown LPE type specified, LPE stack effectively disabled' || true
done

# Merge pages to one document
echo "Merging pages to one document"
pdfunite build/skill-pdfs/page-*.pdf build/skills.pdf
