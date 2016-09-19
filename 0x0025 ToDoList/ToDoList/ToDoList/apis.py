from datetime import datetime
from flask import *
import MongoAction
from ToDoList import app

@app.route("/api/ToDoList")
def ToDolist():
    dbAct=MongoAction.MongoAction()
    data=[{"title":"1","description":"this is a test1"},{"title":"2","description":"this is a test2"},{"title":"3","description":"this is a test3"}]
    return jsonify(data)