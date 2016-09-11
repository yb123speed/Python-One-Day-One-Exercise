# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 19:59:44 2016

@author: Lon Chaney
"""

"""
将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
Pillow：Python Imaging Library
PIL.ImageDraw.Draw.text(xy, text, fill=None, font=None, anchor=None)
"""
from PIL import Image,ImageDraw,ImageFont

original_avatar='original.jpg'
saved_avatar='new_avatar.jpg'
windows_font='arial.ttf'
color=(255,0,0)

def draw_text(text,fill_color,windows_font):
    try:
        img=Image.open(original_avatar)
        x,y=img.size
        print "The size of avatar is : "
        print(img.format,img.size,img.mode)
        #img.show()
        draw=ImageDraw.Draw(img)
        font=ImageFont.truetype(windows_font,100)
        draw.text((x-100,7),text,fill_color,font)
        img.save(saved_avatar)
        img.show()
        
    except:
        print "Unable to load image."
        
        
if __name__=="__main__":
    #number=str(raw_input('please input your number:'))
    number=str(4)
    draw_text(number,color,windows_font)
        
        
