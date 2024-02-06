import RPi.GPIO as GPIO
import threading
import time

red = 12
green = 18

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

pwm_red = GPIO.PWM(red, 200)
pwm_green = GPIO.PWM(green, 200)
pwm_red.start(0)
pwm_green.start(0)

flag_exit = False
def t1():
        while True:
            print("\tGreen LED ON!")
            for t_high in range(0, 100):
                pwm_green.ChangeDutyCycle(t_high)
                time.sleep(0.013)
            for t_high in range(100, -1):
                pwm_green.ChangeDutyCycle(t_high)
                time.sleep(0.013) 
                if flag_exit: break

thread = threading.Thread(target=t1)
thread.start()

try:
        while True:
            print("main Red LED ON!")
            for t_high in range(0, 100):
                pwm_red.ChangeDutyCycle(t_high)
                time.sleep(0.007)
            for t_high in range(100, -1):
                pwm_red.ChangeDutyCycle(t_high)
                time.sleep(0.007)

except KeyboardInterrupt:
        pass
flag_exit = True
thread.join()

pwm_red.stop()
pwm_green.stop()
GPIO.cleanup()

