# ! /usr/bin/env python
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

# Create an instance of an mqtt Client
publisher = mqtt.Client()

rc = publisher.connect("localhost", 1883, 60)
if rc == 0:
    print("Connection Suscessfull")
else:
    print("Connection failed")

print("Joining")

rc = 0
while rc == 0:
    rc = publisher.loop()
    publisher.publish("/color", "RED")
    print("RED")
    time.sleep(5)
    publisher.publish("/color", "GREEN")
    print("GREEN")
    time.sleep(5)
    publisher.publish("/color", "BLUE")
    print("BLUE")
    time.sleep(5)
