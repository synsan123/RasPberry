import RPi.GPIO as GPIO
import time
import threading
import queue

STEP_MOTOR = [16, 17, 18, 19]
led = [4, 5, 6]
SW1 = 22

StepCounter = 0
StepCount = 4
buttonState = 0

Que_Size = 30
MessageQue = queue.Queue(Que_Size)

Seq = [[1, 0, 0, 0],
       [0, 1, 0, 0],
       [0, 0, 1, 0],
       [0, 0, 0, 1]]

flag_exit = False

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for pin in STEP_MOTOR:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

for pin in led:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def rotate_motor(angle): # 역방향 회전
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

def AllOff():
    for pin in led:
        GPIO.output(pin,False)

def LED_State_Print_Interrupt(channel):
    global buttonState
    buttonState += 1
    if buttonState == 1:
        MessageQue.put("LED RED ON")
    elif buttonState == 2:
        MessageQue.put("LED GREEN ON")
    elif buttonState == 3:
        MessageQue.put("LED BLUE ON")
    elif buttonState == 4:
        MessageQue.put("LED All OFF")
        buttonState = 0

GPIO.add_event_detect(SW1, GPIO.FALLING, callback=LED_State_Print_Interrupt, bouncetime=200)

def StepMotor_KeyBoard_Thread():
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
        elif flag_exit:
            break

StepMotor_Thread = threading.Thread(target=StepMotor_KeyBoard_Thread)
StepMotor_Thread.start()

try:
    while True:
            led_data = MessageQue.get()
            if led_data == "LED RED ON":
                GPIO.output(led[0], True)
            elif led_data == "LED GREEN ON":
                GPIO.output(led[1], True)
            elif led_data == "LED BLUE ON":
                GPIO.output(led[2], True)
            elif led_data == "LED All OFF":
                AllOff()
except KeyboardInterrupt:
    flag_exit = True
    StepMotor_Thread.join()
GPIO.cleanup()
