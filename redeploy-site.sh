#!/bin/bash

# Exit immediately if a command fails
set -e

# Change directory to project folder
cd /root/portfolio-zdm

# Fetch and reset git repository to latest main branch
git fetch && git reset origin/main --hard

# Activate python virtual environment and install dependencies
source python3-virtualenv/bin/activate
pip install -r requirements.txt

# Restart systemd service
sudo systemctl restart myportfolio

# Print status
sudo systemctl status myportfolio --no-pager
