import RPi.GPIO as GPIO
import threading
import time

red = 4
green = 5
blue = 13

STEP_MOTOR = [16, 17, 18, 19]
StepCounter = 0
StepCount = 4

# 정방향(시계 방향) 회전 배열 
# Seq = [[0, 0, 0, 1],
#        [0, 0, 1, 0],
#        [0, 1, 0, 0],
#        [1, 0, 0, 0]]

flag_exit = False

# 역방향(반시계) 회전 배열
Seq = [[1, 0, 0, 0],
       [0, 1, 0, 0],
       [0, 0, 1, 0],
       [0, 0, 0, 1]]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

GPIO.output(red,False)
GPIO.output(green,False)

for pin in STEP_MOTOR:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

pwm_blue = GPIO.PWM(blue, 200)
pwm_blue.start(0)

def rotate_motor(angle): # 역방향(반시계 방향) 회전
    global StepCounter
    steps = int(5.75 * angle) # 오차 발생함(5.75는 장치의 정확한 회전각도가 아님)
    for i in range(steps):
        for pin in range(4):
            xpin = STEP_MOTOR[pin]
            if Seq[StepCounter][pin] != 0:
                GPIO.output(xpin, True)
            else:
                GPIO.output(xpin, False)
        StepCounter += 1
        if StepCounter == StepCount:
            StepCounter = 0
        if StepCounter < 0:
            StepCounter = StepCount
        time.sleep(0.01)


def t1():
        while True:
                print("\tGreen LED ON!")
                GPIO.output(green, True)
                time.sleep(1.3)
                GPIO.output(green, False)
                time.sleep(1.3)
                if flag_exit: break


def t2():
        while True:
            print("\tBLUE LED ON!")
            for t_high in range(0, 1024):
                pwm_blue.ChangeDutyCycle(t_high * 0.09765)
                time.sleep(0.002)
            for t_high in range(1024, -1):
                pwm_blue.ChangeDutyCycle(t_high * 0.09765)
                time.sleep(0.002) 
                if flag_exit: break


def t3():
        while True:
            rotate_motor(180)  # 180도 회전
            time.sleep(1.8)  # 1.8초 대기
            rotate_motor(0)  # 0도로 돌아감
            time.sleep(1.8)  # 1.8초 대기
            if flag_exit: break

thread = threading.Thread(target=t1)
thread1 = threading.Thread(target=t2)
thread2 = threading.Thread(target=t3)
thread.start()
thread1.start()
thread2.start()

try:
        while True:
                print("main Red LED ON!")
                GPIO.output(red,True)
                time.sleep(0.7)
                GPIO.output(red,False)
                time.sleep(0.7)

except KeyboardInterrupt:
        pass
flag_exit = True
thread.join()
thread1.join()
thread2.join()

pwm_blue.stop()
GPIO.cleanup()
