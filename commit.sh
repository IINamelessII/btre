#!/bin/bash
COMMIT_MESSAGE="\"$1\""

git add .
git commit -m "Add registration and login"
git push