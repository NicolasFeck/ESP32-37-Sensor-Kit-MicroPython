from machine import Pin
import time

MS_PIN = Pin(3, Pin.IN, Pin.PULL_UP)
led = Pin(2, Pin.OUT)

while True:
    if MS_PIN.value() == 0: 
        led.value(1)
        print(MS_PIN.value())
        print("ON")
    else:
        led.value(0)
        print(MS_PIN.value())
        print("OFF")
 
    time.sleep(0.05)