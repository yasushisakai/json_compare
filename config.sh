#!/usr/bin/env bash

git config filter.consistent.clean ./json-std_conv.py
git config filter.consistent.smudge cat
