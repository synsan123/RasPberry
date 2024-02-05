import RPi.GPIO as GPIO
import time

red = 18

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(red, GPIO.OUT)

pwm = GPIO.PWM(red, 100)
pwm.start(100)

try:
    while True:
        keyboard = input("LED 0% = '0', LED 50% = '5', LED 100% = 't', Program Exit = 'x' : ")
        if keyboard == '0':
            pwm.ChangeDutyCycle(0)
        elif keyboard == '5':
            pwm.ChangeDutyCycle(50)
        elif keyboard == 't':
            pwm.ChangeDutyCycle(100)
        elif keyboard == 'x':
            break
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()