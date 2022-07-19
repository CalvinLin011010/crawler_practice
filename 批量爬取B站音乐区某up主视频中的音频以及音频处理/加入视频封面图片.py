# -*- coding:utf-8 -*-
"""
作者：Calvin_Lin
日期：2022年07月17日 13:37:08
"""


import pandas as pd
import re
import time
import random

import requests
import os
from pydub import AudioSegment

# 读取爬虫得到的数据
# data = pd.read_csv("music_collection_utf_8_pic.tsv", sep="\t")
# print(data)
# 返回结果是[264 rows x 1 columns]，

# 分类
title = []
web = []
style = []
picture = []
description = []

flag = 0
with open("music_collection_utf_8_pic.tsv", 'r', encoding="utf-8") as f:
    for line in f:
        line = line.strip("\n").split("\t")   # 先去掉 "\n" ，再利用 "\t" 切分

        # print(line)
        if flag == 0:  # 不读取第一行表头
            flag = 1
        else:
            print(line[1])
            title.append(line[0])
            web.append(line[1])
            style.append(line[2])
            picture.append(line[3])
            description.append(line[4])


print(web)


pic_path = "F:\\爬虫专题\\test1\\audio批量下载\\pic\\"


for tit, we, pi in zip(title, web, picture):

    url = we

    header = {
        # 'Accept': '*/*',
        # 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
        # get_user_agent(),
        # "cookie" : "buvid3=372A487D-1542-4470-8C60-2503E21E52AF185004infoc; rpdid=|(u~||uYRuu~0J'uYuJmYJm~Y; LIVE_BUVID=AUTO6016152892965344; fingerprint_s=8b3086c61f86a80218156caae72cedad; sid=jtdev49e; balh_is_closed=; balh_server_inner=__custom__; CURRENT_QUALITY=80; buvid4=C1956CDB-179B-1779-B8F2-6F960E87172A07626-022012513-TDIcPGmL6+DQbqtq+GY7QQ%3D%3D; _uuid=539271F6-6867-D661-66EB-F8BC108623191069010infoc; i-wanna-go-back=-1; buvid_fp_plain=undefined; buvid_fp=7fd288d755e22d4b2add100fa2a001ae; DedeUserID=436357525; DedeUserID__ckMd5=e6f9115234b561c4; SESSDATA=9de81950%2C1661762124%2C40887*31; bili_jct=c2417a4db7989384247d73d6a0e0803a; b_ut=5; fingerprint3=75665b35aecc752028fc8c91dd13ab4b; fingerprint=7fd288d755e22d4b2add100fa2a001ae; nostalgia_conf=-1; CURRENT_BLACKGAP=0; blackside_state=0; bp_video_offset_436357525=682315405562216400; CURRENT_FNVAL=4048; innersign=1; b_lsid=EF28275D_181FFCEEFBF; b_timer=%7B%22ffp%22%3A%7B%22333.1007.fp.risk_372A487D%22%3A%22181FF7C03BD%22%2C%22333.788.fp.risk_372A487D%22%3A%22181FFC2F808%22%2C%22333.999.fp.risk_372A487D%22%3A%22181FFC29045%22%2C%22333.337.fp.risk_372A487D%22%3A%22181FFBC49BF%22%2C%22777.5.0.0.fp.risk_372A487D%22%3A%22181FFBE8A8B%22%2C%22888.2421.fp.risk_372A487D%22%3A%22181FFE5F541%22%7D%7D; PVID=1"
        "referer": url
    }

    # 请求html页面内容（包含音频和视频的实际url）
    response = requests.get(url, headers=header)
    html = response.text
    time.sleep(2)
    # print(html)
    response.close()

    # 利用正则表达式定位对应包含目标url的标签的内容（缩小范围）
    obj_info = re.compile(r"<script>window\.__playinfo__={(?P<info>.*?)</script>", re.S)
    info = obj_info.findall(html)[0]
    # print(info)

    # 精确地从html（js）页面中获取音频和视频的url
    # video_url = re.findall(r'"video":.*?,"baseUrl":"(.*?)","', info)[0]
    audio_url = re.findall(r'"audio":.*?,"baseUrl":"(.*?)",', info)[0]
    # print("video_url:")
    # print(video_url)
    print("audio_url:")
    print(audio_url)

    # 请求资源下载
    # video = requests.get(video_url, headers=header)
    audio = requests.get(audio_url, headers=header)

    # with open("test_video" + ".mp4", "wb") as f:
    #     f.write(video.content)
    with open(tit + ".mp3", mode="wb") as f:
        f.write(audio.content)

    time.sleep(3)
    # 睡3秒防止被当成爬虫，然后记得关闭和服务器的会话
    # video.close()
    audio.close()
    print(tit + ".mp3  download  over!!!\n")


    """
    
    res.content拿到的并不是完整页面的代码
    拿到的只是一个主的html加一堆js文件的加载路径，并没有拿到包含着图片标签的代码。
    也就是说，我通过浏览器访问这个网址看到页面的时候，其实已经进行过多次请求响应了
    而我通过代码单独请求这个网址，只拿到了单次请求主页的内容，所以这么搞并不能拿到指定的内容。
    
    """


    # 获取图片

    response_pic = requests.get(pi, headers=header)

    obj_bvid = re.compile(r'/video/(?P<bvid>.*?)$', re.S)
    bvid = re.search(obj_bvid, we).group("bvid")

    print("bvid : " + bvid)


    with open(pic_path + bvid + ".jpg", "wb") as f:
        f.write(response_pic.content)

    print("\n" + tit + " -------> " + bvid + ".jpg  download  over!!!\n\n")


    time.sleep(2)

    sound = AudioSegment.from_file("music1.mp3", frame_rate=44100, channels=2,
                                   sample_width=2)  # , frame_rate=44100, channels=2, sample_width=2

    file_handle = sound.export("\\output\\" + tit + ".mp3",
                               format="mp3",
                               cover="\\pic\\" + bvid + ".jpg"
                               )

    print("\n  封面添加完成   !!!\n")

