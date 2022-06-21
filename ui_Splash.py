# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SplashyTxFen.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication

import ui_Dashboard_User
from ui_login import Login
import main
#import ui_Dashboard_admin as main

counter = 0

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(671, 270)
        SplashScreen.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"\n"
"QWidget {\n"
"    font-size: 11px;\n"
"}\n"
"\n"
"QTableView {\n"
"    font-size: 10px;\n"
"    alternate-background-color: #EEEEFF;\n"
"}\n"
"\n"
"Browser QPushButton {\n"
"    font-size: 10px;\n"
"    min-width: 10px;\n"
"}\n"
"\n"
"ColorButton::enabled {\n"
"    border: 1px solid #444444;\n"
"}\n"
"\n"
"ColorButton::disabled {\n"
"    border: 1px solid #AAAAAA;\n"
"}\n"
"\n"
"\n"
"Browser QGroupBox {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #E0E0E0, stop: 1 #FFFFFF);\n"
"    border: 2px solid #999999;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"    font-size: 13px;\n"
"    color: black;\n"
"}\n"
"\n"
"Browser QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    font-size: 13px;\n"
"    color: black;\n"
"}\n"
"\n"
"PluginIte"
                        "m {\n"
"    border: 2px solid black;\n"
"    background: white;\n"
"}\n"
"\n"
"\n"
"PluginItem Frame {\n"
"    background: #CCCCCC;\n"
"}\n"
"\n"
"\n"
"TabButton {\n"
"    border: 1px solid #8f8f91;\n"
"    border-radius: 2px;\n"
"    padding: 3px;\n"
"    min-width: 120px;\n"
"}\n"
"\n"
"TabButton::checked {\n"
"    background-color: qlineargradient(x1: 0, y1: 0 , x2: 0, y2: 1,\n"
"                                      stop: 0 #9a9b9e, stop: 1 #babbbe);\n"
"}\n"
"\n"
"\n"
"TabButton::pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0 , x2: 0, y2: 1,\n"
"                                      stop: 0 #9a9b9e, stop: 1 #babbbe);\n"
"}\n"
"")
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"\n"
"\n"
"QFrame{\n"
"\n"
"border -radius: 10px;\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, -1, 0)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"font: 75 35pt \"Century Gothic\";\n"
"")
        self.label.setTextFormat(Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 75 15pt \"Century Gothic\";\n"
"\n"
"")

        self.verticalLayout_5.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.progressBar = QProgressBar(self.frame_4)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"text-align: center;\n"
"border-style: none;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"border-radius: 10px;\n"
"background-color: rgb(36, 56, 84);\n"
"}")
        self.progressBar.setValue(24)
        self.progressBar.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.progressBar)

        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet(u"font: 75 12pt \"Century Gothic\";\n"
"")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, -1, 0)

        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.frame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("SplashScreen", u"Check My Symptomps", None))
        self.label_4.setText(QCoreApplication.translate("SplashScreen", u"Your HealthCare Buddy!!", None))
        self.label_3.setText(QCoreApplication.translate("SplashScreen", u"loading...", None))
    # retranslateUi

class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)
        # Start the main app
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS

    def progress(self):
        global counter
        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)
        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()
            # SHOW MAIN WINDOW
            if Login.Type == 'User':
                self.main = ui_Dashboard_User.Main()
                print("Employee")
            elif Login.Type == 'Admin':
                self.main = main.Main()
                print("Admin")
            self.main.show()
            # CLOSE SPLASH SCREEN
            self.close()
        # INCREASE COUNTER
        counter += 4

