# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 19:37:45 2020

@author: liuyuntao
"""

import requests
from lxml import etree
import csv
import re


headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cookie": "wuid=668662581679504; wuid_createAt=2020-04-29 14:52:00; Hm_lvt_15fafbae2b9b11d280c79eff3b840e45=1588143121; captcha=s%3A6006d2fdde67fc3d0f6e1f1029c52f40.51FjGWxklo3l8WcSjlRECHEPVMsxhqlYdkx7xeBq0Nk; Hm_lpvt_15fafbae2b9b11d280c79eff3b840e45=1588160016",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}


data = csv.reader(open('C:\\Users\\liuyuntao\\Desktop\\data_source\\yidianzixun.csv'))

with open(r"C:\Users\liuyuntao\Desktop\result\yidianzixun.csv", "w+", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Url", "阅读量", "评论量"])
    for i in data:
        try:
            res = requests.get(i[0], headers=headers)
            comment = re.findall('"comment_count":(\d+)', res.text)
            comment_num = sum([int(i) for i in comment])
            print(i[0], comment_num)
            writer.writerow([i[0], "", comment_num])
        except:
            print(i[0], "失效", "失效")
            writer.writerow([i[0], "失效", "失效"])

