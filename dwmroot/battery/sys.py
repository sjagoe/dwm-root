from __future__ import print_function, unicode_literals, absolute_import

import os

if not os.path.isdir('/sys/class/power_supply/BAT0'):
    raise ImportError('/sys/class/power_supply/BAT0 not found')


def _get_battery_item(filename):
    with open(filename) as fh:
        return fh.read().strip()


def get_total_capacity():
    return float(_get_battery_item('/sys/class/power_supply/BAT0/charge_full'))


def get_remaining_capacity():
    return float(_get_battery_item('/sys/class/power_supply/BAT0/charge_now'))


def get_charging_state():
    state = _get_battery_item('/sys/class/power_supply/BAT0/status')
    if state.lower() == 'charging':
        return '+'
    elif state.lower() == 'discharging':
        return '-'
    else:
        return ' '


def get_battery_percentage():
    total = get_total_capacity()
    remaining = get_remaining_capacity()
    state = get_charging_state()
    percentage = (remaining / total) * 100
    return '{0:.2f}{1}'.format(percentage, state)
