#!/usr/bin/env bash

set -u

if [[ $# -eq 0 ]]; then
    echo "Usage: head.sh FILE [NUM_LINES]"
	exit 1
fi

INPUT_FILE=$1
NUM_ITERATIONS=${2:-3}

if [[ ! -f "$INPUT_FILE" ]]; then
    echo "$INPUT_FILE is not a file"
	exit 2
fi

i=0
while read -r LINE; do
	echo $LINE
	i=$((i+1))
	if [[ $i -eq "$NUM_ITERATIONS" ]]; then
		break
	fi
done < "$INPUT_FILE"
