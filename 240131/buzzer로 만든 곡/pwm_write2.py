import RPi.GPIO as GPIO
import time

led_red = 18

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(led_red,GPIO.OUT)

pwm = GPIO.PWM(led_red,1000)
pwm.start(0)

try:
    while True:
        for t_high in range(0, 101):
            pwm.ChangeDutyCycle(t_high)
            time.sleep(0.2)
        for t_high in range(100, -1):
            pwm.ChangeDutyCycle(t_high)
            time.sleep(0.2)  
except KeyboardInterrupt:
    pass
pwm.stop()
GPIO.cleanup()
