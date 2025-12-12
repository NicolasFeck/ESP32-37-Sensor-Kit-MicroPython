from machine import ADC, Pin
import time
import math

A0 = ADC(Pin(34))
D0 = Pin(32, Pin.IN)
A0.atten(ADC.ATTN_11DB)

BETA = 3950 
R0 = 10000
T0 = 298.15
VCC = 3.3   #Supply voltage
R_SERIE = 10000 #Fixed resistance in the divider (10kΩ)

def read_temperature():
    value = A0.read()
    
    #Convert to voltage
    v_out = (value / 4095) * VCC
    
    #Calculate NTC resistance
    if v_out == 0:  #Avoid division by zero
        return None
    r_ntc = R_SERIE * (v_out / (VCC - v_out))

    #Calculate temperature using the Beta equation
    temp_k = 1 / (1/T0 + (1/BETA) * math.log(r_ntc / R0))
    temp_c = temp_k - 273.15
    
    return temp_c

while True:
    digital_value = D0.value()
    raw_temp = read_temperature()
    
    if raw_temp is not None:
        temp = round(raw_temp) #Round to integer
        print(f"Temperature: {temp}°C")
    else:
        print("Error")
        
    print(f"Digital value: {digital_value}")
    time.sleep(1)