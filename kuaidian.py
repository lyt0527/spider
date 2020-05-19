# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 12:50:03 2020

@author: liuyuntao
"""
import requests
from lxml import etree
import csv
import re

headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Cookie": "RK=J3pEXrrSW7; ptcz=5dad53c626304b56f90dcce50bf8a967d389228314451100447e63bf74b1057f; pgv_pvid=5288187837; pgv_pvi=845607936; o_cookie=1344232394; pac_uid=1_1344232394; ied_qq=o1344232394; kb_h5_user_id=KBH5UserId_15881351703404402",
        "Host": "kuaibao.qq.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",      
}

data = csv.reader(open('C:\\Users\\liuyuntao\\Desktop\\data_source\\kuaibao_v1.csv'))

with open(r"C:\Users\liuyuntao\Desktop\result\kuaibao_v1.csv", "a+", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Url", "阅读量", "评论量"])
    for i in data:
        try:
            url_ = "http://kuaibao.qq.com/getSubNewsContent?id=%s" % i[0][-16:]
            res = requests.get(url_, headers=headers)
            comment_num = re.findall('"comments":(\d+)', res.text)[0]
            print(i[0], comment_num)
            writer.writerow([i[0], "", comment_num])
        except:
            print(i[0], "失效", "失效")
            writer.writerow([i[0], "失效", "失效"])
            