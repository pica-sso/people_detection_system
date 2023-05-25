# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUI.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenuBar, QPlainTextEdit, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1062, 614)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(30, 360, 281, 211))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.midButton = QPushButton(self.gridLayoutWidget)
        self.midButton.setObjectName(u"midButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.midButton.sizePolicy().hasHeightForWidth())
        self.midButton.setSizePolicy(sizePolicy)
        self.midButton.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.midButton, 1, 1, 1, 1)

        self.rightButton = QPushButton(self.gridLayoutWidget)
        self.rightButton.setObjectName(u"rightButton")
        sizePolicy.setHeightForWidth(self.rightButton.sizePolicy().hasHeightForWidth())
        self.rightButton.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.rightButton, 1, 2, 1, 1)

        self.leftButton = QPushButton(self.gridLayoutWidget)
        self.leftButton.setObjectName(u"leftButton")
        sizePolicy.setHeightForWidth(self.leftButton.sizePolicy().hasHeightForWidth())
        self.leftButton.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.leftButton, 1, 0, 1, 1)

        self.goButton = QPushButton(self.gridLayoutWidget)
        self.goButton.setObjectName(u"goButton")
        sizePolicy.setHeightForWidth(self.goButton.sizePolicy().hasHeightForWidth())
        self.goButton.setSizePolicy(sizePolicy)
        self.goButton.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.goButton, 0, 1, 1, 1)

        self.backButton = QPushButton(self.gridLayoutWidget)
        self.backButton.setObjectName(u"backButton")
        sizePolicy.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy)
        self.backButton.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.backButton, 2, 1, 1, 1)

        self.logText = QPlainTextEdit(self.centralwidget)
        self.logText.setObjectName(u"logText")
        self.logText.setGeometry(QRect(30, 30, 301, 311))
        self.logText.setStyleSheet(u"font: 9pt \"Consolas\";")
        self.startButton = QPushButton(self.centralwidget)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setGeometry(QRect(320, 500, 111, 65))
        sizePolicy.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)
        self.startButton.setMinimumSize(QSize(80, 0))
        self.stopButton = QPushButton(self.centralwidget)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setGeometry(QRect(320, 430, 111, 65))
        sizePolicy.setHeightForWidth(self.stopButton.sizePolicy().hasHeightForWidth())
        self.stopButton.setSizePolicy(sizePolicy)
        self.stopButton.setMinimumSize(QSize(60, 0))
        self.sensingText = QPlainTextEdit(self.centralwidget)
        self.sensingText.setObjectName(u"sensingText")
        self.sensingText.setGeometry(QRect(340, 30, 91, 311))
        self.sensingText.setStyleSheet(u"font: 9pt \"Consolas\";")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 91, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(340, 10, 131, 16))
        self.webEngineView = QWebEngineView(self.centralwidget)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setGeometry(QRect(450, 20, 601, 541))
        self.webEngineView.setUrl(QUrl(u"about:blank"))
        self.refreshButton = QPushButton(self.centralwidget)
        self.refreshButton.setObjectName(u"refreshButton")
        self.refreshButton.setGeometry(QRect(320, 360, 111, 65))
        sizePolicy.setHeightForWidth(self.refreshButton.sizePolicy().hasHeightForWidth())
        self.refreshButton.setSizePolicy(sizePolicy)
        self.refreshButton.setMinimumSize(QSize(60, 0))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1062, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.startButton.clicked.connect(MainWindow.start)
        self.goButton.clicked.connect(MainWindow.go)
        self.leftButton.clicked.connect(MainWindow.left)
        self.rightButton.clicked.connect(MainWindow.right)
        self.midButton.clicked.connect(MainWindow.mid)
        self.backButton.clicked.connect(MainWindow.back)
        self.stopButton.clicked.connect(MainWindow.stop)
        self.webEngineView.loadStarted.connect(MainWindow.video)
        self.refreshButton.clicked.connect(MainWindow.refresh_webview)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.midButton.setText(QCoreApplication.translate("MainWindow", u"Mid", None))
        self.rightButton.setText(QCoreApplication.translate("MainWindow", u"Right", None))
        self.leftButton.setText(QCoreApplication.translate("MainWindow", u"Left", None))
        self.goButton.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.backButton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"command Table", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"sensingTable", None))
        self.refreshButton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
    # retranslateUi

