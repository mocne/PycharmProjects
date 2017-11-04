# -*- coding: utf-8 -*-
import datetime
import time
import requests
import json
import pymysql

taaaa = int(time.mktime(datetime.datetime.now().timetuple()) * 1000)

urls = "https://a.cnaidai.com/webjr/invest/investListPlan.cgi?currentPage=1&pageSize=100&timeLimitType=null&aprType=null&_=" + str(
    taaaa)

session = requests.session()
d1 = session.get(urls)
d2 = d1.content
d3 = json.loads(d2)
for i in range(0, 99):
    totle = d3["list"][i]["account"]
    alreday = d3["list"][i]["alreadyInvestTotal"]
    if d3["list"][i]["id"] == 19:
        print(d3["list"][i])