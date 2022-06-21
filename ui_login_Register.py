# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_RegisteryPjKLG.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import admin_rc
import orange_icons_rc
import background_rc
import blue_icons_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1011, 651)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/newPrefix/log-in.svg", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"\n"
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
"PluginItem {\n"
"    border: 2px solid black;\n"
""
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
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_12 = QFrame(self.frame)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_12)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_3 = QFrame(self.frame_12)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"\n"
"font: 75 42pt \"Century Gothic\";\n"
"\n"
"")
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)

        self.verticalLayout_12.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 75 20pt \"Century Gothic\";")

        self.verticalLayout_12.addWidget(self.label_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignTop)

        self.frame_11 = QFrame(self.frame_12)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy1)
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_11)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_3 = QLabel(self.frame_11)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"")
        self.label_3.setPixmap(QPixmap(u":/icons_blue/icons/login-user-icon.png"))
        self.label_3.setScaledContents(True)

        self.verticalLayout_11.addWidget(self.label_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.frame_11)


        self.horizontalLayout.addWidget(self.frame_12)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 75 38pt \"Century Gothic\";\n"
"")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_5)


        self.verticalLayout_3.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_7 = QFrame(self.frame_8)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_6 = QLabel(self.frame_7)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font: 75 21pt \"Century Gothic\";\n"
"")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_6)

        self.admin_username_2 = QLineEdit(self.frame_7)
        self.admin_username_2.setObjectName(u"admin_username_2")
        self.admin_username_2.setStyleSheet(u"font: 13pt \"Century Gothic\";\n"
"")

        self.verticalLayout_8.addWidget(self.admin_username_2)

        self.admin_username_4 = QLineEdit(self.frame_7)
        self.admin_username_4.setObjectName(u"admin_username_4")
        self.admin_username_4.setStyleSheet(u"font: 13pt \"Century Gothic\";\n"
"")

        self.verticalLayout_8.addWidget(self.admin_username_4)

        self.admin_username_3 = QLineEdit(self.frame_7)
        self.admin_username_3.setObjectName(u"admin_username_3")
        self.admin_username_3.setStyleSheet(u"font: 13pt \"Century Gothic\";\n"
"")

        self.verticalLayout_8.addWidget(self.admin_username_3)

        self.admin_username = QLineEdit(self.frame_7)
        self.admin_username.setObjectName(u"admin_username")
        self.admin_username.setStyleSheet(u"font: 13pt \"Century Gothic\";\n"
"")

        self.verticalLayout_8.addWidget(self.admin_username)

        self.admin_username_5 = QLineEdit(self.frame_7)
        self.admin_username_5.setObjectName(u"admin_username_5")
        self.admin_username_5.setStyleSheet(u"font: 13pt \"Century Gothic\";\n"
"")

        self.verticalLayout_8.addWidget(self.admin_username_5)


        self.verticalLayout_7.addWidget(self.frame_7)

        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_9)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.login = QPushButton(self.frame_9)
        self.login.setObjectName(u"login")
        self.login.setStyleSheet(u"font: 75 16pt \"Century Gothic\";\n"
"")

        self.verticalLayout_9.addWidget(self.login)


        self.verticalLayout_7.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.clear = QPushButton(self.frame_10)
        self.clear.setObjectName(u"clear")
        self.clear.setStyleSheet(u"font: 75 16pt \"Century Gothic\";\n"
"")

        self.verticalLayout_10.addWidget(self.clear)


        self.verticalLayout_7.addWidget(self.frame_10, 0, Qt.AlignTop)


        self.verticalLayout_5.addWidget(self.frame_8)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.quit = QPushButton(self.frame_6)
        self.quit.setObjectName(u"quit")
        self.quit.setStyleSheet(u"font: 75 16pt \"Century Gothic\";\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons_blue/icons/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.quit.setIcon(icon1)
        self.quit.setIconSize(QSize(25, 25))

        self.verticalLayout_6.addWidget(self.quit)


        self.verticalLayout_3.addWidget(self.frame_6, 0, Qt.AlignRight|Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"PharmaSoft | Login", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Check My Symptomps", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Your HealthCare Buddy!!", None))
        self.label_3.setText("")
        self.label_5.setText(QCoreApplication.translate("Dialog", u"WELCOME", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Register", None))
        self.admin_username_2.setInputMask("")
        self.admin_username_2.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.admin_username_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"User Name", None))
        self.admin_username_4.setInputMask("")
        self.admin_username_4.setText(QCoreApplication.translate("Dialog", u"UserName", None))
        self.admin_username_4.setPlaceholderText(QCoreApplication.translate("Dialog", u"User Name", None))
        self.admin_username_3.setInputMask("")
        self.admin_username_3.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.admin_username_3.setPlaceholderText(QCoreApplication.translate("Dialog", u"User Name", None))
        self.admin_username.setInputMask("")
        self.admin_username.setText(QCoreApplication.translate("Dialog", u"City", None))
        self.admin_username.setPlaceholderText(QCoreApplication.translate("Dialog", u"User Name", None))
        self.admin_username_5.setInputMask("")
        self.admin_username_5.setText(QCoreApplication.translate("Dialog", u"State", None))
        self.admin_username_5.setPlaceholderText(QCoreApplication.translate("Dialog", u"User Name", None))
        self.login.setText(QCoreApplication.translate("Dialog", u"Register", None))
        self.clear.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.quit.setText(QCoreApplication.translate("Dialog", u"Exit", None))
    # retranslateUi

