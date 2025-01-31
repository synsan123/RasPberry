from flask import Flask, render_template, url_for, redirect   # flask 모듈과 관련함수 불러옴
import RPi.GPIO as GPIO     # 라즈베리파이 GPIO 관련 모듈을 불러옴
import time                 # 시간 관련 모듈 불러옴
import threading            # 스레드 관련 모듈 불러옴

GPIO.setmode(GPIO.BCM)      # GPIO 핀들의 번호를 지정하는 규칙 설정

led_pin_dict = {'red': 14, 'green': 15, 'blue': 18}     # LED 핀들을 딕셔너리 변수로 선언
GPIO.setup(led_pin_dict['red'], GPIO.OUT)               # 각각의 LED 핀들을 출력으로 설정
GPIO.setup(led_pin_dict['green'], GPIO.OUT)  
GPIO.setup(led_pin_dict['blue'], GPIO.OUT)   

# 각각의 두 종류 스레드의 상태를 나타내는 변수(0이면 진행상황 안보임(대기), 1이면 보임(실행))
blink_thread_state = {'red':0, 'green':0, 'blue':0}
time_thread_state = {'red':0, 'green':0, 'blue':0} 
app = Flask(__name__)               # Flask라는 이름의 객체 생성
# 외부 변수인 thread_state[color]의 값이 1이면 LED를 3초간 켜주고 꺼줌
# 꺼주고 난 뒤에 thread_state[color]를 0으로 만들어주어서 다시 켜지지 않음
# 다시 켜려면 웹사이트의 버튼을 눌러서 thread_state[color]를 1로 만들어주어야 함
def LED_on_3_sec_core(color):                           # 3초간 LED를 켜주는 함수 선언
    while True:                                         # 무한루프
        past_time = int(time.time())                    # 과거시간 측정(정수로)  
        while time_thread_state[color]:                      # 해당 컬러의 스레드 상태가 1이면(0이면 과거시간만 측정함)
            GPIO.output(led_pin_dict[color], GPIO.HIGH) # 해당 컬러의 LED를 켜줌
            current_time = int(time.time())             # 현재시간 측정
            if current_time - past_time > 2.9:            # 현재시간 - 과거시간이 3초 이상이면(3초가 지나면) 
                GPIO.output(led_pin_dict[color], GPIO.LOW)  # 3초가 지났으니 LED를 꺼줌
                time_thread_state[color] = False             # 해당 컬러의 스레드 상태를 0으로 해줌(더이상 켜고 꺼지지 않음)
                
# 외부 변수인 thread_state[color]의 값이 1이면 LED를 1초간격으로 켜주고 꺼줌
# 사실 LED 상태를 1초마다 갱신을 해주다가, thread_state[color]가 1일때만 LED 핀에 반영을 해주는 것
def LED_blink_core():                      # 3초간 LED를 켜주는 함수 선언
    past_time = int(time.time())                # 과거시간 측정(정수로)
    led_state_dict = {'red': 0, 'green': 0, 'blue': 0}  # LED의 현재상태를 나타내는 변수
    while True:                                 # 무한루프
        current_time = int(time.time())         # 현재시간 측정(정수로)
        if current_time - past_time > 0.9:        # 현재시간 - 과거시간이 1초 이상이면(1초가 지나면) 
            for color_idx in ['red', 'green', 'blue']: # 모든 색상(3가지)에 대해
                led_state_dict[color_idx] = not led_state_dict[color_idx]   # LED의 현재 상태 토글
                if blink_thread_state[color_idx]:       # 해당 컬러의 스레드 상태가 1이면(스레드를 실행하도록 설정하면)
                    GPIO.output(led_pin_dict[color_idx], led_state_dict[color_idx])    # 해당 LED 핀에 LED 상태를 반영(켜주거나 꺼주도록)
            past_time = current_time            # 과거시간을 현재시간으로 갱신

# 3개의 색상에 해당하는 스레드를 2종류 만들어줌(위의 함수를 백그라운드에서 계속 돌리는 것)
blink_thread = threading.Thread(target=LED_blink_core, args=())
time_thread_dict = {'red': threading.Thread(target=LED_on_3_sec_core, args=('red', )), 
                'green' : threading.Thread(target=LED_on_3_sec_core, args=('green', )), 
                'blue': threading.Thread(target=LED_on_3_sec_core, args=('blue', ))}

# 각 스레드들을 모두 실행
blink_thread.start()
for color_idx in ['red', 'green', 'blue']:    
    time_thread_dict[color_idx].start()
    
@app.route('/')                     # 기본 주소
def home():                         # 여기서 led3sec1sec.html을 화면에 보여줌
    return render_template('led3sec1sec.html')  

@app.route('/<color>/<int:state>')            # 각각의 LED를 켜고 끄기 위한 주소(ON, OFF 버튼을 눌렀을때 실행됨)
def LED_control(color, state):                # 각각의 LED를 켜고 끄기 위한 뷰함수
    time_thread_state[color] = False          # 해당 color의 스레드가 실행중이면 대기로(ON, OFF 버튼 누른게 우선)
    blink_thread_state[color] = False         # 
    GPIO.output(led_pin_dict[color], state)   # 입력받은 color와 state를 바탕으로 LED를 조절해줌    
    return redirect(url_for('home'))          # LED 제어가 끝나면 기본주소로 돌아감

@app.route('/<color>/time')                   # 각각의 LED를 3초간 켜고 끄기 위한 주소(3 sec 버튼을 눌렀을 때 실행됨)
def LED_on_3_sec(color):                      # 해당 페이지의 뷰함수 정의
    blink_thread_state[color] = False         # 해당 컬러의 깜빡임 스레드를 대기로
    time_thread_state[color] = True           # 해당 컬러의 3초 스레드를 실행으로
    return redirect(url_for('home'))          # LED 제어가 끝나면 기본주소로 돌아감

@app.route('/<color>/blink')                  # 각각의 LED를 1초간격으로 깜빡이게 하기 위한 주소(blink 버튼을 눌렀을 때 실행됨)
def LED_blink(color):                         # 해당 페이지의 뷰함수 정의
    time_thread_state[color] = False          # 해당 color의 3초 스레드를 대기로
    blink_thread_state[color] = True          # 해당 컬러의 깜빡임 스레드를 실행으로
    return redirect(url_for('home'))          # LED 제어가 끝나면 기본주소로 돌아감

@app.route('/all/<int:state>')      # 모든 LED를 한번에 제어하는 주소
def whole_control(state):           # 모든 LED를 한번에 제어하기 위한 뷰함수
    if state is 0 or state is 1:                            # 입력받은 state가 0이나 1(ON, OFF 버튼을 눌렀으면)
        for color_idx in ['red', 'green', 'blue']:          # 각각의 색상값에 대해
            time_thread_state[color_idx] = False            # 모든 스레드를 대기로
            blink_thread_state[color_idx] = False           #
            GPIO.output(led_pin_dict[color_idx], state)     # 각각의 LED 핀들에 state를 인가해서 켜거나 꺼줌
    elif state is 2:                                        # 입력받은 state가 2이면 (blink 버튼을 눌렀으면)
        for color_idx in ['red', 'green', 'blue']:          # 각각의 색상값에 대해
            time_thread_state[color_idx] = False            # 해당 color의 3초 스레드는 대기로
            blink_thread_state[color_idx] = True            # 해당 color의 깜빡임 스레드는 실행으로
    elif state is 3:                                        # 입력받은 state가 3이면 (3 sec 버튼을 눌렀으면)
        for color_idx in ['red', 'green', 'blue']:          # 각각의 색상값에 대해
            blink_thread_state[color_idx] = False            # 해당 color의 깜빡임 스레드는 대기로
            time_thread_state[color_idx] = True            # 해당 color의 3초 스레드는 실행으로  
    return redirect(url_for('home'))      # LED 제어가 끝나면 기본주소로 돌아감

if __name__ == "__main__":  # 웹사이트를 호스팅하여 접속자에게 보여주기 위한 부분
   app.run(host="192.168.0.31", port = "8080")
   # host는 현재 라즈베리파이의 내부 IP, port는 임의로 설정
   # 해당 내부 IP와 port를 포트포워딩 해두면 외부에서도 접속가능