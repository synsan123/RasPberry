import RPi.GPIO as GPIO
import time

buzzer = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT)

pwm = GPIO.PWM(buzzer, 1.0)
pwm.start(3.0)

#도(0) 레(1) 미(2) 파(3) 솔(4) 라(5) 시(6) 도(7),
#scale = [262, 294, 330, 349, 392, 440, 494, 370]
scale = [523, 587, 659, 698, 784, 880, 988, 1047]
twinkle = [4,4,5,5,4,4,2,
           4,4,2,2,1,
           4,4,5,5,4,4,2,
           4,2,1,2,0] 

try:
    for i in range(0,24):
        pwm.ChangeFrequency(scale[twinkle[i]])
        if i == 6 or i == 18:
            time.sleep(1)
        elif i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 7 or i == 8 or i == 9 or i == 10 or i == 12 or i == 13 or i == 14 or i == 15 or i == 16 or i == 17 or i == 19 or i == 20 or i == 21 or i == 22:
            time.sleep(0.5) 
        elif i == 11 or i == 23:
            time.sleep(1.2)
    pwm.stop()
finally:
    GPIO.cleanup()
