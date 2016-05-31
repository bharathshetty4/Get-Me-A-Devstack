#!/bin/bash
set -eux

# Give passwordless sudo privileges to all users
echo "ALL      ALL = (ALL) NOPASSWD: ALL"\
> /etc/sudoers

#Creating a stack user 
sudo python create-stack-user.py
sudo su stack
cd ~/
