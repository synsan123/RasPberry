#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>
#include <unistd.h>
#include <time.h>
#define PIR_D 2
int main(void){
	int pir_val,i;
  	if(wiringPiSetup()==-1)
      	return -1;
	pinMode(PIR_D,INPUT);
	for(i=0;i<20;i++){
		pir_val = digitalRead(PIR_D);
		if(pir_val == 1)
			printf("PIR Detected !! \n");
		else
			printf("PIR Not detect !! \n");
		sleep(1);
	}
	return 0;
}