from machine import Pin
import time

BS_PIN = Pin(3, Pin.IN, Pin.PULL_UP)
led = Pin(2, Pin.OUT)

while True:
    if BS_PIN.value() == 0: 
        led.value(1)
        print(BS_PIN.value())
        print("ON")
    else:
        led.value(0)
        print(BS_PIN.value())
        print("OFF")
 
    time.sleep(0.05)