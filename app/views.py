#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: GreenJedi
# @Date:   2018-01-31 12:40:10
# @Last Modified by:   JJLasher
# @Last Modified time: 2018-01-31 13:12:49
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html")
