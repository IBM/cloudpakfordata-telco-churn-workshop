#!/bin/bash

set -o xtrace

echo `pwd`
pip install -r ./deploy/requirements.txt
git clone git@gitlab.com:ibm/skills-network/courses/IBMDeveloperSkillsNetwork-DS0201EN-SkillsNetwork.git ./deploy/skillsnetwork_repo
python ./deploy/pull-from-gitbook.py 
cd ./deploy/skillsnetwork_repo && git diff 
cd ./deploy/skillsnetwork_repo && git add .
cd ./deploy/skillsnetwork_repo && git status