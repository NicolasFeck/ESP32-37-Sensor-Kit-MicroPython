import machine
import onewire
import ds18x20
import time

sensor_pin = 5

#Initialize the OneWire bus and the DS18B20 sensor
datapin = machine.Pin(sensor_pin)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(datapin))

#.scan() searches for the connected sensors (for this example we use only 1)
roms = ds_sensor.scan()
print("Sensors found:", roms)

while True:
    ds_sensor.convert_temp()  #Start temperature conversion
    time.sleep(1)
        
    for rom in roms:
        temp = round(ds_sensor.read_temp(rom), 2)  #Temperature reading with 2-decimal resolution
        print(f"Temperature: {temp}°C")
        
    time.sleep(0.5)