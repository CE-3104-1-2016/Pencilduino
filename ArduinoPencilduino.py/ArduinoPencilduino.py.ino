#include <Stepper.h>
#include <Servo.h>


//Constants
const int stepsPerRevolution = 50;
const int stepSpeed = 60;
const int headPin = 13;
const int stepperPins[4] = {9, 10, 11, 12};

//Motors
int servoPosition=0;
Servo head; // The Markers Head
Stepper xAxis(stepsPerRevolution, stepperPins[0],
stepperPins[1]); //Horizontal Axis Motor
Stepper yAxis(stepsPerRevolution, stepperPins[2], 
stepperPins[3]); //Vertical Axis Motor

void setup() {
  //Stepper Speed 
  xAxis.setSpeed(stepSpeed);
  yAxis.setSpeed(stepSpeed);
  head.attach(headPin); //
}

