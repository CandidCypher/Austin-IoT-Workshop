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
front_pir = 26
back_pir = 13
io.setup(front_pir, io.IN)
io.setup(back_pir, io.IN)

def front_Motion(PIR_PIN):
    print("Front Motion Detected @", time.ctime())
    publisher.publish("PIR_Motion/Front", "Motion Detected @ "
                      + str(time.ctime()))

def back_Motion(PIR_PIN):
    print("Back Motion Detected @", time.ctime())
    publisher.publish("PIR_Motion/Back", "Motion Detected @ "
                      + str(time.ctime()))

###############################
## Setting MQTT Portion
##############################

publisher = mqtt.Client()


##############################
## Starting up Security system service
##############################

print("Starting Motion Services")
print("Connecting to motion capture server")
rc = publisher.connect("odin.local", 1883)
if rc == 0:
    print("Connection Successfull")
else:
    print("Connection failed with rc = ", rc)

publisher.publish("PIR_Motion", "Joining system")
time.sleep(1)
print("System is armed")

rc = 0
while rc == 0:
    rc = publisher.loop()
    try:
        io.add_event_detect(front_pir, io.RISING, callback=front_Motion)
        io.add_event_detect(back_pir, io.RISING, callback=back_Motion)
        while 1:
            time.sleep(1)

    except KeyboardInterrupt:
        print("Quitting")
        io.cleanup()
