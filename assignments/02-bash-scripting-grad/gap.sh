#!/usr/bin/env bash

set -u

REGEX=${1:-*}
DIR=$PWD/../../data/gapminder
FILES_LIST=$(mktemp)

find "$DIR" -type f -iregex ".*/$REGEX[^/]*$" | sort > "$FILES_LIST"

NUM_LINES=$(wc -l "$FILES_LIST" | awk '{print $1}')

if [[ $NUM_LINES -lt 1 ]]; then
	    echo "There are no countries starting with \"$REGEX\""
    fi

i=0
while read -r FILENAME; do 
    BASENAME=$(basename "$FILENAME")
    let i++
    printf "%3d %s\n" $i "$BASENAME"
done < "$FILES_LIST"

rm "$FILES_LIST"
