UNDER CONSTRUCTION

Prerequisites:

Install both Docker and docker-compose. Start up Docker. Build the Docker image by running "docker-compose build" in the top-level directory (where docker-compose.yml is located).

Also, make sure that you have an X server running on your machine (e.g., VcXsrv or Xming). This is necessary because Blackbox will open two xterm windows: one for the Ryu controller and one for the Mininet CLI.

Visual Studio Code is necessary for debugging.

To run Blackbox:

Simply run "docker-compose up". This will start the Ryu SDN controller and the Mininet CLI.

If you would like to debug the Ryu controller, you'll need to add the -d option to the startblackbox command in docker-compose.yml. Then run "docker-compose up" to start. Once Blackbox is started, open up the project in Visual Studio Code. The "Python: Remote Debug" configuration is set up to debug the Ryu controller. Run this configuration and see that the debugger attaches, which will be confirmed visually in the Visual Studio Code UI. To see if everything works, try setting a breakpoint in the packet-in handler of your Ryu application (e.g., simple_switch_13.py).

Upcoming enhancements:

Allow for customizing which Ryu application is run without having to modify the startblackbox script.

Notes:

If modifying the startblackbox script on windows, note that it needs to be saved with LF line endings. Otherwise, you'll end up with an error while running the script: "standard_init_linux.go:190: exec user process caused 'no such file or directory'".
