from snortunsock import snort_listener
import requests
import dpkt
import socket
import json

SOCKET_PATH = "/var/log/snort/snort_alert"
POLICY_IP = "10.0.0.2"

if __name__ == "__main__":
    for msg in snort_listener.start_recv(SOCKET_PATH):
        eth = dpkt.ethernet.Ethernet(msg.pkt)
        src_ip = socket.inet_ntop(socket.AF_INET, eth.data.src)
        dst_ip = socket.inet_ntop(socket.AF_INET, eth.data.dst)
        alert_msg = ''.join(msg.alertmsg[0].decode("utf-8").replace("\x00", ""))
        alert_dict = {"msg": alert_msg, "src": src_ip, "dst": dst_ip}
        requests.post(url = "http://" + POLICY_IP + ":8080/ids_alert", json = alert_dict)
