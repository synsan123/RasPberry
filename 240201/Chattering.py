import RPi.GPIO as GPIO
import time
import random

# GPIO 핀 설정
SW1 = 22
SW2 = 23
SW3 = 24
SW4 = 25
led_pins = [4, 5, 6]
buzzer_pin = 18

# 초기화
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# LED 핀을 출력으로 설정
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)

# 버튼 핀을 입력으로 설정
# 내부풀업을 사용하여 스위치가 입력상태가 아닐 때 스위치는 HIGH를 유지. 스위치를 누르면(입력하면) LOW가 됨
buttons = [SW1, SW2, SW3, SW4]
for button in buttons:
    GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# 부저 핀을 출력으로 설정
GPIO.setup(buzzer_pin, GPIO.OUT)

# 부저의 PWM을 설정
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
        GPIO.output(color, GPIO.HIGH)
        play_tone(0.3, color)
        GPIO.output(color, GPIO.LOW)
        time.sleep(0.3)

# 버튼 콜백 함수는 GPIO라이브러리의 add_event_detect()함수를 통해 콜백 함수로 등록됨
# 이 함수는 스위치가 눌리면 호출되는 함수임
def button_callback(channel):
    global user_input
    # 눌린 버튼의 번호를 user_input 리스트에 추가
    # index(channel)은 리스트 내에서 channel이라는 값의 인덱스를 반환하는 메소드(함수)
    # channel에는 콜백함수가 호출될 때 GPIO핀 번호가 들어감
    # buttons = [SW1, SW2, SW3, SW4]임 
    # 그리고 각 핀 번호는 22, 23, 24, 25임
    # SW1를 누르면 index(channel)함수는 buttons 리스트의 SW1의 위치인 0을 반환함
    # 이 값에 4를 더해서 user_input 리스트에 4를 추가함.
    # 이유는 user_input != sequence 부분에서 sequence는 led_pins의 값인 4, 5, 6 중에 하나를 가지고 있음
    # 그렇다면 0 ~ 4값을 가진 user_input은 무조건 조건을 만족시켜서 게임을 끝내버림
    # 그렇기 때문에 4를 더하여 각각 [4 ,5, 6, 7]의 값을 만들어 조건을 만족시키지 않아 게임을 이어나감
    user_input.append(buttons.index(channel) + 4)
    play_tone(0.1)

def main():
    global user_input
    try:
        sequence = []
        while True:
            sequence.append(random.choice(led_pins)) # 랜덤으로 출력된 LED를 sequence 배열(리스트)에 하나 추가한다.
            play_sequence(sequence) # 랜덤으로 출력된 LED가 추가된 시퀀스 리스트를 재생한다.

            user_input = []
            for _ in range(len(sequence)): # 시퀀스리스트의 길이만큼 사용자 입력을 받는다.
                while len(user_input) < len(sequence):
                    pass

            if user_input != sequence: # 사용자 입력이 시퀀스와 다르면 게임 종료
                print("Game Over! Your score:", len(sequence) - 1) # 점수 출력
                break

            time.sleep(1)

    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    for button in buttons:
        # 스위치의 채터링 현상을 잡는 디바운스 기술을 사용.
        # 디바운스는 스위치를 누르거나 땔 때 발생하는 빠른 전압 변화를 필터링하여 안정적인 입력을 받는 방법
        GPIO.add_event_detect(button, GPIO.FALLING, callback=button_callback, bouncetime=200)
    main()
