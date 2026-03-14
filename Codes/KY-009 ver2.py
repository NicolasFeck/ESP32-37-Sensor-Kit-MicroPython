from machine import Pin, PWM
from time import sleep

#Note: This sensor requires resistors in series before each LED
red_led = PWM(Pin(32), freq=1000) #With a 75 ohm resistor
green_led = PWM(Pin(33), freq=1000) #With a 27 ohm resistor
blue_led = PWM(Pin(25), freq=1000) #With a 27 ohm resistor

def gradient_rgb(pwm_r, pwm_g, pwm_b, max_duty=1023, delay=0.001):
    for duty in range(max_duty + 1):
        pwm_r.duty(max_duty)
        pwm_g.duty(duty)
        pwm_b.duty(0)
        sleep(delay)

    for duty in range(max_duty + 1):
        pwm_r.duty(max_duty - duty)
        pwm_g.duty(max_duty)
        pwm_b.duty(duty)
        sleep(delay)

    for duty in range(max_duty + 1):
        pwm_r.duty(duty)
        pwm_g.duty(max_duty - duty)
        pwm_b.duty(max_duty)
        sleep(delay)

while True:
    gradient_rgb(red_led, green_led, blue_led)