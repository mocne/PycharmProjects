# -*- coding: utf-8 -*-

import xlrd
import json
import codecs
import os

def Excel2Json(file_path, sheetName):

    if get_data(file_path) is not None:
        book = get_data(file_path)
        sheet = book.sheet_by_name(sheetName)
        row_0 = sheet.row(0)  # 第一行是表单标题
        nrows = sheet.nrows
        ncols = sheet.ncols

        dicts = []
        dic = {}
        tmp = {}
        tmpStr = ''
        cols = sheet.row_values(0)
        result = {'title': sheetName, 'cols': cols, 'datas': {}}
        for i in range(1, nrows):
            # 行转字典
            for j in range(0, ncols):
                title_de = str(row_0[j])
                title_cn = title_de.split('\'')[1]
                tmp[title_cn] = sheet.row_values(i)[j]
            if i > 1:
                if tmp['模块'] == tmpStr:
                    dic[str(tmp['模块']) + str(int(tmp['次级编号']))] = tmp
                    dicts[str(sheet.row_values(i)[1])] = dic
                    tmpStr = str(tmp['模块'])
                    print('asd')
                else:
                    tmp.clear()
            elif i is 1:
                dic[str(tmp['模块']) + str(int(tmp['次级编号']))] = tmp
                dicts[int(tmp['次级编号'])] = dic
                tmpStr = str(tmp['模块'])
        result['datas'] = dicts
        json_data_temp = json.dumps(result, indent=4, sort_keys=True)
        saveFile(os.getcwd(), sheetName, json_data_temp)
        return json.loads(json_data_temp)
    else:
        result = {'title': sheetName, 'cols': 'NULL', 'children': 'NULL', 'myData': 'NULL'}
        return result

def get_data(file_path):
    try:
        data = xlrd.open_workbook(file_path)
        return data
    except Exception as e:
        print(u'excel表格读取失败：%s' % e)
        return None

def saveFile(file_path, file_name, data):
    output = codecs.open(file_path + '/' + file_name + '.json', 'w', 'utf-8')
    output.write(data)
    output.close()

if __name__ == '__main__':
    datas = Excel2Json('../testData.xlsx', '爱贷网-PC')
