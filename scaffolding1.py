from machine import Pin, TouchPad
from neopixel import NeoPixel
import time

PIN = 5
NUM_LEDS = 16
ring = NeoPixel(Pin(PIN), NUM_LEDS)
vibration_sensor = Pin(27, Pin.IN)
touch_sensor = TouchPad(Pin(12))

touch_threshold = 100
def set_color(color):
    for i in range(NUM_LEDS):
        ring[i] = color
    ring.write()

def pixel_by_pixel(color):
    for i in range(NUM_LEDS):
        ring[i] = color
        ring.write()
        time.sleep(0.05)

def pulse(color):
    # Fade In
    for brightness in range(0, 256, 5):
        for i in range(NUM_LEDS):
            ring[i] = (
                (brightness * color[0]) // 255,
                (brightness * color[1]) // 255,
                (brightness * color[2]) // 255
            )
        ring.write()
        time.sleep(0.02)

    for brightness in range(255, -1, -5):
        for i in range(NUM_LEDS):
            ring[i] = (
                (brightness * color[0]) // 255,
                (brightness * color[1]) // 255,
                (brightness * color[2]) // 255
            )
        ring.write()
        time.sleep(0.02)

while True:
    vibration = vibration_sensor.value()
    touch = touch_sensor.read() < touch_threshold

    if vibration:
        pixel_by_pixel((175, 10, 0))
        while vibration_sensor.value():  # Keep pulsing while vibration is active
            pulse((175, 10, 0))

    elif touch:
        # Touch Detected -> Blue Pixel by Pixel and Pulse
        pixel_by_pixel((0, 45, 45))
        while touch_sensor.read() < touch_threshold:
            pulse((0, 45, 45))

    else:
        # Default State -> Green
        set_color((0, 130, 10))
