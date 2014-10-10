from __future__ import print_function, unicode_literals

from datetime import datetime
import subprocess
import time

from .battery import get_battery_percentage
from .twmn import poll_twmn_processes


class DwmRoot(object):

    def __init__(self):
        self.twmnd = poll_twmn_processes(None)

    def main(self):
        while True:
            self.twmnd = poll_twmn_processes(self.twmnd)
            battery = get_battery_percentage()
            now = datetime.now().strftime('%Y/%m/%d %H:%M')
            dwm_root = '{0} | {1}'.format(battery, now)
            subprocess.call(['xsetroot', '-name', dwm_root])
            time.sleep(15)


def main():
    root = DwmRoot()
    root.main()
