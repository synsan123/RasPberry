#include <signal.h> //Signal 사용 헤더파일
#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>
#include <unistd.h>
#include <time.h>
#define LED_RED 7
#define LED_GREEN 21
#define LED_BLUE 22

void sig_handler(int signo); // 마지막 종료 함수 ctlr-C 로 종료

int main(void){
	int i;

    signal(SIGINT, (void *)sig_handler); //시그널 핸들러 함수

	if(wiringPiSetup () == -1)
		return 1;
	pinMode(LED_RED,OUTPUT);
	pinMode(LED_GREEN,OUTPUT);
	pinMode(LED_BLUE,OUTPUT);
	digitalWrite(LED_RED,0);
	digitalWrite(LED_GREEN,0);
	digitalWrite(LED_BLUE,0);
	printf("3 Color LED Control Start !! \n");
    for(i=0;i<10;i++){
	printf("Red LED On !! \n");
	digitalWrite(LED_RED,1);
	usleep(500000);
	printf("Red LED Off !! \nGreen LED On !!\n");		
    digitalWrite(LED_RED,0);
	digitalWrite(LED_GREEN,1);
	usleep(500000);
	printf("Green LED Off !! \nBlue LED On !!\n");
	digitalWrite(LED_GREEN,0);
	digitalWrite(LED_BLUE,1);
	usleep(500000);
	printf("Blue LED Off !! \n");
	digitalWrite(LED_BLUE,0);
	}
	return 0;
}

void sig_handler(int signo)  //마지막 처리를 위한 signal 핸들러 함수 모두 OFF
{
    printf("process stop\n");
    digitalWrite(LED_RED,0);
    digitalWrite(LED_GREEN,0);
    digitalWrite(LED_BLUE,0); // Off
    
    exit(0);
}