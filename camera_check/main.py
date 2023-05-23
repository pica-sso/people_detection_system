from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from test import Ui_MainWindow
import cv2
from time import *

class MyThread(QThread):
    mySignal = Signal(QPixmap, QPixmap)
    
    def __init__(self):
        super().__init__()
        self.cam = cv2.VideoCapture(0)
        self.cam.set(3,480)
        self.cam.set(4,320)
        
    def run(self):
        while True:
            ret, self.img = self.cam.read()
            if ret :
                self.printImage(self.img)
            sleep(0.1)
            
    def printImage(self, imgBGR):
        imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
        h, w, byte = imgRGB.shape
        img = QImage(imgRGB, w, h, byte*w, QImage.Format_RGB888)
        pix_img = QPixmap(img)
        
        imgGray = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2GRAY)
        imgCanny = cv2.Canny(imgGray, 100, 100)
        img2 = QImage(imgCanny, w, h, imgCanny.strides[0], QImage.Format_Grayscale8)
        pix_img2 = QPixmap(img2)
        
        self.mySignal.emit(pix_img, pix_img2)
        
class myapp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        self.th = MyThread()
        self.th.mySignal.connect(self.setImage)
        
    def setImage(self, img, img2):
        self.pic1.setPixmap(img)
        self.pic2.setPixmap(img2)
    
    def mode(self):
        pass

    def play(self):
        self.th.start()

    def closeEvent(self, event):
        self.th.terminate()
        self.th.wait(3000)
        self.close()

app = QApplication()
win = myapp()
win.show()
app.exec_()
