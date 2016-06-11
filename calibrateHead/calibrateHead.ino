#include <Stepper.h>
#include <Servo.h>
#include <SoftwareSerial.h>
SoftwareSerial wifi(3, 2); // RX | TX


const short stepsPerRevolution = 50;
const short stepSpeed = 60;
const short headPin = 7;
const short stepperPins[4] = {9, 10, 11, 12};//9 and 10 for x axis 11 and 12 for y axis
const short bluePos = 10; //----------------------------------------------
const short redPos = 180; // Servo position for the color or move state
const short spaces = 15; //Squares on a row or column
const short blueMove = 25; //---------------------------------------------
const short redMove = 165;
const short height = 650 / spaces; //Steps for the height of the square
const short width = 650 / spaces; //Steps for the height of the square
const short moveTime[3]  = {100, 100, 50}; //Time to wait the motor to move x, y, servo
const short blue = 0;
const short red = 1;
const short dirs[2] = {1, -1};//To calibrate the motor direction x, y
const short changePos = 8;
short lastMove = blueMove;

//Board Matrix
byte boardMatrix[spaces][spaces];
byte actualPos[3] = {0, 0, 0}; //x, y, servo
short lastColor = blue;

//Motors
Servo head; // The Markers Head
Stepper xAxis(stepsPerRevolution, stepperPins[0],
              stepperPins[1]); //Horizontal Axis Motor
Stepper yAxis(stepsPerRevolution, stepperPins[2],
              stepperPins[3]); //Vertical Axis Motor

//WIFI
String inputbuffer = "";
const String commands[4] = {"punto", "rellene", "diagonald", "diagonali"};
boolean command = false;

void setup()
{ Serial.begin(9600);
  wifi.begin(9600);
  //Stepper Speed
  xAxis.setSpeed(stepSpeed);
  yAxis.setSpeed(stepSpeed);
  head.attach(headPin); //Servo pin
  head.write(blueMove);
  actualPos[2] = blueMove;
  inputbuffer.reserve(50);
  for (int i = 0; i < spaces ; i++) {
    for (int j = 0; j < spaces ; j++) {
      boardMatrix[i][j] = B00011;
    }
  }
}
//Serial Listener
void serialEvent() {
  //Triggered when the serial Recieves new data
  if (!command) {
    if (wifi.available()) {
      Serial.println("Order received");
      // get the new byte:
      char inChar;
      while (inChar != '\n') {
        inChar = wifi.read();
        inputbuffer += inChar;
        delay(10);
      }
      command = true;
      inputbuffer.toLowerCase();
    } else {
      if (Serial.available()) {
        Serial.println("Order received");
        char inChar;
        while (inChar != '\n') {
          inChar = wifi.read();
          inputbuffer += inChar;
          delay(10);
        }
        command = true;
        inputbuffer.toLowerCase();
      }
    }
  }

}


//Dot draw method
bool dot(char*  entry) {
  Serial.println(entry);
  int values[3] = {0, 0, 0}; //X, Y, Color
  char* param = strtok(entry, "_");
  Serial.println(param);
  for (int i = 0; i < 3; i++) {
    param = strtok(NULL, "_");
    if (param == NULL) {
      return false;
    }
    values[i] = atoi(param);
  }
  if (boardMatrix[values[0]][values[1]] == B00011) {
    changeColor(values[2]);
    if (movePencil(values[0], values[1]) && draw(values[2])) {
      boardMatrix[values[0]][values[1]] = lastColor;
      return true;
    } else {
      return false;
    }
  } else {
    return false;
  }
}

//Diagonal method
bool diagonal(char* entry, short dirx) {
  short value = 0;
  char* param = strtok(entry, "_");
  param = strtok(NULL, "_");
  if (param == NULL) {
    return false;
  }
  value = atoi(param);
  if (value == 0) {
    return true;
  }
  short diry = value / value;
  if ( (0 <= actualPos[0] + value * dirx < spaces) && (0 <= actualPos[1] + diry * value < spaces)) {
    for (short i = 0; i < value; i++) {
      movePencil(actualPos[0] + dirx, actualPos[1] + diry);
      draw(lastColor);
    }
    return true;
  } else {
    return false;
  }
}

//Fill method
bool fill(char* entry) {
  short value = 0;
  char* param = strtok(entry, "_");
  param = strtok(NULL, "_");
  if (param == NULL) {
    return false;
  }
  value = atoi(param);
  if (value == 0) {
    return true;
  }
  /*for(int i=0; i<value i++;){
    for(int j=
    }*/
}

//Move method
bool movePencil(short x, short y) {
  if (actualPos[2] != lastMove) {
    Serial.print("Sweep for move");
    Serial.println(lastMove);
    sweep(lastMove);
  }
  if ( (0 <= x < spaces) && (0 < y < spaces) ) { //If is not out of boundary
    xAxis.step((x - actualPos[0])*width * dirs[0]); //Moves the x to the final position minus the initial position times the width of the square.
    delay(moveTime[0]); //Wait for the motor to move
    yAxis.step((y - actualPos[1])*height * dirs[1]);
    delay(moveTime[1]);
    actualPos[0] = x;
    actualPos[1] = y;
    Serial.println("Movin ");
    return true;
  } else {
    return false;
  }
}


void changeColor(short Color) {
  Serial.println("Write changing color");
  short actual = actualPos[1];
  if (actualPos[1] < 5 || actualPos[1] > 10) {
    short movePos;
    switch (Color) {
      case blue:
        Serial.println("blue move");
        movePos = blueMove;
        lastColor = blue;
        break;
      case red:
        Serial.println("red move");
        movePos = redMove;
        lastColor = red;
        break;
      default:
        Serial.println("blue  default move");
        movePos = blueMove;
        lastColor = blue;
        break;
    }

    if (actualPos[2] != movePos) {
      if (movePencil(actualPos[0], changePos)) {
        Serial.print("Movin from change");
        Serial.println(movePos);
        lastMove=movePos;
        sweep(lastMove);
      }
      movePencil(actualPos[0], actual);
    }
  } else {
    colorAux(Color);
  }
}
//Change color aux method
void colorAux(short color) {
  switch (color) {
    case red:
      if (actualPos[2] != redPos) {
        sweep(redPos);
      }
      lastColor = red;
      lastMove = redMove;
      break;
    case blue:
      if (actualPos[2] != bluePos) {
        sweep(bluePos);
      }
      lastColor = blue;
      lastMove = blueMove;
      break;
    default:
      break;
  }
}

//sweep method to change the velocity of the change
void sweep(short pos) {
  switch (pos) {
    case bluePos:
      for (short i = actualPos[2]; i > bluePos; i -= 5) {
        head.write(i);
        delay(moveTime[2]);
      }
      head.write(bluePos);
      delay(moveTime[2]);
      break;
    case redPos:
      for (short i = actualPos[2]; i < redPos; i += 5) {
        head.write(i);
        delay(moveTime[2]);
      }
      head.write(redPos);
      delay(moveTime[2]);
      break;
    case blueMove:
      if (actualPos[2] == redPos) {
        for (short i = actualPos[2]; i > blueMove; i -= 5) {
          head.write(i);
          delay(moveTime[2]);
        }
      }
      else {
        for (short i = actualPos[2]; i < blueMove; i += 5) {
          head.write(i);
          delay(moveTime[2]);
        }
      }
      head.write(blueMove);
      delay(moveTime[2]);
      break;
    case redMove:
      if (actualPos[2] == redPos) {
        for (short i = actualPos[2]; i > redMove; i -= 5) {
          head.write(i);
          delay(moveTime[2]);
        }
      }
      else {
        for (short i = actualPos[2]; i < redMove; i += 5) {
          head.write(i);
          delay(moveTime[2]);
        }
      }
      head.write(redMove);
      delay(moveTime[2]);
      break;
    default:
      break;

  }
  actualPos[2] = pos;

}


//Draw method
bool draw(short colr) {
  switch (colr) {
    case blue:
      sweep(bluePos);
      break;
    case red:
      sweep(redPos);
      break;
    default:
      sweep(bluePos);
      break;
  }
  changeColor(colr);
  short dir = 1;
  for (int i = 0; i < height; i++) {
    xAxis.step(width * dir * dirs[0]); //Move a line
    delay(10); //Wait for the motor to move
    dir = dir * -1;
    yAxis.step(1 * dirs[1]); //Move step by step
    delay(2); //Wait for the motor to move
  }
  yAxis.step(-height * dirs[1]); //Return to the home position for the matrix
  delay(10); //Wait for the motor to move
  if (width % 2 == 0) {
    xAxis.step(-width * dirs[0]);
    delay(10); //Wait for the motor to move
  }
  return true;
}


void loop()
{
  changeColor(0);
  delay(2000);
  changeColor(1);
  delay(2000);
  movePencil(14, 0);
  changeColor(0);
  delay(2000);
  changeColor(1);
  delay(2000);
  movePencil(10, 5);
  changeColor(0);
  delay(2000);
  changeColor(1);
  delay(2000);
  movePencil(14, 14);
  changeColor(0);
  delay(2000);
  changeColor(1);
  delay(2000);
  movePencil(10, 10);
  changeColor(0);
  delay(2000);
  changeColor(1);
  delay(2000);
  movePencil(0, 14);
  changeColor(0);
  delay(2000);
  changeColor(1);
  delay(000);
  movePencil(5, 7);
  changeColor(0);
  delay(2000);
  changeColor(1);
  delay(2000);
  movePencil(0, 0);
}



