#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module adds a key, deletes a key, and inserts a new key in lieu of delete"""


import data


CORRECTED = data.BANDS.copy()

CORRECTED['Dylan'] = {'Bob Dylan': ['vocals', 'guitar', 'harmonica']}

del CORRECTED['Van Halen']['David Lee Roth']

CORRECTED['Van Halen']['Sammy Haggar'] = ['vocals']
