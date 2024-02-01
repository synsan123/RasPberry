#include <stdio.h>
#include <wiringPi.h>

int main(void) {
        const int button_pin = 3;
        const int led_pin = 1;

        wiringPiSetup();

        pinMode(button_pin, INPUT);
        pinMode(led_pin, OUTPUT);

        while(1) {
                int buttonInput = digitalRead(button_pin);
                if(buttonInput == 0)
                        digitalWrite(led_pin, 1000);
                else
                        digitalWrite(led_pin, 0);
        }
}