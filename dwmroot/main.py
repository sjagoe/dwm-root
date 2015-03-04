from __future__ import print_function, unicode_literals, absolute_import

from datetime import datetime
import subprocess
import time

from .battery import get_battery_percentage


class DwmRoot(object):

    def main(self):
        while True:
            battery = get_battery_percentage()
            now = datetime.now().strftime('%Y/%m/%d %H:%M')
            dwm_root = '{0} | {1}'.format(battery, now)
            subprocess.call(['xsetroot', '-name', dwm_root])
            time.sleep(15)


def main():
    root = DwmRoot()
    root.main()
