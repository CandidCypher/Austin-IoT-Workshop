#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 pi <pi@bumblebee>
#
# Distributed under terms of the MIT license.

"""
This is a basic python scrip that subscribes to a specific mqtt topic and
displays messages posted to said topic.
"""

import paho.mqtt.client as mqtt

#define callback used for "on_message"

def on_message(client, userdata, message):
    print("Message recieved: " + message.payload.decode("UTF-8"))

subscriber = mqtt.Client()
subscriber.on_message = on_message

rc = subscriber.connect("localhost", 1883)
if rc == 0:
    print("Connection Successful")
else:
    print("Connection Failed!!")
subscriber.subscribe("/Doors")

rc = 0
print("Running")
while rc == 0:
    rc = subscriber.loop()
