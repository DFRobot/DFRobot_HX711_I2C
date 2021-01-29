/*!
 * @file DFRobot_HX711_I2C.h
 * @brief Define the basic structure of class DFRobot_HX711_I2C 
 * @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
 * @licence     The MIT License (MIT)
 * @author [fengli](li.feng@dfrobot.com)
 * @version  V1.0
 * @date  2020-12-23
 * @get from https://www.dfrobot.com
 * @https://github.com/DFRobot/DFRobot_HX711_I2C
 */

#ifndef DFROBOT_HX711_I2C_H
#define DFROBOT_HX711_I2C_H
#if ARDUINO >= 100
 #include "Arduino.h"
#else
 #include "WProgram.h"
#endif
#include <Wire.h>

//#define ENABLE_DBG

#ifdef ENABLE_DBG
#define DBG(...) {Serial.print("["); Serial.print(__FUNCTION__); Serial.print("(): "); Serial.print(__LINE__); Serial.print(" ] "); Serial.println(__VA_ARGS__);}
#else
#define DBG(...)
#endif

#define HX711_I2C_ADDR  (0x64)  /*sensor IIC address*/

//#define ERR_OK             0      //ok
//#define ERR_DATA_BUS      -1      //error in data bus
//#define ERR_IC_VERSION    -2      //chip version mismatch

class DFRobot_HX711_I2C
{
public:
  #define REG_DATA_GET_RAM_DATA       0x66     /*Get sensor raw data*/
  #define REG_DATA_GET_CALIBRATION    0x67     /*Gets the automatic calibration value*/
  #define REG_DATA_GET_PEEL_FLAG      0x69     /*Obtain peeling position*/
  #define REG_DATA_INIT_SENSOR        0x70     /*Module initialization*/
  #define REG_SET_CAL_THRESHOLD       0x71     /*Set the calibration trigger threshold*/
  #define REG_SET_TRIGGER_WEIGHT      0x72     /*Set calibration weight*/
  /*!
   * @brief Constructor 
   * @param pWire I2c controller
   * @param addr  I2C address(0x64/0x65/0x660x67)
   */
  DFRobot_HX711_I2C(TwoWire * pWire = &Wire,uint8_t addr = HX711_I2C_ADDR);
  
  /**
   * @brief init function
   * @return Return 1 if initialization succeeds, otherwise return non-zero and error code.
   */
  int begin(void);
  
  /**
   * @brief Get the weight of the object
   * @param times Take the average several times
   * @return Return the read weight value, unit: g
   */
  float readWeight(uint8_t times = 12);
  
  /**
   * @brief get calibration value 
   * @return return the read calibration value
   */
  float getCalibration();

  /**
   * @brief Set calibration value
   * @param value
   * @return return the read calibration value
   */
  void  setCalibration(float value);

  /**
   * @brief Set the trigger threshold when the weight sensor module is automatically calibrated(g)
   * @param threshold
   */
  void  setThreshold(uint16_t threshold);
  
  /**
   * @brief Set the calibration weight when the weight sensor module is automatically calibrated(g)
   * @param triWeight 
   */
  void  setCalWeight(uint16_t triWeight);
private:
  long getValue();
  uint8_t peelFlag();
  long average(uint8_t times = 10);
  /**
   * @brief Write command into sensor chip 
   * @param reg
   * @param data  Data included in command
   * @param size  The number of the byte of command
   */
    int readReg(uint8_t reg,uint8_t * data ,size_t size);
  /**
   * @brief Write command into sensor chip 
   * @param reg  
   * @param data  Data included in command
   * @param size  The number of the byte of command
   */
    uint8_t  writeReg(uint8_t reg,const void *data,size_t size);   
    uint8_t _address;
    uint8_t pFlag = 0;
    long _offset;
    TwoWire *_pWire;
    float _calibration = 2236.0f;
    
};
#endif