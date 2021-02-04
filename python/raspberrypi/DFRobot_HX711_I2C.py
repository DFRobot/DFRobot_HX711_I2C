# -*- coding: utf-8 -*
""" 
  @file DFRobot_HX711_I2C.py
  @brief Define the basic structure of class DFRobot_HX711_I2C 
  @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  @licence     The MIT License (MIT)
  @author [fengli](li.feng@dfrobot.com)
  @version  V1.0
  @date  2021-1-29
  @get from https://www.dfrobot.com
  @url https://github.com/DFRobot/DFRobot_HX711_I2C
"""
import serial
import time
import smbus
import struct

class DFRobot_HX711_I2C(object):


  
  ''' register configuration '''
  I2C_ADDR                   = 0x60
  REG_DATA_GET_RAM_DATA      = 0x66
  REG_DATA_GET_CALIBRATION   = 0x67
  REG_DATA_SET_CALIBRATION   = 0x68
  REG_DATA_GET_PEEL_FLAG     = 0x69
  REG_SET_CAL_THRESHOLD      = 0x71    
  REG_SET_TRIGGER_WEIGHT     = 0x72 
  
  ''' Conversion data '''
  rxbuf      = [0,0,0,0]
  _calibration = 2210.0
  _offset = 0
  #_addr      =  0x50
  #_mode      =  0
  #   idle =    0
  def __init__(self ,bus,address):
    self.i2cbus = smbus.SMBus(bus)
    self._addr = address
    self.idle =    0
  '''
    @brief Module initialization
  '''
  def begin(self):
    self._offset = self.average(20)
    time.sleep(0.05)
    
  '''
    @brief Get the weight of the object
    @param times: Take the average from the number of measurements
    @return  The object weight, (g)
  '''
  def readWeight(self,times):
    value = self.average(times)
    time.sleep(0.05)
    ppFlag = self.peelFlag()
    if ppFlag == 1:
      self._offset = self.average(times)
    elif ppFlag == 2:
      b = self.getCalibration()
      self._calibration = b[0]
    #Serial.println("pppppppppppppppppppppp----------------------");
    #print(value);
    print(self._calibration)
    return ((value - self._offset)/self._calibration) 

   
  '''
    @brief Obtain the automatic calibration value of weight sensor module
    @return Automatic calibration value
  '''
  def getCalibration(self):
      data = self.read_reg(self.REG_DATA_GET_CALIBRATION,4);
      aa= bytearray(data) 
      
      return struct.unpack('>f', aa)

  '''
    @brief Manually set the automatic calibration value
    @param times: the value of Calibration
  '''
  def setCalibration(self ,value):
      self._offset = self.average(15)
      self._calibration = value
  def peelFlag(self):
      data = self.read_reg(self.REG_DATA_GET_PEEL_FLAG,1);
      if(data[0] == 0x01 or data[0] == 129):
        return 1
      elif data[0] == 0x02:
        return 2
      else:
        return 0
  def getValue(self):
      data = self.read_reg(self.REG_DATA_GET_RAM_DATA,4);
      value = 0;
      if(data[0] == 0x12):
        value = (data[1])
        value = ((value << 8) | data[2])
        value = ((value << 8) | data[3])
      else:
        return 0
      return value^0x800000
  '''
    @brief Set calibration weight
    @param times: The calibration weight(g)
  '''
  def setCalWeight(self,triWeight):
   txData = [0,0]
   txData[0] = triWeight >> 8
   txData[1] = triWeight & 0xFF
   self.write_data(self.REG_SET_TRIGGER_WEIGHT)
   self.write_data(txData[0])
   self.write_data(txData[1])
   time.sleep(0.05)
  '''
    @brief Set calibration threshold value, when the calibration weight is greater than this value, sensor calibration will begin
    @param times: The threshold value(g)
  '''
  def setThreshold(self,threshold):
   txData = [0,0]
   txData[0] = threshold >> 8
   txData[1] = threshold & 0xFF
   self.write_data(self.REG_SET_CAL_THRESHOLD)
   self.write_data(txData[0])
   self.write_data(txData[1])
   time.sleep(0.05)
   
  def average(self,times):
    
    sum = 0
    for i in range(times):
        #
        data = self.getValue()
        if data == 0 :
           times = times -1
        else:
           sum = sum + data
    #print(times)
    #print("--------------------------")
    if(times == 0):
       times =1
    return  sum/times
  def peel(self):
    self._offset = self.average(15)
    self.write_data(0x73)
  def enableCal(self):
    time.sleep(0.1)
    self.write_data(0x74)
    time.sleep(0.1)
  def getCalFlag(self):
    ppFlag = self.peelFlag()
    if ppFlag == 2:
      return True
    else:
      return False
  def write_data(self, data):
    self.i2cbus.write_byte(self._addr ,data)
    
  def write_reg(self, reg, data):
    self.i2cbus.write_byte(self._addr ,reg)
    self.i2cbus.write_byte(self._addr ,data)

  def read_reg(self, reg ,len):

    self.i2cbus.write_byte(self._addr,reg)
    time.sleep(0.03)
    for i in range(len):
      #time.sleep(0.03)
      self.rxbuf[i] = self.i2cbus.read_byte(self._addr)
    #print(self.rxbuf)
    return self.rxbuf