import RPi.GPIO as GPIO
import random
import time

led_red = 13
led_green = 18
led_blue = 19

ComputerPattern = []
MyPattern = [0, 0, 0, 0, 0, 0]
colors = [led_red, led_green, led_blue]

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_red,GPIO.OUT)
GPIO.setup(led_green,GPIO.OUT)
GPIO.setup(led_blue,GPIO.OUT)

pwm_red = GPIO.PWM(led_red,100)
pwm_green = GPIO.PWM(led_green,100)
pwm_blue = GPIO.PWM(led_blue,100)

def alloff():
    GPIO.output(led_red,False)
    GPIO.output(led_green,False)
    GPIO.output(led_blue,False)

def generPattern():
    return [random.choice(colors) for i in range(6)]

def turnOnOff(pattern, timeWrite):
    for i in pattern:
        GPIO.output(i, True)
        time.sleep(timeWrite)
        GPIO.output(i, False)
        time.sleep(timeWrite)

def WrongAnswer():
    for i in range(3):
        GPIO.output(led_red,True)
        time.sleep(1)
        GPIO.output(led_red,False)
        time.sleep(1)
        print("틀렸습니다")
    
def Answer():
    GPIO.output(led_red,True)
    time.sleep(0.5)        
    GPIO.output(led_red,False)
    time.sleep(0.5)
    GPIO.output(led_green,True)
    time.sleep(0.5)
    GPIO.output(led_green,False)
    time.sleep(0.5)
    GPIO.output(led_blue,True)
    time.sleep(0.5)
    GPIO.output(led_blue,False)
    time.sleep(0.5)
    print("정답입니다")

#게임 시작
alloff()
print("LED 패턴 암기 테스트")
time.sleep(1)
print("게임을 시작하지")
time.sleep(1)
print("이 게임은 순서대로 켜지는 LED의 패턴을 외우는 것이다.")
time.sleep(1)
print("패턴을 기억한 후 정답을 입력하도록")
time.sleep(1)
print("키보드의 키 중 아무거나 선택하여 누르면 시작할 것이다")
time.sleep(1)
print("행운을 빌지")
time.sleep(1)
input()
print("게임은 시작됐다. 패턴을 잘보도록")
time.sleep(1)

#패턴 생성
ComputerPattern = generPattern()

#생성된 패턴 점등
turnOnOff(ComputerPattern, 1)


#패턴 입력
print("패턴을 입력하도록 RED = 13 GREEN = 18 BLUE = 19")
#for i in range(6):
    #MyPattern = int(input())
# map함수는 연속으로 입력이 가능하도록 만들어줌 + 입력된 문자열 값을 int로 형변환
# split함수는 공백을 기준으로 문자열을 나눔
# 입력한 값을 정수형으로 형변환한 후 list에 저장하여 MyPattern에 저장
MyPattern = list(map(int,input().split()))

#패턴 판단
if ComputerPattern == MyPattern:
    Answer()
else:
    WrongAnswer()
    print("정답은 ", ComputerPattern, " 입니다")

GPIO.cleanup()


