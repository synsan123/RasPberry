import RPi.GPIO as GPIO
import threading
import time

red = 4
green = 5
blue = 6

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

GPIO.output(red,False)
GPIO.output(green,False)
GPIO.output(blue,False)

flag_exit = False
def t1():
        while True:
                print("\tGreen LED ON!")
                GPIO.output(green, True)
                time.sleep(1.3)
                GPIO.output(green, False)
                time.sleep(1.3)
                if flag_exit: break

def t2():
        while True:
                print("\tBlue LED ON!")
                GPIO.output(blue, True)
                time.sleep(1.7)
                GPIO.output(blue, False)
                time.sleep(1.7)
                if flag_exit: break

thread = threading.Thread(target=t1)
thread1 = threading.Thread(target=t2)
thread.start()
thread1.start()

try:
        while True:
                print("main Red LED ON!")
                GPIO.output(red,True)
                time.sleep(0.7)
                GPIO.output(red,False)
                time.sleep(0.7)

except KeyboardInterrupt:
        pass
flag_exit = True
thread.join()
thread1.join()

GPIO.output(red, False)
GPIO.output(green, False)
GPIO.output(blue, False)
GPIO.cleanup()
