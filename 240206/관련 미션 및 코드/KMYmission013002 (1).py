import RPi.GPIO as GPIO
import time

led_pin = 18 # 1 for WiringPi

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

pwm = GPIO.PWM(led_pin, 100) # channel=led_pin frequency=100Hz
pwm.start(0)

while 1:
    print("1. LED 켜기\n")
    print("2. LED 끄기\n")
    print("3. LED 3초간 점점 밝기\n")
    print("4. LED 3초간 점점 어둡기\n")
    print("5. LED 3초간 점점 밝다가 3초간 점점 어둡기\n")
    print("6. 원하는 초 입력\n")
    print("0. 종료\n")

    number = int(input("원하는 기능: "))

    if number == 1:
        pwm.ChangeDutyCycle(100)
    elif number == 2:
        pwm.ChangeDutyCycle(0)
    elif number == 3:
        for t_high in range(0, 101, 1):
            pwm.ChangeDutyCycle(t_high)
            time.sleep(0.03)
    elif number == 4:
        for t_high in range(100, -1, -1):
            pwm.ChangeDutyCycle(t_high)
            time.sleep(0.03)
    elif number == 5:
        for t_high in range(0, 101, 1):
            pwm.ChangeDutyCycle(t_high)
            time.sleep(0.03)
        for t_high in range(100, -1, -1):
            pwm.ChangeDutyCycle(t_high)
            time.sleep(0.03)
    elif number == 6:
        timeN = int(input("원하는 시간: "))
        for t_high in range(0, 101, 1):
            pwm.ChangeDutyCycle(t_high)
            time.sleep(timeN*0.01)
        for t_high in range(100, -1, -1):
            pwm.ChangeDutyCycle(t_high)
            time.sleep(timeN*0.01)
    elif number == 0:
        break


GPIO.cleanup()