import datetime
import time


def get_current_timestamp():
    return datetime.datetime.fromtimestamp(time.time()).strftime(
        '%Y-%m-%d %H:%M:%S')