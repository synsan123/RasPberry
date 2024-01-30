<h1>Raspberry Pi GPIO Pin 사용 및 LED </h1>
<p>1. cd ~, pwd 입력. 현재 디렉토리 확인</p>
<p>2. Terminal에서 git clone https://github.com/WiringPi/WiringPi 입력</p>
<p>3. cd WiringPi 입력</p>
<p>4. ./bulid 입력</p>
<p>5. gpio -v로 다운로드 및 버전 확인 </p>
<p>6. gpio readall 입력 </p>
<p>6.1. GPIO Pin 사용 가능하도록 작업 완료 </p>
<p>7. Terminal에서 nano led_rgb.c 또는 vi led_rgb.c 입력 후 코드 입력 </p>
<p>8. gcc -o led_rgb led_rgb.c -l wiringPi 입력하여 목적파일 및 컴파일하여 실행파일 생성</p>
<p>9. ./led_rgb 입력하여 실행 </p>
<p>-------------------------------------------------------------------------------------------- </p>
<p>1. cd ~/Documents, mkdir 0130, cd 0130, mv ~/WiringPi/led*.* ~/Documents/0130 입력 </p>
<p>1.1 WiringPi디렉토리에서 /Documents/0130디렉토리로 led파일로 이동</p>
<p>2. nano에서 ctrl + K가 오려두기. ctrl + 6 입력하여 복사모드 후 원하는 곳 지정. alt + 6으로 복사. ctrl + u로 붙여넣기</p>
<p>-------------------------------------------------------------------------------------------- </p>
<p>1. nano ledRed.py 입력</p>
<p>2. import RPi.GPIO as GPIO 입력, import time 입력 </p>
<p>3. Code 입력 후 저장. Terminal에서 sudo python ./ledRed.py 입력하여 실행</p>
<p>-------------------------------------------------------------------------------------------- </p>
<p>1. sudo apt install samba samba-common-bin 입력 </p>
<p>2. samba -V 입력</p>
<p>3. sudo smbpasswd -a busan 입력 후 비번 2번 입력</p>
<p>4. sudo nano /etc/samba/smb.conf 입력</p>
<p>5. profiles를 찾아서 세미콜론 부분 다 없앰. 
<p>   profiles를 pi로 변경. 이후 아래에</p>
<p>   commnet = superuser</p>
<p>   path = /home/</p>
<p>   valid users = busan</p>
<p>   guest ok = no</p>
<p>   browseable = yes</p>
<p>   writable = yes</p>
<p>   create mask = 0777</p>
<p>   directory mask = 0777 변경 후 ctrl + o 후 enter로 저장 ctrl + x로 종료 </p>
<p>6. sudo service smbd restart 입력</p>
<p>7. 윈도우 탐색기에서 \\Raspberry Pi IP주소 입력으로 들어갈 수 있음 </p>
<p>-------------------------------------------------------------------------------------------- </p>
<p> </p>
