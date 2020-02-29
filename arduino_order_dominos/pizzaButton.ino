int switchState = 0; 
int incomingByte = 0; 

void setup() {
  pinMode(2, INPUT); 
  pinMode(4, OUTPUT); 
  Serial.begin(9600); 

}

void loop() {
  switchState = digitalRead(2); 
  if (Serial.available()> 0)
  {
    incomingByte = Serial.read();
  }

  if(switchState == HIGH)
  {
    Serial.println("1\n"); 
    digitalWrite(4, HIGH); 
  }
  else
  {
    digitalWrite(4, LOW); 
  }

  if(incomingByte == '1')
  {
     digitalWrite(4, HIGH); 
  }

}
