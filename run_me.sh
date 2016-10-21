#!/bin/bash
set -eux

#append the below line to give nopasswd privileges for all users
cat <<EOT >> /etc/sudoers
ALL      ALL = (ALL) NOPASSWD: ALL
EOT

#Creating a stack user.
sudo python python-scripts.py create_stack_user

#clone the devstack repo from the github
sudo python python-scripts.py clone_devstack


if [ $# -eq 0 ]
then
export project="cinder"
else
project=$1
fi

#copy the appropriate loacl.conf file
sudo python python-scripts.py copy_local_conf $project

#run stack.sh file
sudo python python-scripts.py run_stack
