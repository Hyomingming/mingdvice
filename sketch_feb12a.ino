int green = 12;
int yellow = 10;
int red = 8;

void setup() {
  Serial.begin(9600);
  pinMode(green, OUTPUT);
  pinMode(yellow, OUTPUT);
  pinMode(red, OUTPUT);
}

void loop() {
  while(Serial.available() > 0) {
    int num = Serial.read();
    printf("%d", num);
    if(num == 1){ 
      digitalWrite(green, LOW);
      digitalWrite(yellow, HIGH);
      digitalWrite(red, LOW);
      delay(1000);
    }else if(num == 2){
      digitalWrite(green, LOW);
      digitalWrite(yellow, LOW);
      digitalWrite(red, HIGH);
      delay(1000);
    }else if(num == 3){
      digitalWrite(green, HIGH);
      digitalWrite(yellow, LOW);
      digitalWrite(red, LOW);
      delay(1000);
    }
  }
}
