from machine import Pin
import time

#Note: This sensor requires resistors in series before each LED
red = Pin(32, Pin.OUT) #With a 75 ohm resistor
green = Pin(33, Pin.OUT) #With a 27 ohm resistor
blue = Pin(25, Pin.OUT) #With a 27 ohm resistor
delay = 1

while True:
    red.value(1)
    time.sleep(delay)
    green.value(1)
    time.sleep(delay)
    blue.value(1)
    time.sleep(delay)
    red.value(0)
    time.sleep(delay)
    green.value(0)
    time.sleep(delay)
    blue.value(0)
    time.sleep(delay)