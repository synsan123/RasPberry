import RPi.GPIO as GPIO
import time
import random

# GPIO 핀 설정
button_pin1 = 22 #SW1 연결
button_pin2 = 23 #SW2 연결
button_pin3 = 24 #SW3 연결
button_pin4 = 25 #SW4 연결
# LED 핀 배열 설정
led_pins = [4, 5, 6] # R, G, B LED 연결 (순서대로 빨간색, 초록색, 파란색)
buzzer_pin = 18 # Buzzer

# 초기화
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# LED 핀을 출력으로 설정
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)

# 버튼 핀을 입력으로 설정
GPIO.setup(button_pin1, GPIO.IN)
GPIO.setup(button_pin2, GPIO.IN)
GPIO.setup(button_pin3, GPIO.IN)
GPIO.setup(button_pin4, GPIO.IN)

# 부저 핀을 출력으로 설정 
GPIO.setup(buzzer_pin, GPIO.OUT)

# 부저의 PWM을 설정 (100Hz) 
buzzer = GPIO.PWM(buzzer_pin, 100)

# 시간과 컬러를 입력받아 소리를 재생한다.(빨간색은 262Hz, 초록색은 294Hz, 파란색은 330Hz)
def play_tone(duration, color=0):
    if color == 4:
        buzzer.ChangeFrequency(262)
    elif color == 5:
        buzzer.ChangeFrequency(294)
    elif color == 6:
        buzzer.ChangeFrequency(330)
    buzzer.start(10)
    time.sleep(duration)
    buzzer.stop()

#순서대로 LED를 켜고 소리를 낸다.
def play_sequence(sequence):
    for color in sequence:
        GPIO.output(color, GPIO.HIGH) # LED 켜기 GPIO.HIGH는 1을 의미
        play_tone(0.3, color)
        GPIO.output(color, GPIO.LOW) # LED 끄기 GPIO.LOW는 0을 의미
        time.sleep(0.3)

#사용자 입력을 받는 함수 
def get_user_input():
    while True:
        if GPIO.input(button_pin1) == GPIO.LOW: # 버튼이 눌리면 해당 색깔을 반환
            return 4
        elif GPIO.input(button_pin2) == GPIO.LOW: # 버튼이 눌리면 해당 색깔을 반환
            return 5
        elif GPIO.input(button_pin3) == GPIO.LOW: # 버튼이 눌리면 해당 색깔을 반환 
            return 6

def main():
    #try-except-finally 구문을 사용하여 GPIO를 정리한다.
    try:
        #시퀀스를 저장할 리스트 시퀀스는 랜덤한 LED 시퀀스를 저장한다.
        sequence = []
        #무한반복
        while True:
            sequence.append(random.choice(led_pins)) # 랜덤으로 LED를 하나 추가한다.
            play_sequence(sequence) # 추가된 시퀀스를 재생한다.

            #사용자의 입력을 받아 저장하는 리스트
            user_input = []
            for _ in range(len(sequence)): # 시퀀스의 길이만큼 사용자 입력을 받는다.
                button_pressed = get_user_input() # 사용자 입력을 받는다.
                user_input.append(button_pressed) # 사용자 입력을 추가한다.
                play_tone(0.1) # 사용자 입력을 받을때 소리를 재생한다.
                #다음 버튼을 누를때까지의 딜레이
                time.sleep(0.3)

            if user_input != sequence: # 사용자 입력이 시퀀스와 다르면 게임 종료
                print("Game Over! Your score:", len(sequence) - 1) # 점수 출력
                break
            
            # 4번째 버튼을 누르면 게임 종료
            if GPIO.input(button_pin4) == GPIO.LOW:
                print("강제 종료! Your score:", len(sequence) - 1) # 점수 출력
                break

            time.sleep(1)
            
    except KeyboardInterrupt:
        pass
    #예외가 발생하지 않았어도 마지막에 GPIO 정리
    finally:
        GPIO.cleanup()

#메인함수 호출
if __name__ == "__main__":
    main()
