from machine import Pin
import time

sensor = Pin(23, Pin.IN)

while True:
     
    if sensor.value() == 0:
        print("Obstacle detected")
    else:
        print("No obstacles detected")    
    time.sleep(0.2)