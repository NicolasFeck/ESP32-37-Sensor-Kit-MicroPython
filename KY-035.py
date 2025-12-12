from machine import ADC, Pin
import time

hall = ADC(Pin(34))
hall.atten(ADC.ATTN_11DB)
VCC = 3.3 

while True:
    value = hall.read()
    voltage = round((value / 4095) * VCC, 2)

    print(f"A0 = {value} | Voltage = {voltage} V")
    time.sleep(0.5)