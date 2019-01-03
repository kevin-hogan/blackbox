Development notes:

Run "docker-compose run blackbox /bin/bash" to start bash in container

Run "service openvswitch-switch start" to start switch service

Then, running "mn --topo single,3 --mac --controller remote --switch ovsk" will start mininet.

For XWindows apps to work, you need to have an xserver application (e.g., Xming) running on your host