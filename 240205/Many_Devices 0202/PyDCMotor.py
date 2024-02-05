from gpiozero import Motor
from time import sleep

# 모터 핀 세팅.
motorR = Motor(forward=12,backward=13) # 모터 객체 생성.

# speed 변수에 0~1 사이의 값을 넣어서 속도를 조절할 수 있다. 수가 클수록 빠르다.
# 3초 동안 전진
motorR.forward(speed=0.7)
sleep(3)

# 3초 동안 후진
motorR.backward(speed=0.7)
sleep(3)

# 3초 동안 전진
motorR.forward(speed=0.7)
sleep(3)

# 3초 동안 후진
motorR.backward(speed=0.7)
sleep(3)

# 모터 정지.
motorR.stop()