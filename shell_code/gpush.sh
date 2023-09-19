#!/bin/bash

# Function to get the default commit message
get_default_commit_message() {
    local current_date_time=$(date +"%Y-%m-%d %H:%M:%S")
    local changed_folder=$(basename "$(pwd)")
    echo "$current_date_time $changed_folder"
}

# Check if a commit message was provided as a parameter
if [ $# -eq 0 ]; then
    # No commit message provided, use the default
    commit_message=$(get_default_commit_message)
else
    # Commit message provided as a parameter
    commit_message="$*"
fi

# Commit changes with the specified or default commit message
git add .
git commit -m "$commit_message"
git push
