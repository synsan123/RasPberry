#include <stdio.h>
#include <wiringPi.h>

int main(void){
    const int buzzer_pin = 1;

    wiringPiSetup();
    pinMode(buzzer_pin,PWM_OUTPUT);

    pwmSetClock(19);
    pwmSetMode(PWM_MODE_MS);

    pwmSetRange(1000000/523);
    pwmWrite(buzzer_pin, 1000000/523/2);

    delay(3000);

    pwmWrite(buzzer_pin,0);
}