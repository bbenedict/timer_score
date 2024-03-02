#!/bin/bash

poetry run pytest -rAs --cov --cov-report=term-missing --cov-report xml --junitxml=report.xml $1
