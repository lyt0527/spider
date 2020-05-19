# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 14:38:55 2020

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

url = "http://news.bitauto.com/hao/wenzhang/30380025"

res = requests.get(url, headers=headers)
time.sleep(20)
ret = etree.HTML(res.text)
read_num = ret.xpath("//span[@id='newsVisitCountId']/text()")

comment_num = ret.xpath("//ul[@class='s-list']/li/a/em/text()")

print(url, read_num, comment_num)