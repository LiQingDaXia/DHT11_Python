#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import RPi.GPIO as GPIO
import time
led_channel = 11

class Led(object):
    """LED CLASS"""
    def __init__(self):
         GPIO.setmode(GPIO.BOARD)
         GPIO.setup(led_channel,GPIO.OUT)
    def On(self):
         GPIO.output(led_channel,GPIO.HIGH)
    def Off(self):
         GPIO.output(led_channel,GPIO.LOW)


if __name__ == "__main__":
    try:
        led = Led()
        while True:
            led.On()
            time.sleep(1)
            led.Off()
            time.sleep(1)
    except KeyboardInterrupt:
            GPIO.cleanup()