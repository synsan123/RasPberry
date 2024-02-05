#include <stdio.h>
#include <wiringPi.h>

PI_THREAD(fading_led) {
        const int led_pin = 1;

        pinMode(led_pin, PWM_OUTPUT);

        while(1) {
                int t_high;
                for(t_high=0;t_high<=1024;t_high++) {
                        pwmWrite(led_pin, t_high);
                        delay(1);
                }
                for(t_high=1024;t_high>=0;t_high--) {
                        pwmWrite(led_pin, t_high);
                        delay(1);
                }
        }
}

int main(void) {
        wiringPiSetup();

        piThreadCreate(fading_led);

        while(1) {
                printf("main\n");
                delay(1000);
        }
}