import os
os.system("sudo groupadd stack")
os.system("useradd -g stack -s /bin/bash -d /opt/stack -m stack")
