#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 cameron <cowens@austiniot.com>
#
# Distributed under terms of the MIT license.
#
# Description: This Python file runs the Hello World Server on a Raspberry Pi
# and is used in the Austin IoT Workshop for MQTT stuffs.
#

"""

"""

import paho.mqtt.client as mqtt
import time


class HelloWorldViewer():
    """
    Hello World MQTT Viewer Class

    Initializer takes three arguments:
        serverIP addres = IP address of the broker server

        port = broker port

        keepalive = Maximum period in seconds allowed between comms between
                    devices and the broker.
    """
    def __init__(self, broker="localhost", port=1883, keepalive=60):
        self.broker = broker
        self.port = port
        self.keepalive = keepalive
        self.viewer = mqtt.Client()

    def connect(self, topic="Hello_World", userdata, flags, rc):
        self.viewer.connect(self.broker, self.port, self.keepalive)
        print("Connected with result code " + str(rc))
        self.viewer.subscribe(topic)

    def on_message(self, userdata, msg):
        bytesObject = msg.payload
        messageString = bytesObject.decode("UTF-8")
        print("Message recieved on topic "+msg.topic
              + " and payload " + msg.payload.decode("UTF-8"))

    def playback():
        rc = 0
        while rc == 0:
            rc = self.viewer.loop()
