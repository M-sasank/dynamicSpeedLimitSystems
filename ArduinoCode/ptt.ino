#include <LiquidCrystal.h>// library for LCD
int Contrast=75;
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);// Arduino pin for the LCD
void setup() {
Serial.begin(115200);
analogWrite(6,Contrast);
     lcd.begin(16, 2);// initializing the Serial communication
lcd.begin(16,2);// initializing the dimensions of LCD
Serial.println("Speed Limit:-");// data to be printed
lcd.setCursor(0,0);// setting the place for the data on LCD
lcd.print("Speed Limit:-");// data to be printed
  }
char a_byte = 0;// defining a character data for a variable
String a_str = "";// creating a string having space

void loop() {
  if (Serial.available() > 0) { /*checking if any input is given on the Serial monitor*/
    a_byte = Serial.read(); /*read if there is any input and save it in the character data type variable*/

        if (a_byte != '\n') {/*to display the data on the next line one line space is added to the string */
    a_str += a_byte;
        }
        else {
          a_str[a_str.length()-1] = ' ' ;
    Serial.println(a_str); // print the string on the serial monitor
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Speed Limit:-");
    lcd.setCursor(0,1);// setting the place for the data
    lcd.print(a_str);// print the data on the LCD
    a_str = "";
    // Serial.println("");// printing the string having space
        }
      }
}