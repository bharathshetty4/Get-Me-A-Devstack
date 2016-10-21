import os
import sys

def create_stack_user():
	os.system("sudo groupadd stack")
	os.system("useradd -g stack -s /bin/bash -d /opt/stack -m stack")



def clone_devstack():
	if(os.path.exists("/opt/stack/devstack/clean.sh")):
		#the devstack folder is already exists
		os.system('su - stack -c "cd ~/devstack; ./clean.sh"')
		os.system('su - stack -c "cd ~;sudo rm -rf devstack"')
	os.system('su - stack -c "cd ~; git clone https://github.com/openstack-dev/devstack.git;"')

def copy_local_conf():
	file_name = "local.conf"
	if(sys.argv[2]=='ironic'):
		file_name = "ironic_local.conf"
	print (file_name)
        cp_command = 'sudo cat '+file_name+' > /opt/stack/devstack/local.conf'
	print cp_command
	os.system('su - stack -c "touch /opt/stack/devstack/local.conf"')
	os.system(cp_command)


def run_stack():
	os.system('su - stack -c "cd ~/devstack; ./stack.sh"')




## code to call the method, passed by a argument as a string
method_name = sys.argv[1]
possibles = globals().copy()
possibles.update(locals())
method = possibles.get(method_name)
if not method:
     raise NotImplementedError("Method %s not implemented" % method_name)
method()
