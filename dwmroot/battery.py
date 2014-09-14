from __future__ import print_function, unicode_literals

import re

CAPACITY = re.compile(r'^last full capacity: +(\d+)')
REMAINING = re.compile(r'^remaining capacity: +(\d+)')


def _get_battery_capacity(filename, regexp):
    with open(filename) as fh:
        for line in fh:
            match = regexp.match(line)
            if match:
                return float(match.group(1))


def get_total_capacity():
    return _get_battery_capacity('/proc/acpi/battery/BAT0/info', CAPACITY)


def get_remaining_capacity():
    return _get_battery_capacity('/proc/acpi/battery/BAT0/state', REMAINING)


def get_battery_percentage():
    total = get_total_capacity()
    remaining = get_remaining_capacity()
    percentage = (remaining / total) * 100
    return '{0:.2f}'.format(percentage)
