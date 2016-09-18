#__*__ coding:utf-8 __*__
import pymongo
import json,os

class MongoAction(object):
    def __init__(self):
        pwd=os.getcwd()
        f=open(pwd+"\\config.json","r")
        self.config=json.load(f)
        f.close()

    def dbInsert(self,data):
        try:
            dbclient = pymongo.MongoClient("mongodb://"+self.config["host"]+":"+self.config["port"])
            db=dbclient.ToDoList
            db.authenticate(self.config["user"],self.config["pwd"])
            db.ListInfo.insert(data)
            return True
        except:
            return False

    def dbUpdate(self,data):
        try:
            dbclient = pymongo.MongoClient("mongodb://"+self.config["host"]+":"+self.config["port"])
            db=dbclient.ToDoList
            db.authenticate(self.config["user"],self.config["pwd"])
            db.ListInfo.update(data)
            return True
        except:
            return False
