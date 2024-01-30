import RPi.GPIO as GPIO
import time

led_red = 4
led_green = 5
led_blue = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_red,GPIO.OUT)
GPIO.setup(led_green,GPIO.OUT)
GPIO.setup(led_blue,GPIO.OUT)

for i in range(20):
	print("LED_RED ON!")
	GPIO.output(led_red,True)
	time.sleep(0.5)
	GPIO.output(led_red,False)
	time.sleep(0.5)
	print("LED_RED OFF!")
	print("LED_GRREN ON!")
	GPIO.output(led_green,True)
	time.sleep(0.5)
	GPIO.output(led_green,False)
	time.sleep(0.5)
	print("LED_GREEN OFF!")
	print("LED_BLUE ON!")
	GPIO.output(led_blue,True)
	time.sleep(0.5)
	GPIO.output(led_blue,False)
	time.sleep(0.5)
	print("LED_BLUE OFF")
	time.sleep(1)
GPIO.clenup()
