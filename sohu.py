# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 13:42:10 2020

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
        "cookie": "SUV=15867406315463n725n; IPLOC=CN4502; gidinf=x099980109ee115723e5f68720004959101be50f96c5; reqtype=pc; t=1588138736795; beans_new_turn_1001800000=%7B%22auto-article%22%3A22%7D; beans_new_turn=%7B%22auto-article%22%3A22%7D; ipcncode=CN440000; sohu_user_ip=157.255.134.162; layerCookie=1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}


url = "https://www.sohu.com/a/337030672_584705"
#data = csv.reader(open('C:\\Users\\liuyuntao\\Desktop\\data_source\\sohu_v1.csv'))
# http://www.sohu
#with open(r"C:\Users\liuyuntao\Desktop\result\sohu.csv", "a+", newline="") as f:
#    writer = csv.writer(f)
#    writer.writerow(["Url", "阅读量", "评论量"])
#    for i in data:
#        try:
#            res = requests.get(i[0], headers=headers)
#            response = etree.HTML(res.text)
#            read_nums = response.xpath("//div[@class='content area']//div[@class='l read-num']/text()")[0]
#            comment_num = response.xpath("//div[@class='content area']//div[@id='autoComment']//span[2]/text()")[0]
#            read_num = re.findall('\d+', read_nums)[0]
#            print(read_num, comment_num)
#            writer.writerow([i[0], read_num, comment_num])
#        except:
#            writer.writerow([i[0], "", ""])

# https://www.sohu
#with open(r"C:\Users\liuyuntao\Desktop\result\sohu_v1.csv", "w+", newline="") as f:
#    writer = csv.writer(f)
#    writer.writerow(["Url", "阅读量", "评论量"])
#    for i in data:
#        res = requests.get(i[0], headers=headers)
#        if res.status_code == 200:
#            res = etree.HTML(res.text)
#            try:
#                read_nums = res.xpath("//div[@class='l read-num']/text()")[0]
#                comment_num = res.xpath("//div[@class='r comment-num-box']/span[2]/text()")[0]
#                read_num = re.findall('\d+', read_nums)[0]
#                print(i[0], read_num, comment_num)
#                writer.writerow([i[0], read_num, comment_num])
#            except:
#                print(i[0], "", "")
#                writer.writerow([i[0], "", ""])
#        else:
#            print(i[0], "失效", "失效")
#            writer.writerow([i[0], "失效", "失效"])

res = requests.get(url, headers=headers)
ret = etree.HTML(res.text)
#ret = etree.HTML(res.text)
read = ret.xpath("//span[@class='read-num']/em/text()")
#read_num = re.findall('\d+', read)[0]

#read_num = re.findall('\d+', read.text)[0]
print(read)
            
            
            
            
            
            