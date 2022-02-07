# DFRobot_HX711_I2C
- [中文版](./README_CN.md)

HX711 is a 24-bit A / D converter chip designed for high-precision electronic scales.<br>
This example is suitable for HX711 sensor and read data through Arduino.<br>


![Product Image](../../resources/images/KIT0176.png)

## Product Link (https://www.dfrobot.com/product-2289.html)
    KIT0176: I2C 1Kg Weight Sensor Kit - HX711

## Table of Contents

* [Summary](#summary)
* [Installation](#installation)
* [Methods](#methods)
* [Compatibility](#compatibility)
* [History](#history)
* [Credits](#credits)

## Summary

Provide an raspberrypi library to get weight by reading data from HX711.

## Installation

To use the library, first download it to Raspberry Pi, then open the routines folder. To execute a routine demox.py, type Python demox.py on the command line. For example, the readweight. py routine, you need to type:
```python
python readWeight.py
```
## Methods

```python
  
  def begin(self):
  '''!
    @fn begin
    @brief init function
    @return return 1 if initialization succeeds, otherwise return non-zero and error code.
  '''
  
  def read_weight(self,times):
  '''!
    @fn read_weight
    @brief Get the weight of the object
    @param times Take the average several times
    @return return the read weight value, unit: g
  '''
  
  def get_calibration(self):
  '''!
    @fn get_calibration
    @brief get calibration value 
    @return return the read calibration value
  '''


  def set_calibration(self ,value):
  '''!
    @fn set_calibration
    @brief Set calibration value
    @param value the calibration value
  '''

  def peel_flag(self):
  '''
    @fn peel_flag
    @brief Wait for sensor calibration to complete
    @return Result 
    @retval true The calibration completed
    @retval false The calibration is not complete
  '''
  
  def set_cal_weight(self,triWeight):
  '''!
    @fn set_cal_weight
    @brief Set the calibration weight when the weight sensor module is automatically calibrated(g)
    @param triWeight   Weight
  '''
  
  def set_threshold(self,threshold):
  '''!
    @fn set_threshold
    @brief Set the trigger threshold when the weight sensor module is automatically calibrated(g)
    @param threshold threshold
  '''

  def peel(self):
  '''!
    @fn peel
    @brief remove the peel
  '''
  
  def enable_cal(self):
  '''!
    @fn enable_cal
    @brief Start sensor calibration
  '''

  def get_cal_flag(self):
  '''!
    @fn get_cal_flag
    @brief Wait for sensor calibration to complete
    @return Result 
    @retval true The calibration completed
    @retval false The calibration is not complete
  '''
```

## Compatibility

MCU                | Work Well    | Work Wrong   | Untested    | Remarks
------------------ | :----------: | :----------: | :---------: | -----
Raspberry pi 3       |      √       |              |             | 
Raspberry pi 4       |      √       |              |             | 

* Python Version

| Python  | Work Well | Work Wrong | Untested | Remarks |
| ------- | :--: | :----: | :----: | ---- |
| Python2 |  √   |        |        |      |
| Python3 |  √   |        |        |      |

## History

- 2020/12/31 - Version 1.0.0 released.
## Credits

Written by fengli(li.feng@dfrobot.com), 2020.12.31 (Welcome to our [website](https://www.dfrobot.com/))

