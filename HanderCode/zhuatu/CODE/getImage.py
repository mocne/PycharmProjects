# -*- coding: utf-8 -*-
import json

import requests
import os
from common import readYaml

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
imgUrlArr = []
isDoneArr = []

def save2file():
    with open("../DATA/imgUrls.json", 'r') as load_f:
        urls = json.load(load_f)
        load_f.close()
        for img_url in urls:
            if img_url not in isDoneArr:

                tempStr = str(img_url).split('/')[-1]
                f = open('../IMG/%s' % tempStr, 'ab')
                f.write(requests.get(img_url).content)
                f.close()
                isDoneArr.append(img_url)

                with open("../DATA/isDone.json", 'w') as done_f:
                    tempData = json.load(done_f)
                    if tempStr not in tempData:
                        tempData.append(tempStr)
                    json.dump(isDoneArr, done_f)
                    print("加载入文件( %s )完成..." % tempStr)
                    done_f.close()



def getImgUrlWithUrlAndParams(URL, PARAM):
    req = requests.get(url=URL, params=PARAM).json()
    dataArr = req["items"]
    for item in dataArr:
        imgUrl = item["pic_url"]
        if imgUrl not in imgUrlArr:
            with open("../DATA/imgUrls.json", "w") as f:
                tempData = json.load(f)
                if imgUrl not in tempData:
                    imgUrlArr.append(imgUrl)
                    json.dump(imgUrlArr, f)
                    print("存入文件（%s）完成..." % item["pic_url"])
                    f.close()

def getUrlsAndParams(DATA):
    subData = DATA["search_meizi"]
    return subData["RequestURL"], subData["Params"]

def getDataWithYAML(ymlFile):
    return readYaml.getYam(ymlFile)

if __name__ == "__main__":
    data = getDataWithYAML("E:\\PycharmProjects\\HanderCode\\zhuatu\\YAML\\sougou_meizi.yml")
    url, params = getUrlsAndParams(data)
    getImgUrlWithUrlAndParams(url, params)
    save2file()