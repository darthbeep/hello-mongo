# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from util import helper
import json
import requests
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/find', methods=["GET", "POST"])
def find():
    searchterm = request.form.get('find')
    term = request.form.get('term')
    found = helper.find({term:searchterm})
    for thing in found:
        thing.pop("_id")
        print json.dumps(thing)
        return json.dumps(thing)
    return json.dumps(found)

@app.route('/findall')
def findall():
    al = []
    lst = helper.findall()
    for thing in lst:
        thing.pop("_id")
        al.append(thing)
    return json.dumps(al)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5000, debug=True)
