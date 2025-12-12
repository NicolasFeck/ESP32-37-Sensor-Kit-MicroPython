from machine import Pin, ADC
import time

sensor_pin = ADC(Pin(34))
sensor_pin.atten(ADC.ATTN_11DB)
led_pin = Pin(2, Pin.OUT)

smoothing_factor = 0.75
previous_filtered_value = 0
max_change = 0

heartbeats = 0
last_heartbeat_time = 0
start_time_count = time.ticks_ms() 
BPM = 0
heartbeat_interval = 250

while True:
    current_value = sensor_pin.read()
    filtered_value = (smoothing_factor * previous_filtered_value) + (1 - smoothing_factor) * current_value
    difference = filtered_value - previous_filtered_value
    previous_filtered_value = filtered_value
    if difference > max_change and (time.ticks_diff(time.ticks_ms(), last_heartbeat_time) > heartbeat_interval):
        max_change = difference
    if difference < 0 and max_change > 15:
        heartbeats += 1
        led_pin.on()
        last_heartbeat_time = time.ticks_ms()
        max_change = 0
    else:
        led_pin.off()

    if time.ticks_diff(time.ticks_ms(), start_time_count) > 15000:
        BPM = heartbeats * 4     
        print(f"{BPM} BPM")
        heartbeats = 0
        start_time_count = time.ticks_ms()

    time.sleep_ms(20)