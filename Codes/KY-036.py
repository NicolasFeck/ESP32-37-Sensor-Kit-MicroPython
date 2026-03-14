from machine import Pin, ADC
import time

A0 = ADC(Pin(34))
D0 = Pin(35, Pin.IN)
A0.atten(ADC.ATTN_11DB)

while True:
    print(f"Analog value: {A0.read()}")
    if D0.value() == 1:
        print("Touched")
    else:
        print("Untouched")
    time.sleep(0.1)