# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide2.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(986, 495)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pic2 = QLabel(self.centralwidget)
        self.pic2.setObjectName(u"pic2")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pic2.sizePolicy().hasHeightForWidth())
        self.pic2.setSizePolicy(sizePolicy)
        self.pic2.setMinimumSize(QSize(480, 320))
        self.pic2.setStyleSheet(u"background-color: rgb(255, 255, 127);")

        self.gridLayout.addWidget(self.pic2, 1, 1, 1, 1)

        self.modeBtn = QPushButton(self.centralwidget)
        self.modeBtn.setObjectName(u"modeBtn")
        self.modeBtn.setMinimumSize(QSize(960, 50))

        self.gridLayout.addWidget(self.modeBtn, 3, 0, 1, 2)

        self.playBtn = QPushButton(self.centralwidget)
        self.playBtn.setObjectName(u"playBtn")
        self.playBtn.setMinimumSize(QSize(960, 50))

        self.gridLayout.addWidget(self.playBtn, 2, 0, 1, 2)

        self.pic1 = QLabel(self.centralwidget)
        self.pic1.setObjectName(u"pic1")
        sizePolicy.setHeightForWidth(self.pic1.sizePolicy().hasHeightForWidth())
        self.pic1.setSizePolicy(sizePolicy)
        self.pic1.setMinimumSize(QSize(480, 320))
        self.pic1.setStyleSheet(u"background-color: rgb(0, 170, 255);")

        self.gridLayout.addWidget(self.pic1, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 986, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.playBtn.clicked.connect(MainWindow.play)
        self.modeBtn.clicked.connect(MainWindow.mode)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pic2.setText("")
        self.modeBtn.setText(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.playBtn.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.pic1.setText("")
    # retranslateUi

