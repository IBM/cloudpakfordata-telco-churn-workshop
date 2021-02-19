#!/bin/bash

set -o xtrace

echo `pwd`
pip install -r ./requirements.txt
git clone git@gitlab.com:ibm/skills-network/courses/IBMDeveloperSkillsNetwork-DS0201EN-SkillsNetwork.git ./skillsnetwork_repo
python ./pull-from-gitbook.py 
cd ./skillsnetwork_repo && diff -r 
cd ./skillsnetwork_repo && add .
cd ./skillsnetwork_repo && status