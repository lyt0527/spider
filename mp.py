# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 12:36:11 2020

@author: liuyuntao
"""


import requests
from lxml import etree
import csv
import re



headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
        }





url = "https://mparticle.uc.cn/article.html?uc_param_str=frdnsnpfvecpntnwprdssskt&wm_aid=aa25ad019aea42b0b22d8ab22639c7bc"

res = requests.get(url, headers=headers)
#response = etree.HTML(res.text)

#text = response.xpath("//div[@class='contentbox']/div/p[1]/text()")
content = re.findall('<title>(.*?)</title>', res.text)

print(content)