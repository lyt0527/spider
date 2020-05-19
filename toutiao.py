# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 11:44:12 2020

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
        "cache-control": "max-age=0",
        "cookie": "__utma=24953151.968183814.1588131898.1588131898.1588131898.1; __utmc=24953151; __utmz=24953151.1588131898.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); s_v_web_id=verify_k9ksqgq8_fOV3buON_yH98_4dXI_A9Iq_BCyyF5xwXBws; ttcid=d8f39b9791984a30b6c40916d149088d30; SLARDAR_WEB_ID=d249b2d9-9fa7-490d-9c40-0ca9bea4d614; __tasessionId=7v6pn5or11588131912749; csrftoken=7911aea88968ebfba1d34f909a3d3408; tt_webid=6820974594854880776; tt_webid=6820974594854880776; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_scid=LEJY6kAFhW7ZLcYAPPxDMwu8PS0OusPqZ5DO4sO7zsFMjEwLtoe-VYo5PKpDF-15dcf6",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}

data = csv.reader(open('C:\\Users\\liuyuntao\\Desktop\\data_source\\https_toutiao.csv'))

with open(r"C:\Users\liuyuntao\Desktop\result\https_toutiao.csv", "a+", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Url", "阅读量", "评论量"])
    for i in data:
        try:
            url_ = "https://www.toutiao.com/article/v2/tab_comments/?aid=24&group_id=%s" % i[0][-20:-1]
            res = requests.get(url_, headers=headers)
            comment_num = re.findall('"total_number":(\d+)', res.text)[0]
            print(i[0], comment_num)
            writer.writerow([i[0], "", comment_num])
        except:
            print(i[0], "失效", "失效")
            writer.writerow([i[0], "失效", "失效"])
