from __future__ import print_function, unicode_literals

from .battery import get_battery_percentage


def main():
    print(get_battery_percentage())
