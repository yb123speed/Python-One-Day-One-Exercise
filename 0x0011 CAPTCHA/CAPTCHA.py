#!/usr/bin/python
#_*_ coding:utf-8 _*_
"""
ͼ����֤��CAPTCHA
@author Lon Chaney
"""
import random
from PIL import Image,ImageDraw, ImageFont, ImageFilter

def randomChar():
    return chr(random.randint(65,90))

#random color
def randomColor():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

width=240
height=40
image=Image.new("RGB",(width,height),(255,255,255))
font=ImageFont.truetype("arial.ttf",36)
draw=ImageDraw.Draw(image)
#���ÿһ����
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=randomColor())
#��֤������
for t in range(4):
    draw.text((60*t+10,10),randomChar(),fill=randomColor(),font=font)
#ģ��
image=image.filter(ImageFilter.BLUR)
#����
image.save("CAPTCHA.PNG",'png')


