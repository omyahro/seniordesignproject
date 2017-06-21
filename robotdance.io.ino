#include <Servo.h>
Servo servoLeft;
Servo servoRight;

void setup() {

  Serial.begin(9600);
  servoLeft.attach(13);
  servoRight.attach(12);

  servoLeft.writeMicroseconds(1500);
  servoRight.writeMicroseconds(1500);
}

void loop() {
  servoRight.writeMicroseconds(1750);
  servoLeft.writeMicroseconds(1300);
  delay(6750);
  servoRight.writeMicroseconds(1700);
  servoLeft.writeMicroseconds(1500);
  delay(2000);
  back_and_forth();
  wave_forward();
  wave_backward();

  for (int x = 0; x < 4; x++) {
    servoRight.writeMicroseconds(1700);
    servoLeft.writeMicroseconds(1700);
    delay(250);
    servoRight.writeMicroseconds(1450);
    servoLeft.writeMicroseconds(1550);
    delay(250);
    servoRight.writeMicroseconds(1300);
    servoLeft.writeMicroseconds(1300);
    delay(500);
    servoRight.writeMicroseconds(1450);
    servoLeft.writeMicroseconds(1550);
    delay(250);
  };
  exit(0);
} 


void back_and_forth () {
  for (int x = 0; x < 6; x++) {
    servoRight.writeMicroseconds(1700);
    servoLeft.writeMicroseconds(1300);
    delay(300);
    servoRight.writeMicroseconds(1300);
    servoLeft.writeMicroseconds(1700);
    delay(300);
  }
}

void wave_forward () {
    servoLeft.writeMicroseconds(1500);
    servoRight.writeMicroseconds(1750);
    delay(1000);
    servoLeft.writeMicroseconds(1300);
    servoRight.writeMicroseconds(1750);
    delay(300);
    servoLeft.writeMicroseconds(1250);
    servoRight.writeMicroseconds(1500);
    delay(1000);
    servoLeft.writeMicroseconds(1300);
    servoRight.writeMicroseconds(1750);
    delay(300);
    servoLeft.writeMicroseconds(1500);
    servoRight.writeMicroseconds(1750);
    delay(1000);
    servoLeft.writeMicroseconds(1300);
    servoRight.writeMicroseconds(1750);
    delay(300);
}

void wave_backward () {
    servoLeft.writeMicroseconds(1500);
    servoRight.writeMicroseconds(1250);
    delay(1000);
    servoLeft.writeMicroseconds(1750);
    servoRight.writeMicroseconds(1300);
    delay(300);
    servoLeft.writeMicroseconds(1750);
    servoRight.writeMicroseconds(1500);
    delay(1000);
    servoLeft.writeMicroseconds(1750);
    servoRight.writeMicroseconds(1300);
    delay(300);
    servoLeft.writeMicroseconds(1500);
    servoRight.writeMicroseconds(1250);
    delay(1000);
    servoLeft.writeMicroseconds(1750);
    servoRight.writeMicroseconds(1300);
    delay(300);
}
