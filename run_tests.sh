#!/bin/bash

echo "
# This is general configuration for the tests.
# Use it in case you need to setup stage specific configs.
site_url = \"\"
" > source/configuration.py
mydir=$(dirname "$0")
cd $mydir
pytest bootstrap_tests.py --junitxml=$5
rm source/configuration.py
