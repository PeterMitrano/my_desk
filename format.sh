#!/bin/bash
yapf -i lambda_function.py
pylint -E lambda_function.py
