#!/usr/bin/python
#_*_ coding:utf-8 _*_
"""
依赖pymongo
@author Lon Chaney
"""
import pymongo

try:
    dbclient = pymongo.MongoClient('mongodb://root:111111@115.28.18.230:27017')
    db = dbclient.codes
    with open('codebyrandom.txt','r') as f:
        keys = f.readlines()
        index = 1
        for key in keys:
            print key
            db.things.insert({"id":index,"key":key})
            index = index + 1
    print "Action Success!"
except:
    print "Unable to finish this action!"

