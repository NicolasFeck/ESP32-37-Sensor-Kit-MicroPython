from machine import Pin, PWM
from time import sleep

#Caution: Connect each positive pin with resistors in series
red_led = PWM(Pin(21), freq=1000) #With a 100 ohm resistor
green_led = PWM(Pin(22), freq=1000) #With a 100 ohm resistor

def gradient_pwm(pwm1, pwm2, max_duty=1023, delay=0.001):
    #The brightness of the red is increased and the brightness of the green is reduced
    for duty in range(max_duty + 1):  
        pwm1.duty(duty)
        pwm2.duty(max_duty - duty)
        sleep(delay)
    #In this other cycle, the opposite of the previous one happens
    for duty in range(max_duty, -1, -1):  
        pwm1.duty(duty)
        pwm2.duty(max_duty - duty)
        sleep(delay)

while True:
    gradient_pwm(red_led, green_led)