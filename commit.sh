#!/bin/bash
COMMIT_MESSAGE=$1
git add .
git commit -m $COMMIT_MESSAGE=$1
git push