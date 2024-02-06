import RPi.GPIO as GPIO
import time

SW1 = 22
SW2 = 23
SW3 = 24
count = 0
STEP_MOTOR = [16, 17, 18, 19]
angleArray = [45, 90, 180]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

for pin in STEP_MOTOR:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

StepCounter = 0
StepCount = 4

Seq = [[1, 0, 0, 0],
       [0, 1, 0, 0],
       [0, 0, 1, 0],
       [0, 0, 0, 1]]

def rotate_motor(angle): # 역방향 회전
    global StepCounter
    steps = int(5.75 * angle) # 오차 발생함(5.75는 장치의 정확한 회전각도가 아님)
    for _ in range(steps):
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
        if GPIO.input(SW1) == GPIO.LOW:
            print("Pushed. 45")
            rotate_motor(angleArray[0])
            time.sleep(0.1)
        elif GPIO.input(SW2) == GPIO.LOW:
            print("Pushed, 90")
            rotate_motor(angleArray[1])
            time.sleep(0.1)
        elif GPIO.input(SW3) == GPIO.LOW:
            print("Pushed, 180")
            rotate_motor(angleArray[2])
            time.sleep(0.1)    
except KeyboardInterrupt:
    GPIO.cleanup()