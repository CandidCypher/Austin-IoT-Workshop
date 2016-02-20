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


class HelloWorldPublish():
    """
    Hello World Publisher Class

    Initializer takes four arguments
    """
    def __init__(self, broker="localhost", port=1883, keepalive=60):
        self.broker = broker
        self.port = port
        self.keepalive = keepalive
        self.publisher = mqtt.Client()
        rc = 0

    def connect(topic="Hello_World", rc):
        self.publisher.connect(self.broker, self.port, self.keepalive)
        print("Connected with result code " + str(rc))
        self.publisher.publish(topic, "Joining system")

    def publish(num_messages=10, message="Hello from publisher"):
        for x in range(num_messages):
            self.publisher.publish(topic, message)
