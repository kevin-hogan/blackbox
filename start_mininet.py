#!/usr/bin/python                                                                            
                                                                                             
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import RemoteController
from mininet.cli import CLI

class SingleSwitchTopo(Topo):
    def build(self, n=2):
        switch = self.addSwitch('s1')
        for h in range(n):
            host = self.addHost('h%s' % (h + 1))
            self.addLink(host, switch)

def createNetwork():
    topo = SingleSwitchTopo(n=3)
    net = Mininet(topo=topo, controller=None)
    controller =net.addController('c0', controller=RemoteController, ip="127.0.0.1", port=6633)
    controller.start()
    net.start()
    return net

def testConnection(net):
    print("Dumping host connections")
    dumpNodeConnections(net.hosts)
    print("Testing network connectivity")
    net.pingAll()

if __name__ == '__main__':
    setLogLevel('info')
    net = createNetwork()
    testConnection(net)
    CLI(net)
    net.stop()