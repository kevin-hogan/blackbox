import requests
from string import Template

class FirewallSourceOfAlert:
    CONTROLLER_IP = "10.0.0.3"
    CONTROLLER_FIREWALL_URI = Template("http://" + CONTROLLER_IP + ":8080/firewall/block/$block_ip")

    def __init__(self):
        pass
    
    def trigger(self, srcIP):
        requests.get(url = self.CONTROLLER_FIREWALL_URI.substitute(block_ip=srcIP))
