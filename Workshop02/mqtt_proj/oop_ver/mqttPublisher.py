#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 cameron <cowens@austiniot.com>
#
# Distributed under terms of the MIT license.

"""
This creates a  class for publishing a specified message to an mqtt topic
"""

import time
import paho.mqtt.client as mqtt


class mqttPublisher():
    """
    Basic MQTT Publisher Class

    """

    def __init__(self, broker="localhost", port=1883, keepalive=60):
        self.publisher = mqtt.Client()
        self.broker = broker
        self.port = port
        self.keepalive = keepalive

    def connect(self):
        rc = self.publisher.connect(self.broker, self.port, self.keepalive)
        if rc == 0:
            print("Connection sucessful")
        else:
            print("Connection failed. rc = " + str(rc))

    def publish(self, message="Message", topic="Hello_World",
                num_msgs = 10, delay = 1):
        for x in range(num_msgs):
            time.sleep(delay)
            self.publisher.publish(topic, message)
