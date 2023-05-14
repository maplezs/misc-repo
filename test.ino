#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#define USE_ARDUINO_INTERRUPTS true
#include <PulseSensorPlayground.h>
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 32 
#define OLED_RESET     -1 
#define SCREEN_ADDRESS 0x3C
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);
PulseSensorPlayground pulseSensor; 
#define interruptPin 2
#define LOGO_HEIGHT   16
#define LOGO_WIDTH    16
// define untuk sensor 
const int PULSE_INPUT = A0;
const int PULSE_BLINK = LED_BUILTIN;
const int THRESHOLD = 550; 
bool state; 
long waktuterakhir;
long menit = 0;
int myBPM;
// setup sebelum program utama mulai
void setup() {
  Serial.begin(115200);
  pinMode(interruptPin, INPUT_PULLUP);
  // Insialisasi layar OLED
  if(!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    Serial.println(F("Alokasi gagal!"));
    for(;;);
  }
    pulseSensor.analogInput(PULSE_INPUT);   
    pulseSensor.blinkOnPulse(LED);    
    pulseSensor.setThreshold(Threshold);
  if (pulseSensor.begin()) {
    Serial.println("We created a pulseSensor Object !");
  }
    display.setTextSize(1);
    display.setTextColor(WHITE);
    display.setCursor(0,0);
    display.println("Selamat Datang");
    display.setCursor(0,1);
    display.println("to Kuliah");
    display.display();
    delay(2000); 
    display.clearDisplay();
}

void loop() {
    if (digitalRead(interruptPin) == LOW){
        state = false;
        display.clearDisplay();
    }
    if (digitalRead(interruptPin) == HIGH){
        display.clearDisplay();
        if(state == false){
            display.clearDisplay();
            display.setTextSize(2);
            display.setTextColor(WHITE);
            display.setCursor(0,0);
            display.println("Memulai Program...");
            display.display();
            delay(2000); 
            state == true
        }
        if(state == true){
            display.clearDisplay();
            display.setTextSize(1);
            display.setCursor(0,0);
            display.println("Menganalisa BPM...");
            display.setCursor(0,1);
            display.println("1 Menit");
            display.display();
            waktuterakhir = 0;
            delay(20);
            if(millis()-waktuterakhir < 60000){
                myBPM = pulseSensor.getBeatsPerMinute();
                if(myBPM < 110 || myBPM > 160){
                    tone(9, 1000);
                    delay(250);
                    noTone(9);
                }
            }
            display.clearDisplay();
            display.setTextSize(2);
            display.setTextColor(WHITE);
            display.setCursor(0,0);
            display.print("BPM :");
            display.println(myBPM/2);
            display.display();
            delay(2000); 
        }
    }
}