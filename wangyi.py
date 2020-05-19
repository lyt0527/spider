# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 10:44:41 2020

@author: liuyuntao
"""

import requests
from lxml import etree
import csv
import time

headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Cookie": "_ntes_nnid=f2963dda672d88d2f22232a2a96f0589,1588127776908; _ntes_nuid=f2963dda672d88d2f22232a2a96f0589; WM_NI=Iq8oHhGX28zmtrIw7WgNGf3ZEMy%2FndDOOpA2Yp8mpxn0MnfyBeso6a%2F51ojuXnscgPkoRpq%2Bc24nlF89iG4M8QObQl90JS%2BUvEKkZgLjLUrGP3aHXjvog8rIuPTo2Y%2FKc1g%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb1bb7ef799aa8cef68f28a8fa3d85e968b9aaaae4ab68bab95e263f58b8ca7f32af0fea7c3b92a8baff890cb648588fed9f967b8ae8798b65da5928987b2528793b7d0ed7088918191c43a9bb0f88ef374aef0838fe57382bbbd90b56bedebff90e97f9cb2bd84e65ca9b19e91f421a1eefc8fef4efce7a7a8b747fc8f8183d468fbf086b4aa5fb69b858cd96d90b684b6f14d94edafa9db62b6b1a9d9f143b7909c90b153ed95add2e637e2a3; WM_TID=WMQfB4L86HxBUEEURAI%2BU7EPtM3vVWAo; NTESwebSI=D95D14E3922E8F5D8070C097BFE8FB3E.hz-subscribe-web-docker-cm-online-rpqqn-8gfzd-exh2j-7797b5r94cg-8081",       
        "Host": "dy.163.com",
        "Referer": "http://dy.163.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
}
#url = "http://dy.163.com/v2/article/detail/EKMV3SDM05474D8L.htmlhttp://dy.163.com/v2/article/detail/EL3OFN5608474DAL.html"
#res = requests.get(url, headers=headers)
#print(res.status_code)
data = csv.reader(open('C:\\Users\\liuyuntao\\Desktop\\data_source\\dy_v1.csv'))

with open(r"C:\Users\liuyuntao\Desktop\result\dy_v1.csv", "a+", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Url", "阅读量", "评论量"])
    for i in data:
        try:
            res = requests.get(i[0], headers=headers)
            response = etree.HTML(res.text)
            read_num = response.xpath("//div[@id='contain']//div[@class='tie-title-bar']//a[2]/text()")[0]
            comment_num = response.xpath("//div[@id='contain']//div[@class='tie-title-bar']//a[1]/text()")[0]
            print(i[0], read_num, comment_num)
            writer.writerow([i[0], read_num, comment_num])
        except:
            print(i[0], "失效", "失效")
            writer.writerow([i[0], "失效", "失效"])