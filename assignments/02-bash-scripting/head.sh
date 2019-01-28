#!/usr/bin/env bash

set -u

if [[ $# -eq 0 ]]; then
    echo "Usage: head.sh FILE [NUM_LINES]"
	exit 1
fi

if [[ ! -f "$1" ]]; then
    echo "$1 is NOT a file"
	exit 2
fi
