#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>
#include <unistd.h>
#include <time.h>
#define STEP_OUTA 27
#define STEP_OUTB 0
#define STEP_OUT2A 1
#define STEP_OUT2B 24
int main(void){
	int i;
	if(wiringPiSetup () == -1)
		return 1;
	pinMode(STEP_OUTA,OUTPUT);
	pinMode(STEP_OUTB,OUTPUT);
	pinMode(STEP_OUT2A,OUTPUT);
	pinMode(STEP_OUT2B,OUTPUT);
	digitalWrite(STEP_OUTA,0);
	digitalWrite(STEP_OUTB,0);
	digitalWrite(STEP_OUT2A,0);
	digitalWrite(STEP_OUT2B,0);
	printf("Step Motor Control Start !! \n");
	for(i=0;i<2000;i++){
		digitalWrite(STEP_OUTA,1);
		usleep(2000);
		digitalWrite(STEP_OUTA,0);
		digitalWrite(STEP_OUTB,1);
		usleep(2000);
		digitalWrite(STEP_OUTB,0);
		digitalWrite(STEP_OUT2A,1);
		usleep(2000);
		digitalWrite(STEP_OUT2A,0);
		digitalWrite(STEP_OUT2B,1);
		usleep(2000);
		digitalWrite(STEP_OUT2B,0);
	}

	return 0;
}
