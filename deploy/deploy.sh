#!/bin/bash

set -o xtrace


pip install -r ./requirements.txt
git clone git@gitlab.com:ibm/skills-network/courses/IBMDeveloperSkillsNetwork-DS0201EN-SkillsNetwork.git ./skillsnetwork_repo
python ./pull-from-gitbook.py 
git diff -r 
git add .
git status