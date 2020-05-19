# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 15:11:41 2020

@author: liuyuntao
"""


import requests
from lxml import etree
import time
import csv
import re


headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}

data = csv.reader(open('C:\\Users\\liuyuntao\\Desktop\\data_source\\zhihu.csv'))

with open(r"C:\Users\liuyuntao\Desktop\result\zhihu.csv", "a+", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Url", "阅读量", "评论量"])
    for i in data:
        try:
            res = requests.get(i[0], headers=headers)
            ret = etree.HTML(res.text)
            read_num = ret.xpath("//div[@class='NumberBoard QuestionFollowStatus-counts NumberBoard--divider']/div[2]//strong/text()")[0]
            
            comment_nums = ret.xpath("//div[@class='List']//h4[@class='List-headerText']/span/text()")[0]
            
            comment_num = re.findall('\d+', comment_nums)[0]
            
            print(url, read_num, comment_num)
            writer.writerow([i[0], read_num, comment_num])
        except:
            writer.writerow([i[0], "", ""])