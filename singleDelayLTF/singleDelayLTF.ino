/**
 * Author: Oakley Katterheinrich
 * Last Edited: 3/15/17
 * Arduino Ver. 1.6.7
 */

/**
 * Libraries used:
 *  Firmata Library for Processing
 *  https://github.com/firmata/processing/releases/tag/latest
 *  - used for communication between Arduino and Processing program
 */

#include <Boards.h>
#include <Firmata.h>

/**
 * TSL235R Wiring:
 *    GND    GND
 *    Vcc    +5V
 *    Data   Digital pin 2
 *    
 * Datasheet: http://www.sparkfun.com/datasheets/Sensors/Imaging/TSL235R-LF.pdf
 */

// Pin definitions
//Out of TSL235R connected to Digital pin 2
# define TSL235R 2
//Red LED anode (long lead) connected to Digital pin 12
# define LED0 12

//Number of milliseconds between printing, and reseting each light frequency measurement
int period = 50;

//Holds number of pulses from TSL235R, equivalent to frequency
volatile long pulses = 0;
//Must be 'volatile' so value can change when triggered by interrupt, definition below:
/* 'volatile' - directs the compiler to load the variable from RAM and not from a storage register
 * A variable should be declared volatile whenever its value can be changed by something beyond 
 * the control of the code section in which it appears
 */

void setup() {
 /* Serial.begin(speed) speed in bps
  * Rates: 300, 600, 1200, 2400, 4800, 9600, 14400, 19200, 28800, 38400, 57600, or 115200
  */
  //Configure the serial port
  Serial.begin(9600);

  //Configure TSL235R interrupt pin to trigger PulseCount method to run when
  //interrupt pin goes from LOW to HIGH
  attachInterrupt(0, PulseCount, RISING);

  //Set TSL235R data pin to input
  pinMode(TSL235R, INPUT);
  
  //Set Red LED pin to output
  pinMode(LED0, OUTPUT);

  //Initialize the TSL235R's pulse counter
  pulses = 0;
}

void loop(){
  //Red LED should ALWAYS be on during measurement
  digitalWrite(LED0, HIGH);
  
  //Print the measured pulse count to serial
  Serial.println(pulses);

  //Reset the pulses counter
  pulses = 0;

  //Wait x milliseconds before writing next pulse measurement
  delay(period);                        
}

/**
 * Method called when interrupt is triggered by TSL235R. 
 * Higher frequency = more interrupts per period = higher pulse count
 */
void PulseCount(){
  //Incriment pulses count
  pulses++;
}
