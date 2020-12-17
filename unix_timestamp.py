#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Converting date into a Unix timestamp """

import datetime
print('Insert year:')
year = int(input())
print('Insert month:')
month = int(input())
print('Insert day:')
day = int(input())
unixtimestamp = datetime.datetime(year,month,day).timestamp()
print(unixtimestamp)
