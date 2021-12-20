#!/bin/bash
export FLASK_APP=./src/hello.py
source $(pipenv --venv)/bin/activate
flask run -h 127.0.0.1:5000