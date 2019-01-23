#!/usr/bin/python                                                                            
                                                                                             
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.link import TCLink

SNORT_HOST_NAME = "snort"

class SingleSwitchTopo(Topo):
    def build(self, n):
        switch = self.addSwitch('s1')
        link_opts = dict(cls=TCLink, bw=100, delay='5ms', max_queue_size=1000, use_htb=True)
        for h in range(n):
            host = self.addHost('h%s' % (h + 1))
            self.addLink(host, switch, **link_opts)

def createNetwork():
    topo = SingleSwitchTopo(2)
    net = Mininet(topo=topo, controller=None)
    net.addNAT(SNORT_HOST_NAME).configDefault()
    controller = net.addController('c0', controller=RemoteController, ip="127.0.0.1", port=6633)
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
    net.get(SNORT_HOST_NAME).cmd("ifconfig snort-eth0 promisc")
    # The -q option is important below. Seending the command to the node
    # this way fails when it has output.
    net.get(SNORT_HOST_NAME).cmd("snort -q -i snort-eth0 -c /etc/snort/snort.conf -A unsock &")
    net.get("h1").cmd("python -m http.server 80 &")
    CLI(net)
    net.stop()