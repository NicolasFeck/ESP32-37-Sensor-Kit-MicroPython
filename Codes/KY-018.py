from machine import Pin, ADC
from time import sleep

adc = ADC(Pin(34))
adc.atten(ADC.ATTN_11DB) 

while True:
    light_value = adc.read()
        
    print(f"Analog value: {light_value}")   
        
    if light_value < 500:
        print("State: Darkness")
    elif light_value < 3000:
        print("State: Dim light")
    else:
        print("State: Bright light")
        
    sleep(0.5)