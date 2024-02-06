import RPi.GPIO as GPIO
import time

STEP_MOTOR = [16, 17, 18, 19]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for pin in STEP_MOTOR:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

StepCounter = 0
StepCount = 4

Seq = [[1, 0, 0, 0],
       [0, 1, 0, 0],
       [0, 0, 1, 0],
       [0, 0, 0, 1]]

def rotate_motor(angle): # 정방향 회전
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

try:
    while True:
        key = input("키보드 입력. q = 0도, w = 90도, e = 180도, x = exit : ")
        if key == 'q':
            rotate_motor(0)  # 0도로 회전. 0도이기 때문에 움직임이 없음
        elif key == 'w':
            rotate_motor(90)  # 90도로 회전
        elif key == 'e':
            rotate_motor(180)  # 180도로 회전
        elif key == 'x':
            break
except KeyboardInterrupt:
    GPIO.cleanup()
