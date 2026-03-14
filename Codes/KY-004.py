from machine import Pin
import time

button_pin = Pin(3, Pin.IN, Pin.PULL_UP)
led = Pin(2, Pin.OUT)

while True:
    if button_pin.value() == 0: 
        led.value(1)
        print(button_pin.value())
        print("ON")
    else:
        led.value(0)
        print(button_pin.value())
        print("OFF")
 
    time.sleep(0.1)