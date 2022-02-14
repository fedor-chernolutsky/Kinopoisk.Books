# -*- coding: utf-8 -*-
from kinopoisk_books import app
from flask import render_template, redirect
from kinopoisk_books.models.book import Book

@app.route('/')
def index():
    ## Главная страница ##
    # Очень необходимо продумать все алгоритмы, определяющие что именно
    #   будет предлагаться пользователю - то есть  выводиться на главной странице.
    # Пока все функции `filter`, `order_by` и тд выполнены в своём начальном
    #   виде, скорее для демонстрации
    banner_book = Book.query.filter(Book.banner != None).order_by(Book.release).first()
    return render_template('page.index.html', banner_book=banner_book)
