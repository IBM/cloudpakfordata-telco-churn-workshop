#!/bin/bash

pip install -r ./deploy/requirements.txt
git clone git@gitlab.com:ibm/skills-network/courses/IBMDeveloperSkillsNetwork-DS0201EN-SkillsNetwork.git ./deploy/skillsnetwork_repo
python ./deploy/pull-from-gitbook.py 
cd ./deploy/skillsnetwork_repo
git diff -r 
git add .
git status