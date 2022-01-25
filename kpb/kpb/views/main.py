# -*- coding: utf-8 -*-
from kpb import app
from flask import render_template

@app.route('/')
def main():
    return render_template('page.main.html')
