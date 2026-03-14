from machine import ADC, Pin
import time
import math

thermistor = ADC(Pin(34))
thermistor.atten(ADC.ATTN_11DB)

R1 = 10000  #10kΩ fixed resistor
c1 = 0.001129148
c2 = 0.000234125
c3 = 0.0000000876741  #Steinhart-Hart coefficients

while True:
    Vo = thermistor.read()  #Read ADC value (0-4095)

    #Calculate the thermistor resistance
    R2 = (R1 * Vo) / (4095 - Vo)

    #Applying Steinhart-Hart
    logR2 = math.log(R2)
    T = 1.0 / (c1 + c2 * logR2 + c3 * logR2**3) #Kelvin
    T = round(T - 273.15, 1) #Celsius. The "round" in this case leaves only 1 decimal place

    print(f"Temperature: {T}°C")
    time.sleep(0.5)