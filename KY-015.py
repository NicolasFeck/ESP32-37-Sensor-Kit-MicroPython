from machine import Pin
import time
import dht

sensor = dht.DHT11(Pin(22))

while True:
    sensor.measure()        
    
    temp = sensor.temperature()  #In degrees Celsius
    hum = sensor.humidity() #In percentage %
    
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {hum}%")
    time.sleep(1)