from machine import Pin
import time

sensor = Pin(32, Pin.IN)
#The middle pin should be connected to 3.3V
led = Pin(2, Pin.OUT)

while True:
    status = sensor.value()
    if status == 0:
        print("No object")
        led.value(0)
    else:
        print("Object detected")
        led.value(1)
        
    time.sleep(0.1)