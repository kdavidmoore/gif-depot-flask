#!/usr/bin/env python

from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/search/')
@app.route('/search/<query>')
def search(query=None):
    params = { 'q': query }
    params.update({ 'api_key': 'dc6zaTOxFJmzC' })
    r = requests.get('http://api.giphy.com/v1/gifs/search', params=params)
    json = r.json()
    return render_template('search.html', results=json['data'])

