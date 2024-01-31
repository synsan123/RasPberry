import RPi.GPIO as GPIO
import random
import time

def Answer():
    GPIO.output(led_red,False)
    GPIO.output(led_green,False)
    GPIO.output(led_blue,False)
    time.sleep(1)
    GPIO.output(led_red,True)
    time.sleep(1)
    GPIO.output(led_green,True)
    time.sleep(1)
    GPIO.output(led_blue,True)
    time.sleep(1)
    GPIO.output(led_red,False)
    GPIO.output(led_green,False)
    GPIO.output(led_blue,False)
    print("정답입니다")

def Wrong_Answer():
    GPIO.output(led_red,False)
    GPIO.output(led_green,False)
    GPIO.output(led_blue,False)
    GPIO.output(led_red,True)
    time.sleep(1)
    GPIO.output(led_red,False)
    time.sleep(1)
    GPIO.output(led_red,True)
    time.sleep(1)
    GPIO.output(led_red,False)
    time.sleep(1)
    GPIO.output(led_red,True)
    time.sleep(1)
    GPIO.output(led_red,False)
    print("틀렸습니다")

led_red = 4
led_green = 5
led_blue = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_red,GPIO.OUT)
GPIO.setup(led_green,GPIO.OUT)
GPIO.setup(led_blue,GPIO.OUT)

print("         빛의 삼원색 게임            ")
print("- 색을 확인하고 합쳐지면 어떤 색이 되는지 맞춰보자 -")
print("-----------------------------------------------------")

GPIO.output(led_red,False)
GPIO.output(led_green,False)
GPIO.output(led_blue,False)

rand_color = [0, 0, 0]
if random.randint(0, 2) != 0:
    rand_color[0] = random.randint(1, 3)
    rand_color[1] = random.randint(1, 3)
    if rand_color[0] == rand_color[1]:
        rand_color[1] == random.randint(1,3)
else: rand_color[2] = 4

time.sleep(2)
if rand_color[0] == 1 and rand_color[1] == 2:
    GPIO.output(led_red,True)
    GPIO.output(led_green,True)
elif rand_color[0] == 2 and rand_color[1] == 1:
    GPIO.output(led_red,True)
    GPIO.output(led_green,True)
elif rand_color[0] == 1 and rand_color[1] == 3:    
    GPIO.output(led_red,True)
    GPIO.output(led_blue,True)
elif rand_color[0] == 3 and rand_color[1] == 1:
    GPIO.output(led_red,True)
    GPIO.output(led_blue,True)
elif rand_color[0] == 2 and rand_color[1] == 3:
    GPIO.output(led_green,True)
    GPIO.output(led_blue,True)
elif rand_color[0] == 3 and rand_color[1] == 2:
    GPIO.output(led_green,True)
    GPIO.output(led_blue,True)
elif rand_color[2] == 4:
    GPIO.output(led_red,True)
    GPIO.output(led_green,True)
    GPIO.output(led_blue,True)

print("랜덤하게 켜진 LED의 색을 보고 아래에서 정답을 선택하라")
print("-----------------------------------------------------")
print("1. yellow")
print("2. magenta")
print("3. cyan")
print("4. white")
print("-----------------------------------------------------")

num = int(input("정답을 입력하시오 : "))

if rand_color[0] == 1 and rand_color[1] == 2 and num == 1:
    print("Yellow")
    Answer()
elif rand_color[0] == 2 and rand_color[1] == 1 and num == 1:
    print("Yellow")
    Answer()
elif rand_color[0] == 1 and rand_color[1] == 3 and num == 2:
    print("Magenta")
    Answer()
elif rand_color[0] == 3 and rand_color[1] == 1 and num == 2:
    print("Magenta")
    Answer()    
elif rand_color[0] == 2 and rand_color[1] == 3 and num == 3:
    print("Cyan")
    Answer()
elif rand_color[0] == 3 and rand_color[1] == 2 and num == 3:
    print("Cyan")
    Answer()    
elif rand_color[2] == 4 and num == 4:
    print("White")
    Answer()
else:
    Wrong_Answer()

GPIO.cleanup()

