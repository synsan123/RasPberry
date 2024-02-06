#include <signal.h> //Signal 사용 헤더파일
#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>
#include <unistd.h>
#include <time.h>
#define STEP_OUTA 27
#define STEP_OUTB 0
#define STEP_OUT2A 1
#define STEP_OUT2B 24
#define SW1 3
#define SW2 4
#define SW3 5
#define SW4 6

void sig_handler(int signo); // 마지막 종료 함수 ctlr-C 로 종료

void rotate(int angle){
    for(int i=0;i<(angle * 1.45);i++){  // 65 = 45도, 130 = 90도, 260 = 180도
                digitalWrite(STEP_OUTA,1);
                usleep(5000);
                digitalWrite(STEP_OUTA,0);
                usleep(5000);
                digitalWrite(STEP_OUTB,1);
                usleep(5000);
                digitalWrite(STEP_OUTB,0);
                digitalWrite(STEP_OUT2A,1);
                usleep(5000);
                digitalWrite(STEP_OUT2A,0);
                digitalWrite(STEP_OUT2B,1);
                usleep(5000);
                digitalWrite(STEP_OUT2B,0);
        }
}

// 첫번째 스위치 인터럽트 처리 함수
void sw1_isr(void) {
  printf("SW1 pressed\n"); // 스위치 눌림을 출력
  rotate(45); // 스텝모터를 45도 시계방향으로 회전
}

// 두번째 스위치 인터럽트 처리 함수
void sw2_isr(void) {
  printf("SW2 pressed\n"); // 스위치 눌림을 출력
  rotate(90); // 스텝모터를 90도 시계방향으로 회전
}

// 세번째 스위치 인터럽트 처리 함수
void sw3_isr(void) {
  printf("SW3 pressed\n"); // 스위치 눌림을 출력
  rotate(180); // 스텝모터를 180도 시계방향으로 회전
}

// 네번째 스위치 인터럽트 처리 함수
void sw4_isr(void) {
  printf("SW4 pressed\n"); // 스위치 눌림을 출력
  printf("Program terminated\n"); // 프로그램 종료를 출력
  exit(0); // 프로그램 종료
}

int main(void){
        signal(SIGINT, (void *)sig_handler); //시그널 핸들러 함수

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
        pinMode(SW1,INPUT);
        pinMode(SW2,INPUT);
        pinMode(SW3,INPUT);
        pinMode(SW4,INPUT);
        wiringPiISR(SW1, INT_EDGE_FALLING, sw1_isr); // 첫번째 스위치가 눌리면 sw1_isr 함수 호출
        wiringPiISR(SW2, INT_EDGE_FALLING, sw2_isr); // 두번째 스위치가 눌리면 sw2_isr 함수 호출
        wiringPiISR(SW3, INT_EDGE_FALLING, sw3_isr); // 세번째 스위치가 눌리면 sw3_isr 함수 호출
        wiringPiISR(SW4, INT_EDGE_FALLING, sw4_isr); // 네번째 스위치가 눌리면 sw4_isr 함수 호출
        printf("Step Motor Control Start !! \n");
        while (1) {
        }
        return 0;
}

void sig_handler(int signo)  //마지막 처리를 위한 signal 핸들러 함수 모두 OFF
{
    printf("process stop\n");
    digitalWrite(STEP_OUTA,0);
    digitalWrite(STEP_OUTB,0);
    digitalWrite(STEP_OUT2A,0);
    digitalWrite(STEP_OUT2B,0);
    
    exit(0);
}
