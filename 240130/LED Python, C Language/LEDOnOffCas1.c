#include <stdio.h>
#include <wiringPi.h>
#define led_pin 7
int main(void){
	wiringPiSetup();
	pinMode(led_pin,OUTPUT);
	while(1){
		int t_high;
		for(t_high = 0; t_high <= 10; t_high++){
			digitalWrite(led_pin,HIGH);
			delay(t_high);
			digitalWrite(led_pin,LOW);
			delay(10-t_high);
		}
	}
}
