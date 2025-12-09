#!/bin/bash

set -eu
###set -x

# In fors go over lines, not words
export IFS=$'\n'

for what in "Skill" "Spell"; do
    # Cleanup
    echo "Deleting previous ${what} build artefacts"
    mkdir -p build/${what}/cards/
    rm -f build/${what}/cards/*.svg
    mkdir -p build/${what}/rows/
    rm -f build/${what}/rows/row-*.svg
    mkdir -p build/${what}/pages/
    rm -f build/${what}/pages/page-*.svg
    mkdir -p build/${what}/pdfs/
    rm -f build/${what}/pdfs/page-*.pdf
    rm -f build/${what}.pdf

    # Generate source cards
    echo "Generate source cards for ${what}"
    tools/doit.py format --model "${what}" --template tools/templates/$( echo "${what}" | tr '[:upper:]' '[:lower:]' ).svg --output-dir build/${what}/cards/

    # Generate rows of 3 cards
    counter=1
    f1=""
    f2=""
    f3=""
    for f in $( ls build/${what}/cards/*.svg | sort ); do
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
        svg_stack/svg_stack.py --direction=h --margin=100 "$f1" "$f2" "$f3" > build/${what}/rows/row-$counter.svg
        f1=""
        f2=""
        f3=""
        (( counter += 1 ))
    done

    # Finish last incomplete row
    if [[ -n $f1 ]]; then
        if [[ -n $f2 ]]; then
            echo "Creating (partial) row $counter from: $f1, $f2"
            svg_stack/svg_stack.py --direction=h --margin=100 "$f1" "$f2" > build/${what}/rows/row-$counter.svg
        else
            echo "Creating (partial) row $counter from: $f1"
            svg_stack/svg_stack.py --direction=h --margin=100 "$f1" > build/${what}/rows/row-$counter.svg
        fi
    fi

    # Generate pages of 3 cards
    counter=1
    f1=""
    f2=""
    f3=""
    for f in $( ls build/${what}/rows/row-*.svg | sort ); do
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
        svg_stack/svg_stack.py --direction=v --margin=100 "$f1" "$f2" "$f3" > build/${what}/pages/page-$counter.svg
        f1=""
        f2=""
        f3=""
        (( counter += 1 ))
    done

    # Finish last incomplete page
    if [[ -n $f1 ]]; then
        if [[ -n $f2 ]]; then
            echo "Creating (partial) page $counter from: $f1, $f2"
            svg_stack/svg_stack.py --direction=v --margin=100 "$f1" "$f2" > build/${what}/pages/page-$counter.svg
        else
            echo "Creating (partial) page $counter from: $f1"
            svg_stack/svg_stack.py --direction=v --margin=100 "$f1" > build/${what}/pages/page-$counter.svg
        fi
    fi

    # Convert pages to PDF
    for f in $( ls build/${what}/pages/page-*.svg | sort ); do
        echo "Converting page $f to PDF"
        ff="$( basename $f .svg )"
        inkscape --export-filename="build/${what}/pdfs/$ff.pdf" --export-overwrite "$f" 2>&1 | grep -v -e '^$' -e 'Unknown LPE type specified, LPE stack effectively disabled' || true
    done

    # Merge pages to one document
    echo "Merging pages to one document"
    pdfunite build/${what}/pdfs/page-*.pdf build/${what}.pdf
done
