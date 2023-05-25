# people_detection_system
![동영상](https://github.com/pica-sso/people_detection_system/assets/89729297/57075fbe-1379-46e9-a1e2-fe8c9e21b758)
## SSAFY 종합 PJT - 인명 탐색 로봇 (2023.05.26.)
### 재난 상황에서 사람이 가지 못하는 곳을 정찰하고 생존자를 찾기 위한 로봇

- SSAFY 9기 광주 6반 임베디드 트랙 <br>
- S2C Team 소세영, 정민서

![car1](https://github.com/pica-sso/people_detection_system/assets/89729297/d4feff19-8eb5-4e7a-ab8e-8d357fa4aa96)

# How to start code

### 1. [remote_control] code is for GUI and control
  - 시작 전, AWS 서버를 활성화 필요
  - RPi에서 "app.py"를 실행
  - 원격 조정기에서 main.py 를 실행
  - 각 버튼을 이용하여 RCcar를 조종
  
  ![people detection1](https://github.com/pica-sso/people_detection_system/assets/89729297/b0bd046b-3a96-4bf6-b330-a52516f048a6)
    
### 2. [human_detect] code is detect people and take pictures
  - RPi에 openCV 설치
  - Tensorflow Lite 활용 : <https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi>
  - "TFLite_detection_webcam.py" 실행
  - label 이름이 person 이며, scores 수치가 60% 이상이면 현재 시간을 current_time에 받아 저장하고 , 사진 이름 설정과 imwrite함수를 이용해 image_path에 사진 저장
  - Flask를 이용해 웹 애플리케이션을 구성하고, 사람의 이미지 프레임을 실시간으로 클라이언트에게 전달해 실시간 스트리밍 사진 전송
  
![image](https://github.com/pica-sso/people_detection_system/assets/89729297/bc92c627-531d-4bb5-a938-da56d2c53d29)  

### 하드웨어 이미지
  ![image](https://github.com/pica-sso/people_detection_system/assets/89729297/d1536e9c-c6a4-4c69-8099-d37e183d47a6)

>### 실행   
   * 주행 및 원격 조종 부분: <https://github.com/pica-sso/people_detection_system/tree/master/1_remote_control>
   * 영상 처리 부분 : <https://github.com/pica-sso/people_detection_system/tree/master/2_human_detect>
