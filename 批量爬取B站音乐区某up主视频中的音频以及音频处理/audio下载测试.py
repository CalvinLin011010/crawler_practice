# -*- coding:utf-8 -*-
"""
作者：Calvin_Lin
日期：2022年07月16日 11:22:13
"""

import re
import time
import random

import requests
import os

def get_user_agent():
    '''获取随机用户代理'''
    user_agents = [
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
        "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
        "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1",
        "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36",
        "Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20",
        "Mozilla/5.0 (Linux;u;Android 4.2.2;zh-cn;) AppleWebKit/534.46 (KHTML,like Gecko) Version/5.1 Mobile Safari/10600.6.3 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
        "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html）"
    ]
    # 在user_agent列表中随机产生一个代理，作为模拟的浏览器
    user_agent = random.choice(user_agents)
    return user_agent

url = "https://www.bilibili.com/video/BV1Ts411p7Gb"

header = {
    # 'Accept': '*/*',
    # 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
    # get_user_agent(),
    # "cookie" : "buvid3=372A487D-1542-4470-8C60-2503E21E52AF185004infoc; rpdid=|(u~||uYRuu~0J'uYuJmYJm~Y; LIVE_BUVID=AUTO6016152892965344; fingerprint_s=8b3086c61f86a80218156caae72cedad; sid=jtdev49e; balh_is_closed=; balh_server_inner=__custom__; CURRENT_QUALITY=80; buvid4=C1956CDB-179B-1779-B8F2-6F960E87172A07626-022012513-TDIcPGmL6+DQbqtq+GY7QQ%3D%3D; _uuid=539271F6-6867-D661-66EB-F8BC108623191069010infoc; i-wanna-go-back=-1; buvid_fp_plain=undefined; buvid_fp=7fd288d755e22d4b2add100fa2a001ae; DedeUserID=436357525; DedeUserID__ckMd5=e6f9115234b561c4; SESSDATA=9de81950%2C1661762124%2C40887*31; bili_jct=c2417a4db7989384247d73d6a0e0803a; b_ut=5; fingerprint3=75665b35aecc752028fc8c91dd13ab4b; fingerprint=7fd288d755e22d4b2add100fa2a001ae; nostalgia_conf=-1; CURRENT_BLACKGAP=0; blackside_state=0; bp_video_offset_436357525=682315405562216400; CURRENT_FNVAL=4048; innersign=1; b_lsid=EF28275D_181FFCEEFBF; b_timer=%7B%22ffp%22%3A%7B%22333.1007.fp.risk_372A487D%22%3A%22181FF7C03BD%22%2C%22333.788.fp.risk_372A487D%22%3A%22181FFC2F808%22%2C%22333.999.fp.risk_372A487D%22%3A%22181FFC29045%22%2C%22333.337.fp.risk_372A487D%22%3A%22181FFBC49BF%22%2C%22777.5.0.0.fp.risk_372A487D%22%3A%22181FFBE8A8B%22%2C%22888.2421.fp.risk_372A487D%22%3A%22181FFE5F541%22%7D%7D; PVID=1"
    "referer": url
}


"""
我们在第一步发送网络请求中，headers请求头中有一个参数referer，这个参数我们一般称为防盗链。这里一定要添加referer。
如果headers请求头中不加referer参数，将会有可能报如下的错误

format mov,mp4,m4a,3gp,3g2,mj2 detected only with low score of 1, misdetection possible...
moov atom not found...
...

错误意思简单来说就是无法拼接已经损坏或无内容的纯音频和纯视频，很显然我们没有下载到视频音频。
那么问题来了，明明一切很合乎常理，为什么会没有下载到视频音频呢。这里就和referer防盗链有关。
referer防盗链是一种简单的反爬机制，用来标识这个请求是从哪个页面发过来的，服务器可以拿到这一信息并做相应的处理，
例如做来源统计、防盗处理等，假如没加防盗链，服务器就可能认为你的请求属于爬虫发送的，服务器就不给出响应。



"""

response = requests.get(url, headers=header)
html = response.text
time.sleep(2)
print(html)
response.close()

obj_info = re.compile(r"<script>window\.__playinfo__={(?P<info>.*?)</script>", re.S)
info = obj_info.findall(html)[0]
print(info)

# 从html（js）页面中获取音频和视频的url
video_url = re.findall(r'"video":.*?,"baseUrl":"(.*?)","', info)[0]
audio_url = re.findall(r'"audio":.*?,"baseUrl":"(.*?)",', info)[0]
print("video_url:")
print(video_url)
print("audio_url:")
print(audio_url)

# 下载
video = requests.get(video_url, headers=header)
audio = requests.get(audio_url, headers=header)

# with open("test_video" + ".mp4", "wb") as f:
#     f.write(video.content)
with open("test_audio" + ".mp3", mode="wb") as f:
    f.write(audio.content)

time.sleep(3)
video.close()
audio.close()






print("over!!!")

# video_url = "https://upos-sz-estgoss.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-30080.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=upos&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=ad387b4de423d641dbb3e5f8d11b7b68&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=0,1&agrr=1&bw=28538&logo=80000000"
# video = requests.get(video_url, headers=header)
# video_data = video.content
# time.sleep(2)
# with open("write_test_video.mp4","wb") as f:
#     f.write(video_data)
# video.close()


# time.sleep(3)
# audio_url = "https://upos-sz-estgoss.bilivideo.com/upgcxcode/97/49/757504997/757504997-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1657947987&gen=playurlv2&os=upos&oi=3746048989&trid=06ccc2620870480faeb0fb2a26df1688u&mid=436357525&platform=pc&upsig=0cc27525d62fee411bed026fe78464fc&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=0,1&agrr=1&bw=39900&logo=80000000"
# audio = requests.get(audio_url,headers=header)
# audio_data = audio.content
# with open("write_test_audio.mp3","wb") as f:
#     f.write(audio_data)
# audio.close()
