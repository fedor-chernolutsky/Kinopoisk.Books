# -*- coding: utf-8 -*-
from kinopoisk_books import constantin

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='templates', static_folder="/")
app.config['SECRET_KEY'] = constantin.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = constantin.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = constantin.SQLALCHEMY_TRACK_MODIFICATIONS

db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)

from kinopoisk_books.models.book import Book

from kinopoisk_books.views import index
