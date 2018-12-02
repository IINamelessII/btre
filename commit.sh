#!/bin/bash
COMMIT_MESSAGE="\"$1\""

git add .
git commit -m "Add logout, dashboard and page's title"
git push