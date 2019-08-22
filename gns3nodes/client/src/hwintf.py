import re
import sys
import argparse

from mininet.cli import CLI
from mininet.log import setLogLevel, info, error
from mininet.net import Mininet
from mininet.link import Intf
from mininet.topolib import TreeTopo
from mininet.util import quietRun
from mininet.node import OVSController

def checkIntf(intf):
    config = quietRun('ifconfig %s' % intf, shell=True)
    if not config:
        error('Error:', intf, 'does not exist!\n')
        exit(1)
    ips = re.findall(r'\d+\.\d+\.\d+\.\d+', config)
    if ips:
        error('Error:', intf, 'has an IP address,'
              'and is probably in use!\n')
        exit(1)


if __name__ == '__main__':
    setLogLevel('info')
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--interface', help='Network interface to connect with', required=True)
    parser.add_argument('-d','--depth', help='Depth of tree topology', type=int, required=True)
    parser.add_argument('-f','--fanout', help='Fanout of tree topology', type=int, required=True)
    args = parser.parse_args()

    intfName = args.interface
    info('*** Connecting to hw intf: %s' % intfName + '\n')

    info('*** Checking', intfName, '\n')
    checkIntf(intfName)

    subnet = "192.168.0."
    num_hosts = args.fanout ** args.depth
    net = Mininet(topo=TreeTopo(depth=args.depth, fanout=args.fanout), controller=OVSController)
    for host_index in range(num_hosts):
        rightmost_bits = host_index % 256 + 5
        net.hosts[host_index].setIP(subnet + str(rightmost_bits))

    switch = net.switches[0]
    info('*** Adding hardware interface', intfName, 'to switch', switch.name, '\n')
    _intf = Intf(intfName, node=switch)

    net.start()
    CLI(net)
    net.stop()
