# -*- coding:utf-8 -*-
import yaml
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
def getYam(home_yaml):
    try:
        with open(home_yaml, encoding='utf-8') as f:
            x = yaml.load(f)
            return x
    except FileNotFoundError:
        print(u"找不到文件")