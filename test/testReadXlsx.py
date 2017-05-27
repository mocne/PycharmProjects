# coding = utf-8

import xlrd

wb = xlrd.open_workbook("E:\Read.xlsx")
table = wb.sheet_by_index(0)       #第一个表
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

listlen = len(list)
j = 0
for j in range(listlen):
    linkUrl = list[j]["linkUrl"]
    print(linkUrl)



