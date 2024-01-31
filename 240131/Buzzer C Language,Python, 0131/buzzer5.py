import RPi.GPIO as GPIO
import time

buzzer = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setwarnings(False)

pwm = GPIO.PWM(buzzer, 262)
pwm.start(50.0) #듀티비를 50%로 높여 설정함
time.sleep(1.5) #1.5초간 음이 울리도록 시간지연

pwm.stop()
GPIO.cleanup()
