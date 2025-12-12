from machine import Pin
import time

IR = Pin(32, Pin.OUT)
#Caution: Use a 36 ohm resistor in series with pin 32
led = Pin(2, Pin.OUT)

while True:
    IR.value(1)
    led.value(1)
    print("IR Led ON")
    time.sleep(1)
    
    IR.value(0)
    led.value(0)
    print("IR Led OFF")
    time.sleep(1)z