from machine import Pin
import time

LC1 = Pin(33, Pin.IN, Pin.PULL_UP)  
LC2 = Pin(14, Pin.IN, Pin.PULL_UP)  

LED_SENSOR1_PIN = Pin(32, Pin.OUT) 
LED_SENSOR2_PIN = Pin(27, Pin.OUT) 
LED_ESP32_PIN = Pin(2, Pin.OUT)   

while True:

    print(LC1.value())
    print(LC2.value())
    #Instead of "and" you can use "or" to change the logic of the conditional
    if LC1.value() == 0 and LC2.value() == 0:
        LED_SENSOR1_PIN.value(1)  
        LED_SENSOR2_PIN.value(1)  
        LED_ESP32_PIN.value(1)    
        print("LEDs ON (Both sensors at 0)")
    else:
        LED_SENSOR1_PIN.value(0)  
        LED_SENSOR2_PIN.value(0)  
        LED_ESP32_PIN.value(0)    
        print("LEDs OFF")

    time.sleep(0.5) 