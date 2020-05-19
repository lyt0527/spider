# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 10:41:09 2020

@author: liuyuntao
"""


import requests
from lxml import etree
import re
import csv



headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cookie": "BIDUPSID=FD0B7099507A36563AAE2930318CA954; PSTM=1579164074; BAIDUID=FD0B7099507A3656B14FA9F149903172:SL=0:NR=10:FG=1; BDUSS=mlTeFdiMjNCWkdDUDgzeS1rejZTcFduYWExckMxLTNGLWpsSlNYNzRnOGdmSmxlSVFBQUFBJCQAAAAAAAAAAAEAAACpuM40t8nP6ExUOTYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDvcV4g73FeN; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_WISE_SIDS=143932_145646_142018_140632_144134_145270_146538_146152_144961_131246_144681_141261_144741_144251_141941_127969_146034_146551_145971_140593_131423_100807_145523_146002_144499_107312_145294_146135_139909_144871_144966_145305_145396_143857_145440_139914_110085; SE_LAUNCH=5%3A26469312; H_PS_PSSID=1425_31169_21126_31425_31341_30910_31463_31228_30823_26350_31164; delPer=0; PSINO=7; PC_TAB_LOG=video_details_page; COMMON_LID=ff41224b4c429bd71965182a66a44c63; Hm_lvt_4aadd610dfd2f5972f1efee2653a2bc5=1588214401; Hm_lpvt_4aadd610dfd2f5972f1efee2653a2bc5=1588214401; reptileData=%7B%22data%22%3A%22b05ffc216c33ef5a0e117d7bbdf78155899e9333164c8603dc39f33837dfb6f9e05c958019600a6d2f43c7c5d79afeae42c00442f8ae88750160d07cf743582b53b327a89d35b845e2f3ea0660ea603a43a5238bd9f79a162381cc84270b81cc9255b18aa5336807f1cd5cb7704e00166ba60959f97648bc2535fd4ceaa78315%22%2C%22key_id%22%3A%2230%22%2C%22sign%22%3A%22dc947a75%22%7D",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}



data = csv.reader(open('C:\\Users\\liuyuntao\\Desktop\\data_source\\haokan.csv'))

with open(r"C:\Users\liuyuntao\Desktop\result\haokan_v1.csv", "w+", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Url", "阅读量", "评论量"])
    for i in data:
        res = requests.get(i[0], headers=headers)
        if res.status_code == 200:
            response = etree.HTML(res.text)
            try:
                read_nums = response.xpath("//span[@class='videoinfo-playnums float-left']/text()")[0]
                read_num = re.findall('\d+', read_nums)[0]
                comment_num = re.findall('"comment":"(\d+)"', res.text)[0]
                print(i[0], read_num, comment_num)
                writer.writerow([i[0], read_num, comment_num])
            except:
                print(i[0], "", "", "报错")
                writer.writerow([i[0], "", ""])
        else:
            print(i[0], "失效", "失效")
            writer.writerow([i[0], "失效", "失效"])
