# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 10:24:09 2020

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
        "cookie": "wafid=f32137a2-879d-40a4-bdcf-fc144910c22c; wafid.sig=mwDW4fzgPS5_SAW4b-3vCNt9QUk; ttwid=6821324533682783757; ttwid.sig=VCtzvjjAeGgihCf4nM-4P6H7O38; xiguavideopcwebid=6821324533682783757; xiguavideopcwebid.sig=ajJN2aeBySkTHjEyqTxkb2VqLI4; ixigua-a-s=0; SLARDAR_WEB_ID=d249b2d9-9fa7-490d-9c40-0ca9bea4d614; _ga=GA1.2.769737654.1588213389; _gid=GA1.2.98484659.1588213389",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}


url = "https://www.ixigua.com/i6730973477160878606/"



#data = csv.reader(open('C:\\Users\\liuyuntao\\Desktop\\data_source\\xigua_v1.csv'))

#with open(r"C:\Users\liuyuntao\Desktop\result\xigua_v1.csv", "a+", newline="") as f:
#    writer = csv.writer(f)
#    writer.writerow(["Url", "阅读量", "评论量"])
#    for i in data:
#        res = requests.get(i[0], headers=headers)
#        if res.status_code == 200:
#            response = etree.HTML(res.text)
#            try:
#                read_num = response.xpath("//div[@class='videoDesc']/div/span[1]/text()")[0]
#                comment_num = response.xpath("//div[@class='commentCount']/text()")[0]
#                print(i[0], read_num, comment_num)
#                writer.writerow([i[0], read_num, comment_num])
#            except:
#                print(i[0], "", "")
#                writer.writerow([i[0], "", ""])
#        else:
#            print(i[0], "失效", "失效")
#            writer.writerow([i[0], "失效", "失效"])
url = "https://www.ixigua.com/i6731655992540397580/"

res = requests.get(url, headers=headers)
print(res.status_code)

            
            
            

