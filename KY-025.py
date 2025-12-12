from machine import Pin, ADC
import time

A0 = ADC(Pin(34))
D0 = Pin(35, Pin.IN)
A0.atten(ADC.ATTN_11DB)

while True:
    digital_value = D0.value()
    analog_value = A0.read()
        
    if digital_value == 1:
        print("Digital Output: Magnet detected!")
    else:
        print("Digital Output: No magnet detected.")
            
    print(f"Analog value: {analog_value}")
    
    time.sleep(1)