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

front_pir = 26
back_pir = 13
io.setup(front_pir, io.IN)
io.setup(back_pir, io.IN)

def front_Motion(PIR_PIN):
    print("Front Motion Detected @", time.ctime())


def back_Motion(PIR_PIN):
    print("Back Motion Detected @", time.ctime())

print("Starting Motion Services")
time.sleep(1)
print("System is armed")

try:
    io.add_event_detect(front_pir, io.RISING, callback=front_Motion)
    io.add_event_detect(back_pir, io.RISING, callback=back_Motion)
    while 1:
        time.sleep(100)

except KeyboardInterrupt:
    print("Quitting")
    io.cleanup()
