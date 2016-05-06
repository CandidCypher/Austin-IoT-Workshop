import smbus
import time
import os
import math

# Define a class for the accelerometer readings
class MMA7660():
    bus = smbus.SMBus(1)
    def __init__(self):
        self.bus.write_byte_data(0x4c, 0x07, 0x00) # Setup the Mode
        self.bus.write_byte_data(0x4c, 0x06, 0x10) # Calibrate
        self.bus.write_byte_data(0x4c, 0x08, 0x00) # Calibrate
        self.bus.write_byte_data(0x4c, 0x07, 0x01) # Calibrate
    def getValueX(self):
        return self.bus.read_byte_data(0x4c, 0x00)
    def getValueY(self):
        return self.bus.read_byte_data(0x4c, 0x01)
    def getValueZ(self):
        return self.bus.read_byte_data(0x4c, 0x02)

mma = MMA7660()

for a in range(1000):
    x = mma.getValueX()
    y = mma.getValueY()
    z = mma.getValueZ()
    print("X=", x)
    print("Y=", y)
    print("Z=", z)
    time.sleep(0.2)
    os.system("clear")
