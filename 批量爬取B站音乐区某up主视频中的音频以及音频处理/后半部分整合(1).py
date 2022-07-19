"""
作者：Calvin_Lin
日期：2022年07月16日 15:05:02
文件读写测试 + audio下载测试
# -*- coding:utf-8 -*-
"""

import pandas as pd
import re
import time
import random

import requests
import os
from pydub import AudioSegment

import chardet


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
with open("music_collection_utf_8_Pic_EscapeCharacter_&_And - 副本 - 副本 - 副本.tsv", 'r', encoding="utf-8") as f:
    for line in f:
        line = line.strip("\n").split("\t")  # 先去掉 "\n" ，再利用 "\t" 切分
        flag += 1
        # print(line)
        if flag <= 2:  # 不读取第一行表头
            continue
        else:
            print(line)
            print(line[1])
            title.append(line[0])
            web.append(line[1])
            style.append(line[2])
            picture.append(line[3])
            description.append(line[4])



print(web)



pic_path = r"F:/爬虫专题/test1/audio批量下载/pic/"

file_path = r"F:/爬虫专题/test1/audio批量下载/"

for tit, we, pi, desc in zip(title, web, picture, description):
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
    # 注意这里的文件名读取方式

    ## './input/' + tit + '.mp3'  报错
    #  FileNotFoundError: [Errno 2] No such file or directory:
    #  './input/【古典圆舞曲／哥特钢琴】バリアス·カラーズ(Various Colors) - Op.149 \\"Dark Gothic Piano Waltz\\".mp3'

    ## str('./input/' + tit.strip("\\") + '.mp3').replace('"', '\"')    报错
    #  FileNotFoundError: [Errno 2] No such file or directory:
    #  './input/【古典圆舞曲／哥特钢琴】バリアス·カラーズ(Various Colors) - Op.149 \\\\"Dark Gothic Piano Waltz\\\\".mp3'


    print(tit)
    print(file_path + 'input/' + tit + '.mp3')
    # print(str('./input/' + tit.strip("\\") + '.mp3').replace('"', '\"'))
    # print(str('./input/' + tit.strip("\\") + '.mp3').replace('"', '\\"'))

    # open() 函数中第一个参数是路径，open() 函数会先解析路径字符串，
    # 如果没有申明取消转义的话，它会自动对字符串中所有的 '\' 前再加上 '\' ，所以在此情况下不可能有单个 '\' 输出的情况
    # 可以使用 repr() 函数来测试输出效果，
    # 因为 repr() 会将得到的字符串通常可以用来重新获得该对象，将对象转化为供解释器直接读取的形式。

    # audio_path = repr(str('./input/' + tit.strip("\\") + '.mp3').replace('"', '\"'))
    audio_path = (file_path.encode("unicode-escape") + 'input/'.encode("unicode-escape") + tit.encode("unicode-escape") + u'.mp3'.encode("unicode-escape"))

    print(audio_path)
    print(type(audio_path))

    print(file_path + r'input/' + tit + r'.mp3')

    print("\nchardet查看编码:")
    print(chardet.detect(str.encode(tit)))
    print("\n")
    # chardet查看编码:
    # {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
    # confidence 是预测这种编码的可能性，encoding是预测的编码名称

    with open('./input/' + tit + '.mp3', mode='wb') as f:
        f.write(audio.content)


    # FileNotFoundError: [Errno 2] No such file or directory:
    # './input/【Chill Hop/优美放松/节奏纯音】Sitting Duck, Tesk, No Spirit - Driftaway.mp3'
    #                                                  ,，


    time.sleep(2)
    # 睡3秒防止被当成爬虫，然后记得关闭和服务器的会话
    # video.close()
    audio.close()
    print("./input/" + tit + ".mp3  download  over!!!\n")

    '''

    res.content拿到的并不是完整页面的代码
    拿到的只是一个主的html加一堆js文件的加载路径，并没有拿到包含着图片标签的代码。
    也就是说，我通过浏览器访问这个网址看到页面的时候，其实已经进行过多次请求响应了
    而我通过代码单独请求这个网址，只拿到了单次请求主页的内容，所以这么搞并不能拿到指定的内容。

    '''

    # 获取图片

    response_pic = requests.get(pi, headers=header)

    obj_bvid = re.compile(r'/video/(?P<bvid>.*?)$', re.S)
    bvid = re.search(obj_bvid, we).group("bvid")

    print("bvid : " + bvid)

    with open(pic_path + bvid + ".jpg", "wb") as f:
        f.write(response_pic.content)

    print("\n" + pic_path + " -------> " + bvid + ".jpg  download  over!!!\n\n")


    sound = AudioSegment.from_file(file_path + 'input/' + tit + '.mp3',
                                   frame_rate=44100,
                                   channels=2,
                                   sample_width=2)  # , frame_rate=44100, channels=2, sample_width=2

    print("./output/" + tit + ".mp3")
    print("./pic/" + bvid + ".jpg")
    file_handle = sound.export(file_path + 'output/' + tit + '.mp3',
                               format="mp3",
                               bitrate="320k",  # 相当于极高音质 320kbit/s
                               tags={"comments": desc},
                               cover="./pic/" + bvid + ".jpg"
                               )

    print("\n  封面添加完成   !!!\n")















