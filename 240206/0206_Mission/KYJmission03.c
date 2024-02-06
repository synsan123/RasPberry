#include <signal.h> //Signal 사용 헤더파일
#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>
#include <unistd.h>
#include <time.h>

#define SW1 3
#define SW2 4
#define SW3 5
#define SW4 6

#define led_red 7
#define led_green 21
#define led_blue 22

const int Buzzer = 1;

void sig_handler(int signo); // 마지막 종료 함수 ctlr-C 로 종료

void Music_One(void) {
    pwmWrite(Buzzer, 10);
    int scale[] = {523, 587, 659, 698, 784, 880, 988, 1047};
    int twinkle[] = {1,1,5,5,6,6,5,4,4,3,3,2,2,1,5,5,4,4,3,3,2,5,5,4,4,3,3,2,1,1,5,5,6,6,5,4,4,3,3,2,2,1};

    for (int i = 0; i < 42; i++) {
        pwmSetRange(1000000/scale[twinkle[i]]);
        pwmWrite(Buzzer, 1000000/scale[twinkle[i]]/10);
        digitalWrite(led_red, 1);
        if (i == 6 || i == 13 || i == 20 || i == 27 || i == 34 || i == 41) {
            delay(1000);
        }
        else {
            delay(500);
        }
    }
    pwmWrite(Buzzer, 0);
    digitalWrite(led_red, 0);
}

void Music_Two(void) {
    pwmWrite(Buzzer, 10);
    int scale[] = {523, 587, 659, 698, 784, 880, 988, 1047};
    int twinkle[] = {4,2,2,
               3,1,1,
               0,1,2,3,4,4,4,
               4,2,2,2,3,1,1,
               0,2,4,4,2,2,2,
               1,1,1,1,1,2,3,
               2,2,2,2,2,3,4,
               4,2,2,
               3,1,1,
               0,2,4,4,2,2,2};

    for (int i = 0; i < 54; i++) {
        pwmSetRange(1000000/scale[twinkle[i]]);
        pwmWrite(Buzzer, 1000000/scale[twinkle[i]]/10);
        digitalWrite(led_green, 1);
        if (i == 2 || i == 5 || i == 12 || i == 19 || i == 26 || i == 33 || i == 40 || i == 43 || i == 46 || i == 53) {
            delay(1000);
        }
        else {
            delay(500);
        }
    }
    pwmWrite(Buzzer, 0);
    digitalWrite(led_green, 0);
}

void Music_Three(void) {
    pwmWrite(Buzzer, 10);
    int scale[] = {523, 587, 659, 698, 784, 880, 988, 1047};
    int twinkle[] = {4,4,5,5,4,4,2,
               4,4,2,2,1,
               4,4,5,5,4,4,2,
               4,2,1,2,0};

    for (int i = 0; i < 24; i++) {
        pwmSetRange(1000000/scale[twinkle[i]]);
        pwmWrite(Buzzer, 1000000/scale[twinkle[i]]/10);
        digitalWrite(led_blue, 1);
        if (i == 6 || i == 18) {
            delay(1000);
        }
        else if (i == 0 || i == 1 || i == 2 || i == 3 || i == 4 || i == 5 || i == 7 || i == 8 || i == 9 || i == 10 || i == 12 || i == 13 || i == 14 || i == 15 || i == 16 || i == 17 || i == 19 || i == 20 || i == 21 || i == 22) {
            delay(500);
        }
        else if (i == 11 || i == 23) {
            delay(1200);
        }
    }
    pwmWrite(Buzzer, 0);
    digitalWrite(led_blue, 0);
}

// 첫번째 스위치 인터럽트 처리 함수
void sw1_isr(void) {
  printf("Music One!\n"); // 스위치 눌림을 출력
  Music_One();
}

// 두번째 스위치 인터럽트 처리 함수
void sw2_isr(void) {
  printf("Music Two!\n"); // 스위치 눌림을 출력
  Music_Two();
}

// 세번째 스위치 인터럽트 처리 함수
void sw3_isr(void) {
  printf("Music Three!\n"); // 스위치 눌림을 출력
  Music_Three();
}

// 네번째 스위치 인터럽트 처리 함수
void sw4_isr(void) {
  printf("SW4 pressed\n"); // 스위치 눌림을 출력
  printf("Program terminated\n"); // 프로그램 종료를 출력
  exit(0); // 프로그램 종료
}

int main(void) {
    signal(SIGINT, (void *)sig_handler); //시그널 핸들러 함수

    if(wiringPiSetup () == -1)
        return 1;
    pinMode(Buzzer, PWM_OUTPUT);
    pinMode(led_red, OUTPUT);
    pinMode(led_green, OUTPUT);
    pinMode(led_blue, OUTPUT);
    pinMode(SW1, INPUT);
    pinMode(SW2, INPUT);
    pinMode(SW3, INPUT);
    pinMode(SW4, INPUT);
    digitalWrite(led_red, 0);
    digitalWrite(led_green, 0);
    digitalWrite(led_blue, 0);
    pwmSetClock(19);
    pwmSetMode(PWM_MODE_MS);
    wiringPiISR(SW1, INT_EDGE_FALLING, sw1_isr); // 첫번째 스위치가 눌리면 sw1_isr 함수 호출
    wiringPiISR(SW2, INT_EDGE_FALLING, sw2_isr); // 두번째 스위치가 눌리면 sw2_isr 함수 호출
    wiringPiISR(SW3, INT_EDGE_FALLING, sw3_isr); // 세번째 스위치가 눌리면 sw3_isr 함수 호출
    wiringPiISR(SW4, INT_EDGE_FALLING, sw4_isr); // 네번째 스위치가 눌리면 sw4_isr 함수 호출
    while (1) {
    }
    return 0;
}

void sig_handler(int signo)  //마지막 처리를 위한 signal 핸들러 함수 모두 OFF
{
    printf("process stop\n");
    pwmWrite(Buzzer, 0); // Off
    digitalWrite(led_red, 0);
    digitalWrite(led_green, 0);
    digitalWrite(led_blue, 0);
    
    exit(0);
}