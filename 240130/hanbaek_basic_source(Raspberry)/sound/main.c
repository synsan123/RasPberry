#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>
#include <unistd.h>
#include <time.h>
#define SPI_CH 0
#define ADC_CH2 2
#define ADC_CS 8
#define SPI_SPEED 500000
int main(void){
	int adcValue=0, i;
	unsigned char buf[3];
	if(wiringPiSetup () == -1)
		return 1;
	pinMode(ADC_CS,OUTPUT);
	if(wiringPiSPISetup(SPI_CH,SPI_SPEED) == -1){
		printf("wiringPi SPI Setup failed!\n");
		exit(0);
	}
	for(i=0; i<200;i++){
		buf[0] = 0x06 | ((ADC_CH2 & 0x07)>>2);
		buf[1] = ((ADC_CH2 & 0x07)<<6);
		buf[2] = 0x00;
		digitalWrite(ADC_CS,0);
		wiringPiSPIDataRW(SPI_CH,buf,3);
		buf[1] = 0x0F & buf[1];
		adcValue = (buf[1] << 8) | buf[2];
		digitalWrite(ADC_CS,1);
		printf("Sound ADC Value -> %d\n",adcValue);
		usleep(100000);
	}	
	return 0;
}
