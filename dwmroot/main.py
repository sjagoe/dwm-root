from __future__ import print_function, unicode_literals

from datetime import datetime
import subprocess
import time

from .battery import get_battery_percentage


def main():
    while True:
        battery = get_battery_percentage()
        now = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        dwm_root = '{0} | {1}'.format(battery, now)
        subprocess.call(['xsetroot', '-name', dwm_root])
        time.sleep(1)
