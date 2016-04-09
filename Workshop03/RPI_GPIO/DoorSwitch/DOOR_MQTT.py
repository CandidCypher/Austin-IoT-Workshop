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

import paho.mqtt.client as mqtt
import RPi.GPIO as io
import time

io.setmode(io.BCM)

################################
## Setting up GPIO Pins
################################
door_pin = 19


def doorOpen(DOOR_PIN):
    message = "Door Opened @ " + str(time.ctime())
    print(message)
    publisher.publish("DOOR_Motion/Front", message)


###############################
## Setting MQTT Portion
##############################

publisher = mqtt.Client()


##############################
## Starting up Security system service
##############################

print("Starting Motion Services")
print("Connecting to motion capture server")
rc = publisher.connect("localhost", 1883)
if rc == 0:
    print("Connection Successfull")
else:
    print("Connection failed with rc = ", rc)

publisher.publish("DOOR_Motion", "Joining system")
time.sleep(1)
print("System is armed")

rc = 0
while rc == 0:
    rc = publisher.loop()
    try:
        io.add_event_detect(door_pin, io.FALLING, callback=doorOpen)
        while 1:
            time.sleep(100)

    except KeyboardInterrupt:
        print("Quitting")
        io.cleanup()
