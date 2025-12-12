from machine import ADC, Pin
import time
#It is recommended to calibrate the sensor to adjust it to the working volume level
A0 = ADC(Pin(34))
A0.atten(ADC.ATTN_11DB)
D0 = Pin(32, Pin.IN) 

while True:
    print(f"A0={A0.read()} D0={D0.value()}")
    time.sleep(0.2)