# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 14:00:29 2020

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
        "cookie": "fvlid=1588139687728Iuvl0lPNXz; sessionid=011FB57E-FCCD-4354-A30A-6DB816187B44%7C%7C2020-04-29+13%3A54%3A47.996%7C%7C0; autoid=afd3fd15299ca9085f2546f3cca0d256; sessionvid=849E57DC-2EE4-4B4F-B99A-E92442A5020D; ahpau=1; __ah_uuid_ng=c_011FB57E-FCCD-4354-A30A-6DB816187B44; v_no=11; visit_info_ad=011FB57E-FCCD-4354-A30A-6DB816187B44||849E57DC-2EE4-4B4F-B99A-E92442A5020D||-1||-1||11; ahpvno=16; pvidchain=3274711,6826274,3274711,3274711,3274711,28086821202,3274711; sessionip=222.84.126.95; ref=0%7C0%7C0%7C0%7C2020-04-29+14%3A13%3A19.796%7C2020-04-29+13%3A54%3A47.996; area=450206; ahrlid=15881407954317FQlkuUF1N-1588140843825",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}

data = csv.reader(open('C:\\Users\\liuyuntao\\Desktop\\data_source\\chejiahao_v1.csv'))
#url = "https://chejiahao.autohome.com.cn/info/4392184#pvareaid=28086821202"

with open(r"C:\Users\liuyuntao\Desktop\result\chejiahao_v1.csv", "a+", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Url", "阅读量", "评论量"])
    for i in data:
        try:
            res = requests.get(i[0], headers=headers)
            ret = etree.HTML(res.text)
            read_nums = ret.xpath("//div[@class='articleTag']/span[2]/text()")[0]
            comment_nums = ret.xpath("//a[@class='comment']//small[@id='ReplyCount']/text()")[0]
            read_num = re.findall('\d+', read_nums)[0]
            comment_num = re.findall('\d+', comment_nums)[0]
            print(i[0], read_num, comment_num)
            writer.writerow([i[0], read_num, comment_num])
        except:
            print(i[0], "失效", "失效")
            writer.writerow([i[0], "失效", "失效"])