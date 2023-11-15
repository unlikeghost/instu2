#include <Wire.h>
#include "MAX30105.h"

MAX30105 particleSensor;

void setup() {

  Serial.begin(9600);

  if (particleSensor.begin(Wire, I2C_SPEED_FAST) == false) { //Use default I2C port, 400kHz speed
    Serial.println("MAX30102 was not found. Please check wiring/power. ");
    while (1);
  }

  particleSensor.setup(0); //Configura el sensor y apaga LEDs

  particleSensor.enableDIETEMPRDY(); //Habilita el interrumpir tempready
}

void loop() {
  float temperature = particleSensor.readTemperature();

  Serial.println(temperature);
  delay (10);
}
