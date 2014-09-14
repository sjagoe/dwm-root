from __future__ import print_function, unicode_literals

from datetime import datetime
import time

from .battery import get_battery_percentage


def main():
    while True:
        battery = get_battery_percentage()
        now = datetime.now()
        print(battery, now.strftime('%Y/%m/%d %H:%M:%S'), sep=' | ')
        time.sleep(1)
