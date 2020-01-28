#!/usr/bin/env bash
set -euf -o pipefail

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

function call_python () {
    python ${DIR}/source/wslhost.py
}

call_python