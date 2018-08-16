#include <Servo.h>

int red=13;
int yellow=12;
int green=11;

void moveY(); void moveG(); void moveR();
Servo myservo1, myservo2,myservo3,myservo4, myservo21, myservo22;
int pos = 0 , s ;
void setup() {
  // put your setup code here, to run once:

  pinMode(red, OUTPUT);
  pinMode(yellow, OUTPUT);
  pinMode(green, OUTPUT);
  
  myservo1.attach(2);
  myservo2.attach(4);
  myservo3.attach(5);
  myservo4.attach(6);

  myservo21.attach(7);
  myservo22.attach(8);
}

void loop() {
  // put your main code here, to run repeatedly:
  myservo1.write(170);
  myservo4.write(140);
  myservo2.write(180);
  changeLights();
    delay(2000);
  

}
void changeLights(){
    // green off, yellow on for 3 seconds
    digitalWrite(green, LOW);
    digitalWrite(yellow, LOW);
    digitalWrite(red, HIGH);
    moveR();
    moveR();
    delay(4000);

    // turn off yellow, then turn red on for 5 seconds
    digitalWrite(yellow, HIGH);
    digitalWrite(red, LOW);
    digitalWrite(green, LOW);
   moveY();
    delay(2000);


    // turn off red and yellow, then turn on green
    digitalWrite(yellow, LOW);
    digitalWrite(red, LOW);
    digitalWrite(green, HIGH);
    moveG();
    moveG();
    delay(2000);
}

void moveG(){
  myservo22.write(0);
 for (pos = 180; pos >= 70; pos -= 1) { // goes from 180 degrees to 0 degrees
    //myservo1.write(pos);              // tell servo to go to position in variable 'pos'
    delay(20); 
   myservo2.write(pos); // waits 15ms for the servo to reach the position
  //myservo3.write(pos);
  //myservo4.write(pos);
  }
  for (pos = 70; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
   // myservo1.write(pos);              // tell servo to go to position in variable 'pos'
    delay(30);                        // waits 15ms for the servo to reach the position
    myservo2.write(pos);              // tell servo to go to position in variable 'pos'
   // delay(15);
    //myservo3.write(pos);
    //myservo4.write(pos);
  }
}
void moveY(){
  myservo22.write(0);
}
void moveR(){
  
 
  for (pos = 150; pos >=30; pos -= 1) { // goes from 0 degrees to 180 degrees
   
    myservo21.write(pos);
    delay(30);
    myservo22.write(pos);
  }
  for (pos = 30; pos <=150; pos += 1) { // goes from 180 degrees to 0 degrees
               // tell servo to go to position in variable 'pos'
    
  
  myservo21.write(pos);
  delay(20); 
  myservo22.write(pos);
  }
}
