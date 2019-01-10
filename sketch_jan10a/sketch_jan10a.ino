const int output = 7; 
int data; 

void setup() {
  Serial.begin(9600); 
  pinMode(output, OUTPUT); 
  digitalWrite(output, LOW); 
}

void loop() {
  while(Serial.available()){
    data = Serial.read(); 
  }

  if(data == '1')
  digitalWrite(output, HIGH); 

  else if (data == '0')
  digitalWrite(output, LOW); 
}
