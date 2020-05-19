# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 13:09:03 2020

@author: liuyuntao
"""


import requests
from lxml import etree
import csv
import re



headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": 'BIDUPSID=FD0B7099507A36563AAE2930318CA954; PSTM=1579164074; BAIDUID=FD0B7099507A3656B14FA9F149903172:SL=0:NR=10:FG=1; BDUSS=mlTeFdiMjNCWkdDUDgzeS1rejZTcFduYWExckMxLTNGLWpsSlNYNzRnOGdmSmxlSVFBQUFBJCQAAAAAAAAAAAEAAACpuM40t8nP6ExUOTYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDvcV4g73FeN; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; x-logic-no=5; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; IsPackUpShare=1; Hmery-Time=1703320451; fortune={"data":"4c56810e1d1a3028426cd38884fb138409ebeeaf6314ec3e10f96c6866731097e956502011c36d41f8d6dc6eeaae25e78e59a3e3912e467fb56a40bbc30189b5f1e077d9e67fe91cbe7c595e184314898f0ac11fbf372d096740429300970df42b9b2a628e1e68fb6abe96b675e40eb243dba6c0882a6807b4a65d91fae35b75","key_id":"31","sign":"b90d915f"}; PSINO=6; H_PS_PSSID=1425_31169_21126_31425_31341_30910_31463_31228_30823_26350_31164',
        "Host": "mbd.baidu.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}

data = csv.reader(open('C:\\Users\\liuyuntao\\Desktop\\data_source\\mbd_v2.csv'))

with open(r"C:\Users\liuyuntao\Desktop\result\mbd_v2.csv", "a+", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Url", "阅读量", "评论量"])
    for i in data:
        try:
            res = requests.get(i[0], headers=headers)
            thread_id = re.findall('"thread_id":"(.*?)"', res.text)[0]
            url_ = "https://ext.baidu.com/api/comment/v1/comment/getlist&thread_id=%s&appid=101" % thread_id
            res_new = requests.get(url_)
            comment_num = re.findall('"comment_count":"(.*?)"', res_new.text)[0]
            writer.writerow([i[0], "", comment_num])
            print(i[0], comment_num)
        except:
            print(i[0], "失效", "失效")
            writer.writerow([i[0], "失效", "失效"])