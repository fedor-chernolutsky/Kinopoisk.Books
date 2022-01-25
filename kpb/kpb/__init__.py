# -*- coding: utf-8 -*-
from kpb import constantin

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = constantin.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = constantin.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = constantin.SQLALCHEMY_TRACK_MODIFICATIONS

db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)

from kpb.models.book import Book

from kpb.views import main
