/*!
 * @file getCalibration.ino
 * @brief to get the calibration value of the sensor and to calibrate the sensor before running this program
 * @N 1. Press the CAL button on the sensor module first, and the sensor will automatically remove the tare weight. After completion, the CAL indicator will be on
 * @n Put a certain mass object (set by setcalWeight function) within 2.5s, and the indicator light turns off to indicate that the module will start calibration
 * @n 3. After the completion of calibration, the indicator flashes 3 times within one second to indicate the completion of calibration
 * @N 4. If 100G items are not placed, the indicator light will be extinguished after 5 seconds. This calibration is invalid
 * @copyright Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
 * @License The MIT License (MIT)
 * @author [fengli](li.feng@dfrobot.com)
 * @ version V1.0
 * @date 2020-12-26
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
  // Set the calibration weight when the weight sensor module is automatically calibrated (g)
  MyScale.setCalWeight(100);
  // Set the trigger threshold (G) for automatic calibration of the weight sensor module. When only the weight of the object on the scale is greater than this value, the module will start the calibration process
  // This value cannot be greater than the calibration weight of the setCalWeight() setting
  MyScale.setThreshold(50);
  
  
  delay(2000);
  //Start sensor calibration
  MyScale.enableCal();
  long time1 = millis();
  //Wait for sensor calibration to complete
  while(!MyScale.getCalFlag()){
       delay(1000);
       if((millis()-time1) > 7000){ 
          Serial.println("Calibration failed, no weight was detected on the scale");
          delay(2000);
       }
  }
  // Obtain the calibration value. The accurate calibration value can be obtained after the calibration operation is completed
  Serial.print("the calibration value of the sensor is: ");
  Serial.println(MyScale.getCalibration());
  //MyScale.setCalibration(MyScale.getCalibration());
  delay(1000);
}

void loop() {
  /*
  Serial.print("weight is: ");
  Serial.print(MyScale.readWeight(), 1);
  Serial.println(" g");
  delay(1000);
  */
}