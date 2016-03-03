#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 pi <pi@bumblebee>
#
# Distributed under terms of the MIT license.

"""
This is a demo mqtt publisher script that publishes messages to
a specified topic at a specified interval
"""

import paho.mqtt.client as mqtt
import time

#Create an instance of an mqtt Client
publisher = mqtt.Client()

rc = publisher.connect("localhost", 1883, 60)
if rc == 0:
    print("Connection Suscessfull")
else:
    print("Connection failed")

publisher.publish("Hello/World", "Joining dialog")
print("Joining")

rc = 0
while rc == 0:
    rc = publisher.loop()
    publisher.publish("Hello/World", "Message @" + str(time.ctime()))
    print("Published message")
    time.sleep(1)
