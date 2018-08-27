#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import smbus
import time

class GuangZhao(object):

   def __init__(self):
       #BH1750地址
       self.__DEV_ADDR=0x23
       #BH1750控制字
       self.__CMD_PWR_OFF=0x00  #关机
       self.__CMD_PWR_ON=0x01   #开机
       self.__CMD_RESET=0x07    #重置
       self.__CMD_CHRES=0x10    #持续高分辨率检测
       self.__CMD_CHRES2=0x11   #持续高分辨率模式2检测
       self.__CMD_CLHRES=0x13   #持续低分辨率检测
       self.__CMD_THRES=0x20    #一次高分辨率
       self.__CMD_THRES2=0x21   #一次高分辨率模式2
       self.__CMD_TLRES=0x23    #一次分辨率
       self.__CMD_SEN100H=0x42  #灵敏度100%,高位
       self.__CMD_SEN100L=0X65  #灵敏度100%，低位
       self.__CMD_SEN50H=0x44   #50%
       self.__CMD_SEN50L=0x6A   #50%
       self.__CMD_SEN200H=0x41  #200%
       self.__CMD_SEN200L=0x73  #200%
       self.guangqiangBus=smbus.SMBus(1)
       self.guangqiangBus.write_byte(self.__DEV_ADDR,self.__CMD_PWR_ON)
       self.guangqiangBus.write_byte(self.__DEV_ADDR,self.__CMD_RESET)
       self.guangqiangBus.write_byte(self.__DEV_ADDR,self.__CMD_SEN100H)
       self.guangqiangBus.write_byte(self.__DEV_ADDR,self.__CMD_SEN100L)
       self.guangqiangBus.write_byte(self.__DEV_ADDR,self.__CMD_PWR_OFF)

   def getIlluminance(self):
       self.guangqiangBus.write_byte(self.__DEV_ADDR,self.__CMD_PWR_ON)
       self.guangqiangBus.write_byte(self.__DEV_ADDR,self.__CMD_THRES2)
       time.sleep(0.2)
       res=self.guangqiangBus.read_word_data(self.__DEV_ADDR,0)
       #read_word_data
       res=((res>>8)&0xff)|(res<<8)&0xff00
       res=round(res/(2*1.2),2)
       #result="GuangZhaoQiangDu: "+str(res)"lx"
       #self.guangqiangBus.write_byte(__DEV_ADDR,__CMD_PWR_OFF)
       return res

   def displayIlluminance(self):
       shuzhi = "当前环境光照值为: "+str(self.getIlluminance())+"lx"
       #shuzhi = "GuangZhaoQiangDu: "+str(self.getIlluminance())+"lx"
       print(shuzhi)

if __name__ == "__main__":
    try:
        guangzhao = GuangZhao()
        while True:
            guangzhao.displayIlluminance()
    except KeyboardInterrupt:
            guangzhao.guangqiangBus.write_byte(0x23,0x00)
