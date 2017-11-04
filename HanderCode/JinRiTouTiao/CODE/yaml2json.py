# -*- coding: utf-8 -*-

import json
import yaml
from format_converter import converter

with open("../YAML/cityInfo.yml") as f:
    datas = yaml.load(f)
    jsonData = json.dumps(datas, indent=4, ensure_ascii=False)
    print(jsonData)
    converter.yml(jsonData) > '../YAML/data.yml'
