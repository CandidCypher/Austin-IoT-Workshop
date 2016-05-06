#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 cameron <cameron@default-VirtualBox>
#
# Distributed under terms of the MIT license.

"""
This is the first flask demo for the Austin IoT group
"""

from flask import Flask, render_template

app = Flask(__name__)

list_sensors = ["light", "temp"]

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/sensor/<name>")
def sensor(name):
    if name in list_sensors:
        return render_template("sensor.html", name=name)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
