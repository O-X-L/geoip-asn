#!/bin/bash

set -e

cd "$(dirname "$0")/.."

export AW_INIT=1

echo ''
echo 'LINTING Python'
echo ''

pylint --recursive=y .

echo ''
echo 'LINTING YAML'
echo ''

yamllint .

