/*
Interface wtih Python through COM port communication
Read input
*/

int userCommand = 6;

// the setup function runs once when you press reset or power the board
void setup() {
  Serial.begin(9600);
  // initialize digital pin 9 as an output.
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  // initial state
  digitalWrite (8,LOW);
  digitalWrite (9,LOW);
  digitalWrite (10,LOW);
}

// the loop function runs over and over again forever
void loop() {
  
  while (Serial.available()){
    
    userCommand = Serial.read();
    
    if (userCommand == '1'){
        digitalWrite(8, HIGH);   // turn the LED on (HIGH is the voltage level)
    }
    
    if (userCommand == '0'){
        digitalWrite(8, LOW);    // turn the LED off by making the voltage LOW                 // wait for a second
    }
    
    if (userCommand == '2'){
        digitalWrite(9, HIGH);    // turn the LED ON and OFF for one cycle
    }
    
    if (userCommand == '3'){
        digitalWrite(9, LOW);

    }
    if (userCommand == '4'){
        digitalWrite(10, HIGH);

    }
    if (userCommand == '5'){
        digitalWrite(10, LOW);

    }
  }
}
