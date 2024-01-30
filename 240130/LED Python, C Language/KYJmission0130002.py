import RPi.GPIO as GPIO
import time

led_pin = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin,GPIO.OUT)

num = int(input("Write Num : "))

def Brightness(sec):
	for i in range(100):
		GPIO.output(led_pin,True)
		time.sleep(sec*0.01*i/100)
		GPIO.output(led_pin,False)
		time.sleep(sec*0.01*(100-i)/100)

def Darkness(sec):
	for i in range(100,0,-1):
		GPIO.output(led_pin,True)
		time.sleep(sec*0.01*i/100)
		GPIO.output(led_pin,False)
		time.sleep(sec*0.01*(100-i)/100)

if num == 1:
	GPIO.output(led_pin,True)
elif num == 2:
	GPIO.output(led_pin,False)
elif num == 3:
	for i in range(100):
		GPIO.output(led_pin,True)
		time.sleep(0.03*i/100)
		GPIO.output(led_pin,False)
		time.sleep(0.03*(100-i)/100)
elif num == 4:
	for i in range(100,0,-1):
		GPIO.output(led_pin,True)
		time.sleep(0.03*i/100)
		GPIO.output(led_pin,False)
		time.sleep(0.03*(100-i)/100)
elif num == 5:
	for i in range(100):
		GPIO.output(led_pin,True)
		time.sleep(0.03*i/100)
		GPIO.output(led_pin,False)
		time.sleep(0.03*(100-i)/100)
	for i in range(100,0,-1):
		GPIO.output(led_pin,True)
		time.sleep(0.03*i/100)
		GPIO.output(led_pin,False)
		time.sleep(0.03*(100-i)/100)
elif num == 6:
	sec = int(input("Write Sec : "))
	Brightness(sec)
	Darkness(sec)
