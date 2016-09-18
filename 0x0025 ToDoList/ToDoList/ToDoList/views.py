"""
Routes and views for the flask application.
"""
from datetime import datetime
from flask import *
from mongodbAction import MongoAction
from ToDoList import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/api/test/<int:name>',methods=['POST','GET'])
def test(name=None):
    dbaction=MongoAction.MongoAction()
    return jsonify(dbaction.dbInsert({"name":name,"age":15}))

