import RPi.GPIO as GPIO
import time

switch =22
LED = 4
flag = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # 내부풀다운 사용
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, False)

def swBlink(channel):      #callback 함수
   global flag
   if flag == False:
      GPIO.output(LED, True)
      print("interrupt")
      flag = True
      time.sleep(0.3)
   else:
      flag = False
      GPIO.output(LED, False)
      time.sleep(0.3)

#인터럽터핀에 라이징 신호가 인가되면 콜백함수로 리턴되어 실행
GPIO.add_event_detect(switch, GPIO.RISING, callback=swBlink)

try:
   while True:
      pass
except KeyboardInterrupt:
   print()
   GPIO.cleanup()