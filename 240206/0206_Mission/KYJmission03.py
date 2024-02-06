import RPi.GPIO as GPIO
import time

buzzer = 18

button_pin1 = 22
button_pin2 = 23
button_pin3 = 24
button_pin4 = 25

led_red = 4
led_green = 5
led_blue = 6

GPIO.setmode(GPIO.BCM) #핀모드 설정
GPIO.setwarnings(False)

GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(led_red, GPIO.OUT)
GPIO.setup(led_green, GPIO.OUT)
GPIO.setup(led_blue, GPIO.OUT)

GPIO.setup(button_pin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_pin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_pin3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_pin4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.output(led_red,False)
GPIO.output(led_green,False)
GPIO.output(led_blue,False)

pwm = GPIO.PWM(buzzer, 1.0)

def Music_One():
    pwm.start(10.0)
    scale = [262, 294, 330, 349, 392, 440, 494]
    twinkle = [1,1,5,5,6,6,5,4,4,3,3,2,2,1,5,5,4,4,3,3,2,5,5,4,4,3,3,2,1,1,5,5,6,6,5,4,4,3,3,2,2,1]

    try:
        for i in range(0,42):
            pwm.ChangeFrequency(scale[twinkle[i] - 1])
            GPIO.output(led_red,True)
            if i == 6 or i == 13 or i == 20 or i == 27 or i == 34 or i == 41:
                time.sleep(1)
            else:
                time.sleep(0.5)
        pwm.stop()
        GPIO.output(led_red,False)
    except KeyboardInterrupt:
        pwm.stop()
        GPIO.output(led_red,False)

def Music_Two():
    pwm.start(10.0)
    scale = [523, 587, 659, 698, 784, 880, 988, 1047]
    twinkle = [4,2,2,
               3,1,1,
               0,1,2,3,4,4,4,
               4,2,2,2,3,1,1,
               0,2,4,4,2,2,2,
               1,1,1,1,1,2,3,
               2,2,2,2,2,3,4,
               4,2,2,
               3,1,1,
               0,2,4,4,2,2,2]

    try:
        for i in range(0,54):
            pwm.ChangeFrequency(scale[twinkle[i]])
            GPIO.output(led_green,True)
            if i == 2 or i == 5 or i == 12 or i == 19 or i == 26 or i == 33 or i == 40 or i == 43 or i == 46 or i == 53:
                time.sleep(1)
            else:
                time.sleep(0.5)
        pwm.stop()
        GPIO.output(led_green,False)
    except KeyboardInterrupt:
        pwm.stop()
        GPIO.output(led_green,False)

def Music_Three():
    pwm.start(10.0)
    scale = [523, 587, 659, 698, 784, 880, 988, 1047]
    twinkle = [4,4,5,5,4,4,2,
               4,4,2,2,1,
               4,4,5,5,4,4,2,
               4,2,1,2,0] 

    try:
        for i in range(0,24):
            pwm.ChangeFrequency(scale[twinkle[i]])
            GPIO.output(led_blue,True)
            if i == 6 or i == 18:
                time.sleep(1)
            elif i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 7 or i == 8 or i == 9 or i == 10 or i == 12 or i == 13 or i == 14 or i == 15 or i == 16 or i == 17 or i == 19 or i == 20 or i == 21 or i == 22:
                time.sleep(0.5) 
            elif i == 11 or i == 23:
                time.sleep(1.2)
        pwm.stop()
    except KeyboardInterrupt:
        pwm.stop()
        GPIO.output(led_blue,False)
       

while True:
    if GPIO.input(button_pin1) == GPIO.LOW:
        print("Button 1 pushed!")
        Music_One()
    elif GPIO.input(button_pin2) == GPIO.LOW:
        print("Button 2 pushed!")
        Music_Two()
    elif GPIO.input(button_pin3) == GPIO.LOW:
        print("Button 3 pushed!")
        Music_Three()
    elif GPIO.input(button_pin4) == GPIO.LOW:
        print("Button 4 pushed!")
        GPIO.output(led_red,False)
        GPIO.output(led_green,False)
        GPIO.output(led_blue,False)
        break
GPIO.cleanup()
