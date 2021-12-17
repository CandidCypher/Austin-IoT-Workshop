# Hello world server in Python
# Binds REP (reply) socket to localhost:5555
# Exects a byte stream "Hello" from client
# replies with a byte stream "World"


import time
import zmq

# Context keeps the list of sockets and manages
# the async IO thead and internal queries.
context = zmq.Context()
socket = context.socket(zmq.REP)
