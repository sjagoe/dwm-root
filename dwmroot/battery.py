from __future__ import print_function, unicode_literals

import re

CAPACITY = re.compile(r'^last full capacity: +(\d+)')
REMAINING = re.compile(r'^remaining capacity: +(\d+)')
CHARGING_STATE = re.compile(r'^charging state: +(\w+)')


def _get_battery_item(filename, regexp):
    with open(filename) as fh:
        for line in fh:
            match = regexp.match(line)
            if match:
                return match.group(1)


def get_total_capacity():
    return float(_get_battery_item('/proc/acpi/battery/BAT0/info', CAPACITY))


def get_remaining_capacity():
    return float(_get_battery_item('/proc/acpi/battery/BAT0/state', REMAINING))


def get_charging_state():
    state = _get_battery_item('/proc/acpi/battery/BAT0/state', CHARGING_STATE)
    if state == 'charging':
        return '+'
    elif state == 'discharging':
        return '-'
    else:
        return ' '


def get_battery_percentage():
    total = get_total_capacity()
    remaining = get_remaining_capacity()
    state = get_charging_state()
    percentage = (remaining / total) * 100
    return '{0:.2f}{1}'.format(percentage, state)
