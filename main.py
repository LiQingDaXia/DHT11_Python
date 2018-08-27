# -*- coding: utf-8 -*- 
import time
import RPi.GPIO as GPIO
from datetime import datetime

from guangzhaochuanganqi import *
from led import *
from jidianqi import *
from yanwubaojingqi import *

import dht11 as temp

jidianqi = 0
led = 0
guangzhao = 0
yanwu = 0

def init_system():
    global jidianqi,led,guangzhao,yanwu
    jidianqi = JiDianQi()
    led = Led()
    guangzhao = GuangZhao()
    yanwu = YanWu()
    temp.initWenDu()
    print("*"*40)

def main():
    global jidianqi,led,guangzhao,yanwu
    init_system()
    while True:
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print("*"*40)
        wendu,shidu = temp.getWenDu()
        if  26 <= wendu <= 29:
            print("当前温度:"+str(wendu)+" 摄氏度,湿度："+str(shidu)+"%,环境舒适。")
        elif wendu < 26:
            print("当前温度："+str(wendu)+" 摄氏度,湿度："+str(shidu)+"%,太冷了，穿厚点吧！")
        elif wendu >29:
            print("当前温度："+str(wendu)+" 摄氏度,湿度："+str(shidu)+"%,贼热，必须开空调！")
        guangzhaozhi = guangzhao.getIlluminance()
        yanwuzhi = yanwu.getYanWuState()
        if yanwuzhi:
            print("火焰预警正常")
            jidianqi.Off()
        else:
            print("当前位置着火，请紧急灭火")
            while not yanwuzhi:
                  jidianqi.Blink()
                  yanwuzhi = yanwu.getYanWuState()
        if guangzhaozhi < 360:
            led.On()
            guangzhao.displayIlluminance()
            print("光照较暗，已自动开灯")
        else:
            led.Off()
            guangzhao.displayIlluminance()
            print("当前光照适合看书，为节省资源已关灯")
        print("*"*40)
        time.sleep(4)
if __name__ == "main":
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
