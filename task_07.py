#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""dictionary iteration using the iteritems() method."""


DATA = {
    2: 7493945,
    76: 4654320,
    3: 4091979,
    90: 1824881,
    82: 714422,
    45: 1137701,
    10: 374362,
    0: 326226,
    -15: 417203,
    -56: 333525,
    67: 323451,
    99: 321696,
    21: 336753,
    -100: 361237,
    55: 1209714,
    5150: 1771800,
    42: 4714011,
    888: 14817667,
    3500: 13760234,
    712: 10903322,
    7: 10443792,
    842: 11716264,
    18584: 10559923,
    666: 9275602,
    70: 11901200,
    153: 12074784,
    8: 4337229
}


def iter_dict_funky_sum(dictionary):
    """
    This function takes dictionary and adds items to total

    Args:
        dictionary (int): the number of data

    Returns:
        int: of the total

    Examples:

        >>> iter_dict_funky_sum(task_07.DATA)
        140166242
    """
    total = 0
    for key, value in dictionary.iteritems():
        total += value - key
    return total
