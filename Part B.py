from machine import Pin, TouchPad, PWM
import time

LED_PUMP = Pin(2, Pin.OUT)
touch_pin = TouchPad(Pin(4))
fadingLED = PWM(LED_PUMP)
# PART B - PUMP
# if touch detected, bulb fades from zero to bright.
threshold = 100
capacitiveValue = 0
LED_PUMP.value(0)
while True:
    capacitiveValue = touch_pin.read()
    if capacitiveValue < threshold:
        fadingLED.freq(500)
        cycle = 0
        while (cycle < 1025):
            fadingLED.duty(cycle)
            time.sleep(0.5)
            cycle = cycle + 64



