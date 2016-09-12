#!/usr/bin/python
#_*_ coding:utf-8 _*_
"""
@author Lon Chaney
"""
def count():
    name=raw_input("请输入文件名:")
    if len(name)<1:
        name="test.txt"
    f=open(name,'r')
    words=list()
    for line in f:
        words+=line.split()
    return len(words)

print count()
