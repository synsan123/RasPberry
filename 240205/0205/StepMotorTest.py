from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

SW1 = 22
STEP_MOTOR = [16, 17, 18, 19]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for pin in STEP_MOTOR:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

StepCounter = 0
StepCount = 4

Seq = [[1, 0, 0, 0],
       [0, 1, 0, 0],
       [0, 0, 1, 0],
       [0, 0, 0, 1]]

def rotate_motor(angle): 
    global StepCounter
    steps = int(5.75 * angle) 
    for i in range(steps):
        for pin in range(4):
            xpin = STEP_MOTOR[pin]
            if Seq[StepCounter][pin] != 0:
                GPIO.output(xpin, True)
            else:
                GPIO.output(xpin, False)
        StepCounter += 1
        if StepCounter == StepCount:
            StepCounter = 0
        if StepCounter < 0:
            StepCounter = StepCount
        time.sleep(0.01)

@app.route('/')
def home():
    return render_template('stepMotor.html')  

@app.route('/motor_control') 
def motor_control():
    angle = request.args.get('angle') 
    angle = int(angle) 
    if angle < 0: angle = 0
    elif angle > 180: angle = 180
    rotate_motor(angle) 
    return render_template('stepMotor.html', angle=angle)

if __name__ == "__main__": 
   app.run(host="192.168.0.31", port = "8080")
