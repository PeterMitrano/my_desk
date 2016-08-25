#!/bin/bash
find . -name "*.py" -exec yapf -i '{}' +
find . -name "*.py" -exec pylint -E '{}' +
