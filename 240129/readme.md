<h1> Raspberry Pi Environment Setting </h1>
<p><h2> Hardware & Software Setting </h2></p>
<p><h3> Introducing Raspberry Pi 3 and Learning its name </h3></p>
<p>1. Mircro SD Card를 Reader기에 삽입</p>
<p>2. Raspberry Pi 공식사이트. Software 클릭. 아래 Imager 다운로드</p>
<p>3. Reader기 본체에 연결. 디바이스, 운영체제, 저장소 설정.</p>
<p>4. 다운로드. 설정화면 나오면 아니오 클릭 후 예 클릭. </p>
<p>5. 다운로드 완료되면, Reader기에서 SD Card제거.</p>
<p>6. 라즈베리파이에 SD Card 삽입 후, 장치 On</p>
<p>7. Set Country에서 South Korea 선택</p>
<p>8. ID(busan), PassWord(city****) 설정 후, Wifi 설정(생략가능)</p>
<p>9. Restart 클릭. 설정 완료</p>
<p>10. Terminal에서 sudo apt update, sudo apt upgrade 입력 </p>
<p>11. sudo apt install -y ibus ibus-hangul 입력 (한글 깨지는거 원상복구)</p>
<p>12. sudo apt install -y fonts-nanum 입력 </p>
<p>13. Raspberry Pi Configuration 들어가서 Interfaces 클릭</p>
<p>14. SSH, VNC 클릭해서 On시키고 OK 클릭 </p>
<p>15. Terminal에서 sudo reboot 입력 </p>
<p>16. Terminal에서 ifconfig입력하여 IP확인 </p>
<p>17. IP확인 후 키보드,마우스,모니터 해제. 본 컴퓨터에서 터미널(명령 프롬프트 또는 Windows Terminal) 관리자권한으로 열기</p>
<p>18. ssh 아이디@IP주소 입력. </p>
<p>19. ls, cd Documents/, ls, vi text.txt로 확인</p>
<p>20. VNC viewer 다운로드 </p>
<p><b>참고사이트 : https://technote.graysky.co.kr/ </p></b>
