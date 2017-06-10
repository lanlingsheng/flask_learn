# -*- coding: utf-8 -*-
__author__ = 'lenovo'
from flask import Flask
from flask import request
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_script import Manager

app = Flask(__name__)

manager = Manager(app)
boostrap = Bootstrap(app)

@app.route('/')
def index():
    #user_agent = request.headers.get('User-Agent')
    #return '<h1>Your Brower is %s<h1>' %user_agent
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    #return '<h1>Hello, %s<h1>' % name
    return render_template('user.html', name = name)

if __name__ =='__main__':
    app.run(debug=True)