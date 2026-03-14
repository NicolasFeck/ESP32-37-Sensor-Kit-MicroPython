from machine import Pin
import time

buzzer = Pin(27, Pin.OUT) 

while True:
    for i in range(100):
        buzzer.value(1)    
        time.sleep(0.001)
        buzzer.value(0)     
        time.sleep(0.001)

    time.sleep(0.05)

    for j in range(100):
        buzzer.value(1)     
        time.sleep(0.002)
        buzzer.value(0)    
        time.sleep(0.002)

    time.sleep(0.05)