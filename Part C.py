# import whatever
# initialise variables...
# vibration sensors, Pin.IN x2
# LED on road, Pin.OUT      x6
# LED on pump, Pin.OUT      x1
# touch sensor on pump      x1
# LED on traffic light      x2
from machine import Pin
import time

road_2 = (2, Pin.IN)

LED_GREEN = Pin(34, Pin.OUT)
LED_RED = Pin(35, Pin.OUT)
# PART C - ROAD 2
# if vibration detected, LED red on for 2 sec
while True:
    sensorValue = road_2.value()
    if sensorValue == 1:
        print("Vibration detected!")
        LED_RED.value(1)
        time.sleep(2)
        LED_RED.value(0)
        LED_GREEN.value(1)
        time.sleep(2)
        LED_GREEN.value(0)
    else:
        LED_GREEN.value(0)
        LED_RED.value(0)
# then LED green
# then it stops
