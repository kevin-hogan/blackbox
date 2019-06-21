from snortunsock import snort_listener
import requests

SOCKET_PATH = "/var/log/snort/snort_alert"
POLICY_IP = "10.0.0.2"

if __name__ == "__main__":
    for msg in snort_listener.start_recv(SOCKET_PATH):
        print('alertmsg: %s' % ''.join(msg.alertmsg[0].decode("utf-8").replace("\x00", "")))
        requests.get(url = "http://" + POLICY_IP + ":8080/ids_alert")
