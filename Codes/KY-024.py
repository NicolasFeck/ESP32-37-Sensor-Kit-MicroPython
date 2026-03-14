from machine import Pin, ADC
import time

A0 = ADC(Pin(34))
D0 = Pin(35, Pin.IN)

A0.atten(ADC.ATTN_11DB)

while True:
    analog_value = A0.read()
    digital_value = D0.value()
    
    if digital_value == 1:
        print("Positive magnetic field detected")

    print(f"Analog value: {analog_value}")
    
    time.sleep(0.5)