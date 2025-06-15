// Define pins for motor control
const int ENB = 9;  // PWM pin for speed control
const int IN3 = 8;  // Direction control pin 1
const int IN4 = 7;  // Direction control pin 2

void setup() {
  // Set pins as outputs
  pinMode(ENB, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);

  // Initialize serial communication
  Serial.begin(9600);

  // Stop motor initially
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
  analogWrite(ENB, 0);
}

void loop() {
  // Check if serial data is available
  if (Serial.available() > 0) {
    char command = Serial.read();  // Read incoming command

    if (command == 'L') {
      // Move motor left (reversed direction)
      digitalWrite(IN3, LOW);
      digitalWrite(IN4, HIGH);
      analogWrite(ENB, 255);  // Maximum speed
    }
    else if (command == 'R') {
      // Move motor right (reversed direction)
      digitalWrite(IN3, HIGH);
      digitalWrite(IN4, LOW);
      analogWrite(ENB, 255);  // Maximum speed
    }
    else if (command == 'S') {
      // Stop motor
      digitalWrite(IN3, LOW);
      digitalWrite(IN4, LOW);
      analogWrite(ENB, 0);
    }
  }
}