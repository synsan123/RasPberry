import RPi.GPIO as GPIO
import time

SW1 = 22
led_red = 4
flag = True

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(led_red, GPIO.OUT)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(led_red, False)

def swBlink(channel):      #callback 함수
   global flag
   if flag == True:
      GPIO.output(led_red, True)
      print("interrupt, LED_ON!")
      flag = False
      time.sleep(0.3)
   else:
      flag = True
      GPIO.output(led_red, False)
      print("interrupt, LED_OUT!")
      time.sleep(0.3)

GPIO.add_event_detect(SW1, GPIO.FALLING, callback=swBlink, bouncetime=200)

try:
   while True:
      pass
except KeyboardInterrupt:
   print()
   GPIO.cleanup()