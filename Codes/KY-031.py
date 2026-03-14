from machine import Pin
import time

sensor_pin = Pin(23, Pin.IN, Pin.PULL_UP)

while True:
    if sensor_pin.value() == 0:
        print("TAP detected!")
    else:
        print("Not detected")
    time.sleep(0.1)
