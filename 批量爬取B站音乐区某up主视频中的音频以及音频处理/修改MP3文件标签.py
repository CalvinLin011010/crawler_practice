# -*- coding:utf-8 -*-
"""
作者：Calvin_Lin
日期：2022年07月16日 16:50:30

收集的注意事项：
Python3.根据ID3v2批量修改mp3文件名_碎积云-程序员ITS201__https://its201.com/article/modabao/106188640
很多中文歌曲的信息编码为GBK，但标记为ISO-8859-1，好在ISO-8859-1似乎是GBK的子集，于是所有ISO-8859-1编码的字节我都用GBK来解码



ID3v2 中文文档 (版本 2.3.0)_DREAMER -程序员ITS201_id3v2___ https://its201.com/article/u011208567/9261311


WinHex————用于查看任意文件的二进制内容

https://its201.com/article/qq_36923771/122425190



"""

from mutagen.id3 import ID3, APIC, TIT2, TPE1, TALB
import os

# def get_mp3(mp3path):
#     mp3_list = []
#     for dirs, dirnames, files in os.walk(mp3path):
#         for file in files:
#             if file.endswith('.mp3'):
#                 mp3_list.append(dirs+'/'+file)
#     return mp3_list
#
#
# def SetMp3Info(mp3file, info):
#     songFile = ID3(mp3file)
#     songFile['APIC'] = APIC(  # 插入封面
#         encoding=3,
#         mime='image/jpeg',
#         type=3,
#         desc=u'Cover',
#         data=info['picData']
#     )
#     songFile['TIT2'] = TIT2(  # 插入歌名
#         encoding=3,
#         text=info['title']
#     )
#     songFile['TPE1'] = TPE1(  # 插入第一演奏家、歌手、等
#         encoding=3,
#         text=info['artist']
#     )
#     songFile['TALB'] = TALB(  # 插入专辑名
#         encoding=3,
#         text=info['album']
#     )
#     songFile.save()


# with open("music1.mp3", "rb") as f:
#     print(f.read().hex()) # 十六进制读取二进制比特数据
#

# 使用pydub
from pydub import AudioSegment
from pydub.playback import play
from imageio.plugins import ffmpeg

'''
format | 示例: "aif" | 默认: "mp3" 输出文件的格式。 原生支持 "wav"和 "raw",需要 ffmpeg 以支持其他的所有格式. "raw" 文件需要三个额外的关键字参数, sample_width, frame_rate, 和 channels, 用以下表述: raw only。这些额外信息之所以需要，是因为原始音频文件不像WAV文件那样拥有一个自身信息的文件头。
sample_width | 示例: 2 raw only — 用 1 表示 8-bit 音频， 2 表示 16-bit (CD品质) and 4 表示 32-bit。这是每种取样的字节数。
channels | 示例: 1 raw only — 1 表示单声道, 2 表示双声道。
frame_rate | 示例: 2 raw only — 也称为采样率, 其值一般为 44100 (44.1kHz - CD音频), 或是 48000 (48kHz - DVD音频)
'''

sound = AudioSegment.from_file("music1.mp3", frame_rate=44100, channels=2, sample_width=2) # , frame_rate=44100, channels=2, sample_width=2
# ffmpeg.probe(sound)


file_handle = sound.export("output_sample_bitrate_320k.mp3",
                            format="mp3",
                            bitrate="320k",
                            cover="music1.jpg"
                           )


############# 最后3个问题
## 1. 下载图片并编号
## 2. 用pydub打开下载的音乐并把封面加上
## 3. 加入description











