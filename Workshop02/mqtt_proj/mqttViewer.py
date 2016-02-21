#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 cameron <cameron@default-VirtualBox>
#
# Distributed under terms of the MIT license.

"""
Basic MQTT Viwer Class
"""

import paho.mqtt.client as mqtt


class mqttSubscriber(mqtt.Client):
    def __init__(self, broker="localhost", port=1883, keepalive=60):
        self.subscriber = mqtt.Client()
        self.broker = broker
        self.port = port
        self.keepalive = keepalive

    def connect(self):
        rc = self.subscriber.connect(self.broker, self.port, self.keepalive)
        if rc == 0:
            print("Connection sucessful")
        else:
            print("Connection failed. rc = " + str(rc))

    def subscribe(self, topic="Hello_World"):
        self.subscriber.subscribe(topic)
        rc = 0
        while rc == 0:
            rc = self.subscriber.loop()
