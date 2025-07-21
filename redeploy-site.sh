systemctl stop myportfolio.service 2>/dev/null
cd ~/Sub-Challenges/portfolio-zdm

git fetch && git reset origin/main --hard
source python3-virtualenv/bin/activate 2>/dev/null

pip install -r requirements.txt
systemctl start myportfolio.service