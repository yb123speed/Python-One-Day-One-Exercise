#!/usr/bin/python
#_*_ coding:utf-8 _*_
"""
“¿¿µMySQL-Python
@author Lon Chaney
"""
import MySQLdb
try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='',port=3306)
    cur=conn.cursor()
    cur.execute('create database if not exists codes')
    conn.select_db('codes')
    cur.execute('create table if not exists activation_code (id int not null auto_increment primary key,code varchar(50))')
    with open('codebyrandom.txt','r') as f:
        codes=f.readlines()
        for code in codes:
            cur.execute("insert into activation_code (code) values ('%s')" % str(code))

    cur.close()
    conn.commit()
    conn.close()
    print "Success"
except:
    print "Unable to finish this action"
