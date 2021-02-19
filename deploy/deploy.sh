#!/bin/bash

set -o xtrace

echo `pwd`
pip install -r ./deploy/requirements.txt
git clone git@gitlab.com:ibm/skills-network/courses/IBMDeveloperSkillsNetwork-DS0201EN-SkillsNetwork.git ./deploy/skillsnetwork_repo
python ./deploy/pull-from-gitbook.py 

cd ./deploy/skillsnetwork_repo
git add .
git status
git commit -m "sync from commit [$TRAVIS_COMMIT]: $TRAVIS_COMMIT_MESSAGE"
git push