#!/usr/bin/env python3

import urllib.request
import socket
import re
import sys
import os

 # 需要抓取的url
url = "https://movie.douban.com/subject/27619748/photos?type=R"

# 定义图片保存路径
targetPath = "DoubanImage"
 
# 保存图片
def saveImg(path):
    if not os.path.isdir(targetPath):
        os.mkdir(targetPath)
    pos = path.rindex('/')
    t = os.path.join(targetPath, path[pos + 1:])
    return t
 
if __name__ == '__main__':

    # 添加header文件伪装成浏览器
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }

    # 要抓取的资源分页，起始页页码
    start = 1
    # 要抓取的资源分页，结束页页码
    end = 4
    urls = ['{path}&start={i}'.format(path=url,i=(id-1)*30)for id in range(start, end+1)]
    #   "https://movie.douban.com/subject/27619748/photos?type=R&start=0"
    for suburl in urls:
        print(suburl)
        req = urllib.request.Request(url=suburl, headers=headers)
        res = urllib.request.urlopen(req)
        data = res.read()
        
        # 豆瓣上海报都在这个路径下
        path = "view/photo/m/public"
        # 通过正则表达式抓取储图片url
        for link, t in set(re.findall(r'(http[s]:[^s]*?(jpg|png|gif|webp|jpeg))', str(data))):
            if path in link:
                print(link)
                try:
                    urllib.request.urlretrieve(link, saveImg(link))
                except:
                    print('失败')
