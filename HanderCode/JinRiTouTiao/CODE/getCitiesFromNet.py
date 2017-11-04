# -*- coding: utf-8 -*-
__author__ = 'pkf'

import requests

def getDataWithUrl(Url, Params):
    reqData = requests.get(url=Url, params=Params)