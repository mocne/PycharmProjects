# -*- coding: utf-8 -*-
__author__ = 'pkf'

import time,datetime

print (time.time())
print (time.localtime())


def datetime_to_timestamp_in_milliseconds(d):
    return int(time.mktime(d.timetuple()) * 1000)

asd = datetime_to_timestamp_in_milliseconds(datetime.datetime.now())
print(asd)