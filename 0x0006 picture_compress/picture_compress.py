#!/usr/bin/python
#_*_ coding:utf-8 _*_
"""
第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
图片压缩
@author Lon Chaney
"""
from PIL import Image
import os

def pic_compress(image):
        im=Image.open(image)
        w,h=im.size
        if h>1136 or w>640 :
            th=h/1136
            tw=w/640
            ts=max(th,tw)
            nh=int(h/ts)
            nw=int(w/ts)
            im.thumbnail((nh,nw))
            #im.resize((nh,nw))
            im.save(image.split('.')[0]+"resized."+image.split('.')[1])
            print "success"
        else:
            print "no need to resize."

if __name__=="__main__":
    path="c:\\Images"
    for url in os.listdir(path):
        picurl=os.path.join(path,url)
        pic_compress(picurl)
