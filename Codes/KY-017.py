from machine import Pin
import time
#Recommendation: Start the program with the tilt switch open (off position)
TS_PIN = Pin(3, Pin.IN, Pin.PULL_UP)
led = Pin(2, Pin.OUT)

while True:
    if TS_PIN.value() == 0: 
        led.value(1)
        print(TS_PIN.value())
        print("ON")
    else:
        led.value(0)
        print(TS_PIN.value())
        print("OFF")
 
    time.sleep(0.05)