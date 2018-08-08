#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask
app = Flask(__name__) # instanciate the app object !
# app.debug = True
@app.route('/')
def index():
    return "Coucou !"

# app.secret_key = '2d9-E2.)f&é,A$p@fpa+zSU03êû9_'

@app.route('/contact/')
def contact():
    # mail = "jean@bon.fr"
    tel = "01 23 45 67 89"
    return "Mail: {} --- Tel: {}".format(mail, tel)


if __name__ == '__main__':
    app.run(debug=True)