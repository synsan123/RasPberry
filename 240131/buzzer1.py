import RPi.GPIO as GPIO
import time

buzzer = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT)

pwm = GPIO.PWM(buzzer, 1.0)
pwm.start(10.0)

#도(0) 레(1) 미(2) 파(3) 솔(4) 라(5) 시(6) 파#(7), 도#(8)
#scale = [262, 294, 330, 349, 392, 440, 494, 370]
scale = [523, 587, 659, 698, 784, 880, 988, 1047]
twinkle = [4,2,2,
           3,1,1,
           0,1,2,3,4,4,4,
           4,2,2,2,3,1,1,
           0,2,4,4,2,2,2,
           1,1,1,1,1,2,3,
           2,2,2,2,2,3,4,
           4,2,2,
           3,1,1,
           0,2,4,4,2,2,2]

try:
    for i in range(0,54):
        pwm.ChangeFrequency(scale[twinkle[i]])
        if i == 2 or i == 5 or i == 12 or i == 19 or i == 26 or i == 33 or i == 40 or i == 43 or i == 46 or i == 53:
            time.sleep(1)
        else:
            time.sleep(0.5)
    pwm.stop()
finally:
    GPIO.cleanup()
