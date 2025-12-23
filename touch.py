#!/usr/bin/env python3
import time
from adafruit_crickit import crickit

RGB = dict(red=0xFF0000, green=0x00FF00, blue=0x0000FF)
POLL_DELAY = 0.1

# LED brightness
crickit.onboard_pixel.brightness = 0.01

# Program runs in an infinite loop
while True:
    # check whether the sensor is being touched and
    # set the throttle accordingly.
    throttle1 = 1 if crickit.touch_1.value else 0  # motor 1
    color = RGB['red'] if crickit.touch_1.value | crickit.touch_2.value else RGB['blue']

    throttle2 = 1 if crickit.touch_2.value else 0  # motor 2

    # Apply to motors and LED
    crickit.onboard_pixel.fill(color)
    crickit.dc_motor_1.throttle = throttle1
    crickit.dc_motor_2.throttle = throttle2

    # Sleep POLL_DELAY seconds before next interation
    time.sleep(POLL_DELAY)
