#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import RPi.GPIO as GPIO
import time
yanwubaojingqi_channel = 13

class YanWu(object):
    """YanWuBaoJingQi CLASS"""
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(yanwubaojingqi_channel,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

    def getYanWuState(self):
        status=GPIO.input(yanwubaojingqi_channel)
        return status

    def judgeYanWu(self):
        if self.getYanWuState(): 
           print ("Everything is OK")      
        else:  
           print ("Dangerous!")

if __name__ == "__main__":
    try:
        yanwu = YanWu()
        while True:
            yanwu.judgeYanWu()
            time.sleep(1)
    except KeyboardInterrupt:
            GPIO.cleanup()
