# -*- coding: utf-8 -*-
__author__ = 'aidai_TEC_QA'
# -*- date:'2017/8/2 0002' -*-

import BaseMonitor

appPackage = ''
signType = ''

def getDeviceRunningInfo(appsPackage, signsType):
    print(appsPackage, signsType)
    datas = []
    cpu = BaseMonitor.get_cpu(appsPackage)
    men = BaseMonitor.get_men(appsPackage)
    flow = BaseMonitor.get_flow(appsPackage, signsType)
    batry = BaseMonitor.get_battery()
    fps = BaseMonitor.get_fps(appsPackage)
    pid = BaseMonitor.get_pid(appsPackage)

    datas.insert(0, cpu)
    datas.insert(1, men)
    datas.insert(2, flow)
    datas.insert(3, batry)
    datas.insert(4, fps)
    datas.insert(5, pid)

    return datas

def saveDeviceInfo():
    return

if __name__ == '__main__':
    getDeviceRunningInfo(appPackage, signType)
    saveDeviceInfo()
    print('ok')