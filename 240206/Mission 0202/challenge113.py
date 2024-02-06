import RPi.GPIO as GPIO
import time

buzzer = 24

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(buzzer, GPIO.OUT)

pwm = GPIO.PWM(buzzer, 100)
pwm.start(0)

def buzzer_start_end(Hz):
    pwm.start(10.0)
    pwm.ChangeFrequency(Hz)
    time.sleep(0.5)
    pwm.stop()

try:
    while True:
        keyboard = input("도 = 'a', 레 = 's', 미 = 'd', 파 = 'f', 솔 = 'g', 라 = 'r', 시 = 'l', 높은 도 = 'k', Exit = 'x' : ")
        if keyboard == 'a':
            buzzer_start_end(523)
        elif keyboard == 's':
            buzzer_start_end(587)
        elif keyboard == 'd':
            buzzer_start_end(659)
        elif keyboard == 'f':
            buzzer_start_end(698)
        elif keyboard == 'g':
            buzzer_start_end(784)
        elif keyboard == 'r':
            buzzer_start_end(880)
        elif keyboard == 'l':
            buzzer_start_end(988)
        elif keyboard == 'k':
            buzzer_start_end(1046)
        elif keyboard == 'x':
            break
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()