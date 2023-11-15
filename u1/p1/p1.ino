void setup() {
  Serial.begin(9600);

}

void loop() {
  float dataF = analogRead(0);
  float dataR = analogRead(1);

  Serial.print("Filtrada:");
  Serial.print(dataR);
  Serial.print(",");
  Serial.print("No_filtrada:");
  Serial.println(dataF);
  
  delay(100);
}
