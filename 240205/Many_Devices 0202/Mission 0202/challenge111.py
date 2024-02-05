import RPi.GPIO as GPIO
import time

red = 4

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(red, GPIO.OUT)

GPIO.output(red,False)

try:
    while True:
        keyboard = input("LED ON = 'N', LED OFF = 'F', Program Exit = 'x' : ")
        if keyboard == 'N':
            GPIO.output(red,True)
        elif keyboard == 'F':
            GPIO.output(red,False)
        elif keyboard == 'x':
            break
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()