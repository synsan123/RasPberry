import RPi.GPIO as GPIO     # 모듈 RPi.GPIO를 사용하겠다는 뜻임(as로 명명가능)
import time                 # time.sleep을 쓰기위해 import로 선언

switch1 = 22                  # 입력핀 설정
LED = 4
state = 1
GPIO.setmode(GPIO.BCM)      # BCM 모드 사용(pin은 BCM으로 쓰겠다는 뜻)

GPIO.setup(switch1, GPIO.IN) # 핀모드(입력) (출력으로 사용하려면 GPIO.OUT으로 사용)
GPIO.setup(LED, GPIO.OUT)

GPIO.output(LED, False)   # 처음 코드 실행때는 불을 끈 상태에서 시작

try:
   while True:
      if GPIO.input(switch1) == GPIO.LOW:
         print("Pushed")
         if (state == 1):           # state가 1이면 불을 킴(홀수)
            GPIO.output(LED, True)
         else:                      # state가 짝수면 불을 끔
            GPIO.output(LED, False)
         time.sleep(0.3)
         state = state + 1          # 스위치 누를때마다 +1해줌
         state = state % 2          # 스위치 누를때마다 나머지연산으로 홀짝을 구분

except KeyboardInterrupt:
   GPIO.cleanup()