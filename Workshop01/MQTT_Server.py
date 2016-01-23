#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 cameron <www.CandidCypher.com>
#
# Distributed under terms of the MIT license.

"""
This Python Module is the Hello World MQTT Publisher
developed for the Austin IoT Workshops.

Author: Cameron Owens
Date: 1/22/2016

Description: This Python script publishes a generic message on the topic
            'hello/world'
"""

# Importing of Modules
import paho.mqtt.client as mqtt
import time


mqttpublisher = mqtt.Client()
mqttpublisher.connect("localhost", 1883, 60)
mqttpublisher.publish("hello/world", "Initial Publish")


# Main loop
rc = 0
while rc == 0:
    rc = mqttpublisher.loop()
    mqttpublisher.publish("hello/world", "Hello World")
    time.sleep(1)
