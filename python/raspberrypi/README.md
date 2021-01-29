# HX711-raspberrypi
HX711 is a 24-bit A / D converter chip designed for high-precision electronic scales.<br>
This example is suitable for HX711 sensor and read data through raspberrypi.<br>


## DFRobot_HX711_I2C Library for raspberrypi
---------------------------------------------------------

Provide an raspberrypi library to get weight by reading data from HX711.

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



## Methods

```python
  
  '''
    @brief Module initialization
  '''
  def begin():
  
  '''
    @brief Get the weight of the object
    @param times: Take the average from the number of measurements
    @return  The object weight, (g)
  '''
  def readWeight(self ,times):

  '''
    @brief Obtain the automatic calibration value of weight sensor module
    @return Automatic calibration value
  '''
  def getCalibration(self):

  '''
    @brief Manually set the automatic calibration value
    @param times: the value of Calibration
  '''
  def setCalibration(self,value):
  
  '''
    @brief Set calibration weight
    @param times: The calibration weight(g)
  '''
  def setCalWeight(self,triWeight):
  
  '''
    @brief Set calibration threshold value, when the calibration weight is greater than this value, sensor calibration will begin
    @param times: The threshold value(g)
  '''
  def setThreshold(self,threshold):
```

## Compatibility

MCU                | Work Well    | Work Wrong   | Untested    | Remarks
------------------ | :----------: | :----------: | :---------: | -----
Raspberry pi 3       |      √       |              |             | 
Raspberry pi 4       |      √       |              |             | 


## History

- data 2020-12-31
- version V1.0


## Credits

Written by(li.feng@dfrobot.com), 2020. (Welcome to our [website](https://www.dfrobot.com/))
