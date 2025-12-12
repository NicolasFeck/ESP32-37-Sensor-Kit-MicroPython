from machine import Pin, ADC
import time

joystick_x = Pin(34) #X-axis
joystick_y = Pin(35) #Y-axis
button_pin = Pin(32, Pin.IN, Pin.PULL_UP)

adc_x = ADC(joystick_x)
adc_y = ADC(joystick_y)

adc_x.atten(ADC.ATTN_11DB)
adc_y.atten(ADC.ATTN_11DB)

while True:
    value_x = adc_x.read()
    value_y = adc_y.read()
    button_state = button_pin.value()

    print(f"X:{value_x},Y:{value_y},Button:{button_state}")

    time.sleep(0.5)