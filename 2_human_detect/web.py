from flask import Flask, render_template, Response
import cv2

#Flask: 웹 애플리케이션 프레임워크.
# render_template: HTML 템플릿을 렌더링하는 데 사용되는 Flask 함수.
#Response: 웹 요청에 대한 응답을 생성하는 Flask 함수.
#cv2: OpenCV 라이브러리로 이미지 처리를 위해 사용.

app = Flask(__name__)

def generate_frames():
# generate_frames(): 무한 루프를 통해 이미지 프레임을 생성하는 제너레이터 함수

    while True:
        # Read image from file
        image_path = '/home/pi/tsample/image/person.jpg'
        frame = cv2.imread(image_path)
        
        # Encode image as JPEG
        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        # Yield image as byte array for response
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    # Return response with generated frames
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='192.168.110.183', port=8000, debug=True)
