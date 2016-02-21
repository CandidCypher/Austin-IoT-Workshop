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

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
