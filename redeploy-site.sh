#!/bin/bash

tmux kill-server 2>/dev/null

cd ~/portfolio-zdm

git fetch && git reset origin/main --hard

source python3-virtualenv/bin/activate 2>/dev/null

pip install -r requirements.txt

tmux new-session -d -s flask -c "$(pwd)" "flask run --host=0.0.0.0"