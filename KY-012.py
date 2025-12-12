from machine import Pin
import time

buzzer = Pin(27, Pin.OUT)
led = Pin(2, Pin.OUT)

while True:
    print("Buzzer ON")
    buzzer.value(1)
    led.value(1)
    time.sleep(0.5)
    print("Buzzer OFF")
    buzzer.value(0)
    led.value(0)
    time.sleep(0.5)