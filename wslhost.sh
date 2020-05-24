#!/usr/bin/env bash
set -euf -o pipefail

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

function read_args () {
    while [[ "$#" -gt 0 ]]; do
        case "${1}" in
        --hp)
        hp="${2}"
        shift;;
        *)
      printf "***********************************************************\n"
      printf "* Error: Invalid argument: '%s', run --help               *\n""${1}"
      printf "***********************************************************\n"
      exit 1
      ;;
    esac
    shift
  done

}

function call_python () {
    python ${DIR}/source/wslhost.py --hp "${hp}"
}

read_args "${@}"
call_python