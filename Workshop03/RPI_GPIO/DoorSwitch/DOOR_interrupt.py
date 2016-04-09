#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 cameron <www.candidcypher.com>
#
# Distributed under terms of the MIT license.

"""
This is basic Python script will print a message when the door switch is
activated.
"""

import time
import RPi.GPIO as io

io.setmode(io.BCM)

door_pin = 19

io.setup(door_pin, io.IN, pull_up_down=io.PUD_DOWN)
# See the guide for more information on Pull up/Pull Down resistors


def doorOpen(DOOR_PIN):
    print("Door Opened @ ", time.ctime())

try:
    io.add_event_detect(door_pin, io.FALLING, callback=doorOpen)
    while 1:
        time.sleep(100)

except KeyboardInterrupt:
    print("Quitting")
    io.cleanup()
