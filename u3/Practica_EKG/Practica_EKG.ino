void setup(){
  Serial.begin(9600);
  pinMode(10, INPUT);
  pinMode(11, INPUT);
}

void loop(){

  // Serial.println(0) ? (digitalRead(10) == 1) || (digitalRead(11) == 1) : Serial.println(analogRead(A0));

  if ((digitalRead(10) == 1) || (digitalRead(11) == 1))
  {
    Serial.println(0);
  }
  else
  {
    Serial.println(analogRead(A0));
  }
  delay(10);
}