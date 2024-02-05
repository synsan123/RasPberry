#360도 무한회전
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

Seq = [[0,0,0,1],
       [0,0,1,0],
       [0,1,0,0],
       [1,0,0,0]]

try:
    while True:
        for pin in range(0, 4):
            xpin = STEP_MOTOR[pin]
            if Seq[StepCounter][pin] != 0:
                GPIO.output(xpin,True)
            else:
                GPIO.output(xpin,False)

        StepCounter += 1

        if(StepCounter == StepCount):
            StepCounter = 0
        if(StepCounter < 0):
            StepCounter = StepCount

        time.sleep(0.01)
except KeyboardInterrupt:
    GPIO.cleanup()






GPIO.cleanup()

