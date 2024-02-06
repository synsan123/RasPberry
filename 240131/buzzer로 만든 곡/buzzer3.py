import RPi.GPIO as GPIO
import time

buzzer = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT)

pwm = GPIO.PWM(buzzer, 1.0)
pwm.start(10.0)

def musicstop(sec):
    pwm.stop()
    time.sleep(sec)
    pwm.start(10.0)

#도(0) 레(1) 미(2) 파(3) 솔(4) 라(5) 시(6) 도(7),
#높은레(8), 미(9), 파(10), 솔(11), 라(12), 시(13), 도(14)
#scale = [262, 294, 330, 349, 392, 440, 494, 370]
scale = [523, 587, 659, 698, 784, 880, 988, 1047,
        1174, 1318, 1397, 1568, 1760, 1975, 2093]
twinkle = [4, 5, 7, 2,
           8, 7, 7, 6, 7,
           5, 7, 9, 12, 12, 12, 13, 11, 10,] 

try:
    for i in range(0,18):
        pwm.ChangeFrequency(scale[twinkle[i]])
        if i == 0 or i == 2 or i == 5 or i == 9 or i == 11 or i == 15 or i == 17:
            time.sleep(0.5)
        elif i == 1 or i == 4 or i == 10 or i == 14 or i == 16:
             time.sleep(0.6875)
        elif i == 3 or i == 8:
            time.sleep(1)
        elif i == 6 or i == 7 or i == 13:
            time.sleep(0.625)
        elif i == 12:
            time.sleep(0.88)
    pwm.stop()
finally:
    GPIO.cleanup()
