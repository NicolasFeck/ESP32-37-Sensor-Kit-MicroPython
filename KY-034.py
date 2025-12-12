from machine import Pin

led = Pin(21, Pin.OUT)
#The lighting effect is handled by the integrated LED.
led.value(1)