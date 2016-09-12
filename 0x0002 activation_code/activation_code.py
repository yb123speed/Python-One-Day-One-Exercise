#!/usr/bin python
# _*_ coding:utf-8 _*_
"""
@author: Lon Chaney
"""
import random,uuid,md5,hashlib
#method_1 uuid
for i in range(0,200,1):
    code=uuid.uuid1()
    file=open('codesbyuuid.txt','a')
    file.write(str(i)+'\t'+str(code)+'\n')
    file.close()
    print str(i)+'\t'+str(code)+'\n'

#method_2 random
st='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
for x in range(0,200,1):
    code1=''
    for y in range(0,10):
        code1+=random.choice(st)    
    file1=open('codebyrandom.txt','a')
    file1.write(code1+'\n')
    file1.close()

#method_3 MD5
#1.md5
m=md5.new()
for x in range(0,200,1):
    code2=''
    for y in range(0,10):
        code2+=random.choice(st)
    m.update(code1)
    file1=open('codebymd5.txt','a')
    file1.write(m.hexdigest()+'\n')
    file1.close()
#2.hashlib.md5
m1=hashlib.md5()
for x in range(0,200,1):
    code3=''
    for y in range(0,10):
        code3+=random.choice(st)
    m1.update(code1)
    file1=open('codebyhashmd5.txt','a')
    file1.write(m1.hexdigest()+'\n')
    file1.close()





