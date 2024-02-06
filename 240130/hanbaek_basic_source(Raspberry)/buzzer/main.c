#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>
#include <unistd.h>
#include <time.h>
#define BUZZER 15
int main(void){
	int buzzer_val,i;
	if(wiringPiSetup () == -1)
		return 1;	
	pinMode(BUZZER,OUTPUT);
	printf("Buzzer Control Start !! \n");
	for(i=0;i<20;i++){
		buzzer_val = 1;
		printf("BUZZER ON !!!\n");
		digitalWrite(BUZZER,buzzer_val);
		sleep(1);
		buzzer_val = 0;
		printf("BUZZER OFF !!!\n");
		digitalWrite(BUZZER,buzzer_val);
		sleep(1);
	}
	return 0;
}
