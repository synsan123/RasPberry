#include <signal.h> //Signal 사용 헤더파일
#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>
#include <unistd.h>
#include <time.h>

const int Buzzer = 1;

void sig_handler(int signo); // 마지막 종료 함수 ctlr-C 로 종료

int main(void) {
        signal(SIGINT, (void *)sig_handler); //시그널 핸들러 함수
        
        if(wiringPiSetup () == -1)
            return 1;

        pinMode(Buzzer, PWM_OUTPUT);

        pwmSetClock(19);
        pwmSetMode(PWM_MODE_MS);

        const int melody[] = {
                523, 587, 659, 698, 784, 880, 988, 1047
        };

        const int twinkle[] = { // 작은 별 노래 배열
                4,2,2,
                3,1,1,
                0,1,2,3,4,4,4,
                4,2,2,2,3,1,1,
                0,2,4,4,2,2,2,
                1,1,1,1,1,2,3,
                2,2,2,2,2,3,4,
                4,2,2,
                3,1,1,
                0,2,4,4,2,2,2
        };

        for(int note=0;note<54;note++) {
                pwmSetRange(1000000/melody[twinkle[note]]);
                pwmWrite(Buzzer, 1000000/melody[twinkle[note]]/10);
                if (note == 2 || note == 5 || note == 12 || note == 19 || note == 26 || note == 33 || note == 40 || note == 43 || note == 46 || note == 53){
                    delay(1000);           
                }
                else delay(500);
        }

        pwmWrite(Buzzer, 0);
}

void sig_handler(int signo)  //마지막 처리를 위한 signal 핸들러 함수 모두 OFF
{
    printf("process stop\n");
    pwmWrite(Buzzer, 0); // Off
    
    exit(0);
}