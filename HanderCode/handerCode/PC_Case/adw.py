# -*- coding: utf-8 -*-

import common.xlsx2json
import common.doSomethingWithElement
import time

def setUp(self):
    self.test_getData()

    # global browser
    # browser = initSeleniumWithInfo('Chrom')

def test_getData():
    data = common.xlsx2json.Excel2Json(file_path='../testData.xlsx', sheetName='爱贷网-PC')
    # with open('./爱贷网-PC.json', 'r') as json_file:
    #     data = json.load(json_file)
    #     json_file.close()
    return data

def test_register(asd):
    registerData = asd['datas']['注册']
    for i in range(1, len(asd['datas']['注册'].keys()) + 1):
        testStr = '注册' + str(i)
        print(registerData[testStr])

def tearDown():
    pass

def printMe(words):
    # fileData = open('../Logs/' + str(time.strftime('%Y%m%d')) + '.txt', 'a+')
    # print(fileData, '【%s】【info】：%s' % (str(time.strftime('%Y_%m_%d %H:%M:%S')), words))
    # fileData.close()
    print(words)

    with open('../Logs/' + str(time.strftime('%Y%m%d')) + '.txt', 'w') as json_file:
        json_file.write('【%s】【info】：%s' % (str(time.strftime('%Y_%m_%d %H:%M:%S')), words))
        json_file.close()

def justDo(driver, parms):
    common.doSomethingWithElement.doWithParm(driver=driver, beheaver=parms['脚本操作'], parm=parms['脚本数据'], behaver1=parms['备用脚本操作'], parm1=parms['备用脚本数据'])

if __name__ == '__main__':

    datas = test_getData()
    test_register(datas)