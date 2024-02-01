import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(27, GPIO.IN)

while 1:
    if GPIO.input(27):
        print ("Detected")
    else:
        print ("Not Detected")
    time.sleep(0.5)

GPIO.cleanup()