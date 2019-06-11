from snortunsock import snort_listener

SOCKET_PATH = "/var/log/snort/snort_alert"

if __name__ == "__main__":
    for msg in snort_listener.start_recv(SOCKET_PATH):
        print('alertmsg: %s' % ''.join(msg.alertmsg[0].decode("utf-8").replace("\x00", "")))
