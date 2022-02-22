#!/bin/bash

set -e

poetry publish -r testpypi -u __token__ -p "$(cat ~/.private/pypi.upload-token.txt)" || exit $?

