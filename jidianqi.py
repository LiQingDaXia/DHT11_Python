#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import RPi.GPIO as GPIO
import time
jidianqi_channel = 15

class JiDianQi(object):
    """JiDianQi CLASS"""
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(jidianqi_channel,GPIO.OUT)
    def On(self):
        GPIO.output(jidianqi_channel,GPIO.HIGH)
    def Off(self):
        GPIO.output(jidianqi_channel,GPIO.LOW)
    def Blink(self):
        self.On()
        time.sleep(1)
        self.Off()
        time.sleep(1)


if __name__ == "__main__":
    try:
        jidianqi = JiDianQi()
        while True:
            jidianqi.Blink()
    except KeyboardInterrupt:
            GPIO.cleanup()
