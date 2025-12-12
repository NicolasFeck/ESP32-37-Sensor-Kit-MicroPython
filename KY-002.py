from machine import Pin
import time

sensor_pin = Pin(23, Pin.IN, Pin.PULL_UP)
led = Pin(2, Pin.OUT)

while True:
    if sensor_pin.value() == 0:
        print("Vibration detected!")
        led.value(1)
    else:
        print("No vibration")
        led.value(0)
    time.sleep(0.1)  
