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

io.setup(door_pin, io.IN, pull_up_down=io.PUD_DOWN)


def doorOpen(DOOR_PIN):
    open_message = "Door Opened @ " + str(time.ctime())
    close_message = "Door Closed @ " +str(time.ctime())
    state = io.input(DOOR_PIN)
    if (state == 0):
        print(open_message)
        publisher.publish("DOOR_Motion/Front", open_message)
    elif (state == 1):
        print(close_message)
        publisher.publish("DOOR_Motion/Front", close_message)



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
        io.add_event_detect(door_pin, io.BOTH, callback=doorOpen)
        while 1:
            time.sleep(100)

    except KeyboardInterrupt:
        print("Quitting")
        io.cleanup()
