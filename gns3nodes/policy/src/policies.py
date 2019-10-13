import time
import sys
from collections import deque, defaultdict

def to_float_timestamp(seconds, microseconds):
    return float(seconds) + (float(microseconds) / (10 ** 6))

class AlertCounter:
    def __init__(self, alert_message, count_threshold, time_window_s, countermeasure):
        self.alert_message = alert_message
        self.count_threshold = count_threshold
        self.time_window_s = time_window_s
        self.countermeasure = countermeasure
        self.alert_timestamps = defaultdict(deque)

    def is_outside_time_window(self, timestamp):
        return (time.time() - timestamp) > self.time_window_s

    def process_event(self, alert):
        ts_for_source = self.alert_timestamps[alert["src"]]
        while ts_for_source and self.is_outside_time_window(ts_for_source[-1]):
            ts_for_source.pop()

        if alert["msg"] == self.alert_message:
            ts_float = to_float_timestamp(alert["tv_sec"], alert["tv_usec"])
            ts_for_source.appendleft(ts_float)
        
        if len(ts_for_source) > self.count_threshold:
            self.countermeasure.trigger(alert["src"])
            ts_for_source.clear()