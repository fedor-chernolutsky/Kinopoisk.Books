# -*- coding: utf-8 -*-
from kinopoisk_books import db


class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode(200), nullable=False)
    description = db.Column(db.UnicodeText)
    big_description = db.Column(db.UnicodeText)
    author = db.Column(db.Unicode(200))
    release = db.Column(db.Date)
    release_year_only = db.Column(db.Boolean)  # известен лишь год издания
    filmed = db.Column(db.Boolean)
    genre = db.Column(db.Unicode(200))  # todo: использовать enum с видами жанров
    country = db.Column(db.Unicode(200))  # todo: использовать enum со странами
    age_restriction = db.Column(db.SmallInteger)  # todo: использовать enum с разными возрастными ограничениями
    rating = db.Column(db.SmallInteger)  # todo: обдумать способ обновления рейтинга при оценивании книги
    original = db.Column(db.Unicode(200))
    coverart = db.Column(db.Unicode(200))
    banner = db.Column(db.Unicode(200))
    publishinghouse = db.Column(db.Unicode(200))  # todo: использовать enum с именами издательств

    def __repr__(self):
        return '< #%d %s >' % (self.id, self.title)
