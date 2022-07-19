# -*- coding:utf-8 -*-
"""
作者：Calvin_Lin
日期：2022年07月15日 13:19:02
"""

import pandas as pd
import requests
import re
import json
import subprocess
import os


data = pd.read_csv("music_collection_utf_8_成功 - 副本.tsv", sep="\t")
# print(data)
# 返回结果是[264 rows x 1 columns]，

title = []
web = []
style = []
description = []

flag = 0
with open("music_collection_utf_8_成功 - 副本.tsv", 'r', encoding="utf-8") as f:
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
            description.append(line[3])

print(title)
print(web)


'''
print("————————————————————————————————————————保存文件————————————————————————————————————————")

header = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
    # get_user_agent(),
    # "cookie" : "buvid3=372A487D-1542-4470-8C60-2503E21E52AF185004infoc; rpdid=|(u~||uYRuu~0J'uYuJmYJm~Y; LIVE_BUVID=AUTO6016152892965344; fingerprint_s=8b3086c61f86a80218156caae72cedad; sid=jtdev49e; balh_is_closed=; balh_server_inner=__custom__; CURRENT_QUALITY=80; buvid4=C1956CDB-179B-1779-B8F2-6F960E87172A07626-022012513-TDIcPGmL6+DQbqtq+GY7QQ%3D%3D
    # ; _uuid=539271F6-6867-D661-66EB-F8BC108623191069010infoc; i-wanna-go-back=-1; buvid_fp_plain=undefined; buvid_fp=7fd288d755e22d4b2add100fa2a001ae; DedeUserID=436357525; DedeUserID__ckMd5=e6f9115234b561c4; SESSDATA=9de81950%2C1661762124%2C40887*31; bili_jct=c2417a4db7989384247d73d6a0e0803a; b_ut=5; fingerprint3=75665b35aecc752028fc8c91dd13ab4b
    # ; fingerprint=7fd288d755e22d4b2add100fa2a001ae; nostalgia_conf=-1; CURRENT_BLACKGAP=0; blackside_state=0; bp_video_offset_436357525=682315405562216400; CURRENT_FNVAL=4048; innersign=1; b_lsid=EF28275D_181FFCEEFBF; b_timer=%7B%22ffp%22%3A%7B%22333.1007.fp.risk_372A487D%22%3A%22181FF7C03BD%22%2C%22333.788.fp.risk_372A487D%22%3A%22181FFC2F808%22%2C%22333.999.fp.
    # risk_372A487D%22%3A%22181FFC29045%22%2C%22333.337.fp.risk_372A487D%22%3A%22181FFBC49BF%22%2C%22777.5.0.0.fp.risk_372A487D%22%3A%22181FFBE8A8B%22%2C%22888.2421.fp.risk_372A487D%22%3A%22181FFE5F541%22%7D%7D; PVID=1"
    "referer": "https://message.bilibili.com/"
}

def send_request(url):
    response = requests.get(url=url, headers=header)
    return response

def get_video_data(html_datas):
    # title1 = re.findall('<title data-vue-meta="true">(.*?)</title>',html_datas)[0].replace("_哔哩哔哩 (゜-゜)つロ 干杯~-bilibili","")
    json_data = re.findall(r'<script>window.__playinfo__=(.*?)</script>',html_datas)[0]
    json_data = json.loads(json_data)
    audio_url = json_data["data"]["dash"]["audio"][0]["backupUrl"][0]
    # video_url = json_data["data"]["dash"]["video"][0]["backupUrl"][0]
    video_datas = [title[0], audio_url]
    return video_datas

def save_data(file_name,audio_url):
    print("正在下载 " + file_name + "的音频...")
    audio_data = send_request(audio_url).content
    print("完成下载 " + file_name + "的音频！")
    with open(file_name + ".mp3", "wb") as f:
        f.write(audio_data)


html_data = requests.get("https://www.bilibili.com/video/" + web[0], headers=header).text
print(html_data)
video_data = get_video_data(html_data)

for item in video_data:
    print(item)


save_data(video_data[0],video_data[1])


# for tit, we in zip(title, web):

    # 获取数据


    # break

print("over!")

# with open("music_collection_utf_8_成功 - 副本.tsv", "r", encoding="utf-8") as f:
#     f.write("'编号','视频标题名称','网址','up对音乐的风格分类','作者 - 音乐名称','作曲者名字','成曲时间','视频简介'" + "\n")
#     for i in range(1,10,1):
#
#         f.write(str(i) + "\n")
#
# print("over!")


'''

'''
window.__playinfo__={
"code":0,"message":"0","ttl":1,
"data":{"from":"local","result":"suee","message":"","quality":80,"format":"flv",
    "timelength":773247,"accept_format":"flv,flv720,flv480,mp4",
    "accept_description":["高清 1080P","高清 720P","清晰 480P","流畅 360P"],
    "accept_quality":[80,64,32,16],"video_codecid":7,"seek_param":"start","seek_type":"offset","dash":{"duration":774,"minBufferTime":1.5,"min_buffer_time":1.5,"video":[{"id":80,
    "baseUrl":"https://upos-sz-estgoss.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-30080.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=upos&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=ad387b4de423d641dbb3e5f8d11b7b68&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=0,1&agrr=1&bw=28538&logo=80000000",
    "base_url":"https://upos-sz-estgoss.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-30080.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=upos&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=ad387b4de423d641dbb3e5f8d11b7b68&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=0,1&agrr=1&bw=28538&logo=80000000",
    "backupUrl":null,"backup_url":null,"bandwidth":228250,"mimeType":"video/mp4","mime_type":"video/mp4","codecs":"avc1.640032","width":1920,"height":1080,"frameRate":"25","frame_rate":"25","sar":"1:1",
    "startWithSap":1,
    "start_with_sap":1,
    "SegmentBase":{"Initialization":"0-996","indexRange":"997-2888"},
    "segment_base":{"initialization":"0-996","index_range":"997-2888"},
    "codecid":7},
    {"id":80,
    "baseUrl":"https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-100026.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=cosbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=ac992de64301f265a98fc8926d433a09&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=0,3&agrr=1&bw=45299&logo=80000000",
    "base_url":"https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-100026.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=cosbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=ac992de64301f265a98fc8926d433a09&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=0,3&agrr=1&bw=45299&logo=80000000",
    "backupUrl":["https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-100026.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=cosbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=ac992de64301f265a98fc8926d433a09&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=1,3&agrr=1&bw=45299&logo=40000000",
                 "https://upos-sz-mirrorcosb.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-100026.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=cosbbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=a211a148afc33309c6e784c35608c74b&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=2,3&agrr=1&bw=45299&logo=40000000"],
    "backup_url":["https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-100026.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=cosbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=ac992de64301f265a98fc8926d433a09&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=1,3&agrr=1&bw=45299&logo=40000000",
                  "https://upos-sz-mirrorcosb.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-100026.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=cosbbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=a211a148afc33309c6e784c35608c74b&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=2,3&agrr=1&bw=45299&logo=40000000"],
    "bandwidth":361336,"mimeType":"video/mp4","mime_type":"video/mp4","codecs":"av01.0.08M.08.0.110.01.01.01.0",
    "width":1920,
    "height":1080,
    "frameRate":"25",
    "frame_rate":"25",
    "sar":"1:1",
    "startWithSap":1,
    "start_with_sap":1,
    "SegmentBase":{
        "Initialization":"0-940","indexRange":"1137-3028"},
        "segment_base":{
            "initialization":"0-940",
            "index_range":"1137-3028"},
            "codecid":13},
    
    {
    "id":64,
    "baseUrl":"https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-30064.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=hwbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=eb19782273ad4a218b4c9f503c951497&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=0,3&agrr=1&bw=13508&logo=80000000",
    "base_url":"https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-30064.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=hwbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=eb19782273ad4a218b4c9f503c951497&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=0,3&agrr=1&bw=13508&logo=80000000",
    "backupUrl":["https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-30064.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=hwbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=eb19782273ad4a218b4c9f503c951497&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=1,3&agrr=1&bw=13508&logo=40000000",
                 "https://upos-sz-mirrorhwb.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-30064.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=hwbbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=95b22ee7b980aace9f801fc50fb1f518&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=2,3&agrr=1&bw=13508&logo=40000000"],
    "backup_url":["https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-30064.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=hwbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=eb19782273ad4a218b4c9f503c951497&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=1,3&agrr=1&bw=13508&logo=40000000",
                  "https://upos-sz-mirrorhwb.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-30064.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=hwbbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=95b22ee7b980aace9f801fc50fb1f518&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=2,3&agrr=1&bw=13508&logo=40000000"],
    "bandwidth":108040,
    "mimeType":"video/mp4",
    "mime_type":"video/mp4",
    "codecs":"avc1.640028",
    "width":1280,"height":720,
    "frameRate":"25",
    "frame_rate":"25",
    "sar":"1:1",
    "startWithSap":1,
    "start_with_sap":1,
    "SegmentBase":{
        "Initialization":"0-994",
        "indexRange":"995-2886"
    },
    "segment_base":{    
        "initialization":"0-994",
        "index_range":"995-2886"
    },
    "codecid":7
    },
    {"id":64,"baseUrl":"https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-100024.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=hwbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=63fe061b2db4c00c0b337b8da5e6de22&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=0,3&agrr=1&bw=27882&logo=80000000",
    "base_url":"https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-100024.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=hwbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=63fe061b2db4c00c0b337b8da5e6de22&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=0,3&agrr=1&bw=27882&logo=80000000",
    "backupUrl":["https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-100024.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=hwbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=63fe061b2db4c00c0b337b8da5e6de22&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=1,3&agrr=1&bw=27882&logo=40000000",
    "https://upos-sz-mirrorhwb.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-100024.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=hwbbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=90a1dec1057e443a0a9aad44cb93852f&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=2,3&agrr=1&bw=27882&logo=40000000"],
    "backup_url":["https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-100024.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=hwbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=63fe061b2db4c00c0b337b8da5e6de22&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=1,3&agrr=1&bw=27882&logo=40000000",
    "https://upos-sz-mirrorhwb.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-100024.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=hwbbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=90a1dec1057e443a0a9aad44cb93852f&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=2,3&agrr=1&bw=27882&logo=40000000"],
    "bandwidth":222031,"mimeType":"video/mp4","mime_type":"video/mp4","codecs":"av01.0.05M.08.0.110.01.01.01.0","width":1280,"height":720,"frameRate":"25","frame_rate":"25","sar":"1:1","startWithSap":1,"start_with_sap":1,"SegmentBase":{"Initialization":"0-940","indexRange":"1137-3028"},"segment_base":{"initialization":"0-940","index_range":"1137-3028"},"codecid":13},{"id":32,
    "baseUrl":"https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-30032.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=cosbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=99b583e5bf9df39ac23e086c0b34882c&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=0,3&agrr=1&bw=6544&logo=80000000",
    "base_url":"https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-30032.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=cosbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=99b583e5bf9df39ac23e086c0b34882c&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=0,3&agrr=1&bw=6544&logo=80000000",
    "backupUrl":["https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-30032.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=cosbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=99b583e5bf9df39ac23e086c0b34882c&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=1,3&agrr=1&bw=6544&logo=40000000",
                 "https://upos-sz-mirrorcosb.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-30032.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=cosbbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=b77bf38f244ded3b104da0bb2a7bb216&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=2,3&agrr=1&bw=6544&logo=40000000"],
    "backup_url":["https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-30032.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=cosbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=99b583e5bf9df39ac23e086c0b34882c&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=1,3&agrr=1&bw=6544&logo=40000000",
    "https://upos-sz-mirrorcosb.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-30032.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=cosbbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=b77bf38f244ded3b104da0bb2a7bb216&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=2,3&agrr=1&bw=6544&logo=40000000"],
    "bandwidth":52345,"mimeType":"video/mp4","mime_type":"video/mp4",
    "codecs":"avc1.64001F","width":852,"height":480,"frameRate":"25","frame_rate":"25","sar":"640:639","startWithSap":1,"start_with_sap":1,"SegmentBase":{"Initialization":"0-999","indexRange":"1000-2891"},"segment_base":{"initialization":"0-999","index_range":"1000-2891"},"codecid":7},{"id":32,
    "baseUrl":"https://upos-sz-estgoss.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-100023.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=upos&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=e6ac91bb2afd8a541ebf0db8441e2c96&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=0,1&agrr=1&bw=13727&logo=80000000",
    "base_url":"https://upos-sz-estgoss.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-100023.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=upos&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=e6ac91bb2afd8a541ebf0db8441e2c96&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=0,1&agrr=1&bw=13727&logo=80000000",
    "backupUrl":null,"backup_url":null,"bandwidth":108808,"mimeType":"video/mp4","mime_type":"video/mp4","codecs":"av01.0.04M.08.0.110.01.01.01.0","width":852,"height":480,"frameRate":"25","frame_rate":"25","sar":"640:639","startWithSap":1,"start_with_sap":1,"SegmentBase":{"Initialization":"0-940","indexRange":"1137-3028"},"segment_base":{"initialization":"0-940","index_range":"1137-3028"},"codecid":13},{"id":16,
    "baseUrl":"https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-30016.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=hwbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=a3dfe6461e20735916e2753da45cb957&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=0,3&agrr=1&bw=4110&logo=80000000",
    "base_url":"https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-30016.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=hwbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=a3dfe6461e20735916e2753da45cb957&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=0,3&agrr=1&bw=4110&logo=80000000",
    "backupUrl":["https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-30016.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=hwbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=a3dfe6461e20735916e2753da45cb957&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=1,3&agrr=1&bw=4110&logo=40000000",
                 "https://upos-sz-mirrorhwb.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-30016.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=hwbbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=2b4997715e96cfff49d62d6044e8471e&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=2,3&agrr=1&bw=4110&logo=40000000"],
    "backup_url":["https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-30016.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=hwbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=a3dfe6461e20735916e2753da45cb957&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=1,3&agrr=1&bw=4110&logo=40000000",
                  "https://upos-sz-mirrorhwb.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-30016.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=hwbbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=2b4997715e96cfff49d62d6044e8471e&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=2,3&agrr=1&bw=4110&logo=40000000"],
    "bandwidth":32876,"mimeType":"video/mp4","mime_type":"video/mp4","codecs":"avc1.64001E","width":640,"height":360,"frameRate":"25","frame_rate":"25","sar":"1:1","startWithSap":1,"start_with_sap":1,"SegmentBase":{"Initialization":"0-1003","indexRange":"1004-2895"},"segment_base":{"initialization":"0-1003","index_range":"1004-2895"},
    "codecid":7},{"id":16,"baseUrl":"https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-100022.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=cosbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=e5f3e9593041c87ed846d1ed25defb7f&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=0,3&agrr=1&bw=8725&logo=80000000",
    "base_url":"https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-100022.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=cosbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=e5f3e9593041c87ed846d1ed25defb7f&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=0,3&agrr=1&bw=8725&logo=80000000",
    "backupUrl":["https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-100022.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=cosbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=e5f3e9593041c87ed846d1ed25defb7f&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=1,3&agrr=1&bw=8725&logo=40000000",
    "https://upos-sz-mirrorcosb.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-100022.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=cosbbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=dea743d9104da9e9a9aeb71ec37158ee&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=2,3&agrr=1&bw=8725&logo=40000000"],
    "backup_url":["https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-100022.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=cosbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=e5f3e9593041c87ed846d1ed25defb7f&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=1,3&agrr=1&bw=8725&logo=40000000",
                  "https://upos-sz-mirrorcosb.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-100022.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=cosbbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=dea743d9104da9e9a9aeb71ec37158ee&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=2,3&agrr=1&bw=8725&logo=40000000"],
    "bandwidth":68804,"mimeType":"video/mp4","mime_type":"video/mp4",
    "codecs":"av01.0.01M.08.0.110.01.01.01.0","width":640,"height":360,"frameRate":"25","frame_rate":"25","sar":"1:1","startWithSap":1,"start_with_sap":1,"SegmentBase":{"Initialization":"0-940","indexRange":"1137-3028"},"segment_base":{"initialization":"0-940","index_range":"1137-3028"},"codecid":13}],
    "audio":[{"id":30280,"baseUrl":"https://upos-sz-estgoss.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=upos&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=0cc27525d62fee411bed026fe78464fc&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=0,1&agrr=1&bw=39900&logo=80000000",
    "base_url":"https://upos-sz-estgoss.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=upos&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=0cc27525d62fee411bed026fe78464fc&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=0,1&agrr=1&bw=39900&logo=80000000",
    "backupUrl":null,"backup_url":null,"bandwidth":319103,"mimeType":"audio/mp4","mime_type":"audio/mp4","codecs":"mp4a.40.2","width":0,"height":0,"frameRate":"","frame_rate":"","sar":"","startWithSap":0,"start_with_sap":0,"SegmentBase":{"Initialization":"0-933","indexRange":"934-2825"},"segment_base":{"initialization":"0-933","index_range":"934-2825"},"codecid":0},{"id":30216,
    "baseUrl":"https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-30216.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=hwbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=c2ac6b69a69268dfd56165fea04f89d8&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=0,3&agrr=1&bw=8410&logo=80000000",
    "base_url":"https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-30216.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=hwbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=c2ac6b69a69268dfd56165fea04f89d8&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=0,3&agrr=1&bw=8410&logo=80000000",
    "backupUrl":["https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-30216.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=hwbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=c2ac6b69a69268dfd56165fea04f89d8&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=1,3&agrr=1&bw=8410&logo=40000000",
    "https://upos-sz-mirrorhwb.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-30216.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=hwbbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=8a23286ab64c56fbc3bf683c56dc3809&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=2,3&agrr=1&bw=8410&logo=40000000"],
    "backup_url":["https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-30216.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=hwbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=c2ac6b69a69268dfd56165fea04f89d8&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=1,3&agrr=1&bw=8410&logo=40000000",
    "https://upos-sz-mirrorhwb.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-30216.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=hwbbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=8a23286ab64c56fbc3bf683c56dc3809&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=2,3&agrr=1&bw=8410&logo=40000000"],
    "bandwidth":67264,"mimeType":"audio/mp4","mime_type":"audio/mp4","codecs":"mp4a.40.2","width":0,"height":0,"frameRate":"","frame_rate":"","sar":"","startWithSap":0,"start_with_sap":0,"SegmentBase":{"Initialization":"0-941","indexRange":"942-2833"},"segment_base":{"initialization":"0-941","index_range":"942-2833"},"codecid":0},{"id":30232,
    "baseUrl":"https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-30232.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=hwbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=79fba747efe20022c24b6ba07bac6859&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=0,3&agrr=1&bw=16605&logo=80000000",
    "base_url":"https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-30232.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=hwbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=79fba747efe20022c24b6ba07bac6859&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=0,3&agrr=1&bw=16605&logo=80000000",
    "backupUrl":["https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-30232.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=hwbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=79fba747efe20022c24b6ba07bac6859&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=1,3&agrr=1&bw=16605&logo=40000000",
    "https://upos-sz-mirrorhwb.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-30232.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=hwbbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=c71c8c54fa7537871393f84d6b705535&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=2,3&agrr=1&bw=16605&logo=40000000"],
    "backup_url":["https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-30232.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=hwbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=79fba747efe20022c24b6ba07bac6859&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=1,3&agrr=1&bw=16605&logo=40000000",
    "https://upos-sz-mirrorhwb.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-30232.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=hwbbv&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=c71c8c54fa7537871393f84d6b705535&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=2,3&agrr=1&bw=16605&logo=40000000"],
    "bandwidth":132800,"mimeType":"audio/mp4","mime_type":"audio/mp4","codecs":"mp4a.40.2","width":0,"height":0,"frameRate":"","frame_rate":"","sar":"","startWithSap":0,
    "start_with_sap":0,"SegmentBase":{"Initialization":"0-933","indexRange":"934-2825"},"segment_base":{"initialization":"0-933","index_range":"934-2825"},"codecid":0}],"dolby":null,"flac":null},"support_formats":[{"quality":80,"format":"flv","new_description":"1080P 高清","display_desc":"1080P","superscript":"","codecs":["av01.0.08M.08.0.110.01.01.01.0","avc1.640032"]},{"quality":64,"format":"flv720","new_description":"720P 高清","display_desc":"720P","superscript":"",
"codecs":["av01.0.05M.08.0.110.01.01.01.0","avc1.640028"]},{"quality":32,"format":"flv480","new_description":"480P 清晰","display_desc":"480P","superscript":"","codecs":["av01.0.04M.08.0.110.01.01.01.0","avc1.64001F"]},{"quality":16,"format":"mp4","new_description":"360P 流畅","display_desc":"360P","superscript":"","codecs":["av01.0.01M.08.0.110.01.01.01.0","avc1.64001E"]}],"high_format":null,"volume":{"measured_i":-14.4,"measured_lra":3.6,"measured_tp":0.2,"measured_threshold":-24.4,"target_offset":-0.3,"target_i":-14,"target_tp":-1}},"session":"a5a7c7da81f5dd643af8936ad14d14f8"}

'''

# https://upos-sz-estgoss.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-30080.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=upos&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=ad387b4de423d641dbb3e5f8d11b7b68&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=0,1&agrr=1&bw=28538&logo=80000000

