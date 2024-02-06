import RPi.GPIO as GPIO
import time

SW1 = 22
led_red = 18
brightness = [0, 50, 100]
count = 0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(led_red, GPIO.OUT)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pwm = GPIO.PWM(led_red, 100)
pwm.start(100)
   
try:
    while True:
        buttoninput = GPIO.input(SW1)
        if buttoninput == GPIO.LOW:
            print("Pushed")
            pwm.ChangeDutyCycle(brightness[count])
            count = (count + 1) % 3
            time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()        