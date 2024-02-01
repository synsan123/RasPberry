import RPi.GPIO as GPIO
import time

PIR = 27
led_red = 4
buzzer = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(led_red,GPIO.OUT)
GPIO.setup(PIR, GPIO.IN)

GPIO.setwarnings(False)

pwm = GPIO.PWM(buzzer, 1074)

try:
        while 1:
                pir_state = GPIO.input(PIR)
                if pir_state == True:
                        GPIO.output(led_red, True)
                        print("Motion Detected")
                        pwm.start(10.0) 
                        time.sleep(1)
                else:
                        GPIO.output(led_red, False)
                        pwm.stop()
                        time.sleep(1)
except KeyboardInterrupt:
        GPIO.cleanup()