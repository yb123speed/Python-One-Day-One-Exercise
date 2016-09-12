#!/usr/bin/python
#_*_ coding:utf-8 _*_
"""
图形验证码CAPTCHA
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
#填充每一个点
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=randomColor())
#验证码内容
for t in range(4):
    draw.text((60*t+10,10),randomChar(),fill=randomColor(),font=font)
#模糊
image=image.filter(ImageFilter.BLUR)
#保存
image.save("CAPTCHA.PNG",'png')


