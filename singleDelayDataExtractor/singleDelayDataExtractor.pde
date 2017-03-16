/**
  Author: Oakley Katterheinrich
  Last Edited: 3/15/17
  Processing Ver. 3.2.4
*/

//Allows the program to read values from serial
import processing.serial.*;

//The serial port used to retrieve measurement data from the Arduino
Serial myPort;        

//Counts the number of measurements retrieved from serial port
int count;    

//Writer object used to write to the data .txt file
PrintWriter output;

//Delay between the Arduino's measurements, make sure it is the same as the Arduino value
int delay = 50;

void setup () {
  //Initialize data counter
  count = 0;
  
  //Creates a new file in the sketch folder and a Writer object to write to it
  output = createWriter("pulseData50.txt");
  
  //Lists available serial ports, choose whichever your Arduino is using
  println(Serial.list());
  
  //Open whichever port the Arduino is using, match the Arduino's bps rate (9600)
  myPort = new Serial(this, Serial.list()[1], 9600);

  //Wait to generate the serialEvent() until you get a new line
  myPort.bufferUntil('\n');
}

void draw () {
}

/**
  Stops retrieving measurements from serial and closes/saves data .txt file
*/
void writePulseData(){
  //Writes the remaining data to the file
  output.flush();
  //Closes the file
  output.close(); 
  //Ends the program
  exit(); 
}

/**
  Manual way to stop retrieving measurements and close data file. 
  Press and key to call this method
*/
void keyPressed() {
  //Writes the remaining data to the file
  output.flush();
  //Closes the file
  output.close(); 
  //Ends the program
  exit(); 
}

/**
  Retrieves measurement data from the Arduino via the serial port
*/
void serialEvent(Serial myPort){
  //Retrieve the ASCII string from the serial port
  String inString = myPort.readStringUntil('\n');

  //Check to make sure the serial input has a value
  if (inString != null) {
    //Breaks input string into String array in case a space somehow made it into serial
    String[] temp = split(inString, ' ');
    //Write measurement data to its respective .txt file
    output.println(float(temp[0]));
    //Incriment data count
    count++;
    //Print data count and its respective measurement value to the console
    println(count+": "+float(temp[0]));
    //Once a full minute of data has been measured, the 
    if(count*delay >= 60000){
      writePulseData();
    }
  }
}