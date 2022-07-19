# -*- coding:utf-8 -*-
"""
作者：Calvin_Lin
日期：2022年07月15日 15:52:52

注意事项：在爬取b站的某个up主的所有视频数据时，
        发现通过 requests.get() 和 通过 webdriver.Chrome对象.get() 获得的数据是不一样的

        并且第一种方法只能获得52条数据就会自动终止，且获得的52条数据排序混乱，
        与 按浏览器 F12 进入（search?mid=6272252&ps=30&tid=0&pn=1&keyword=&order=pubdate&jsonp=jsonp）看到的数据顺序完全不同（部分内容不同）

        而第二种方法因为能模拟浏览器的访问，即使我没加 params 和 headers 也能自由地正常访问，读取的数据就是网页html数据，和 浏览器按 F12 看到的完全一致


"""
import requests
import re
import pandas as pd
import numpy as np
import time
import random
import sys
import io

# from jieba import xrange
from selenium import webdriver
from concurrent.futures import ThreadPoolExecutor

import json

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

# 这里选择保存为tsv文件的原因是：信息中包含英文逗号，导致干扰csv的单元格划分，
# 编码格式选择GBK，因为我们使用excel打开tsv文件，而excel默认是utf-8，会导致中文乱码
# 但是使用GBK在识别第三页第5、6个视频的信息时报错UnicodeEncodeError: 'gbk' codec can't encode character '\xf6' in position 57: illegal multibyte sequence
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding="gb18030")

with open("music_collection_utf_8_Pic_EscapeCharacter_&_And.tsv", "a", encoding="utf-8") as f:
    f.write("'视频标题名称'\\t'网址'\\t'up对音乐的风格分类'\\t'视频简介'" + "\n")

    cnt = 0

    for pn in range(1, 10, 1):  # 视频共9页
        # 设置请求头等参数，防止被反爬
        header = {
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
            # get_user_agent(),
            # "cookie" : "buvid3=372A487D-1542-4470-8C60-2503E21E52AF185004infoc; rpdid=|(u~||uYRuu~0J'uYuJmYJm~Y; LIVE_BUVID=AUTO6016152892965344; fingerprint_s=8b3086c61f86a80218156caae72cedad; sid=jtdev49e; balh_is_closed=; balh_server_inner=__custom__; CURRENT_QUALITY=80; buvid4=C1956CDB-179B-1779-B8F2-6F960E87172A07626-022012513-TDIcPGmL6+DQbqtq+GY7QQ%3D%3D; _uuid=539271F6-6867-D661-66EB-F8BC108623191069010infoc; i-wanna-go-back=-1; buvid_fp_plain=undefined; buvid_fp=7fd288d755e22d4b2add100fa2a001ae; DedeUserID=436357525; DedeUserID__ckMd5=e6f9115234b561c4; SESSDATA=9de81950%2C1661762124%2C40887*31; bili_jct=c2417a4db7989384247d73d6a0e0803a; b_ut=5; fingerprint3=75665b35aecc752028fc8c91dd13ab4b; fingerprint=7fd288d755e22d4b2add100fa2a001ae; nostalgia_conf=-1; CURRENT_BLACKGAP=0; blackside_state=0; bp_video_offset_436357525=682315405562216400; CURRENT_FNVAL=4048; innersign=1; b_lsid=EF28275D_181FFCEEFBF; b_timer=%7B%22ffp%22%3A%7B%22333.1007.fp.risk_372A487D%22%3A%22181FF7C03BD%22%2C%22333.788.fp.risk_372A487D%22%3A%22181FFC2F808%22%2C%22333.999.fp.risk_372A487D%22%3A%22181FFC29045%22%2C%22333.337.fp.risk_372A487D%22%3A%22181FFBC49BF%22%2C%22777.5.0.0.fp.risk_372A487D%22%3A%22181FFBE8A8B%22%2C%22888.2421.fp.risk_372A487D%22%3A%22181FFE5F541%22%7D%7D; PVID=1"
        }

        # 获取源代码
        url = "https://api.bilibili.com/x/space/arc/search"
        param = {
            #     mid=6272252&ps=30&tid=0&pn=1&keyword=&order=pubdate&jsonp=jsonp
            "mid": 6272252,
            "ps": 30,
            "tid": 0,
            "pn": str(pn),
            "keyword": 0,
            "order": "pubdate",
            "jsonp": "jsonp"
        }

        url_str = url + "?mid=6272252&ps=30&tid=0&pn=" + str(pn) + "&keyword=&order=pubdate&jsonp=jsonp"

        chromedriver = "E:\ANACONDA\chromedriver"
        bro = webdriver.Chrome(chromedriver)  # 初始化浏览器窗口对象
        bro.get(url_str)  # 进入网页

        time.sleep(3)  # 模拟鼠标滚轮滚动网页（在这里没啥用）
        bro.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        # time.sleep(2)
        # bro.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        # time.sleep(1)
        # bro.execute_script('window.scrollTo(0, document.body.scrollHeight)')

        resp = requests.get(url=url, params=param, headers=header, verify=False)  # verify=False 去掉安全验证

        # 输出中文乱码的解决方法
        # print(resp.encoding)
        # print(requests.utils.get_encodings_from_content(resp.text)[0])  # requests 去猜测获取的文本编码格式
        resp.encoding = "utf-8"

        time.sleep(1)

        resp.close()
        print("第" + str(pn) +"页数据：")
        print("resp.text\n")
        # print(resp.text)
        # print(type(resp.text))
        # print(type(resp))
        print("\n\n")
        print("bro.page_source")
        print(bro.page_source)
        # print(type(bro.page_source))
        # print(type(bro))
        print("\n\n\n")


        # obj_bro = re.compile(r'"vlist":\[(.*?)]}', re.S)

        bro_str = re.search(r'"vlist":\[(.*?)]}', bro.page_source, re.S).group().strip('"vlist":\["')
        print(bro_str)

        # bro_str = obj_bro.finditer(bro.page_source)
        # for it in bro_str:
        #     cut = it.group("comment")
        #     print(cut)

        # 视频标题名称
        obj_title = re.compile(r'"title":"(?P<title>.*?)","', re.S)   #  () 用来分组  其中 ?P<title> 表示该分组名字是 title
        title = obj_title.finditer(bro_str)

        # for tit in title:   # title 是可迭代对象 <class 'callable_iterator'>
        #     print(tit.group("title"))  # group() 用来提出分组截获的字符串

        # 网址+该视频的b站番号
        obj_web = re.compile(r'"bvid":"(?P<bvid>.*?)","', re.S)
        web = obj_web.finditer(bro_str)

        # for w in web:   # web 是可迭代对象 <class 'callable_iterator'>
        #     print(w.group("bvid"))  # group() 用来提出分组截获的字符串


        # up对音乐的风格分类  (第九页一个小问题，有一个视频不是按照这个规则归类的)
        obj_styles = re.compile(r'"title":"【(?P<style>.*?)】', re.S)
        styles = obj_styles.finditer(bro_str)

        # for st in styles:
        #     print(st.group("style"))

        ## 乐曲的图片封面
        obj_pic = re.compile(r'"play":(.*?),"pic":"(?P<pic>.*?)","', re.S)
        pic = obj_pic.finditer(bro_str)

        ## 由于乐曲的作者、成曲时间等部分信息不是在每一个视频里都有，所以直接统计description
        obj_desc = re.compile(r'"description":"(?P<description>.*?)","', re.S)
        description = obj_desc.finditer(bro_str)

        # for des in description:
        #     print(des.group("description"))




        print("text")

        print(type(title))

        title_lst = []

        # 成功存储 可迭代对象 <class 'callable_iterator'>
        # for tit in title:
        #     print(tit.group("title"))
        #     title_lst.append((tit.group("title")))
        # print(title_lst)

        # len(title)  # 报错
        # print(xrange(title))  # xrange好像只能转为int类型， 并且xrange是python2的内置函数，python3已经没有了
        # print(type(xrange(title)))
        # title_lst = list(title)
        # print(title_lst)

        # next(title)

        # for tit in title:  # title 是可迭代对象 <class 'callable_iterator'>
        #     print(next(tit))  # group() 用来提出分组截获的字符串

        # for w in web:  # web 是可迭代对象 <class 'callable_iterator'>
        #     print(w.group("bvid"))  # group() 用来提出分组截获的字符串
        #
        # for st in styles:
        #     print(st.group("style"))
        #
        # for des in description:
        #     print(des.group("description"))

        # for tit, w in title, web:
        #     print(tit)

        # list = bro.json()   # 报错  AttributeError: 'str' object has no attribute 'json'

        lst = []
        for tit, w, st, des, pi in zip(title, web, styles, description, pic):   # python多个迭代对象变量循环，要把被迭代对象用zip封装，否则报错ValueError: not enough values to unpack (expected 2, got 0)
            # print(tit.group("title"))   # 似乎这个迭代对象在一次循环内被操作了就会清空
            # print("https://www.bilibili.com/video/" + w.group("bvid"))
            # print(st.group("style"))
            # print(des.group("description"))

            tmp = []
            tmp.append((tit.group("title")).replace('\\"', ';').replace(r"\u0026", "And"))

            tmp.append("https://www.bilibili.com/video/" + w.group("bvid"))
            tmp.append(st.group("style").replace(r"\u0026", "And"))
            tmp.append(pi.group("pic"))
            tmp.append(des.group("description").replace(r"\u0026", "And"))

            lst.append(tmp)

            for ite in tmp:
                f.write(ite + '\t')
            f.write("\n")

        # print(lst)


print("over!!!")
