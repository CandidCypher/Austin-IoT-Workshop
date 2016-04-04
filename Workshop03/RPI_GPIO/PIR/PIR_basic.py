#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 cameron <cameron@cameron-Lenovo-ideapad-300-15ISK>
#
# Distributed under terms of the MIT license.

"""
This basic script displays basic messages if the PIR sensor dectects any
motion. This was based off the demo stuff on Adafruit.
"""

import time
import RPi.GPIO as io
io.setmode(io.BCM)

pir_pin = 26

io.setup(pir_pin, io.IN)


while True:
    if io.input(pir_pin):
        print("Motion Detected ", time.ctime())
        time.sleep(1)
    time.sleep(0.5)
