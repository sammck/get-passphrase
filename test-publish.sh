#!/bin/bash

set -e

poetry config repositories.test-pypi https://test.pypi.org/legacy/
poetry publish -r test-pypi -u __token__ -p "$(cat ~/.private/test.pypi.upload-token.txt)" || exit $?

