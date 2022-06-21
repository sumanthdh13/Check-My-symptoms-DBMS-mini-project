# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dashboard_UserAOIGgX.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from ui_login import *
from ui_Splash import *
from database import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer 
from PyQt5.QtWidgets import QMainWindow, QInputDialog, QLineEdit, QDialog
from PyQt5.QtWidgets import QApplication
import sys
import PySide2
from PySide2 import *
import os
from PyQt5.uic import loadUiType
from PySide2 import QtGui
from Custom_Widgets.Widgets import *
import sqlite3 as sql

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu

import background_rc
import orange_icons_rc
import blue_icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1109, 826)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        icon = QIcon()
        icon.addFile(u":/icons_blue/icons/airplay.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"\n"
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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slide_menu = QCustomSlideMenu(self.centralwidget)
        self.slide_menu.setObjectName(u"slide_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slide_menu.sizePolicy().hasHeightForWidth())
        self.slide_menu.setSizePolicy(sizePolicy)
        self.slide_menu.setMinimumSize(QSize(200, 0))
        self.slide_menu.setMaximumSize(QSize(0, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.slide_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.slide = QFrame(self.slide_menu)
        self.slide.setObjectName(u"slide")
        self.slide.setMinimumSize(QSize(196, 0))
        self.slide.setStyleSheet(u"")
        self.slide.setFrameShape(QFrame.NoFrame)
        self.slide.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_5 = QVBoxLayout(self.slide)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, -1)
        self.frame_3 = QFrame(self.slide)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"color: rgb(80, 168, 212);\n"
"\n"
"background-color: rgb(36, 56, 84);")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.verticalLayout_8 = QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"\n"
"font: 75 22pt \"Century Gothic\";\n"
"")
        self.label_4.setFrameShape(QFrame.NoFrame)
        self.label_4.setFrameShadow(QFrame.Sunken)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_4)


        self.verticalLayout_5.addWidget(self.frame_3, 0, Qt.AlignTop)

        self.frame_7 = QFrame(self.slide)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy1)
        self.frame_7.setStyleSheet(u"\n"
"\n"
"background-color: rgb(36, 56, 84);")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_9 = QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.dashboard_btn = QPushButton(self.frame_7)
        self.dashboard_btn.setObjectName(u"dashboard_btn")
        self.dashboard_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.dashboard_btn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding: 10px 5px;\n"
"text-align: left;\n"
"font: 75 16pt \"Century Gothic\";\n"
"border-top-left-radius: 20px ;\n"
"border-bottom-left-radius: 20px ;\n"
"border-top-right-radius: 20px ;\n"
"border-bottom-right-radius: 20px ;")
        icon1 = QIcon()
        icon1.addFile(u":/icons_blue/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dashboard_btn.setIcon(icon1)
        self.dashboard_btn.setIconSize(QSize(25, 25))
        self.dashboard_btn.setAutoDefault(False)
        self.dashboard_btn.setFlat(False)

        self.verticalLayout_9.addWidget(self.dashboard_btn)

        self.inventory_btn = QPushButton(self.frame_7)
        self.inventory_btn.setObjectName(u"inventory_btn")
        self.inventory_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.inventory_btn.setStyleSheet(u"\n"
"padding: 10px 5px;\n"
"text-align: left;\n"
"font: 75 16pt \"Century Gothic\";\n"
"border-top-left-radius: 20px ;\n"
"border-bottom-left-radius: 20px ;\n"
"border-top-right-radius: 20px ;\n"
"border-bottom-right-radius: 20px ;color: rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u":/icons_blue/icons/slack.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.inventory_btn.setIcon(icon2)
        self.inventory_btn.setIconSize(QSize(25, 25))
        self.inventory_btn.setFlat(False)

        self.verticalLayout_9.addWidget(self.inventory_btn)

        self.sale_history_btn = QPushButton(self.frame_7)
        self.sale_history_btn.setObjectName(u"sale_history_btn")
        self.sale_history_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.sale_history_btn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding: 10px 5px;\n"
"text-align: left;\n"
"font: 75 16pt \"Century Gothic\";\n"
"border-top-left-radius: 20px ;\n"
"border-bottom-left-radius: 20px ;\n"
"border-top-right-radius: 20px ;\n"
"border-bottom-right-radius: 20px ;")
        icon3 = QIcon()
        icon3.addFile(u":/icons_blue/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sale_history_btn.setIcon(icon3)
        self.sale_history_btn.setIconSize(QSize(25, 25))
        self.sale_history_btn.setFlat(False)

        self.verticalLayout_9.addWidget(self.sale_history_btn)

        self.developer_info = QPushButton(self.frame_7)
        self.developer_info.setObjectName(u"developer_info")
        self.developer_info.setCursor(QCursor(Qt.PointingHandCursor))
        self.developer_info.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding: 10px 5px;\n"
"text-align: left;\n"
"font: 75 16pt \"Century Gothic\";\n"
"border-top-left-radius: 20px ;\n"
"border-bottom-left-radius: 20px ;\n"
"border-top-right-radius: 20px ;\n"
"border-bottom-right-radius: 20px ;")
        icon4 = QIcon()
        icon4.addFile(u":/icons_blue/icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.developer_info.setIcon(icon4)
        self.developer_info.setIconSize(QSize(25, 25))
        self.developer_info.setFlat(False)

        self.verticalLayout_9.addWidget(self.developer_info)


        self.verticalLayout_5.addWidget(self.frame_7)


        self.verticalLayout_2.addWidget(self.slide)


        self.horizontalLayout.addWidget(self.slide_menu)

        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_body)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.main_body)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setCursor(QCursor(Qt.ArrowCursor))
        self.header_frame.setAutoFillBackground(False)
        self.header_frame.setStyleSheet(u"background-color: rgb(36, 56, 84);")
        self.header_frame.setFrameShape(QFrame.NoFrame)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.header_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.menu_btn = QPushButton(self.frame_2)
        self.menu_btn.setObjectName(u"menu_btn")
        self.menu_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_btn.setAutoFillBackground(False)
        icon5 = QIcon()
        icon5.addFile(u":/icons_blue/icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_btn.setIcon(icon5)
        self.menu_btn.setIconSize(QSize(30, 30))
        self.menu_btn.setFlat(True)

        self.verticalLayout_4.addWidget(self.menu_btn, 0, Qt.AlignLeft)


        self.horizontalLayout_3.addWidget(self.frame_2)

        self.frame_6 = QFrame(self.header_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"font: 22pt \"Century Gothic\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout_3.addWidget(self.frame_6)

        self.frame = QFrame(self.header_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.refresh_btn = QPushButton(self.frame)
        self.refresh_btn.setObjectName(u"refresh_btn")
        self.refresh_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.refresh_btn.setAutoFillBackground(False)
        icon6 = QIcon()
        icon6.addFile(u":/icons_blue/icons/refresh-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.refresh_btn.setIcon(icon6)
        self.refresh_btn.setIconSize(QSize(20, 20))
        self.refresh_btn.setFlat(True)

        self.horizontalLayout_5.addWidget(self.refresh_btn)

        self.users_btn_2 = QPushButton(self.frame)
        self.users_btn_2.setObjectName(u"users_btn_2")
        self.users_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.users_btn_2.setAutoFillBackground(False)
        icon7 = QIcon()
        icon7.addFile(u":/icons_blue/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.users_btn_2.setIcon(icon7)
        self.users_btn_2.setIconSize(QSize(20, 20))
        self.users_btn_2.setFlat(True)

        self.horizontalLayout_5.addWidget(self.users_btn_2)

        self.logout_btn = QPushButton(self.frame)
        self.logout_btn.setObjectName(u"logout_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.logout_btn.sizePolicy().hasHeightForWidth())
        self.logout_btn.setSizePolicy(sizePolicy2)
        self.logout_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.logout_btn.setAutoFillBackground(False)
        icon8 = QIcon()
        icon8.addFile(u":/icons_blue/icons/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_btn.setIcon(icon8)
        self.logout_btn.setIconSize(QSize(20, 20))
        self.logout_btn.setAutoDefault(False)
        self.logout_btn.setFlat(True)

        self.horizontalLayout_5.addWidget(self.logout_btn)


        self.horizontalLayout_3.addWidget(self.frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.main_body_contents = QFrame(self.main_body)
        self.main_body_contents.setObjectName(u"main_body_contents")
        sizePolicy1.setHeightForWidth(self.main_body_contents.sizePolicy().hasHeightForWidth())
        self.main_body_contents.setSizePolicy(sizePolicy1)
        self.main_body_contents.setStyleSheet(u"")
        self.main_body_contents.setFrameShape(QFrame.NoFrame)
        self.main_body_contents.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.main_body_contents)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.main_body_contents)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.stackedWidget.setFrameShadow(QFrame.Raised)
        self.info_page = QWidget()
        self.info_page.setObjectName(u"info_page")
        self.verticalLayout_164 = QVBoxLayout(self.info_page)
        self.verticalLayout_164.setSpacing(0)
        self.verticalLayout_164.setObjectName(u"verticalLayout_164")
        self.verticalLayout_164.setContentsMargins(0, 0, 0, 0)
        self.frame_230 = QFrame(self.info_page)
        self.frame_230.setObjectName(u"frame_230")
        self.frame_230.setFrameShape(QFrame.NoFrame)
        self.frame_230.setFrameShadow(QFrame.Plain)
        self.verticalLayout_163 = QVBoxLayout(self.frame_230)
        self.verticalLayout_163.setSpacing(0)
        self.verticalLayout_163.setObjectName(u"verticalLayout_163")
        self.verticalLayout_163.setContentsMargins(0, 0, 0, 0)
        self.label_74 = QLabel(self.frame_230)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setStyleSheet(u"font: 20pt \"Century Gothic\";")
        self.label_74.setAlignment(Qt.AlignCenter)

        self.verticalLayout_163.addWidget(self.label_74)


        self.verticalLayout_164.addWidget(self.frame_230, 0, Qt.AlignTop)

        self.frame_57 = QFrame(self.info_page)
        self.frame_57.setObjectName(u"frame_57")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_57.sizePolicy().hasHeightForWidth())
        self.frame_57.setSizePolicy(sizePolicy3)
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.verticalLayout_165 = QVBoxLayout(self.frame_57)
        self.verticalLayout_165.setSpacing(6)
        self.verticalLayout_165.setObjectName(u"verticalLayout_165")
        self.verticalLayout_165.setContentsMargins(0, 9, 0, 0)
        self.frame_231 = QFrame(self.frame_57)
        self.frame_231.setObjectName(u"frame_231")
        self.frame_231.setFrameShape(QFrame.StyledPanel)
        self.frame_231.setFrameShadow(QFrame.Raised)
        self.verticalLayout_166 = QVBoxLayout(self.frame_231)
        self.verticalLayout_166.setSpacing(0)
        self.verticalLayout_166.setObjectName(u"verticalLayout_166")
        self.verticalLayout_166.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.frame_231)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"font: 20pt \"Century Gothic\";\n"
"")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.verticalLayout_166.addWidget(self.label_23)


        self.verticalLayout_165.addWidget(self.frame_231, 0, Qt.AlignTop)

        self.frame_232 = QFrame(self.frame_57)
        self.frame_232.setObjectName(u"frame_232")
        sizePolicy3.setHeightForWidth(self.frame_232.sizePolicy().hasHeightForWidth())
        self.frame_232.setSizePolicy(sizePolicy3)
        self.frame_232.setFrameShape(QFrame.StyledPanel)
        self.frame_232.setFrameShadow(QFrame.Raised)
        self.verticalLayout_167 = QVBoxLayout(self.frame_232)
        self.verticalLayout_167.setObjectName(u"verticalLayout_167")
        self.frame_234 = QFrame(self.frame_232)
        self.frame_234.setObjectName(u"frame_234")
        self.frame_234.setFrameShape(QFrame.StyledPanel)
        self.frame_234.setFrameShadow(QFrame.Raised)
        self.verticalLayout_168 = QVBoxLayout(self.frame_234)
        self.verticalLayout_168.setObjectName(u"verticalLayout_168")
        self.label_16 = QLabel(self.frame_234)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"font: 14pt \"Century Gothic\";\n"
"")
        self.label_16.setWordWrap(True)

        self.verticalLayout_168.addWidget(self.label_16)


        self.verticalLayout_167.addWidget(self.frame_234)

        self.frame_238 = QFrame(self.frame_232)
        self.frame_238.setObjectName(u"frame_238")
        self.frame_238.setFrameShape(QFrame.StyledPanel)
        self.frame_238.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_85 = QHBoxLayout(self.frame_238)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.frame_233 = QFrame(self.frame_238)
        self.frame_233.setObjectName(u"frame_233")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_233.sizePolicy().hasHeightForWidth())
        self.frame_233.setSizePolicy(sizePolicy4)
        self.frame_233.setFrameShape(QFrame.StyledPanel)
        self.frame_233.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_84 = QHBoxLayout(self.frame_233)
        self.horizontalLayout_84.setSpacing(0)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.frame_235 = QFrame(self.frame_233)
        self.frame_235.setObjectName(u"frame_235")
        self.frame_235.setFrameShape(QFrame.StyledPanel)
        self.frame_235.setFrameShadow(QFrame.Raised)
        self.verticalLayout_169 = QVBoxLayout(self.frame_235)
        self.verticalLayout_169.setSpacing(0)
        self.verticalLayout_169.setObjectName(u"verticalLayout_169")
        self.verticalLayout_169.setContentsMargins(0, 0, 0, 0)
        self.label_24 = QLabel(self.frame_235)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"font: 16pt \"Century Gothic\";\n"
"")
        self.label_24.setWordWrap(True)

        self.verticalLayout_169.addWidget(self.label_24)

        self.label_34 = QLabel(self.frame_235)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"font: 14pt \"Century Gothic\";\n"
"")

        self.verticalLayout_169.addWidget(self.label_34)


        self.horizontalLayout_84.addWidget(self.frame_235, 0, Qt.AlignBottom)

        self.frame_236 = QFrame(self.frame_233)
        self.frame_236.setObjectName(u"frame_236")
        self.frame_236.setFrameShape(QFrame.StyledPanel)
        self.frame_236.setFrameShadow(QFrame.Raised)
        self.verticalLayout_171 = QVBoxLayout(self.frame_236)
        self.verticalLayout_171.setSpacing(0)
        self.verticalLayout_171.setObjectName(u"verticalLayout_171")
        self.verticalLayout_171.setContentsMargins(0, 0, 0, 0)
        self.label_36 = QLabel(self.frame_236)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setLayoutDirection(Qt.LeftToRight)
        self.label_36.setStyleSheet(u"font: 16pt \"Century Gothic\";\n"
"")
        self.label_36.setAlignment(Qt.AlignCenter)
        self.label_36.setWordWrap(True)

        self.verticalLayout_171.addWidget(self.label_36)

        self.label_35 = QLabel(self.frame_236)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"font: 14pt \"Century Gothic\";\n"
"")
        self.label_35.setAlignment(Qt.AlignCenter)

        self.verticalLayout_171.addWidget(self.label_35)


        self.horizontalLayout_84.addWidget(self.frame_236)


        self.horizontalLayout_85.addWidget(self.frame_233)


        self.verticalLayout_167.addWidget(self.frame_238, 0, Qt.AlignBottom)

        self.frame_237 = QFrame(self.frame_232)
        self.frame_237.setObjectName(u"frame_237")
        self.frame_237.setFrameShape(QFrame.StyledPanel)
        self.frame_237.setFrameShadow(QFrame.Raised)
        self.verticalLayout_170 = QVBoxLayout(self.frame_237)
        self.verticalLayout_170.setSpacing(0)
        self.verticalLayout_170.setObjectName(u"verticalLayout_170")
        self.verticalLayout_170.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_167.addWidget(self.frame_237, 0, Qt.AlignBottom)


        self.verticalLayout_165.addWidget(self.frame_232)


        self.verticalLayout_164.addWidget(self.frame_57)

        self.stackedWidget.addWidget(self.info_page)
        self.page_sale_history = QWidget()
        self.page_sale_history.setObjectName(u"page_sale_history")
        self.verticalLayout_65 = QVBoxLayout(self.page_sale_history)
        self.verticalLayout_65.setSpacing(0)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.frame_83 = QFrame(self.page_sale_history)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setFrameShape(QFrame.NoFrame)
        self.frame_83.setFrameShadow(QFrame.Plain)
        self.verticalLayout_64 = QVBoxLayout(self.frame_83)
        self.verticalLayout_64.setSpacing(0)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.label_47 = QLabel(self.frame_83)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setStyleSheet(u"font: 20pt \"Century Gothic\";")
        self.label_47.setAlignment(Qt.AlignCenter)

        self.verticalLayout_64.addWidget(self.label_47)


        self.verticalLayout_65.addWidget(self.frame_83, 0, Qt.AlignTop)

        self.frame_97 = QFrame(self.page_sale_history)
        self.frame_97.setObjectName(u"frame_97")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_97.sizePolicy().hasHeightForWidth())
        self.frame_97.setSizePolicy(sizePolicy5)
        self.frame_97.setFrameShape(QFrame.NoFrame)
        self.frame_97.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_73 = QHBoxLayout(self.frame_97)
        self.horizontalLayout_73.setSpacing(0)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.frame_97)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_22)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.frame_98 = QFrame(self.frame_22)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setFrameShape(QFrame.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_98)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.frame_99 = QFrame(self.frame_98)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setFrameShape(QFrame.StyledPanel)
        self.frame_99.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_99)
        self.horizontalLayout_34.setSpacing(3)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.label_48 = QLabel(self.frame_99)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setStyleSheet(u"font: 16pt \"Century Gothic\";")
        self.label_48.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_34.addWidget(self.label_48)


        self.horizontalLayout_33.addWidget(self.frame_99)

        self.frame_100 = QFrame(self.frame_98)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setFrameShape(QFrame.StyledPanel)
        self.frame_100.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_100)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.sale_history_show_all_btn = QPushButton(self.frame_100)
        self.sale_history_show_all_btn.setObjectName(u"sale_history_show_all_btn")
        self.sale_history_show_all_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.sale_history_show_all_btn.setStyleSheet(u"font: 12pt \"Century Gothic\";")
        self.sale_history_show_all_btn.setFlat(True)

        self.horizontalLayout_35.addWidget(self.sale_history_show_all_btn)


        self.horizontalLayout_33.addWidget(self.frame_100)


        self.verticalLayout_55.addWidget(self.frame_98)

        self.frame_101 = QFrame(self.frame_22)
        self.frame_101.setObjectName(u"frame_101")
        sizePolicy1.setHeightForWidth(self.frame_101.sizePolicy().hasHeightForWidth())
        self.frame_101.setSizePolicy(sizePolicy1)
        self.frame_101.setFrameShape(QFrame.StyledPanel)
        self.frame_101.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_101)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.tableWidget_2 = QTableWidget(self.frame_101)
        if (self.tableWidget_2.columnCount() < 7):
            self.tableWidget_2.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setStyleSheet(u"font: 10pt \"Century Gothic\";\n"
"\n"
"")
        self.tableWidget_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_2.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.horizontalHeader().setProperty("showSortIndicator", False)

        self.horizontalLayout_48.addWidget(self.tableWidget_2)


        self.verticalLayout_55.addWidget(self.frame_101)


        self.horizontalLayout_73.addWidget(self.frame_22)


        self.verticalLayout_65.addWidget(self.frame_97)

        self.stackedWidget.addWidget(self.page_sale_history)
        self.page_new = QWidget()
        self.page_new.setObjectName(u"page_new")
        self.verticalLayout_24 = QVBoxLayout(self.page_new)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame_180 = QFrame(self.page_new)
        self.frame_180.setObjectName(u"frame_180")
        self.frame_180.setFrameShape(QFrame.NoFrame)
        self.frame_180.setFrameShadow(QFrame.Plain)
        self.verticalLayout_127 = QVBoxLayout(self.frame_180)
        self.verticalLayout_127.setSpacing(0)
        self.verticalLayout_127.setObjectName(u"verticalLayout_127")
        self.verticalLayout_127.setContentsMargins(0, 0, 0, 0)
        self.label_93 = QLabel(self.frame_180)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setStyleSheet(u"font: 20pt \"Century Gothic\";")
        self.label_93.setAlignment(Qt.AlignCenter)

        self.verticalLayout_127.addWidget(self.label_93)


        self.verticalLayout_24.addWidget(self.frame_180)

        self.frame_159 = QFrame(self.page_new)
        self.frame_159.setObjectName(u"frame_159")
        sizePolicy1.setHeightForWidth(self.frame_159.sizePolicy().hasHeightForWidth())
        self.frame_159.setSizePolicy(sizePolicy1)
        self.frame_159.setFrameShape(QFrame.NoFrame)
        self.frame_159.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_159)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.frame_176 = QFrame(self.frame_159)
        self.frame_176.setObjectName(u"frame_176")
        sizePolicy5.setHeightForWidth(self.frame_176.sizePolicy().hasHeightForWidth())
        self.frame_176.setSizePolicy(sizePolicy5)
        self.frame_176.setFrameShape(QFrame.StyledPanel)
        self.frame_176.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_126 = QVBoxLayout(self.frame_176)
        self.verticalLayout_126.setSpacing(0)
        self.verticalLayout_126.setObjectName(u"verticalLayout_126")
        self.verticalLayout_126.setContentsMargins(0, 0, 0, 0)
        self.frame_181 = QFrame(self.frame_176)
        self.frame_181.setObjectName(u"frame_181")
        sizePolicy1.setHeightForWidth(self.frame_181.sizePolicy().hasHeightForWidth())
        self.frame_181.setSizePolicy(sizePolicy1)
        self.frame_181.setFrameShape(QFrame.StyledPanel)
        self.frame_181.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_181)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_181)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy6)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_8)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy1.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy1)
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.pushButton_2 = QPushButton(self.frame_10)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"font: 11pt \"Century Gothic\";")

        self.verticalLayout_14.addWidget(self.pushButton_2)


        self.verticalLayout_10.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_8)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_11)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.pushButton = QPushButton(self.frame_11)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"font: 11pt \"Century Gothic\";")
        icon9 = QIcon()
        icon9.addFile(u":/icons_blue/icons/rotate-ccw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon9)

        self.verticalLayout_12.addWidget(self.pushButton)


        self.verticalLayout_10.addWidget(self.frame_11, 0, Qt.AlignBottom)


        self.horizontalLayout_7.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_181)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_9)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_9)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_12)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_12)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 20pt \"Century Gothic\";")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_5)


        self.verticalLayout_11.addWidget(self.frame_12, 0, Qt.AlignTop)

        self.frame_13 = QFrame(self.frame_9)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_13)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_2 = QStackedWidget(self.frame_13)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_16 = QVBoxLayout(self.page)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_6 = QLabel(self.page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font: 32pt \"Century Gothic\";")
        self.label_6.setWordWrap(True)

        self.verticalLayout_16.addWidget(self.label_6)

        self.stackedWidget_2.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_17 = QVBoxLayout(self.page_2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_14 = QFrame(self.page_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_14)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_14)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font: 14pt \"Century Gothic\";")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_7)


        self.verticalLayout_17.addWidget(self.frame_14, 0, Qt.AlignTop)

        self.frame_15 = QFrame(self.page_2)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy7)
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_15)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.comboBox = QComboBox(self.frame_15)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_20.addWidget(self.comboBox)

        self.comboBox_2 = QComboBox(self.frame_15)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.verticalLayout_20.addWidget(self.comboBox_2)

        self.comboBox_3 = QComboBox(self.frame_15)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.verticalLayout_20.addWidget(self.comboBox_3)

        self.comboBox_4 = QComboBox(self.frame_15)
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.verticalLayout_20.addWidget(self.comboBox_4)


        self.verticalLayout_17.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.page_2)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_16)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.pushButton_3 = QPushButton(self.frame_16)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"font: 11pt \"Century Gothic\";")
        icon10 = QIcon()
        icon10.addFile(u":/icons_blue/icons/thumbs-up.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon10)

        self.verticalLayout_19.addWidget(self.pushButton_3)


        self.verticalLayout_17.addWidget(self.frame_16, 0, Qt.AlignBottom)

        self.stackedWidget_2.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_21 = QVBoxLayout(self.page_3)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_17 = QFrame(self.page_3)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_17)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_17)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font: 18pt \"Century Gothic\";")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_8)


        self.verticalLayout_21.addWidget(self.frame_17, 0, Qt.AlignTop)

        self.frame_18 = QFrame(self.page_3)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy1.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy1)
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_19)
        self.formLayout.setObjectName(u"formLayout")
        self.label_9 = QLabel(self.frame_19)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font: 16pt \"Century Gothic\";")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_9)

        self.label_10 = QLabel(self.frame_19)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font: 16pt \"Century Gothic\";")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_10)

        self.label_11 = QLabel(self.frame_19)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font: 16pt \"Century Gothic\";")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_11)

        self.label_12 = QLabel(self.frame_19)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"font: 16pt \"Century Gothic\";")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_12)

        self.label_13 = QLabel(self.frame_19)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"font: 16pt \"Century Gothic\";")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_13)

        self.label_14 = QLabel(self.frame_19)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"font: 16pt \"Century Gothic\";")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_14)

        self.label_15 = QLabel(self.frame_19)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"font: 16pt \"Century Gothic\";")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_15)

        self.label_17 = QLabel(self.frame_19)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"font: 16pt \"Century Gothic\";")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.label_17)

        self.label_18 = QLabel(self.frame_19)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"font: 16pt \"Century Gothic\";")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_18)

        self.label_19 = QLabel(self.frame_19)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"font: 16pt \"Century Gothic\";")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.label_19)

        self.label_20 = QLabel(self.frame_19)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"font: 16pt \"Century Gothic\";")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_20)

        self.label_21 = QLabel(self.frame_19)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"font: 16pt \"Century Gothic\";")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.label_21)

        self.label_22 = QLabel(self.frame_19)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"font: 16pt \"Century Gothic\";")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_22)

        self.label_25 = QLabel(self.frame_19)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"font: 16pt \"Century Gothic\";")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.label_25)


        self.horizontalLayout_8.addWidget(self.frame_19)


        self.verticalLayout_21.addWidget(self.frame_18, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedWidget_2.addWidget(self.page_3)

        self.verticalLayout_15.addWidget(self.stackedWidget_2)


        self.verticalLayout_11.addWidget(self.frame_13)


        self.horizontalLayout_7.addWidget(self.frame_9)


        self.verticalLayout_126.addWidget(self.frame_181)


        self.horizontalLayout_23.addWidget(self.frame_176)


        self.verticalLayout_24.addWidget(self.frame_159)

        self.stackedWidget.addWidget(self.page_new)
        self.page_dashboard = QWidget()
        self.page_dashboard.setObjectName(u"page_dashboard")
        self.verticalLayout_118 = QVBoxLayout(self.page_dashboard)
        self.verticalLayout_118.setSpacing(0)
        self.verticalLayout_118.setObjectName(u"verticalLayout_118")
        self.verticalLayout_118.setContentsMargins(0, 0, 0, 0)
        self.frame_135 = QFrame(self.page_dashboard)
        self.frame_135.setObjectName(u"frame_135")
        self.frame_135.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_135.setFrameShape(QFrame.StyledPanel)
        self.frame_135.setFrameShadow(QFrame.Raised)
        self.verticalLayout_116 = QVBoxLayout(self.frame_135)
        self.verticalLayout_116.setObjectName(u"verticalLayout_116")
        self.frame_144 = QFrame(self.frame_135)
        self.frame_144.setObjectName(u"frame_144")
        self.frame_144.setStyleSheet(u"")
        self.frame_144.setFrameShape(QFrame.StyledPanel)
        self.frame_144.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_144)
        self.horizontalLayout_46.setSpacing(0)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.frame_157 = QFrame(self.frame_144)
        self.frame_157.setObjectName(u"frame_157")
        sizePolicy1.setHeightForWidth(self.frame_157.sizePolicy().hasHeightForWidth())
        self.frame_157.setSizePolicy(sizePolicy1)
        self.frame_157.setFrameShape(QFrame.StyledPanel)
        self.frame_157.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_157)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_83 = QLabel(self.frame_157)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setStyleSheet(u"font: 75 40pt \"Century Gothic\";\n"
"")
        self.label_83.setFrameShadow(QFrame.Plain)
        self.label_83.setTextFormat(Qt.AutoText)
        self.label_83.setScaledContents(False)
        self.label_83.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_83)

        self.user_name = QLabel(self.frame_157)
        self.user_name.setObjectName(u"user_name")
        self.user_name.setStyleSheet(u"font: 75 25pt \"Century Gothic\";")
        self.user_name.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.user_name)


        self.horizontalLayout_46.addWidget(self.frame_157, 0, Qt.AlignTop)


        self.verticalLayout_116.addWidget(self.frame_144)

        self.frame_136 = QFrame(self.frame_135)
        self.frame_136.setObjectName(u"frame_136")
        self.frame_136.setFrameShape(QFrame.StyledPanel)
        self.frame_136.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_136)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.frame_150 = QFrame(self.frame_136)
        self.frame_150.setObjectName(u"frame_150")
        self.frame_150.setFrameShape(QFrame.StyledPanel)
        self.frame_150.setFrameShadow(QFrame.Raised)
        self.verticalLayout_117 = QVBoxLayout(self.frame_150)
        self.verticalLayout_117.setObjectName(u"verticalLayout_117")
        self.label_71 = QLabel(self.frame_150)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setStyleSheet(u"font: 22pt \"Century Gothic\";")
        self.label_71.setAlignment(Qt.AlignCenter)

        self.verticalLayout_117.addWidget(self.label_71)

        self.number_of_Hospitals = QLabel(self.frame_150)
        self.number_of_Hospitals.setObjectName(u"number_of_Hospitals")
        self.number_of_Hospitals.setStyleSheet(u"font: 22pt \"Century Gothic\";")
        self.number_of_Hospitals.setAlignment(Qt.AlignCenter)

        self.verticalLayout_117.addWidget(self.number_of_Hospitals)


        self.horizontalLayout_44.addWidget(self.frame_150)

        self.frame_151 = QFrame(self.frame_136)
        self.frame_151.setObjectName(u"frame_151")
        self.frame_151.setFrameShape(QFrame.StyledPanel)
        self.frame_151.setFrameShadow(QFrame.Raised)
        self.verticalLayout_119 = QVBoxLayout(self.frame_151)
        self.verticalLayout_119.setObjectName(u"verticalLayout_119")
        self.label_73 = QLabel(self.frame_151)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setStyleSheet(u"font: 22pt \"Century Gothic\";")
        self.label_73.setAlignment(Qt.AlignCenter)

        self.verticalLayout_119.addWidget(self.label_73)

        self.number_of_cases = QLabel(self.frame_151)
        self.number_of_cases.setObjectName(u"number_of_cases")
        self.number_of_cases.setStyleSheet(u"font: 22pt \"Century Gothic\";")
        self.number_of_cases.setAlignment(Qt.AlignCenter)

        self.verticalLayout_119.addWidget(self.number_of_cases)


        self.horizontalLayout_44.addWidget(self.frame_151)

        self.frame_152 = QFrame(self.frame_136)
        self.frame_152.setObjectName(u"frame_152")
        self.frame_152.setFrameShape(QFrame.StyledPanel)
        self.frame_152.setFrameShadow(QFrame.Raised)
        self.verticalLayout_120 = QVBoxLayout(self.frame_152)
        self.verticalLayout_120.setObjectName(u"verticalLayout_120")
        self.label_75 = QLabel(self.frame_152)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setStyleSheet(u"font: 22pt \"Century Gothic\";")
        self.label_75.setAlignment(Qt.AlignCenter)

        self.verticalLayout_120.addWidget(self.label_75)

        self.number_of_doctors = QLabel(self.frame_152)
        self.number_of_doctors.setObjectName(u"number_of_doctors")
        self.number_of_doctors.setStyleSheet(u"font: 22pt \"Century Gothic\";")
        self.number_of_doctors.setAlignment(Qt.AlignCenter)

        self.verticalLayout_120.addWidget(self.number_of_doctors)


        self.horizontalLayout_44.addWidget(self.frame_152)


        self.verticalLayout_116.addWidget(self.frame_136)

        self.frame_201 = QFrame(self.frame_135)
        self.frame_201.setObjectName(u"frame_201")
        self.frame_201.setFrameShape(QFrame.StyledPanel)
        self.frame_201.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_201)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.frame_218 = QFrame(self.frame_201)
        self.frame_218.setObjectName(u"frame_218")
        self.frame_218.setFrameShape(QFrame.StyledPanel)
        self.frame_218.setFrameShadow(QFrame.Raised)
        self.verticalLayout_159 = QVBoxLayout(self.frame_218)
        self.verticalLayout_159.setObjectName(u"verticalLayout_159")
        self.label_110 = QLabel(self.frame_218)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setStyleSheet(u"font: 22pt \"Century Gothic\";")
        self.label_110.setAlignment(Qt.AlignCenter)

        self.verticalLayout_159.addWidget(self.label_110)

        self.total_users = QLabel(self.frame_218)
        self.total_users.setObjectName(u"total_users")
        self.total_users.setStyleSheet(u"font: 22pt \"Century Gothic\";")
        self.total_users.setAlignment(Qt.AlignCenter)

        self.verticalLayout_159.addWidget(self.total_users)


        self.horizontalLayout_53.addWidget(self.frame_218)

        self.frame_219 = QFrame(self.frame_201)
        self.frame_219.setObjectName(u"frame_219")
        self.frame_219.setFrameShape(QFrame.StyledPanel)
        self.frame_219.setFrameShadow(QFrame.Raised)
        self.verticalLayout_160 = QVBoxLayout(self.frame_219)
        self.verticalLayout_160.setObjectName(u"verticalLayout_160")
        self.label_125 = QLabel(self.frame_219)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setStyleSheet(u"font: 22pt \"Century Gothic\";")
        self.label_125.setAlignment(Qt.AlignCenter)

        self.verticalLayout_160.addWidget(self.label_125)

        self.total_diseases = QLabel(self.frame_219)
        self.total_diseases.setObjectName(u"total_diseases")
        self.total_diseases.setStyleSheet(u"font: 22pt \"Century Gothic\";")
        self.total_diseases.setAlignment(Qt.AlignCenter)

        self.verticalLayout_160.addWidget(self.total_diseases)


        self.horizontalLayout_53.addWidget(self.frame_219)


        self.verticalLayout_116.addWidget(self.frame_201)


        self.verticalLayout_118.addWidget(self.frame_135)

        self.stackedWidget.addWidget(self.page_dashboard)

        self.horizontalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.main_body_contents)

        self.footer = QFrame(self.main_body)
        self.footer.setObjectName(u"footer")
        sizePolicy.setHeightForWidth(self.footer.sizePolicy().hasHeightForWidth())
        self.footer.setSizePolicy(sizePolicy)
        self.footer.setStyleSheet(u"")
        self.footer.setFrameShape(QFrame.NoFrame)
        self.footer.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.footer)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.footer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"border: none;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 75 9pt \"Century Gothic\";\n"
"\n"
"")

        self.verticalLayout_6.addWidget(self.label_2)


        self.horizontalLayout_4.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.footer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"border: none;\n"
"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 75 9pt \"Century Gothic\";\n"
"")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_7.addWidget(self.label_3)


        self.horizontalLayout_4.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.footer, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.dashboard_btn.setDefault(False)
        self.logout_btn.setDefault(False)
        self.stackedWidget.setCurrentIndex(2)
        self.stackedWidget_2.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CheckMySymptomps | Dashboard", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.dashboard_btn.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.inventory_btn.setText(QCoreApplication.translate("MainWindow", u"Check Health", None))
        self.sale_history_btn.setText(QCoreApplication.translate("MainWindow", u"SearchHistory", None))
        self.developer_info.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.menu_btn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Check My Symptomps", None))
        self.refresh_btn.setText("")
        self.users_btn_2.setText("")
        self.logout_btn.setText("")
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Project Info", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Infectious Diseases and Management System", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"1.Infectious Diseases:Diseases caused by an infectiuos agents such as a bacteria,virus,protozoan(fungus)that can be passed on to others.\n"
"\n"
"2.Different Groups of agent that cause Diseases are:bacteria,viruses,fungi,protozoa,animals.\n"
"\n"
"3.Infectious Diseases are transimetted through water,wind,animals,human to human,direct and indirect contacts,food and water borne diseases,sexually transmitted,vectorborne diseases.\n"
"\n"
"4.Examples:corona,influenza,E.coli,bird flue,Syphills,HIV/AIDS,rubella,Zika etc...\n"
"\n"
"5.Controll measures:Taking vaccines,Medication,Changing of environments,etc...\n"
"", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Project Members\n"
"", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"1.Sumanth Hegde  \n"
"\n"
"2. Anil Kumar S", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Contact Me@\n"
"", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"sumanthdh13@gmail.com ", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Patient Search History", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Categories", None))
        self.sale_history_show_all_btn.setText(QCoreApplication.translate("MainWindow", u"Show All", None))
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"PatientID", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u" ILLNESS", None));
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Hospital Name", None));
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Dept Name", None));
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Doctor Name", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"Check Health", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Click to Check Symptoms", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Symptomps & Results", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Hello User,\n"
"How are You..\n"
"Not Feeling Well..?\n"
"Then Check Your Symptoms\n"
":)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Select your Symptomps", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Predicted Results", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Predicted Illness :", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"illness", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Recommended :\n"
"Hospital", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"hospital", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Department : ", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"dept", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Doctor", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"doctor", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Phone No : ", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"phno", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"City : ", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"city", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"State : ", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"state", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Welcome", None))
        self.user_name.setText(QCoreApplication.translate("MainWindow", u"User_Name", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u" Hospitals", None))
        self.number_of_Hospitals.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Departments", None))
        self.number_of_cases.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Doctors", None))
        self.number_of_doctors.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"Appointments", None))
        self.total_users.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"Record", None))
        self.total_diseases.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Health and Illness @Anil kumar @Sumanth Hegde", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Ver - 1.000.4  ", None))
    # retranslateUi




#-----------------Dashboard----------------------------

class Main(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        self.dashBoard()
        self.showMaximized()
        self.Handel_Buttons()

    def Handel_Buttons(self):

        #----------------MenuButtons---------------------

        self.ui.dashboard_btn.clicked.connect(lambda: self.dashBoard())
        self.ui.sale_history_btn.clicked.connect(lambda: self.SaleHistory())
        self.ui.inventory_btn.clicked.connect(lambda: self.pageDisease())
        self.ui.developer_info.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.info_page))
        # self.ui.inventory_sort1_combo.currentIndexChanged.connect(lambda: self.Inventory_Combo_Details())
        #--------------------------------------------------

        #---------------TopMenuButtons---------------------

        self.ui.logout_btn.clicked.connect(self.logOut)        
        self.ui.users_btn_2.clicked.connect(lambda: self.PopUser())
        self.ui.refresh_btn.clicked.connect(lambda: self.refresh())

        # #--------------------------------------------------

        # #-----------------NewProduct-ChemicalPageButtons-----------------

        self.ui.pushButton_2.clicked.connect(lambda: self.goToPageSymptomps())
        self.ui.pushButton.clicked.connect(lambda: self.gobackDashboard())
        self.ui.pushButton_3.clicked.connect(lambda: self.resultPage())

        # #--------------------------------------------------

        # #-----------------SaleHistoryPageButtons-----------------

        self.ui.sale_history_show_all_btn.clicked.connect(lambda: self.SaleHistoryAll())
        #self.ui.sale_history_deleteAll.clicked.connect(lambda: self.SaleHistoryDeleteAll())

        # #--------------------------------------------------

    #------------TopButtonFunctionalities-----------------------

    def logOut(self):
        self.close()
        print("You have been successfully logged out!")
        QMessageBox.information(self, "Logout", Login.User_Name+"\nYou have been successfully logged out!")

    def PopUser(self):
        QMessageBox.information(self, "User Details", "User Name : "+Login.User_ID+"\nName : "+Login.User_Name+"\nID : "+Login.ID+"\nID : "+Login.Type)
              
    def refresh(self):
        DataBase_Connection()

    #-----------------------------------------------------

    #---------------Dashboard Setup-----------------------
    def dashBoard(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_dashboard)
        self.ui.user_name.setText(Login.User_Name)
        self.dashBoardDetails()

    def dashBoardDetails(self):
        self.ui.number_of_Hospitals.setText(DataBase_Connection.totalhospital(self))
        self.ui.number_of_cases.setText(DataBase_Connection.totalsearchhistory(self))
        self.ui.number_of_doctors.setText(DataBase_Connection.numberdoctors(self))
        self.ui.total_users.setText(DataBase_Connection.totalusers(self))
        self.ui.total_diseases.setText(DataBase_Connection.totaldiseases(self))

    #--------------------------------------------------------

    #-----------------------Diseases-------------------------

    def pageDisease(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_new)
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page)

    def DiseasesAll(self):
        self.ui.tableWidget_6.setHorizontalHeaderLabels(['illnessID', 'illnessName', 'Agent Name', 'Symptomps',''])
        query1 = '''SELECT DISTINCT I.IllnessID, I.Illnessname, A.Agentname, S.Symptompname
                    from ILLNESS I, SYMPTOMPS S, AGENT A
                    where I.IllnessID = A.IllnessID and S.IllnessID = I.IllnessID'''
        try:
            conn = sql.connect('IDMS.db')
            cursor = conn.cursor()
            cursor.execute(query1)
            row = cursor.fetchall()
            self.ui.tableWidget_6.setRowCount(0)
            for row_number, row_data in enumerate(row):
                self.ui.tableWidget_6.insertRow(row_number)
                for coloumn_number, data in enumerate(row_data):
                    self.ui.tableWidget_6.setItem(row_number, coloumn_number, QTableWidgetItem(str(data)))
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Error", "Please Check again\nError: "+str(e))


    def gobackDashboard(self):
        self.dashBoard()
        
    def resultClear(self):
        pass

    def goToPageSymptomps(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_2)
        self.combo1()
        self.combo2()
        self.combo3()
        self.combo4()

    def combo1(self):
        try:
            conn = sql.connect('IDMS.db')
            cursor = conn.cursor()
            cursor.execute('''select Symptompname from SYMPTOMPS''')
            row = cursor.fetchall()
            for i in row:
                self.ui.comboBox.addItems(i)
        except Exception as e:
            print(e)

    def combo2(self):
        try:
            conn = sql.connect('IDMS.db')
            cursor = conn.cursor()
            cursor.execute('''select Symptompname from SYMPTOMPS''')
            row = cursor.fetchall()
            for i in row:
                self.ui.comboBox_2.addItems(i)
        except Exception as e:
            print(e)

    def combo3(self):
        try:
            conn = sql.connect('IDMS.db')
            cursor = conn.cursor()
            cursor.execute('''select Symptompname from SYMPTOMPS''')
            row = cursor.fetchall()
            for i in row:
                self.ui.comboBox_3.addItems(i)
        except Exception as e:
            print(e)

    def combo4(self):
        try:
            conn = sql.connect('IDMS.db')
            cursor = conn.cursor()
            cursor.execute('''select Symptompname from SYMPTOMPS''')
            row = cursor.fetchall()
            for i in row:
                self.ui.comboBox_4.addItems(i)
        except Exception as e:
            print(e)


    def resultPage(self):
        symptom = self.ui.comboBox.currentText()
        query1 = ''' SELECT I.IllnessID,I.Illnessname
                    FROM SYMPTOMPS S NATURAL JOIN ILLNESS I
                    WHERE S.Symptompname = ?'''
        query2 = ''' select HOSPITAL.Name, DEPARTMENT.Deptname, DEPARTMENT.Doctorname, HOSPITAL.Phnumber, HOSPITAL.City, HOSPITAL.State
                    from ( ( HOSPITAL NATURAL JOIN DEPARTMENT ) NATURAL JOIN AGENT)
                    WHERE IllnessID = ?'''
        try:
            conn = sql.connect('IDMS.db')
            cursor = conn.cursor()
            cursor.execute(query1, (symptom,))
            row = cursor.fetchone()
            id = int(row[0])
            illnessName = str(row[1])
            try:
                cursor.execute(query2, (id,))
                row1 = cursor.fetchone()
                self.ui.label_10.setText(illnessName)
                self.ui.label_12.setText(str(row1[0]))
                self.ui.label_14.setText(str(row1[1]))
                self.ui.label_17.setText(str(row1[2]))
                self.ui.label_19.setText(str(row1[3]))
                self.ui.label_21.setText(str(row1[4]))
                self.ui.label_25.setText(str(row1[5]))
                self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_3)
            except Exception as e:
                print(e)
                QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))

        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))



    #-------------------------------------------------------

    #----------------SaleHistory-------------------------
    def SaleHistory(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_sale_history)

    def SaleHistoryAll(self):      
        query = ''' SELECT P.UserID, U.Name, I.Illnessname, H.Name, D.Deptname, D.Doctorname, P.Date
                FROM PATIENTHISTORY P, USERS U, ILLNESS I, DEPARTMENT D, HOSPITAL H
                WHERE P.UserID = U.ID and P.IllnessID = I.IllnessID and P.DeptID = D.DeptID  and D.HospitalID = H.HospitalID and P.UserID = ?'''   
        try:
            conn = sql.connect('IDMS.db')
            cursor = conn.cursor()
            cursor.execute(query, (Login.ID,))
            row = cursor.fetchall()
            self.ui.tableWidget_2.setRowCount(0)
            for row_number, row_data in enumerate(row):
                self.ui.tableWidget_2.insertRow(row_number)
                for coloumn_number, data in enumerate(row_data):
                    self.ui.tableWidget_2.setItem(row_number, coloumn_number, QTableWidgetItem(str(data)))
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Error", "please Check again\nError: "+str(e))

