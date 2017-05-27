# coding = utf-8
import unittest
import requests
import json
import xlrd

session = requests.session()
#前置条件--登录并进入商家后台
loginURl = 'http://192.168.4.15:8001/1.5.0/api/0.2/account/signin/pwd'
loginData = {'username': '13333333333', 'pwd': '666666'}
login = session.post(loginURl, data=loginData)

#进入商家后台
detailURL = 'http://192.168.4.15:8005/api/0.2/cms/supplier/detail'
detail = session.post(detailURL)

# json解析出brandContainerId
j1 = detail.json()
dic1_json = json.dumps(j1, sort_keys=True, indent=10, ensure_ascii=False)
dic2 = json .loads(dic1_json)
brandId = dic2["r"]["supplier"]["brandIds"][2]    #取出brandId第二个

onSaleItemsURL = 'http://192.168.4.15:8005/api/0.2/cms/supplier/onSaleItems'
onSaleItemsData = {'brandContainerId': brandId, 'p': '1', 'l': '51'}
onSaleItems = session.post(onSaleItemsURL, data=onSaleItemsData)

notOnSaleItemsURL = 'http://192.168.4.15:8005/api/0.2/cms/supplier/notOnSaleItems'
notOnSaleItemsData = {'brandContainerId': brandId, 'p': '1', 'l': '51'}
notOnSaleItems = session.post(notOnSaleItemsURL, data=notOnSaleItemsData)

# 读取Excel中的linkUrl
wb = xlrd.open_workbook("E:\Read.xlsx")
table = wb.sheet_by_index(0)  # 第一个表
nrows = table.nrows
ncols = table.ncols
colnameindex = 0
colnames = table.row_values(colnameindex)
list = []
for rownum in range(1, nrows):
    row = table.row_values(rownum)
    if row:
        app = {}
        for i in range(len(colnames)):
            app[colnames[i]] = row[i]
            list.append(app)
# json解析出itemId
# j = notOnSaleItems.json()
j = onSaleItems.json()
dic_json = json.dumps(j, sort_keys=True, indent=100, ensure_ascii=False)
dic = json.loads(dic_json)
dic1 = dic["r"]
list1 = dic1["list"]                                                                                       # 取出itemId

listlen = len(list)
j = 0
x = 0
for x in range(len(list1)):
    linkUrl = list[x]["linkUrl"]
    price = int(list[x]["price"]*100)                                         #Excel读取的price为text类型，需要转化为int
    # itemId = list1[x]["id"]
    itemId = list1[x]["saleInfo"]["itemId"]
    print(price)
    shelveURL = 'http://192.168.4.15:8005/api/0.2/cms/supplier/shelve'
    shelveData = {'itemId': itemId, 'brandContainerId': brandId, 'price': price, 'linkUrl': linkUrl}
    shelve = session.post(shelveURL, shelveData)
    j2 = shelve.json()
    dic7_json = json.dumps(j2, sort_keys=True, indent=4, ensure_ascii=False)
    dic8 = json.loads(dic7_json)["m"]
    print(shelve.text)

# linkUrl = dic3["saleInfo"]["linkUrl"]



