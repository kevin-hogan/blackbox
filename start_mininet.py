#!/usr/bin/python                                                                            
                                                                                             
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.link import TCLink

SNORT_HOST_NAME = "snort"
WEBSERVER_HOST_NAME = "webserver"

class SingleSwitchTopo(Topo):
    def build(self, numClients):
        switch = self.addSwitch('s1')
        link_opts = dict(cls=TCLink, bw=100, delay='5ms', max_queue_size=1000, use_htb=True)
        for num in range(numClients):
            host = self.addHost('client%s' % (num + 1))
            self.addLink(host, switch, **link_opts)
        snort = self.addHost(SNORT_HOST_NAME, inNamespace=False)
        self.addLink(snort, switch, **link_opts)
        webserver = self.addHost(WEBSERVER_HOST_NAME, inNamespace=False)
        self.addLink(webserver, switch, **link_opts)

def createNetwork():
    topo = SingleSwitchTopo(1)
    net = Mininet(topo=topo, controller=None)
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
    # The -q option, which silences output, is important below. Sending the command to the node
    # this way fails when it has output.
    net.get(SNORT_HOST_NAME).cmd("snort -q -i snort-eth0 -c /etc/snort/snort.conf -A unsock &")
    net.get(WEBSERVER_HOST_NAME).cmd("socat TCP4-LISTEN:80,fork TCP4:webserver:8080 &")
    CLI(net)
    net.stop()