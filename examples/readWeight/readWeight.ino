/*!
 * @file readWeight.ino
 * @brief Get the weight of the object, press the RST button on the module, the 
 * @n program will automatically remove the skin
 * @copyright  Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
 * @License     The MIT License (MIT)
 * @author [fengli](li.feng@dfrobot.com)
 * @version  V1.0
 * @date  2020-12-26
 * @https://github.com/DFRobot/DFRobot_HX711_I2C
*/

#include <DFRobot_HX711_I2C.h>

/*!
 * @brief Constructor 
 * @param pWire I2c controller
 * @param addr  I2C address(0x64/0x65/0x660x67)
 */
//DFRobot_HX711_I2C MyScale(&Wire,/*addr=*/0x64);
DFRobot_HX711_I2C MyScale;

void setup() {
  Serial.begin(9600);
  while (!MyScale.begin()) {
    Serial.println("The initialization of the chip is failed, please confirm whether the chip connection is correct");
    delay(1000);
  }
  //Manually set the calibration values
  MyScale.setCalibration(2236.f);
  //remove the peel
  MyScale.peel();
}

void loop() {
  // Get the weight of the object
  Serial.print("weight is: ");
  Serial.print(MyScale.readWeight(), 1);
  Serial.println(" g");
  delay(1500);
}