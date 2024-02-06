import RPi.GPIO as GPIO
import time

led_red = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_red,GPIO.OUT)

pwm = GPIO.PWM(led_red,100)

GPIO.output(led_red,True)
time.sleep(0.5)