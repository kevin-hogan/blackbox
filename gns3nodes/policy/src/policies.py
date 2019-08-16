import time
from collections import deque, defaultdict

class AlertCounter:
    def __init__(self, alert_message, count_threshold, time_window_s, countermeasure):
        self.alert_message = alert_message
        self.count_threshold = count_threshold
        self.time_window_s = time_window_s
        self.countermeasure = countermeasure
        self.alert_timestamps = defaultdict(deque)

    def process_event(self, alert):
        ts_for_source = self.alert_timestamps[alert["src"]]
        while ts_for_source and (time.time() - ts_for_source[-1]) > self.time_window_s:
            ts_for_source.pop()

        if alert["msg"] == self.alert_message:
            ts_for_source.appendleft(alert["ts"])
        
        if len(ts_for_source) > self.count_threshold:
            self.countermeasure.trigger(alert["src"])
            ts_for_source.clear()