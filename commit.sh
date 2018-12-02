#!/bin/bash
COMMIT_MESSAGE="\"$1\""

git add .
git reset -- btre/settings.py
git commit -m "Add inquiry contacts"
git push