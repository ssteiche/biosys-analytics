#!/usr/bin/env bash

INPUT_FILE=$1

set -u

if [[ $# -eq 0 ]]; then
    echo "Usage: cat-n.sh FILE"
	exit 1
fi

if [[ ! -f "$1" ]]; then
    echo "$1 is NOT a file"
	exit 2
fi

i=0
while read -r LINE; do
	i=$((i+1))
	printf "%3d: %s\n" $i $LINE
done < $INPUT_FILE
