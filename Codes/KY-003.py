from machine import Pin
import time

hall = Pin(36, Pin.IN)

while True:
    if hall.value() == 0:
        print("Magnet detected")
    else:
        print("Without a magnetic field")
    time.sleep(0.2)