UNDER CONSTRUCTION!

## Setup

Install both Docker and docker-compose. Start up Docker. Build the Docker image by running `docker-compose build` in the top-level directory (where docker-compose.yml is located).

Also, make sure that you have an X server running on your machine (e.g., VcXsrv or Xming). This is necessary because Blackbox will open two xterm windows: one for the Ryu controller and one for the Mininet CLI.

Visual Studio Code is necessary for debugging.

## Running Blackbox

Simply run `docker-compose up`. This will start the Ryu SDN controller, the Mininet CLI, and a bash window for convenience.

If you would like to debug the Ryu controller, you'll need to add the `-d` option to the `startblackbox` command in `docker-compose.yml`. Then run `docker-compose up` to start. Once Blackbox is started, open up the project in Visual Studio Code. The `Python: Remote Debug` configuration is set up to debug the Ryu controller. Run this configuration and see that the debugger attaches, which will be confirmed visually in the Visual Studio Code UI. To see if everything works, try setting a breakpoint in the packet-in handler of your Ryu application (e.g., `simple_switch_snort.py`).

## Network topology

The network topology is configured through the Mininet Python API in `start_mininet.py`. Currently, it creates one webserver host (`h1`), one regular host (`h2`), and one Snort IDS host (`snort`). See below for details on Snort.

## Snort integration

This tool is currently configured to work with Snort IDS. For testing purposes, I've created a very simple rule in the `snort/blackbox.rules` file that will throw an alert on detecting any packet with "POST" in it.

To see this in action, start up Blackbox, then type `h2 wget --post-data "qwerty" h1` in the Mininet CLI. You'll then see the "Under Attack!" alert message appear in the Ryu console as well as a printout of the packet that triggered the alert.

## Upcoming enhancements

Allow for customizing which Ryu application is run without having to modify the `startblackbox` script.

Respond to alerts with more interesting behavior, like blocking traffic from the IP that triggered the alert.

## Notes

If modifying the `startblackbox` script on windows, note that it needs to be saved with LF line endings. Otherwise, you'll end up with an error while running the script: `standard_init_linux.go:190: exec user process caused 'no such file or directory'`.
