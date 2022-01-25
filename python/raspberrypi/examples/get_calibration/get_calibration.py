# -*- coding: utf-8 -*-
"""
  @file get_calibration.py
  @brief to get the calibration value of the sensor and to calibrate the sensor before running this program
  @N 1. Press the CAL button on the sensor module first, and the sensor will automatically remove the tare weight. After completion, the CAL indicator will be on
  @n Put a certain mass object (set by set_cal_weight function) within 2.5s, and the indicator light turns off to indicate that the module will start calibration
  @n 3. After the completion of calibration, the indicator flashes 3 times within one second to indicate the completion of calibration
  @N 4. If 100G items are not placed, the indicator light will be extinguished after 5 seconds. This calibration is invalid
  @copyright Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  @License The MIT License (MIT)
  @author [fengli](li.feng@dfrobot.com)
  @ version V1.0
  @date 2020-12-26
  @https://github.com/DFRobot/DFRobot_HX711_I2C
"""
import sys
import time
sys.path.append("../..")
from DFRobot_HX711_I2C import *

IIC_MODE         = 0x01           # default use IIC1
IIC_ADDRESS      = 0x64            # default iic device address
'''
   # The first  parameter is to select iic0 or iic1
   # The second parameter is the iic device address
'''
hx711 = DFRobot_HX711_I2C(IIC_MODE ,IIC_ADDRESS)

time.sleep(0.1)
# Set the trigger threshold (G) for automatic calibration of the weight sensor module. When only the weight of the object on the scale is greater than this value, the module will start the calibration process
# This value cannot be greater than the calibration weight of the set_cal_weight() setting
hx711.set_threshold(50)
# Set the calibration weight when the weight sensor module is automatically calibrated (g)
hx711.set_cal_weight(100)

hx711.enable_cal()
while hx711.get_cal_flag() != 1: 
  time.sleep(1)

print("the calibration value of the sensor is: ")
# Obtain the calibration value. The accurate calibration value can be obtained after the calibration operation is completed
calibration = hx711.get_calibration()
print(calibration[0])
time.sleep(0.1)

