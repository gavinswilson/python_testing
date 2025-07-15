#!/bin/bash
echo "Running entrypoint script"

echo "=========================="

git config --global user.name "${GITHUB_ACTOR}"
git config --global user.email "${INPUT_EMAIL}"
git config --global --add safe.directory /github/workspace


python3 /usr/bin/update.py

git add -A && git commit -m "Update readme.md"
git push --set-upstream origin main

echo "=========================="

echo "Script completed successfully"
#permissions for the repo to allow write access for the actions user
