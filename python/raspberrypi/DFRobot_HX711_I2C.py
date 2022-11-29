# -*- coding: utf-8 -*
""" 
  @file DFRobot_HX711_I2C.py
  @brief Define the basic structure of class DFRobot_HX711_I2C 
  @details By a simple mechanical structure with the sensor, that can be read to the mass of the body
  @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  @License     The MIT License (MIT)
  @author [fengli](li.feng@dfrobot.com)
  @version  V1.0
  @date  2021-1-29
  @url https://github.com/DFRobot/DFRobot_HX711_I2C
"""
import serial
import time
import smbus
import struct

class DFRobot_HX711_I2C(object):


  
  ''' register configuration '''
  I2C_ADDR                   = 0x60  #Get sensor raw data
  REG_DATA_GET_RAM_DATA      = 0x66  #Get sensor raw data
  REG_DATA_GET_CALIBRATION   = 0x67  #Gets the automatic calibration value
  REG_DATA_SET_CALIBRATION   = 0x68  #Obtain peeling position
  REG_DATA_GET_PEEL_FLAG     = 0x69  #Module initialization
  REG_SET_CAL_THRESHOLD      = 0x71  #Set the calibration trigger threshold
  REG_SET_TRIGGER_WEIGHT     = 0x72  #Set calibration weight
  
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

  def begin(self):
    '''!
      @fn begin
      @brief init function
      @return return 1 if initialization succeeds, otherwise return non-zero and error code.
    '''
    self._offset = self.average(20)
    time.sleep(0.05)
    

  def read_weight(self,times):
    '''!
      @fn read_weight
      @brief Get the weight of the object
      @param times Take the average several times
      @return return the read weight value, unit: g
    '''
    value = self.average(times)
    time.sleep(0.05)
    ppFlag = self.peel_flag()
    if ppFlag == 1:
      self._offset = self.average(times)
    elif ppFlag == 2:
      b = self.getCalibration()
      self._calibration = b[0]
    #Serial.println("pppppppppppppppppppppp----------------------");
    #print(value);
    print(self._calibration)
    return ((value - self._offset)/self._calibration) 

   

  def get_calibration(self):
      '''!
        @fn get_calibration
        @brief get calibration value 
        @return return the read calibration value
      '''
      data = self.read_reg(self.REG_DATA_GET_CALIBRATION,4);
      aa= bytearray(data) 
      
      return struct.unpack('>f', aa)


  def set_calibration(self ,value):
      '''!
        @fn set_calibration
        @brief Set calibration value
        @param value the calibration value
      '''
      self._offset = self.average(15)
      self._calibration = value
  '''
    @fn peel_flag
    @brief Wait for sensor calibration to complete
    @return Result 
    @retval true The calibration completed
    @retval false The calibration is not complete
  '''
  def peel_flag(self):
      data = self.read_reg(self.REG_DATA_GET_PEEL_FLAG,1);
      if(data[0] == 0x01 or data[0] == 129):
        return 1
      elif data[0] == 0x02:
        return 2
      else:
        return 0
        
  def get_value(self):
      data = self.read_reg(self.REG_DATA_GET_RAM_DATA,4);
      value = 0;
      if(data[0] == 0x12):
        value = (data[1])
        value = ((value << 8) | data[2])
        value = ((value << 8) | data[3])
      else:
        return 0
      return value^0x800000

  def set_cal_weight(self,triWeight):
   '''!
     @fn set_cal_weight
     @brief Set the calibration weight when the weight sensor module is automatically calibrated(g)
     @param triWeight   Weight
   '''
   txData = [0,0]
   txData[0] = triWeight >> 8
   txData[1] = triWeight & 0xFF
   self.write_data(self.REG_SET_TRIGGER_WEIGHT)
   self.write_data(txData[0])
   self.write_data(txData[1])
   time.sleep(0.05)
  

  def set_threshold(self,threshold):
   '''!
     @fn set_threshold
     @brief Set the trigger threshold when the weight sensor module is automatically calibrated(g)
     @param threshold threshold
   '''
   txData = [0,0]
   txData[0] = threshold >> 8
   txData[1] = threshold & 0xFF
   self.write_data(self.REG_SET_CAL_THRESHOLD)
   self.write_data(txData[0])
   self.write_data(txData[1])
   time.sleep(0.05)

  def peel(self):
    '''!
      @fn peel
      @brief remove the peel
    '''
    self._offset = self.average(15)
    self.write_data(0x73)

  def enable_cal(self):
    '''!
      @fn enable_cal
      @brief Start sensor calibration
    '''
    time.sleep(0.1)
    self.write_data(0x74)
    time.sleep(0.1)

  def get_cal_flag(self):
    '''!
      @fn get_cal_flag
      @brief Wait for sensor calibration to complete
      @return Result 
      @retval true The calibration completed
      @retval false The calibration is not complete
    '''
    ppFlag = self.peel_flag()
    if ppFlag == 2:
      return True
    else:
      return False
      
  def average(self,times):
    
    sum = 0
    for i in range(times):
        #
        data = self.get_value()
        if data == 0 :
           times = times -1
        else:
           sum = sum + data
    #print(times)
    #print("--------------------------")
    if(times == 0):
       times =1
    return  sum/times



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