const int buttonBoi = 2;

void setup() {
  pinMode(buttonBoi, INPUT);
  
  Serial.begin(9600);
  Serial.setTimeout(100);
}

void loop() {
  String inputString = Serial.readString();

  if (inputString != "") {
    Serial.print("recieved ");
    Serial.println(inputString);
  }
  
  if (digitalRead(buttonBoi) == HIGH) {
    Serial.println("ring ring");
  }
}  
