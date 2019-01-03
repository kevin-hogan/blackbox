Development notes:

Run "docker-compose run -p 3000:3000 blackbox /bin/bash" to start bash in container

Start Ryu controller with "xterm -e python -m ptvsd --host 0.0.0.0 --port 3000 ./usr/local/bin/ryu-manager --verbose --enable-debugger src/simple_switch_13.py &". Then start debugging in Visual Studio Code with the Python: Remote Debug configuration. Optionally add --wait just after the port number if you want to start the debug from the beginning of executing the program.

Run "service openvswitch-switch start" to start switch service

Then, running "mn --topo single,3 --mac --controller remote --switch ovsk" will start mininet.

For XWindows apps to work, you need to have an xserver application (e.g., Xming) running on your host