#!/bin/bash
COMMIT_MESSAGE="\"$1\""

git add .
git commit -m "Add messages(alerts) to registration and login"
git push