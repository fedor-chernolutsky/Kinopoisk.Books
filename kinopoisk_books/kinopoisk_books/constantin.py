# -*- coding: utf-8 -*-
import os

SECRET_KEY = os.urandom(24)
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://cliff:gomer@localhost/books'
SQLALCHEMY_TRACK_MODIFICATIONS = True
