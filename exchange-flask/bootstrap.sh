#!/bin/sh
export FLASK_APP=./exchange/index.py
pipenv run flask --debug run -h 0.0.0.0 -p 3000