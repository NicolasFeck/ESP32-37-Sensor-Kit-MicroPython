from machine import Pin
import time

laser = Pin(32, Pin.OUT)

while True:
    laser.value(1)
    print("Laser ON")
    time.sleep(1)
    laser.value(0)
    print("Laser OFF")
    time.sleep(1)
    