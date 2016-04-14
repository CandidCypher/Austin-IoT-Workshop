#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 pi <pi@bumblebee>
#
# Distributed under terms of the MIT license.

"""
This is a basic publisher that will send messages to the Node MCU
every X seconds.
"""

import paho.mqtt.client as mqtt
import time

publisher = mqtt.Client()

rc = publisher.connect("localhost", 1883, 60)
if rc == 0:
    print("Connection Successful")
else:
    print("Connection failed with: ", rc)

rc = 0
while rc == 0:
    rc = publisher.loop()
    publisher.publish("BlinkTopic/", "Blink")
    print("Blink")
    time.sleep(3)
