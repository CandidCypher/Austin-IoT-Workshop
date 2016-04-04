#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 pi <pi@bumblebee>
#
# Distributed under terms of the MIT license.

"""
This Python Script is to show interrupts on the Pi.
"""

import RPi.GPIO as io
import time

io.setmode(io.BCM)

pir_pin = 26

io.setup(pir_pin, io.IN)

def Motion(PIR_PIN):
    print("Motion Detected @", time.ctime())

print("Starting Motion Services")
time.sleep(1)
print("System is armed")

try:
    io.add_event_detect(pir_pin, io.RISING, callback=Motion)
    while 1:
        time.sleep(100)

except KeyboardInterrupt:
    print("Quitting")
    io.cleanup()
