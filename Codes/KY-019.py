from machine import Pin
import time

led = Pin(2, Pin.OUT)
activator = Pin(4, Pin.OUT)

while True:
    activator.value(1)
    led.value(1)
    print("Relay ON")
    
    time.sleep(1)
    
    activator.value(0)
    led.value(0)
    print("Relay OFF")
    
    time.sleep(1)