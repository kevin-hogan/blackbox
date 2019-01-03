Development notes:

Run "docker-compose run -p 3000:3000 blackbox /bin/bash" to start bash in container

In /src, start Ryu controller with "xterm -e ./ryu-manager --verbose --enable-debugger simple_switch_13.py &"

Run "service openvswitch-switch start" to start switch service

Then, running "mn --topo single,3 --mac --controller remote --switch ovsk" will start mininet.

For XWindows apps to work, you need to have an xserver application (e.g., Xming) running on your host