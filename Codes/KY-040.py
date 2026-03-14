from machine import Pin
import time

CLK = Pin(14, Pin.IN, Pin.PULL_UP)
DT  = Pin(12, Pin.IN, Pin.PULL_UP)
SW  = Pin(27, Pin.IN, Pin.PULL_UP)

last_clk = CLK.value()

def check_rotation():
    global last_clk
    
    clk_state = CLK.value()
    dt_state = DT.value()
    
    if clk_state != last_clk:
        if dt_state != clk_state:
            print("Clockwise rotation →")
        else:
            print("Counter-clockwise rotation ←")
    
    last_clk = clk_state

while True:
    check_rotation()
    if SW.value() == 0:
        print("Button pressed")
        time.sleep(0.2)
    time.sleep(0.001)