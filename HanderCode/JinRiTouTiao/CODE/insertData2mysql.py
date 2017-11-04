# -*- coding: utf-8 -*-
__author__ = 'pkf'

import pymysql

dataDic= {}

try:
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='mocne', passwd='000000', db='jinritoutiao', charset='utf8')
except Exception as e:
    print(e)
else:
    cursor = conn.cursor()

    # 执行SQL，并返回收影响行数
    effect_row = cursor.executemany("insert into cities_info(city_name, city_code, belong_to, add_time)values(%s, %s, %s, %s)", ("u1", "u1pass", "11111"))

    conn.commit()

    cursor.close()
    conn.close()
