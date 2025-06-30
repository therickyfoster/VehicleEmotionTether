#!/bin/bash
echo "Auto-syncing and pushing to GitHub..."

# Configure Git (optional)
git config --global core.autocrlf input
git config --global user.name "RickyFoster"
git config --global user.email "your-email@example.com"

# Navigate to project root
cd "$(dirname "$0")"

# Initialize Git if not already
if [ ! -d .git ]; then
    git init
fi

# Add, commit, and push
git add .
git commit -m "Auto-synced project"
git branch -M main
git remote add origin https://github.com/TheRickyFoster/ProjectMaster33.git 2>/dev/null
git pull --rebase origin main || true
git push -u origin main
