#include <stdio.h>
#include <wiringPi.h>

#define BUZZER 14
int main(void){
	int buzzer_val,I;
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
