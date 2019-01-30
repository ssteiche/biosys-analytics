#!/usr/bin/env bash

set -u

if [[ $# -eq 0 ]] || [[ $# -gt 2 ]]; then
    echo "Usage: hello.sh GREETING [NAME]"
	exit 1
fi

GREETING=$1
NAME=${2:-"Human"}

echo "$GREETING", "$NAME"!
