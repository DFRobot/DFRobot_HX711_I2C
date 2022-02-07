# DFRobot_HX711_I2C
- [中文版](./README_CN.md)

HX711 is a 24-bit A / D converter chip designed for high-precision electronic scales.<br>
This example is suitable for HX711 sensor and read data through Arduino.<br>


![Product Image](./resources/images/KIT0176.png)

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

Provide an Arduino library to get weight by reading data from HX711.

## Installation

To use this library, first download the library file, paste it into the \Arduino\libraries directory, then open the examples folder and run the demo in the folder.

## Methods

```C++
  /*!
   * @fn begin
   * @brief init function
   * @return return 1 if initialization succeeds, otherwise return non-zero and error code.
   */
  int begin(void);
  
  /*!
   * @fn readWeight
   * @brief Get the weight of the object
   * @param times Take the average several times
   * @return return the read weight value, unit: g
   */
  float readWeight(uint8_t times = 12);
  
  /*!
   * @fn getCalibration
   * @brief get calibration value 
   * @return return the read calibration value
   */
  float getCalibration();

  /*!
   * @fn setCalibration
   * @brief Set calibration value
   * @param value the calibration value
   */
  void  setCalibration(float value);

  /*!
   * @fn setThreshold
   * @brief Set the trigger threshold when the weight sensor module is automatically calibrated(g)
   * @param threshold threshold
   */
  void  setThreshold(uint16_t threshold);
  
  /*!
   * @fn setCalWeight
   * @brief Set the calibration weight when the weight sensor module is automatically calibrated(g)
   * @param triWeight   Weight
   */
  void  setCalWeight(uint16_t triWeight);
  
  /*!
   * @fn enableCal
   * @brief Start sensor calibration
   */
  void enableCal();
  
  /*!
   * @fn peel
   * @brief remove the peel
   */
  void peel();
  
  /*!
   * @fn getCalFlag
   * @brief Wait for sensor calibration to complete
   * @return Result 
   * @retval true The calibration completed
   * @retval false The calibration is not complete
   */
  bool getCalFlag();
```

## Compatibility

MCU                | Work Well    | Work Wrong   | Untested    | Remarks
------------------ | :----------: | :----------: | :---------: | -----
Arduino uno        |      √       |              |             | 
FireBeetle-ESP8266        |      √       |              |             | 
FireBeetle-ESP32        |      √       |              |             | 
mpython        |      √       |              |             | 
microbit        |      √       |              |             | 



## History

- 2020/12/31 - Version 1.0.0 released.
## Credits

Written by fengli(li.feng@dfrobot.com), 2020.12.31 (Welcome to our [website](https://www.dfrobot.com/))
