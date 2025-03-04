from machine import Pin
from time import sleep

vibration_sensor = Pin(15, Pin.IN)
while True:
    vibration_detected = vibration_sensor.value()
    if vibration_detected:
        print("OUCH!!!")

    else:
        print("Challenge me!")
sleep(0.1)

