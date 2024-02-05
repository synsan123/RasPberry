import RPi.GPIO as GPIO
import time

buzzer = 24
SW1 = 22
count = 0

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pwm = GPIO.PWM(buzzer, 100)
pwm.start(0)

scale = [523, 587, 659, 698, 784, 880, 988, 1047]

try:
    while True:
        buttoninput = GPIO.input(SW1)
        if buttoninput == GPIO.LOW:
            print("Pushed")
            pwm.start(10.0)
            pwm.ChangeFrequency(scale[count])
            count = (count + 1) % 8
            time.sleep(0.5)
            pwm.stop()
except KeyboardInterrupt:
    GPIO.cleanup()   