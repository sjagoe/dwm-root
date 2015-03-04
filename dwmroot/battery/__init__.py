from __future__ import print_function, unicode_literals, absolute_import

try:
    from .proc import (
        get_total_capacity, get_remaining_capacity, get_charging_state)
except ImportError:
    from .sys import (
        get_total_capacity, get_remaining_capacity, get_charging_state)


def get_battery_percentage():
    total = get_total_capacity()
    remaining = get_remaining_capacity()
    state = get_charging_state()
    percentage = (remaining / total) * 100
    return '{0:.2f}{1}'.format(percentage, state)
