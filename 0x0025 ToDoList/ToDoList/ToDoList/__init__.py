﻿"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import ToDoList.views
import ToDoList.apis