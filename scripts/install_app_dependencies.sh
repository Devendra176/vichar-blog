#!/bin/bash
sudo pip3 install virtualenv
cd /home/ubuntu/project/
virtualenv env
source env/bin/activate
pip install -r requirements.txt
