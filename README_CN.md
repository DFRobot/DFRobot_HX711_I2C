# DFRobot_HX711_I2C
- [English Version](./README.md)

HX711是一款为高精度电子秤设计的24位a / D转换芯片。
本示例适用于HX711传感器，通过Arduino读取数据。


![Product Image](./resources/images/KIT0176.png)

## 产品链接 (https://www.dfrobot.com.cn/goods-3128.html)
     KIT0176: I2C 1Kg Weight Sensor Kit - HX711
	 
## 目录

  * [概述](#概述)
  * [库安装](#库安装)
  * [方法](#方法)
  * [兼容性](#兼容性)
  * [历史](#历史)
  * [创作者](#创作者)
## 概述
提供一个Arduino库，通过从HX711读取数据来获得质量。

## 库安装

要使用这个库，首先下载库文件，将其粘贴到\Arduino\libraries目录中，然后打开示例文件夹并在文件夹中运行演示程序。

## 方法
```C++
  /*!
   * @fn begin
   * @brief 初始化
   * @return 1(初始化成功)
   */
  int begin(void);
  
  /*!
   * @fn readWeight
   * @brief 获取称上面的物体的重量
   * @param times 次数(多此测量取平均值)
   * @return 物体重量, 单位: g
   */
  float readWeight(uint8_t times = 12);
  
  /*!
   * @fn getCalibration
   * @brief 获取校准值 
   * @return 返回校准值
   */
  float getCalibration();

  /*!
   * @fn setCalibration
   * @brief 设置校准值
   * @param value 校准值
   */
  void  setCalibration(float value);

  /*!
   * @fn setThreshold
   * @brief 设置自动触发校准的阈值
   * @param threshold 阈值
   */
  void  setThreshold(uint16_t threshold);
  
  /*!
   * @fn setCalWeight
   * @brief 重量传感器模块自动校准时设置校准重量(g)
   * @param triWeight   重量值
   */
  void  setCalWeight(uint16_t triWeight);
  
  /*!
   * @fn enableCal
   * @brief 开始传感器校准
   */
  void enableCal();
  
  /*!
   * @fn peel
   * @brief 去皮
   */
  void peel();
  
  /*!
   * @fn getCalFlag
   * @brief 获取校准是否完成信号
   * @return 结果
   * @retval true 完成
   * @retval false 未完成
   */
  bool getCalFlag();
```

## 兼容性

MCU                | Work Well    | Work Wrong   | Untested    | Remarks
------------------ | :----------: | :----------: | :---------: | -----
Arduino Uno        |      √       |              |             | 
Mega2560        |      √       |              |             | 
Leonardo        |      √       |              |             | 
ESP32        |      √       |              |             | 
ESP8266        |      √       |              |             | 
M0        |      √       |              |             | 


## 历史

- 2020/12/31 - Version 1.0.0 released.

## 创作者

Written by fengli(li.feng@dfrobot.com), 2020.12.31 (Welcome to our [website](https://www.dfrobot.com/))
