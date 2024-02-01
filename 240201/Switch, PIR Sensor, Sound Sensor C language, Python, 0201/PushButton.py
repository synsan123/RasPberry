import RPi.GPIO as GPIO
import time

# 사용할 GPIO 핀의 번호를 설정
button_pin1 = 22
button_pin2 = 23
button_pin3 = 24
button_pin4 = 25
led_red = 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #핀모드 설정

# 버튼 핀의 입력설정
GPIO.setup(button_pin1, GPIO.IN)
GPIO.setup(button_pin2, GPIO.IN)
GPIO.setup(button_pin3, GPIO.IN)
GPIO.setup(button_pin4, GPIO.IN)
GPIO.setup(led_red, GPIO.OUT)

while 1:
    if GPIO.input(button_pin1) == GPIO.LOW:
        print("Button 1 pushed!")
        GPIO.output(led_red,True)
        time.sleep(1)
        GPIO.output(led_red,False)
    time.sleep(0.1)
    if GPIO.input(button_pin2) == GPIO.LOW:
        print("Button 2 pushed!")
    time.sleep(0.1)
    if GPIO.input(button_pin3) == GPIO.LOW:
        print("Button 3 pushed!")
    time.sleep(0.1)
    if GPIO.input(button_pin4) == GPIO.LOW:
        print("Button 4 pushed!")
    time.sleep(0.1)
GPIO.cleanup()