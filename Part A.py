# import whatever
from machine import Pin
import time
road_1 = (15, Pin.IN)

LED1 = Pin(13, Pin.OUT)
LED2 = Pin(12, Pin.OUT)
LED3 = Pin(14, Pin.OUT)

LED4 = Pin(27, Pin.OUT)
LED5 = Pin(26, Pin.OUT)
LED6 = Pin(25, Pin.OUT)

# PART A - ROAD 1
# if vibration detected, LED1.value(1), LED2.value(1)
while True:
    sensorValue = road_1 .value()
    if sensorValue == 1:
        print("Vibration detected!")
        LED1.value(1)
        LED4.value(1)
        time.sleep(0.25)
        LED2.value(1)
        LED5.value(1)
        time.sleep(0.25)
        LED3.value(1)
        LED6.value(1)
        time.sleep(0.25)
    else:
        print("No vibration...")

    time.sleep(0.1)
# time.sleep(0.25)
# LED3.value(1), LED4.value(1)
# and so on
