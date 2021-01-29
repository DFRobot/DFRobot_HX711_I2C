# -*- coding:utf-8 -*-
"""
  @file readWeight.py
  @brief Get the weight of the object, press the RST button on the module, the 
  @n program will automatically remove the skin
  @copyright  Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  @licence     The MIT License (MIT)
  @author [fengli](li.feng@dfrobot.com)
  @version  V1.0
  @date  2020-12-26
  @get from https://www.dfrobot.com
  @https://github.com/DFRobot/DFRobot_HX711_I2C
"""
import sys
import time
sys.path.append("../..")
from DFRobot_HX711_I2C import *

IIC_MODE         = 0x01            # default use IIC1
IIC_ADDRESS      = 0x64        # default i2c device address
'''
   # The first  parameter is to select iic0 or iic1
   # The second parameter is the iic device address
'''
hx711 = DFRobot_HX711_I2C(IIC_MODE ,IIC_ADDRESS)
"""
  @brief Initialization function
"""

hx711.begin()

print("start\r\n")
#Manually set the calibration values
hx711.setCalibration(2242.0)
while(1):
  # Get the weight of the object
  data = hx711.readWeight(10)
  print('weight is %.1f g' % data)
  time.sleep(2)
  #hx711.peelFlag();
