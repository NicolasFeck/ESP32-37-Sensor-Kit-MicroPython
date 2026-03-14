from machine import Pin
import time

ir_receiver = Pin(33, Pin.IN)  

while True:
    if ir_receiver.value() == 0:
        print("IR signal detected")
    else:
        print("No IR signal")
    time.sleep(0.02)