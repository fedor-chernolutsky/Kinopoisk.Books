# -*- coding: utf-8 -*-
# Execute this in Python Shell and continue working with db object
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://cliff:gomer@localhost/testbooks'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
#
# - - - Теперь вы можете работать с переменной db - - -
#
