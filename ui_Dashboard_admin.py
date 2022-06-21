# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dashboard_admineAXpbF.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

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

        self.Hospital_btn = QPushButton(self.frame_7)
        self.Hospital_btn.setObjectName(u"Hospital_btn")
        self.Hospital_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.Hospital_btn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding: 10px 5px;\n"
"text-align: left;\n"
"font: 75 16pt \"Century Gothic\";\n"
"border-top-left-radius: 20px ;\n"
"border-bottom-left-radius: 20px ;\n"
"border-top-right-radius: 20px ;\n"
"border-bottom-right-radius: 20px ;")
        icon2 = QIcon()
        icon2.addFile(u":/icons_blue/icons/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Hospital_btn.setIcon(icon2)
        self.Hospital_btn.setIconSize(QSize(25, 25))
        self.Hospital_btn.setFlat(False)

        self.verticalLayout_9.addWidget(self.Hospital_btn)

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
        icon3 = QIcon()
        icon3.addFile(u":/icons_blue/icons/slack.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.inventory_btn.setIcon(icon3)
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
        icon4 = QIcon()
        icon4.addFile(u":/icons_blue/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sale_history_btn.setIcon(icon4)
        self.sale_history_btn.setIconSize(QSize(25, 25))
        self.sale_history_btn.setFlat(False)

        self.verticalLayout_9.addWidget(self.sale_history_btn)

        self.users_btn = QPushButton(self.frame_7)
        self.users_btn.setObjectName(u"users_btn")
        self.users_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.users_btn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding: 10px 5px;\n"
"text-align: left;\n"
"font: 75 16pt \"Century Gothic\";\n"
"border-top-left-radius: 20px ;\n"
"border-bottom-left-radius: 20px ;\n"
"border-top-right-radius: 20px ;\n"
"border-bottom-right-radius: 20px ;")
        icon5 = QIcon()
        icon5.addFile(u":/icons_blue/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.users_btn.setIcon(icon5)
        self.users_btn.setIconSize(QSize(25, 25))
        self.users_btn.setFlat(False)

        self.verticalLayout_9.addWidget(self.users_btn)

        self.custom_querying = QPushButton(self.frame_7)
        self.custom_querying.setObjectName(u"custom_querying")
        self.custom_querying.setCursor(QCursor(Qt.PointingHandCursor))
        self.custom_querying.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding: 10px 5px;\n"
"text-align: left;\n"
"font: 14pt \"Century Gothic\";\n"
"border-top-left-radius: 20px ;\n"
"border-bottom-left-radius: 20px ;\n"
"border-top-right-radius: 20px ;\n"
"border-bottom-right-radius: 20px ;")
        icon6 = QIcon()
        icon6.addFile(u":/icons_blue/icons/database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.custom_querying.setIcon(icon6)
        self.custom_querying.setIconSize(QSize(25, 25))
        self.custom_querying.setFlat(False)

        self.verticalLayout_9.addWidget(self.custom_querying)

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
        icon7 = QIcon()
        icon7.addFile(u":/icons_blue/icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.developer_info.setIcon(icon7)
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
        icon8 = QIcon()
        icon8.addFile(u":/icons_blue/icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_btn.setIcon(icon8)
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
        icon9 = QIcon()
        icon9.addFile(u":/icons_blue/icons/refresh-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.refresh_btn.setIcon(icon9)
        self.refresh_btn.setIconSize(QSize(20, 20))
        self.refresh_btn.setFlat(True)

        self.horizontalLayout_5.addWidget(self.refresh_btn)

        self.users_btn_2 = QPushButton(self.frame)
        self.users_btn_2.setObjectName(u"users_btn_2")
        self.users_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.users_btn_2.setAutoFillBackground(False)
        self.users_btn_2.setIcon(icon5)
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
        icon10 = QIcon()
        icon10.addFile(u":/icons_blue/icons/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_btn.setIcon(icon10)
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
        self.custom_query = QWidget()
        self.custom_query.setObjectName(u"custom_query")
        self.verticalLayout_150 = QVBoxLayout(self.custom_query)
        self.verticalLayout_150.setSpacing(0)
        self.verticalLayout_150.setObjectName(u"verticalLayout_150")
        self.verticalLayout_150.setContentsMargins(0, 0, 0, 0)
        self.frame_223 = QFrame(self.custom_query)
        self.frame_223.setObjectName(u"frame_223")
        self.frame_223.setFrameShape(QFrame.NoFrame)
        self.frame_223.setFrameShadow(QFrame.Plain)
        self.verticalLayout_149 = QVBoxLayout(self.frame_223)
        self.verticalLayout_149.setSpacing(0)
        self.verticalLayout_149.setObjectName(u"verticalLayout_149")
        self.verticalLayout_149.setContentsMargins(0, 0, 0, 0)
        self.label_72 = QLabel(self.frame_223)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setStyleSheet(u"font: 20pt \"Century Gothic\";")
        self.label_72.setAlignment(Qt.AlignCenter)

        self.verticalLayout_149.addWidget(self.label_72)


        self.verticalLayout_150.addWidget(self.frame_223)

        self.frame_224 = QFrame(self.custom_query)
        self.frame_224.setObjectName(u"frame_224")
        sizePolicy1.setHeightForWidth(self.frame_224.sizePolicy().hasHeightForWidth())
        self.frame_224.setSizePolicy(sizePolicy1)
        self.frame_224.setFrameShape(QFrame.NoFrame)
        self.frame_224.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_78 = QHBoxLayout(self.frame_224)
        self.horizontalLayout_78.setSpacing(0)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.frame_56 = QFrame(self.frame_224)
        self.frame_56.setObjectName(u"frame_56")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_56.sizePolicy().hasHeightForWidth())
        self.frame_56.setSizePolicy(sizePolicy5)
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.verticalLayout_162 = QVBoxLayout(self.frame_56)
        self.verticalLayout_162.setObjectName(u"verticalLayout_162")
        self.query_RadioBtn = QRadioButton(self.frame_56)
        self.query_RadioBtn.setObjectName(u"query_RadioBtn")
        self.query_RadioBtn.setStyleSheet(u"font: 12pt \"Century Gothic\";\n"
"")

        self.verticalLayout_162.addWidget(self.query_RadioBtn, 0, Qt.AlignTop)

        self.frame_240 = QFrame(self.frame_56)
        self.frame_240.setObjectName(u"frame_240")
        self.frame_240.setFrameShape(QFrame.StyledPanel)
        self.frame_240.setFrameShadow(QFrame.Raised)
        self.verticalLayout_174 = QVBoxLayout(self.frame_240)
        self.verticalLayout_174.setObjectName(u"verticalLayout_174")
        self.query_reset = QPushButton(self.frame_240)
        self.query_reset.setObjectName(u"query_reset")
        sizePolicy2.setHeightForWidth(self.query_reset.sizePolicy().hasHeightForWidth())
        self.query_reset.setSizePolicy(sizePolicy2)
        self.query_reset.setCursor(QCursor(Qt.PointingHandCursor))
        self.query_reset.setStyleSheet(u"font: 16pt \"Century Gothic\";")
        self.query_reset.setFlat(True)

        self.verticalLayout_174.addWidget(self.query_reset)

        self.query_header = QPushButton(self.frame_240)
        self.query_header.setObjectName(u"query_header")
        sizePolicy2.setHeightForWidth(self.query_header.sizePolicy().hasHeightForWidth())
        self.query_header.setSizePolicy(sizePolicy2)
        self.query_header.setCursor(QCursor(Qt.PointingHandCursor))
        self.query_header.setStyleSheet(u"font: 16pt \"Century Gothic\";")
        self.query_header.setFlat(True)

        self.verticalLayout_174.addWidget(self.query_header)

        self.query_save = QPushButton(self.frame_240)
        self.query_save.setObjectName(u"query_save")
        sizePolicy2.setHeightForWidth(self.query_save.sizePolicy().hasHeightForWidth())
        self.query_save.setSizePolicy(sizePolicy2)
        self.query_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.query_save.setStyleSheet(u"font: 16pt \"Century Gothic\";")
        self.query_save.setFlat(True)

        self.verticalLayout_174.addWidget(self.query_save)


        self.verticalLayout_162.addWidget(self.frame_240)

        self.frame_79 = QFrame(self.frame_56)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.verticalLayout_173 = QVBoxLayout(self.frame_79)
        self.verticalLayout_173.setObjectName(u"verticalLayout_173")
        self.query1 = QPushButton(self.frame_79)
        self.query1.setObjectName(u"query1")
        sizePolicy2.setHeightForWidth(self.query1.sizePolicy().hasHeightForWidth())
        self.query1.setSizePolicy(sizePolicy2)
        self.query1.setCursor(QCursor(Qt.PointingHandCursor))
        self.query1.setStyleSheet(u"font: 16pt \"Century Gothic\";")
        self.query1.setFlat(True)

        self.verticalLayout_173.addWidget(self.query1)

        self.query2 = QPushButton(self.frame_79)
        self.query2.setObjectName(u"query2")
        sizePolicy2.setHeightForWidth(self.query2.sizePolicy().hasHeightForWidth())
        self.query2.setSizePolicy(sizePolicy2)
        self.query2.setCursor(QCursor(Qt.PointingHandCursor))
        self.query2.setStyleSheet(u"font: 16pt \"Century Gothic\";")
        self.query2.setFlat(True)

        self.verticalLayout_173.addWidget(self.query2)

        self.query3 = QPushButton(self.frame_79)
        self.query3.setObjectName(u"query3")
        sizePolicy2.setHeightForWidth(self.query3.sizePolicy().hasHeightForWidth())
        self.query3.setSizePolicy(sizePolicy2)
        self.query3.setCursor(QCursor(Qt.PointingHandCursor))
        self.query3.setStyleSheet(u"font: 16pt \"Century Gothic\";")
        self.query3.setFlat(True)

        self.verticalLayout_173.addWidget(self.query3)

        self.query4 = QPushButton(self.frame_79)
        self.query4.setObjectName(u"query4")
        sizePolicy2.setHeightForWidth(self.query4.sizePolicy().hasHeightForWidth())
        self.query4.setSizePolicy(sizePolicy2)
        self.query4.setCursor(QCursor(Qt.PointingHandCursor))
        self.query4.setStyleSheet(u"font: 16pt \"Century Gothic\";")
        self.query4.setFlat(True)

        self.verticalLayout_173.addWidget(self.query4)

        self.query5 = QPushButton(self.frame_79)
        self.query5.setObjectName(u"query5")
        sizePolicy2.setHeightForWidth(self.query5.sizePolicy().hasHeightForWidth())
        self.query5.setSizePolicy(sizePolicy2)
        self.query5.setCursor(QCursor(Qt.PointingHandCursor))
        self.query5.setStyleSheet(u"font: 16pt \"Century Gothic\";")
        self.query5.setFlat(True)

        self.verticalLayout_173.addWidget(self.query5)


        self.verticalLayout_162.addWidget(self.frame_79, 0, Qt.AlignBottom)


        self.horizontalLayout_78.addWidget(self.frame_56)

        self.frame_48 = QFrame(self.frame_224)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_155 = QVBoxLayout(self.frame_48)
        self.verticalLayout_155.setObjectName(u"verticalLayout_155")
        self.frame_248 = QFrame(self.frame_48)
        self.frame_248.setObjectName(u"frame_248")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_248.sizePolicy().hasHeightForWidth())
        self.frame_248.setSizePolicy(sizePolicy6)
        self.frame_248.setFrameShape(QFrame.StyledPanel)
        self.frame_248.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_181 = QVBoxLayout(self.frame_248)
        self.verticalLayout_181.setSpacing(0)
        self.verticalLayout_181.setObjectName(u"verticalLayout_181")
        self.verticalLayout_181.setContentsMargins(0, 0, 0, 0)
        self.frame_249 = QFrame(self.frame_248)
        self.frame_249.setObjectName(u"frame_249")
        self.frame_249.setFrameShape(QFrame.StyledPanel)
        self.frame_249.setFrameShadow(QFrame.Raised)
        self.verticalLayout_182 = QVBoxLayout(self.frame_249)
        self.verticalLayout_182.setSpacing(0)
        self.verticalLayout_182.setObjectName(u"verticalLayout_182")
        self.verticalLayout_182.setContentsMargins(0, 0, 0, 0)
        self.label_119 = QLabel(self.frame_249)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setStyleSheet(u"font: 16pt \"Century Gothic\";")
        self.label_119.setAlignment(Qt.AlignCenter)

        self.verticalLayout_182.addWidget(self.label_119)


        self.verticalLayout_181.addWidget(self.frame_249, 0, Qt.AlignTop)

        self.frame_250 = QFrame(self.frame_248)
        self.frame_250.setObjectName(u"frame_250")
        sizePolicy1.setHeightForWidth(self.frame_250.sizePolicy().hasHeightForWidth())
        self.frame_250.setSizePolicy(sizePolicy1)
        self.frame_250.setFrameShape(QFrame.StyledPanel)
        self.frame_250.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_83 = QHBoxLayout(self.frame_250)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.query_table = QTableWidget(self.frame_250)
        if (self.query_table.columnCount() < 11):
            self.query_table.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.query_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.query_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.query_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.query_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.query_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.query_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.query_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.query_table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.query_table.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.query_table.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.query_table.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.query_table.setObjectName(u"query_table")
        self.query_table.setStyleSheet(u"font: 10pt \"Century Gothic\";\n"
"\n"
"")
        self.query_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.query_table.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed)
        self.query_table.setAlternatingRowColors(False)
        self.query_table.setSortingEnabled(False)

        self.horizontalLayout_83.addWidget(self.query_table)


        self.verticalLayout_181.addWidget(self.frame_250)


        self.verticalLayout_155.addWidget(self.frame_248)

        self.frame_225 = QFrame(self.frame_48)
        self.frame_225.setObjectName(u"frame_225")
        sizePolicy.setHeightForWidth(self.frame_225.sizePolicy().hasHeightForWidth())
        self.frame_225.setSizePolicy(sizePolicy)
        self.frame_225.setFrameShape(QFrame.NoFrame)
        self.frame_225.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_65 = QHBoxLayout(self.frame_225)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, -1, -1)
        self.frame_226 = QFrame(self.frame_225)
        self.frame_226.setObjectName(u"frame_226")
        self.frame_226.setFrameShape(QFrame.StyledPanel)
        self.frame_226.setFrameShadow(QFrame.Raised)
        self.verticalLayout_156 = QVBoxLayout(self.frame_226)
        self.verticalLayout_156.setSpacing(0)
        self.verticalLayout_156.setObjectName(u"verticalLayout_156")
        self.verticalLayout_156.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_226)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font: 16pt \"Century Gothic\";")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_156.addWidget(self.label_9)

        self.query_inbox = QPlainTextEdit(self.frame_226)
        self.query_inbox.setObjectName(u"query_inbox")
        self.query_inbox.setStyleSheet(u"font: 18pt \"Century Gothic\";")

        self.verticalLayout_156.addWidget(self.query_inbox, 0, Qt.AlignBottom)


        self.horizontalLayout_65.addWidget(self.frame_226)

        self.frame_47 = QFrame(self.frame_225)
        self.frame_47.setObjectName(u"frame_47")
        sizePolicy.setHeightForWidth(self.frame_47.sizePolicy().hasHeightForWidth())
        self.frame_47.setSizePolicy(sizePolicy)
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_172 = QVBoxLayout(self.frame_47)
        self.verticalLayout_172.setObjectName(u"verticalLayout_172")
        self.query_search = QPushButton(self.frame_47)
        self.query_search.setObjectName(u"query_search")
        sizePolicy2.setHeightForWidth(self.query_search.sizePolicy().hasHeightForWidth())
        self.query_search.setSizePolicy(sizePolicy2)
        self.query_search.setCursor(QCursor(Qt.PointingHandCursor))
        self.query_search.setStyleSheet(u"font: 16pt \"Century Gothic\";")
        self.query_search.setFlat(True)

        self.verticalLayout_172.addWidget(self.query_search)

        self.query_clear = QPushButton(self.frame_47)
        self.query_clear.setObjectName(u"query_clear")
        sizePolicy2.setHeightForWidth(self.query_clear.sizePolicy().hasHeightForWidth())
        self.query_clear.setSizePolicy(sizePolicy2)
        self.query_clear.setCursor(QCursor(Qt.PointingHandCursor))
        self.query_clear.setStyleSheet(u"font: 16pt \"Century Gothic\";")
        self.query_clear.setFlat(True)

        self.verticalLayout_172.addWidget(self.query_clear)


        self.horizontalLayout_65.addWidget(self.frame_47)


        self.verticalLayout_155.addWidget(self.frame_225)


        self.horizontalLayout_78.addWidget(self.frame_48)


        self.verticalLayout_150.addWidget(self.frame_224)

        self.stackedWidget.addWidget(self.custom_query)
        self.page_users = QWidget()
        self.page_users.setObjectName(u"page_users")
        self.verticalLayout_113 = QVBoxLayout(self.page_users)
        self.verticalLayout_113.setObjectName(u"verticalLayout_113")
        self.verticalLayout_113.setContentsMargins(0, 0, 0, 0)
        self.frame_108 = QFrame(self.page_users)
        self.frame_108.setObjectName(u"frame_108")
        self.frame_108.setFrameShape(QFrame.NoFrame)
        self.frame_108.setFrameShadow(QFrame.Plain)
        self.verticalLayout_76 = QVBoxLayout(self.frame_108)
        self.verticalLayout_76.setSpacing(0)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.label_57 = QLabel(self.frame_108)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setStyleSheet(u"font: 20pt \"Century Gothic\";")
        self.label_57.setAlignment(Qt.AlignCenter)

        self.verticalLayout_76.addWidget(self.label_57)


        self.verticalLayout_113.addWidget(self.frame_108)

        self.frame_117 = QFrame(self.page_users)
        self.frame_117.setObjectName(u"frame_117")
        sizePolicy1.setHeightForWidth(self.frame_117.sizePolicy().hasHeightForWidth())
        self.frame_117.setSizePolicy(sizePolicy1)
        self.frame_117.setFrameShape(QFrame.NoFrame)
        self.frame_117.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_117)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.frame_125 = QFrame(self.frame_117)
        self.frame_125.setObjectName(u"frame_125")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frame_125.sizePolicy().hasHeightForWidth())
        self.frame_125.setSizePolicy(sizePolicy7)
        self.frame_125.setFrameShape(QFrame.NoFrame)
        self.frame_125.setFrameShadow(QFrame.Plain)
        self.verticalLayout_88 = QVBoxLayout(self.frame_125)
        self.verticalLayout_88.setSpacing(0)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.verticalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.frame_126 = QFrame(self.frame_125)
        self.frame_126.setObjectName(u"frame_126")
        sizePolicy4.setHeightForWidth(self.frame_126.sizePolicy().hasHeightForWidth())
        self.frame_126.setSizePolicy(sizePolicy4)
        self.frame_126.setFrameShape(QFrame.StyledPanel)
        self.frame_126.setFrameShadow(QFrame.Raised)
        self.verticalLayout_92 = QVBoxLayout(self.frame_126)
        self.verticalLayout_92.setSpacing(0)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.verticalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.label_60 = QLabel(self.frame_126)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setStyleSheet(u"font: 16pt \"Century Gothic\";")
        self.label_60.setAlignment(Qt.AlignCenter)

        self.verticalLayout_92.addWidget(self.label_60)


        self.verticalLayout_88.addWidget(self.frame_126)

        self.frame_127 = QFrame(self.frame_125)
        self.frame_127.setObjectName(u"frame_127")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.frame_127.sizePolicy().hasHeightForWidth())
        self.frame_127.setSizePolicy(sizePolicy8)
        font = QFont()
        font.setFamily(u"Century Gothic")
        self.frame_127.setFont(font)
        self.frame_127.setAutoFillBackground(False)
        self.frame_127.setFrameShape(QFrame.NoFrame)
        self.frame_127.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_127)
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.frame_128 = QFrame(self.frame_127)
        self.frame_128.setObjectName(u"frame_128")
        sizePolicy5.setHeightForWidth(self.frame_128.sizePolicy().hasHeightForWidth())
        self.frame_128.setSizePolicy(sizePolicy5)
        self.frame_128.setFrameShape(QFrame.NoFrame)
        self.frame_128.setFrameShadow(QFrame.Plain)
        self.verticalLayout_93 = QVBoxLayout(self.frame_128)
        self.verticalLayout_93.setSpacing(0)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.verticalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.frame_130 = QFrame(self.frame_128)
        self.frame_130.setObjectName(u"frame_130")
        self.frame_130.setFrameShape(QFrame.StyledPanel)
        self.frame_130.setFrameShadow(QFrame.Raised)
        self.verticalLayout_95 = QVBoxLayout(self.frame_130)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.label_62 = QLabel(self.frame_130)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setStyleSheet(u"font: 12pt \"Century Gothic\";\n"
"")

        self.verticalLayout_95.addWidget(self.label_62)


        self.verticalLayout_93.addWidget(self.frame_130)

        self.frame_131 = QFrame(self.frame_128)
        self.frame_131.setObjectName(u"frame_131")
        self.frame_131.setFrameShape(QFrame.StyledPanel)
        self.frame_131.setFrameShadow(QFrame.Raised)
        self.verticalLayout_96 = QVBoxLayout(self.frame_131)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.label_63 = QLabel(self.frame_131)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setStyleSheet(u"font: 12pt \"Century Gothic\";\n"
"")

        self.verticalLayout_96.addWidget(self.label_63)


        self.verticalLayout_93.addWidget(self.frame_131)

        self.frame_132 = QFrame(self.frame_128)
        self.frame_132.setObjectName(u"frame_132")
        self.frame_132.setFrameShape(QFrame.StyledPanel)
        self.frame_132.setFrameShadow(QFrame.Raised)
        self.verticalLayout_97 = QVBoxLayout(self.frame_132)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.label_64 = QLabel(self.frame_132)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setStyleSheet(u"font: 12pt \"Century Gothic\";\n"
"")

        self.verticalLayout_97.addWidget(self.label_64)


        self.verticalLayout_93.addWidget(self.frame_132)

        self.frame_133 = QFrame(self.frame_128)
        self.frame_133.setObjectName(u"frame_133")
        self.frame_133.setFrameShape(QFrame.StyledPanel)
        self.frame_133.setFrameShadow(QFrame.Raised)
        self.verticalLayout_98 = QVBoxLayout(self.frame_133)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.label_65 = QLabel(self.frame_133)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setStyleSheet(u"font: 12pt \"Century Gothic\";\n"
"")

        self.verticalLayout_98.addWidget(self.label_65)


        self.verticalLayout_93.addWidget(self.frame_133)

        self.frame_198 = QFrame(self.frame_128)
        self.frame_198.setObjectName(u"frame_198")
        self.frame_198.setFrameShape(QFrame.StyledPanel)
        self.frame_198.setFrameShadow(QFrame.Raised)
        self.verticalLayout_143 = QVBoxLayout(self.frame_198)
        self.verticalLayout_143.setObjectName(u"verticalLayout_143")
        self.users_add_btn = QPushButton(self.frame_198)
        self.users_add_btn.setObjectName(u"users_add_btn")
        self.users_add_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.users_add_btn.setStyleSheet(u"font: 16pt \"Century Gothic\";")
        self.users_add_btn.setFlat(True)

        self.verticalLayout_143.addWidget(self.users_add_btn)


        self.verticalLayout_93.addWidget(self.frame_198)


        self.horizontalLayout_42.addWidget(self.frame_128)

        self.frame_137 = QFrame(self.frame_127)
        self.frame_137.setObjectName(u"frame_137")
        sizePolicy5.setHeightForWidth(self.frame_137.sizePolicy().hasHeightForWidth())
        self.frame_137.setSizePolicy(sizePolicy5)
        self.frame_137.setFrameShape(QFrame.NoFrame)
        self.frame_137.setFrameShadow(QFrame.Plain)
        self.verticalLayout_102 = QVBoxLayout(self.frame_137)
        self.verticalLayout_102.setSpacing(0)
        self.verticalLayout_102.setObjectName(u"verticalLayout_102")
        self.verticalLayout_102.setContentsMargins(0, 0, 0, 0)
        self.frame_139 = QFrame(self.frame_137)
        self.frame_139.setObjectName(u"frame_139")
        self.frame_139.setFrameShape(QFrame.StyledPanel)
        self.frame_139.setFrameShadow(QFrame.Raised)
        self.verticalLayout_104 = QVBoxLayout(self.frame_139)
        self.verticalLayout_104.setObjectName(u"verticalLayout_104")
        self.users_contact_no = QLineEdit(self.frame_139)
        self.users_contact_no.setObjectName(u"users_contact_no")
        sizePolicy4.setHeightForWidth(self.users_contact_no.sizePolicy().hasHeightForWidth())
        self.users_contact_no.setSizePolicy(sizePolicy4)

        self.verticalLayout_104.addWidget(self.users_contact_no)


        self.verticalLayout_102.addWidget(self.frame_139)

        self.frame_140 = QFrame(self.frame_137)
        self.frame_140.setObjectName(u"frame_140")
        self.frame_140.setFrameShape(QFrame.StyledPanel)
        self.frame_140.setFrameShadow(QFrame.Raised)
        self.verticalLayout_105 = QVBoxLayout(self.frame_140)
        self.verticalLayout_105.setObjectName(u"verticalLayout_105")
        self.users_username = QLineEdit(self.frame_140)
        self.users_username.setObjectName(u"users_username")
        sizePolicy4.setHeightForWidth(self.users_username.sizePolicy().hasHeightForWidth())
        self.users_username.setSizePolicy(sizePolicy4)

        self.verticalLayout_105.addWidget(self.users_username)


        self.verticalLayout_102.addWidget(self.frame_140)

        self.frame_141 = QFrame(self.frame_137)
        self.frame_141.setObjectName(u"frame_141")
        self.frame_141.setFrameShape(QFrame.StyledPanel)
        self.frame_141.setFrameShadow(QFrame.Raised)
        self.verticalLayout_106 = QVBoxLayout(self.frame_141)
        self.verticalLayout_106.setObjectName(u"verticalLayout_106")
        self.users_password = QLineEdit(self.frame_141)
        self.users_password.setObjectName(u"users_password")
        sizePolicy4.setHeightForWidth(self.users_password.sizePolicy().hasHeightForWidth())
        self.users_password.setSizePolicy(sizePolicy4)

        self.verticalLayout_106.addWidget(self.users_password)


        self.verticalLayout_102.addWidget(self.frame_141)

        self.frame_142 = QFrame(self.frame_137)
        self.frame_142.setObjectName(u"frame_142")
        self.frame_142.setFrameShape(QFrame.StyledPanel)
        self.frame_142.setFrameShadow(QFrame.Raised)
        self.verticalLayout_107 = QVBoxLayout(self.frame_142)
        self.verticalLayout_107.setObjectName(u"verticalLayout_107")
        self.users_id_type_combo = QComboBox(self.frame_142)
        self.users_id_type_combo.addItem("")
        self.users_id_type_combo.addItem("")
        self.users_id_type_combo.setObjectName(u"users_id_type_combo")
        self.users_id_type_combo.setCursor(QCursor(Qt.PointingHandCursor))
        self.users_id_type_combo.setStyleSheet(u"font: 10pt \"Century Gothic\";\n"
"")

        self.verticalLayout_107.addWidget(self.users_id_type_combo)


        self.verticalLayout_102.addWidget(self.frame_142)

        self.frame_199 = QFrame(self.frame_137)
        self.frame_199.setObjectName(u"frame_199")
        self.frame_199.setFrameShape(QFrame.StyledPanel)
        self.frame_199.setFrameShadow(QFrame.Raised)
        self.verticalLayout_144 = QVBoxLayout(self.frame_199)
        self.verticalLayout_144.setObjectName(u"verticalLayout_144")
        self.uses_clear_btn = QPushButton(self.frame_199)
        self.uses_clear_btn.setObjectName(u"uses_clear_btn")
        self.uses_clear_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.uses_clear_btn.setStyleSheet(u"font: 16pt \"Century Gothic\";")
        self.uses_clear_btn.setFlat(True)

        self.verticalLayout_144.addWidget(self.uses_clear_btn)


        self.verticalLayout_102.addWidget(self.frame_199)


        self.horizontalLayout_42.addWidget(self.frame_137)


        self.verticalLayout_88.addWidget(self.frame_127)

        self.User_RadioBtn = QRadioButton(self.frame_125)
        self.User_RadioBtn.setObjectName(u"User_RadioBtn")
        self.User_RadioBtn.setStyleSheet(u"font: 12pt \"Century Gothic\";\n"
"")

        self.verticalLayout_88.addWidget(self.User_RadioBtn, 0, Qt.AlignVCenter)

        self.frame_146 = QFrame(self.frame_125)
        self.frame_146.setObjectName(u"frame_146")
        sizePolicy.setHeightForWidth(self.frame_146.sizePolicy().hasHeightForWidth())
        self.frame_146.setSizePolicy(sizePolicy)
        self.frame_146.setFrameShape(QFrame.NoFrame)
        self.frame_146.setFrameShadow(QFrame.Plain)
        self.verticalLayout_100 = QVBoxLayout(self.frame_146)
        self.verticalLayout_100.setSpacing(0)
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")
        self.verticalLayout_100.setContentsMargins(0, 0, 0, 0)
        self.label_67 = QLabel(self.frame_146)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setStyleSheet(u"font: 16pt \"Century Gothic\";")
        self.label_67.setAlignment(Qt.AlignCenter)

        self.verticalLayout_100.addWidget(self.label_67, 0, Qt.AlignTop)

        self.frame_8 = QFrame(self.frame_146)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_101 = QVBoxLayout(self.frame_9)
        self.verticalLayout_101.setObjectName(u"verticalLayout_101")
        self.label_87 = QLabel(self.frame_9)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setStyleSheet(u"font: 12pt \"Century Gothic\";\n"
"")

        self.verticalLayout_101.addWidget(self.label_87)

        self.label_68 = QLabel(self.frame_9)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setStyleSheet(u"font: 12pt \"Century Gothic\";")

        self.verticalLayout_101.addWidget(self.label_68)

        self.label_70 = QLabel(self.frame_9)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setStyleSheet(u"font: 12pt \"Century Gothic\";\n"
"")

        self.verticalLayout_101.addWidget(self.label_70)


        self.horizontalLayout_43.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_114 = QVBoxLayout(self.frame_10)
        self.verticalLayout_114.setObjectName(u"verticalLayout_114")
        self.users_user_name = QLineEdit(self.frame_10)
        self.users_user_name.setObjectName(u"users_user_name")
        sizePolicy4.setHeightForWidth(self.users_user_name.sizePolicy().hasHeightForWidth())
        self.users_user_name.setSizePolicy(sizePolicy4)

        self.verticalLayout_114.addWidget(self.users_user_name)

        self.users_current_password = QLineEdit(self.frame_10)
        self.users_current_password.setObjectName(u"users_current_password")
        sizePolicy4.setHeightForWidth(self.users_current_password.sizePolicy().hasHeightForWidth())
        self.users_current_password.setSizePolicy(sizePolicy4)

        self.verticalLayout_114.addWidget(self.users_current_password)

        self.users_new_password = QLineEdit(self.frame_10)
        self.users_new_password.setObjectName(u"users_new_password")
        sizePolicy4.setHeightForWidth(self.users_new_password.sizePolicy().hasHeightForWidth())
        self.users_new_password.setSizePolicy(sizePolicy4)

        self.verticalLayout_114.addWidget(self.users_new_password)


        self.horizontalLayout_43.addWidget(self.frame_10)


        self.verticalLayout_100.addWidget(self.frame_8)

        self.frame_11 = QFrame(self.frame_146)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_115 = QVBoxLayout(self.frame_11)
        self.verticalLayout_115.setObjectName(u"verticalLayout_115")
        self.users_update_btn = QPushButton(self.frame_11)
        self.users_update_btn.setObjectName(u"users_update_btn")
        self.users_update_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.users_update_btn.setStyleSheet(u"font: 16pt \"Century Gothic\";")
        self.users_update_btn.setFlat(True)

        self.verticalLayout_115.addWidget(self.users_update_btn)

        self.users_delete_btn = QPushButton(self.frame_11)
        self.users_delete_btn.setObjectName(u"users_delete_btn")
        self.users_delete_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.users_delete_btn.setStyleSheet(u"font: 16pt \"Century Gothic\";")
        self.users_delete_btn.setFlat(True)

        self.verticalLayout_115.addWidget(self.users_delete_btn)


        self.verticalLayout_100.addWidget(self.frame_11)


        self.verticalLayout_88.addWidget(self.frame_146, 0, Qt.AlignBottom)


        self.horizontalLayout_41.addWidget(self.frame_125)

        self.frame_147 = QFrame(self.frame_117)
        self.frame_147.setObjectName(u"frame_147")
        sizePolicy6.setHeightForWidth(self.frame_147.sizePolicy().hasHeightForWidth())
        self.frame_147.setSizePolicy(sizePolicy6)
        self.frame_147.setFrameShape(QFrame.StyledPanel)
        self.frame_147.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_111 = QVBoxLayout(self.frame_147)
        self.verticalLayout_111.setSpacing(0)
        self.verticalLayout_111.setObjectName(u"verticalLayout_111")
        self.verticalLayout_111.setContentsMargins(0, 0, 0, 0)
        self.frame_148 = QFrame(self.frame_147)
        self.frame_148.setObjectName(u"frame_148")
        self.frame_148.setFrameShape(QFrame.StyledPanel)
        self.frame_148.setFrameShadow(QFrame.Raised)
        self.verticalLayout_112 = QVBoxLayout(self.frame_148)
        self.verticalLayout_112.setSpacing(0)
        self.verticalLayout_112.setObjectName(u"verticalLayout_112")
        self.verticalLayout_112.setContentsMargins(0, 0, 0, 0)
        self.label_69 = QLabel(self.frame_148)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setStyleSheet(u"font: 16pt \"Century Gothic\";")
        self.label_69.setAlignment(Qt.AlignCenter)

        self.verticalLayout_112.addWidget(self.label_69)


        self.verticalLayout_111.addWidget(self.frame_148, 0, Qt.AlignTop)

        self.frame_149 = QFrame(self.frame_147)
        self.frame_149.setObjectName(u"frame_149")
        sizePolicy1.setHeightForWidth(self.frame_149.sizePolicy().hasHeightForWidth())
        self.frame_149.setSizePolicy(sizePolicy1)
        self.frame_149.setFrameShape(QFrame.StyledPanel)
        self.frame_149.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_149)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.tableWidget_5 = QTableWidget(self.frame_149)
        if (self.tableWidget_5.columnCount() < 5):
            self.tableWidget_5.setColumnCount(5)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        self.tableWidget_5.setObjectName(u"tableWidget_5")
        self.tableWidget_5.setStyleSheet(u"font: 10pt \"Century Gothic\";\n"
"\n"
"")
        self.tableWidget_5.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_5.setSortingEnabled(True)

        self.horizontalLayout_52.addWidget(self.tableWidget_5)


        self.verticalLayout_111.addWidget(self.frame_149)


        self.horizontalLayout_41.addWidget(self.frame_147)


        self.verticalLayout_113.addWidget(self.frame_117)

        self.stackedWidget.addWidget(self.page_users)
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
        sizePolicy6.setHeightForWidth(self.frame_97.sizePolicy().hasHeightForWidth())
        self.frame_97.setSizePolicy(sizePolicy6)
        self.frame_97.setFrameShape(QFrame.NoFrame)
        self.frame_97.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_73 = QHBoxLayout(self.frame_97)
        self.horizontalLayout_73.setSpacing(0)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.frame_30 = QFrame(self.frame_97)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_82 = QVBoxLayout(self.frame_30)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.frame_222 = QFrame(self.frame_30)
        self.frame_222.setObjectName(u"frame_222")
        sizePolicy.setHeightForWidth(self.frame_222.sizePolicy().hasHeightForWidth())
        self.frame_222.setSizePolicy(sizePolicy)
        self.frame_222.setFrameShape(QFrame.NoFrame)
        self.frame_222.setFrameShadow(QFrame.Plain)
        self.verticalLayout_151 = QVBoxLayout(self.frame_222)
        self.verticalLayout_151.setSpacing(0)
        self.verticalLayout_151.setObjectName(u"verticalLayout_151")
        self.verticalLayout_151.setContentsMargins(0, 0, 0, 0)
        self.label_106 = QLabel(self.frame_222)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setStyleSheet(u"font: 16pt \"Century Gothic\";")
        self.label_106.setAlignment(Qt.AlignCenter)

        self.verticalLayout_151.addWidget(self.label_106, 0, Qt.AlignTop)

        self.frame_227 = QFrame(self.frame_222)
        self.frame_227.setObjectName(u"frame_227")
        self.frame_227.setFrameShape(QFrame.StyledPanel)
        self.frame_227.setFrameShadow(QFrame.Raised)
        self.verticalLayout_154 = QVBoxLayout(self.frame_227)
        self.verticalLayout_154.setSpacing(0)
        self.verticalLayout_154.setObjectName(u"verticalLayout_154")
        self.verticalLayout_154.setContentsMargins(0, 0, 0, 0)
        self.frame_228 = QFrame(self.frame_227)
        self.frame_228.setObjectName(u"frame_228")
        self.frame_228.setFrameShape(QFrame.StyledPanel)
        self.frame_228.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_81 = QHBoxLayout(self.frame_228)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.label_121 = QLabel(self.frame_228)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setStyleSheet(u"font: 12pt \"Century Gothic\";\n"
"")

        self.horizontalLayout_81.addWidget(self.label_121)

        self.employee_update_ssn_3 = QLineEdit(self.frame_228)
        self.employee_update_ssn_3.setObjectName(u"employee_update_ssn_3")
        self.employee_update_ssn_3.setStyleSheet(u"font: 10pt \"Century Gothic\";\n"
"\n"
"")

        self.horizontalLayout_81.addWidget(self.employee_update_ssn_3, 0, Qt.AlignRight)


        self.verticalLayout_154.addWidget(self.frame_228)

        self.sale_history_delete = QPushButton(self.frame_227)
        self.sale_history_delete.setObjectName(u"sale_history_delete")
        self.sale_history_delete.setCursor(QCursor(Qt.PointingHandCursor))
        self.sale_history_delete.setStyleSheet(u"font: 16pt \"Century Gothic\";")
        self.sale_history_delete.setFlat(True)

        self.verticalLayout_154.addWidget(self.sale_history_delete)

        self.frame_239 = QFrame(self.frame_227)
        self.frame_239.setObjectName(u"frame_239")
        sizePolicy4.setHeightForWidth(self.frame_239.sizePolicy().hasHeightForWidth())
        self.frame_239.setSizePolicy(sizePolicy4)
        self.frame_239.setFrameShape(QFrame.StyledPanel)
        self.frame_239.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_80 = QHBoxLayout(self.frame_239)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.sale_history_checkbox = QRadioButton(self.frame_239)
        self.sale_history_checkbox.setObjectName(u"sale_history_checkbox")
        sizePolicy8.setHeightForWidth(self.sale_history_checkbox.sizePolicy().hasHeightForWidth())
        self.sale_history_checkbox.setSizePolicy(sizePolicy8)
        self.sale_history_checkbox.setMinimumSize(QSize(53, 0))
        self.sale_history_checkbox.setStyleSheet(u"font: 12pt \"Century Gothic\";\n"
"")

        self.horizontalLayout_80.addWidget(self.sale_history_checkbox)


        self.verticalLayout_154.addWidget(self.frame_239, 0, Qt.AlignLeft)


        self.verticalLayout_151.addWidget(self.frame_227, 0, Qt.AlignBottom)


        self.verticalLayout_82.addWidget(self.frame_222, 0, Qt.AlignTop)

        self.sale_history_deleteAll = QPushButton(self.frame_30)
        self.sale_history_deleteAll.setObjectName(u"sale_history_deleteAll")
        self.sale_history_deleteAll.setCursor(QCursor(Qt.PointingHandCursor))
        self.sale_history_deleteAll.setStyleSheet(u"font: 16pt \"Century Gothic\";")
        self.sale_history_deleteAll.setFlat(True)

        self.verticalLayout_82.addWidget(self.sale_history_deleteAll)


        self.horizontalLayout_73.addWidget(self.frame_30)

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

        self.sale_history_billsearch = QLineEdit(self.frame_99)
        self.sale_history_billsearch.setObjectName(u"sale_history_billsearch")
        sizePolicy9 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.sale_history_billsearch.sizePolicy().hasHeightForWidth())
        self.sale_history_billsearch.setSizePolicy(sizePolicy9)
        self.sale_history_billsearch.setStyleSheet(u"font: 10pt \"Century Gothic\";\n"
"\n"
"")

        self.horizontalLayout_34.addWidget(self.sale_history_billsearch)

        self.sale_history_sort1_combo = QComboBox(self.frame_99)
        self.sale_history_sort1_combo.addItem("")
        self.sale_history_sort1_combo.addItem("")
        self.sale_history_sort1_combo.addItem("")
        self.sale_history_sort1_combo.setObjectName(u"sale_history_sort1_combo")
        self.sale_history_sort1_combo.setCursor(QCursor(Qt.PointingHandCursor))
        self.sale_history_sort1_combo.setStyleSheet(u"font: 10pt \"Century Gothic\";\n"
"")

        self.horizontalLayout_34.addWidget(self.sale_history_sort1_combo)


        self.horizontalLayout_33.addWidget(self.frame_99)

        self.frame_100 = QFrame(self.frame_98)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setFrameShape(QFrame.StyledPanel)
        self.frame_100.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_100)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.sale_history_sort2_combo = QComboBox(self.frame_100)
        self.sale_history_sort2_combo.setObjectName(u"sale_history_sort2_combo")
        self.sale_history_sort2_combo.setCursor(QCursor(Qt.PointingHandCursor))
        self.sale_history_sort2_combo.setStyleSheet(u"font: 10pt \"Century Gothic\";\n"
"\n"
"")

        self.horizontalLayout_35.addWidget(self.sale_history_sort2_combo)

        self.sale_history_search_btn = QPushButton(self.frame_100)
        self.sale_history_search_btn.setObjectName(u"sale_history_search_btn")
        self.sale_history_search_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.sale_history_search_btn.setStyleSheet(u"font: 12pt \"Century Gothic\";")
        self.sale_history_search_btn.setFlat(True)

        self.horizontalLayout_35.addWidget(self.sale_history_search_btn)

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
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem22)
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
        self.frame_160 = QFrame(self.frame_159)
        self.frame_160.setObjectName(u"frame_160")
        sizePolicy5.setHeightForWidth(self.frame_160.sizePolicy().hasHeightForWidth())
        self.frame_160.setSizePolicy(sizePolicy5)
        self.frame_160.setFrameShape(QFrame.NoFrame)
        self.frame_160.setFrameShadow(QFrame.Plain)
        self.verticalLayout_54 = QVBoxLayout(self.frame_160)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.frame_169 = QFrame(self.frame_160)
        self.frame_169.setObjectName(u"frame_169")
        sizePolicy4.setHeightForWidth(self.frame_169.sizePolicy().hasHeightForWidth())
        self.frame_169.setSizePolicy(sizePolicy4)
        self.frame_169.setFrameShape(QFrame.NoFrame)
        self.frame_169.setFrameShadow(QFrame.Plain)
        self.verticalLayout_125 = QVBoxLayout(self.frame_169)
        self.verticalLayout_125.setSpacing(0)
        self.verticalLayout_125.setObjectName(u"verticalLayout_125")
        self.verticalLayout_125.setContentsMargins(0, 0, 0, 0)
        self.frame_170 = QFrame(self.frame_169)
        self.frame_170.setObjectName(u"frame_170")
        self.frame_170.setFrameShape(QFrame.StyledPanel)
        self.frame_170.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_170)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_45 = QLabel(self.frame_170)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setStyleSheet(u"font: 16pt \"Century Gothic\";")
        self.label_45.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_45, 0, Qt.AlignBottom)

        self.frame_171 = QFrame(self.frame_170)
        self.frame_171.setObjectName(u"frame_171")
        self.frame_171.setFrameShape(QFrame.StyledPanel)
        self.frame_171.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.frame_171)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.new_combo = QComboBox(self.frame_171)
        self.new_combo.addItem("")
        self.new_combo.addItem("")
        self.new_combo.setObjectName(u"new_combo")
        self.new_combo.setStyleSheet(u"font: 10pt \"Century Gothic\";\n"
"")

        self.horizontalLayout_56.addWidget(self.new_combo)


        self.verticalLayout_17.addWidget(self.frame_171)

        self.frame_173 = QFrame(self.frame_170)
        self.frame_173.setObjectName(u"frame_173")
        self.frame_173.setFrameShape(QFrame.StyledPanel)
        self.frame_173.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_173)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.label_89 = QLabel(self.frame_173)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setStyleSheet(u"font: 12pt \"Century Gothic\";\n"
"")

        self.horizontalLayout_58.addWidget(self.label_89)

        self.new_name = QLineEdit(self.frame_173)
        self.new_name.setObjectName(u"new_name")

        self.horizontalLayout_58.addWidget(self.new_name)


        self.verticalLayout_17.addWidget(self.frame_173, 0, Qt.AlignTop)

        self.frame_174 = QFrame(self.frame_170)
        self.frame_174.setObjectName(u"frame_174")
        self.frame_174.setFrameShape(QFrame.StyledPanel)
        self.frame_174.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.frame_174)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.label_90 = QLabel(self.frame_174)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setStyleSheet(u"font: 12pt \"Century Gothic\";\n"
"")

        self.horizontalLayout_59.addWidget(self.label_90)

        self.new_name_2 = QLineEdit(self.frame_174)
        self.new_name_2.setObjectName(u"new_name_2")

        self.horizontalLayout_59.addWidget(self.new_name_2, 0, Qt.AlignRight)


        self.verticalLayout_17.addWidget(self.frame_174, 0, Qt.AlignTop)

        self.frame_184 = QFrame(self.frame_170)
        self.frame_184.setObjectName(u"frame_184")
        self.frame_184.setFrameShape(QFrame.StyledPanel)
        self.frame_184.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.frame_184)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.label_97 = QLabel(self.frame_184)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setStyleSheet(u"font: 12pt \"Century Gothic\";")

        self.horizontalLayout_68.addWidget(self.label_97)

        self.new_chemical3_combo = QComboBox(self.frame_184)
        self.new_chemical3_combo.addItem("")
        self.new_chemical3_combo.addItem("")
        self.new_chemical3_combo.addItem("")
        self.new_chemical3_combo.addItem("")
        self.new_chemical3_combo.addItem("")
        self.new_chemical3_combo.addItem("")
        self.new_chemical3_combo.addItem("")
        self.new_chemical3_combo.addItem("")
        self.new_chemical3_combo.addItem("")
        self.new_chemical3_combo.setObjectName(u"new_chemical3_combo")
        self.new_chemical3_combo.setStyleSheet(u"font: 10pt \"Century Gothic\";\n"
"")

        self.horizontalLayout_68.addWidget(self.new_chemical3_combo)


        self.verticalLayout_17.addWidget(self.frame_184)

        self.new_add = QPushButton(self.frame_170)
        self.new_add.setObjectName(u"new_add")
        self.new_add.setCursor(QCursor(Qt.PointingHandCursor))
        self.new_add.setStyleSheet(u"font: 16pt \"Century Gothic\";")
        self.new_add.setFlat(True)

        self.verticalLayout_17.addWidget(self.new_add)


        self.verticalLayout_125.addWidget(self.frame_170, 0, Qt.AlignVCenter)


        self.verticalLayout_54.addWidget(self.frame_169)

        self.radioButton = QRadioButton(self.frame_160)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"font: 12pt \"Century Gothic\";\n"
"")

        self.verticalLayout_54.addWidget(self.radioButton, 0, Qt.AlignVCenter)

        self.frame_203 = QFrame(self.frame_160)
        self.frame_203.setObjectName(u"frame_203")
        sizePolicy.setHeightForWidth(self.frame_203.sizePolicy().hasHeightForWidth())
        self.frame_203.setSizePolicy(sizePolicy)
        self.frame_203.setFrameShape(QFrame.NoFrame)
        self.frame_203.setFrameShadow(QFrame.Plain)
        self.verticalLayout_109 = QVBoxLayout(self.frame_203)
        self.verticalLayout_109.setSpacing(9)
        self.verticalLayout_109.setObjectName(u"verticalLayout_109")
        self.verticalLayout_109.setContentsMargins(0, 0, 0, 0)
        self.frame_204 = QFrame(self.frame_203)
        self.frame_204.setObjectName(u"frame_204")
        self.frame_204.setFrameShape(QFrame.StyledPanel)
        self.frame_204.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_204)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(9, 9, 9, 9)
        self.label_44 = QLabel(self.frame_204)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setStyleSheet(u"font: 16pt \"Century Gothic\";")
        self.label_44.setAlignment(Qt.AlignCenter)

        self.verticalLayout_46.addWidget(self.label_44, 0, Qt.AlignBottom)

        self.frame_205 = QFrame(self.frame_204)
        self.frame_205.setObjectName(u"frame_205")
        self.frame_205.setFrameShape(QFrame.StyledPanel)
        self.frame_205.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_205)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.inventory_update_combo_2 = QComboBox(self.frame_205)
        self.inventory_update_combo_2.addItem("")
        self.inventory_update_combo_2.addItem("")
        self.inventory_update_combo_2.setObjectName(u"inventory_update_combo_2")
        self.inventory_update_combo_2.setStyleSheet(u"font: 10pt \"Century Gothic\";\n"
"")

        self.horizontalLayout_31.addWidget(self.inventory_update_combo_2)


        self.verticalLayout_46.addWidget(self.frame_205)

        self.frame_206 = QFrame(self.frame_204)
        self.frame_206.setObjectName(u"frame_206")
        self.frame_206.setFrameShape(QFrame.StyledPanel)
        self.frame_206.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_70 = QHBoxLayout(self.frame_206)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.label_78 = QLabel(self.frame_206)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setStyleSheet(u"font: 12pt \"Century Gothic\";")

        self.horizontalLayout_70.addWidget(self.label_78)

        self.inventory_name_3 = QLineEdit(self.frame_206)
        self.inventory_name_3.setObjectName(u"inventory_name_3")

        self.horizontalLayout_70.addWidget(self.inventory_name_3, 0, Qt.AlignRight)


        self.verticalLayout_46.addWidget(self.frame_206, 0, Qt.AlignTop)

        self.frame_221 = QFrame(self.frame_204)
        self.frame_221.setObjectName(u"frame_221")
        self.frame_221.setFrameShape(QFrame.StyledPanel)
        self.frame_221.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_72 = QHBoxLayout(self.frame_221)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.label_80 = QLabel(self.frame_221)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setStyleSheet(u"font: 12pt \"Century Gothic\";\n"
"")

        self.horizontalLayout_72.addWidget(self.label_80)

        self.inventory_name_2 = QLineEdit(self.frame_221)
        self.inventory_name_2.setObjectName(u"inventory_name_2")

        self.horizontalLayout_72.addWidget(self.inventory_name_2, 0, Qt.AlignRight)


        self.verticalLayout_46.addWidget(self.frame_221, 0, Qt.AlignTop)

        self.new_delete_btn = QPushButton(self.frame_204)
        self.new_delete_btn.setObjectName(u"new_delete_btn")
        self.new_delete_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.new_delete_btn.setStyleSheet(u"font: 16pt \"Century Gothic\";")
        self.new_delete_btn.setFlat(True)

        self.verticalLayout_46.addWidget(self.new_delete_btn)


        self.verticalLayout_109.addWidget(self.frame_204, 0, Qt.AlignVCenter)


        self.verticalLayout_54.addWidget(self.frame_203, 0, Qt.AlignBottom)


        self.horizontalLayout_23.addWidget(self.frame_160)

        self.frame_176 = QFrame(self.frame_159)
        self.frame_176.setObjectName(u"frame_176")
        sizePolicy6.setHeightForWidth(self.frame_176.sizePolicy().hasHeightForWidth())
        self.frame_176.setSizePolicy(sizePolicy6)
        self.frame_176.setFrameShape(QFrame.StyledPanel)
        self.frame_176.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_126 = QVBoxLayout(self.frame_176)
        self.verticalLayout_126.setSpacing(0)
        self.verticalLayout_126.setObjectName(u"verticalLayout_126")
        self.verticalLayout_126.setContentsMargins(0, 0, 0, 0)
        self.frame_177 = QFrame(self.frame_176)
        self.frame_177.setObjectName(u"frame_177")
        self.frame_177.setFrameShape(QFrame.StyledPanel)
        self.frame_177.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.frame_177)
        self.horizontalLayout_61.setSpacing(0)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.frame_178 = QFrame(self.frame_177)
        self.frame_178.setObjectName(u"frame_178")
        self.frame_178.setFrameShape(QFrame.StyledPanel)
        self.frame_178.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.frame_178)
        self.horizontalLayout_62.setSpacing(0)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.label_92 = QLabel(self.frame_178)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setStyleSheet(u"font: 16pt \"Century Gothic\";")
        self.label_92.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_62.addWidget(self.label_92)


        self.horizontalLayout_61.addWidget(self.frame_178)

        self.frame_179 = QFrame(self.frame_177)
        self.frame_179.setObjectName(u"frame_179")
        self.frame_179.setFrameShape(QFrame.StyledPanel)
        self.frame_179.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.frame_179)
        self.horizontalLayout_63.setSpacing(0)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.new_show_all_btn = QPushButton(self.frame_179)
        self.new_show_all_btn.setObjectName(u"new_show_all_btn")
        self.new_show_all_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.new_show_all_btn.setStyleSheet(u"font: 12pt \"Century Gothic\";")
        self.new_show_all_btn.setFlat(True)

        self.horizontalLayout_63.addWidget(self.new_show_all_btn, 0, Qt.AlignRight)


        self.horizontalLayout_61.addWidget(self.frame_179)


        self.verticalLayout_126.addWidget(self.frame_177, 0, Qt.AlignTop)

        self.frame_181 = QFrame(self.frame_176)
        self.frame_181.setObjectName(u"frame_181")
        sizePolicy1.setHeightForWidth(self.frame_181.sizePolicy().hasHeightForWidth())
        self.frame_181.setSizePolicy(sizePolicy1)
        self.frame_181.setFrameShape(QFrame.StyledPanel)
        self.frame_181.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_64 = QHBoxLayout(self.frame_181)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.tableWidget_6 = QTableWidget(self.frame_181)
        if (self.tableWidget_6.columnCount() < 5):
            self.tableWidget_6.setColumnCount(5)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(3, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(4, __qtablewidgetitem27)
        self.tableWidget_6.setObjectName(u"tableWidget_6")
        self.tableWidget_6.setStyleSheet(u"font: 10pt \"Century Gothic\";\n"
"\n"
"")
        self.tableWidget_6.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_6.setSortingEnabled(False)

        self.horizontalLayout_64.addWidget(self.tableWidget_6)


        self.verticalLayout_126.addWidget(self.frame_181)


        self.horizontalLayout_23.addWidget(self.frame_176)


        self.verticalLayout_24.addWidget(self.frame_159)

        self.stackedWidget.addWidget(self.page_new)
        self.page_wholesaler = QWidget()
        self.page_wholesaler.setObjectName(u"page_wholesaler")
        self.verticalLayout_91 = QVBoxLayout(self.page_wholesaler)
        self.verticalLayout_91.setSpacing(0)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.verticalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.frame_124 = QFrame(self.page_wholesaler)
        self.frame_124.setObjectName(u"frame_124")
        self.frame_124.setFrameShape(QFrame.NoFrame)
        self.frame_124.setFrameShadow(QFrame.Plain)
        self.verticalLayout_90 = QVBoxLayout(self.frame_124)
        self.verticalLayout_90.setSpacing(0)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.verticalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.label_59 = QLabel(self.frame_124)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setStyleSheet(u"font: 20pt \"Century Gothic\";")
        self.label_59.setAlignment(Qt.AlignCenter)

        self.verticalLayout_90.addWidget(self.label_59)


        self.verticalLayout_91.addWidget(self.frame_124)

        self.frame_84 = QFrame(self.page_wholesaler)
        self.frame_84.setObjectName(u"frame_84")
        sizePolicy1.setHeightForWidth(self.frame_84.sizePolicy().hasHeightForWidth())
        self.frame_84.setSizePolicy(sizePolicy1)
        self.frame_84.setFrameShape(QFrame.NoFrame)
        self.frame_84.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_84)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.frame_85 = QFrame(self.frame_84)
        self.frame_85.setObjectName(u"frame_85")
        sizePolicy7.setHeightForWidth(self.frame_85.sizePolicy().hasHeightForWidth())
        self.frame_85.setSizePolicy(sizePolicy7)
        self.frame_85.setFrameShape(QFrame.NoFrame)
        self.frame_85.setFrameShadow(QFrame.Plain)
        self.verticalLayout_66 = QVBoxLayout(self.frame_85)
        self.verticalLayout_66.setSpacing(0)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.frame_86 = QFrame(self.frame_85)
        self.frame_86.setObjectName(u"frame_86")
        sizePolicy4.setHeightForWidth(self.frame_86.sizePolicy().hasHeightForWidth())
        self.frame_86.setSizePolicy(sizePolicy4)
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.verticalLayout_67 = QVBoxLayout(self.frame_86)
        self.verticalLayout_67.setSpacing(0)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.label_49 = QLabel(self.frame_86)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setStyleSheet(u"font: 16pt \"Century Gothic\";")
        self.label_49.setAlignment(Qt.AlignCenter)

        self.verticalLayout_67.addWidget(self.label_49, 0, Qt.AlignTop)


        self.verticalLayout_66.addWidget(self.frame_86)

        self.frame_87 = QFrame(self.frame_85)
        self.frame_87.setObjectName(u"frame_87")
        sizePolicy8.setHeightForWidth(self.frame_87.sizePolicy().hasHeightForWidth())
        self.frame_87.setSizePolicy(sizePolicy8)
        self.frame_87.setFont(font)
        self.frame_87.setAutoFillBackground(False)
        self.frame_87.setFrameShape(QFrame.NoFrame)
        self.frame_87.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_87)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.frame_88 = QFrame(self.frame_87)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setFrameShape(QFrame.NoFrame)
        self.frame_88.setFrameShadow(QFrame.Plain)
        self.verticalLayout_68 = QVBoxLayout(self.frame_88)
        self.verticalLayout_68.setSpacing(0)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.frame_102 = QFrame(self.frame_88)
        self.frame_102.setObjectName(u"frame_102")
        self.frame_102.setFrameShape(QFrame.StyledPanel)
        self.frame_102.setFrameShadow(QFrame.Raised)
        self.verticalLayout_70 = QVBoxLayout(self.frame_102)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.label_51 = QLabel(self.frame_102)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setStyleSheet(u"font: 12pt \"Century Gothic\";\n"
"")

        self.verticalLayout_70.addWidget(self.label_51)


        self.verticalLayout_68.addWidget(self.frame_102)

        self.frame_103 = QFrame(self.frame_88)
        self.frame_103.setObjectName(u"frame_103")
        self.frame_103.setFrameShape(QFrame.StyledPanel)
        self.frame_103.setFrameShadow(QFrame.Raised)
        self.verticalLayout_71 = QVBoxLayout(self.frame_103)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.label_52 = QLabel(self.frame_103)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setStyleSheet(u"font: 12pt \"Century Gothic\";\n"
"")

        self.verticalLayout_71.addWidget(self.label_52)


        self.verticalLayout_68.addWidget(self.frame_103)

        self.frame_104 = QFrame(self.frame_88)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setFrameShape(QFrame.StyledPanel)
        self.frame_104.setFrameShadow(QFrame.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.frame_104)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.label_53 = QLabel(self.frame_104)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setStyleSheet(u"font: 12pt \"Century Gothic\";\n"
"")

        self.verticalLayout_72.addWidget(self.label_53)


        self.verticalLayout_68.addWidget(self.frame_104)

        self.frame_107 = QFrame(self.frame_88)
        self.frame_107.setObjectName(u"frame_107")
        self.frame_107.setFrameShape(QFrame.StyledPanel)
        self.frame_107.setFrameShadow(QFrame.Raised)
        self.verticalLayout_75 = QVBoxLayout(self.frame_107)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.label_56 = QLabel(self.frame_107)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setStyleSheet(u"font: 12pt \"Century Gothic\";\n"
"")

        self.verticalLayout_75.addWidget(self.label_56)


        self.verticalLayout_68.addWidget(self.frame_107)

        self.frame_114 = QFrame(self.frame_88)
        self.frame_114.setObjectName(u"frame_114")
        self.frame_114.setFrameShape(QFrame.StyledPanel)
        self.frame_114.setFrameShadow(QFrame.Raised)
        self.verticalLayout_85 = QVBoxLayout(self.frame_114)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.label_76 = QLabel(self.frame_114)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setStyleSheet(u"font: 12pt \"Century Gothic\";\n"
"")

        self.verticalLayout_85.addWidget(self.label_76)


        self.verticalLayout_68.addWidget(self.frame_114)

        self.frame_115 = QFrame(self.frame_88)
        self.frame_115.setObjectName(u"frame_115")
        self.frame_115.setFrameShape(QFrame.StyledPanel)
        self.frame_115.setFrameShadow(QFrame.Raised)
        self.verticalLayout_86 = QVBoxLayout(self.frame_115)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.label_77 = QLabel(self.frame_115)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setStyleSheet(u"font: 12pt \"Century Gothic\";\n"
"")

        self.verticalLayout_86.addWidget(self.label_77)


        self.verticalLayout_68.addWidget(self.frame_115)

        self.frame_145 = QFrame(self.frame_88)
        self.frame_145.setObjectName(u"frame_145")
        self.frame_145.setFrameShape(QFrame.StyledPanel)
        self.frame_145.setFrameShadow(QFrame.Raised)
        self.verticalLayout_122 = QVBoxLayout(self.frame_145)
        self.verticalLayout_122.setObjectName(u"verticalLayout_122")
        self.label_86 = QLabel(self.frame_145)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setStyleSheet(u"font: 12pt \"Century Gothic\";\n"
"")

        self.verticalLayout_122.addWidget(self.label_86)


        self.verticalLayout_68.addWidget(self.frame_145)


        self.horizontalLayout_37.addWidget(self.frame_88)

        self.frame_109 = QFrame(self.frame_87)
        self.frame_109.setObjectName(u"frame_109")
        self.frame_109.setFrameShape(QFrame.NoFrame)
        self.frame_109.setFrameShadow(QFrame.Plain)
        self.verticalLayout_77 = QVBoxLayout(self.frame_109)
        self.verticalLayout_77.setSpacing(0)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.frame_111 = QFrame(self.frame_109)
        self.frame_111.setObjectName(u"frame_111")
        self.frame_111.setFrameShape(QFrame.StyledPanel)
        self.frame_111.setFrameShadow(QFrame.Raised)
        self.verticalLayout_79 = QVBoxLayout(self.frame_111)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.wholesaler_name = QLineEdit(self.frame_111)
        self.wholesaler_name.setObjectName(u"wholesaler_name")
        sizePolicy4.setHeightForWidth(self.wholesaler_name.sizePolicy().hasHeightForWidth())
        self.wholesaler_name.setSizePolicy(sizePolicy4)

        self.verticalLayout_79.addWidget(self.wholesaler_name)


        self.verticalLayout_77.addWidget(self.frame_111)

        self.frame_112 = QFrame(self.frame_109)
        self.frame_112.setObjectName(u"frame_112")
        self.frame_112.setFrameShape(QFrame.StyledPanel)
        self.frame_112.setFrameShadow(QFrame.Raised)
        self.verticalLayout_83 = QVBoxLayout(self.frame_112)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.wholesaler_phone_no = QLineEdit(self.frame_112)
        self.wholesaler_phone_no.setObjectName(u"wholesaler_phone_no")
        sizePolicy4.setHeightForWidth(self.wholesaler_phone_no.sizePolicy().hasHeightForWidth())
        self.wholesaler_phone_no.setSizePolicy(sizePolicy4)
        self.wholesaler_phone_no.setMaxLength(10)

        self.verticalLayout_83.addWidget(self.wholesaler_phone_no)


        self.verticalLayout_77.addWidget(self.frame_112)

        self.frame_113 = QFrame(self.frame_109)
        self.frame_113.setObjectName(u"frame_113")
        self.frame_113.setFrameShape(QFrame.StyledPanel)
        self.frame_113.setFrameShadow(QFrame.Raised)
        self.verticalLayout_84 = QVBoxLayout(self.frame_113)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.wholesaler_address = QLineEdit(self.frame_113)
        self.wholesaler_address.setObjectName(u"wholesaler_address")
        sizePolicy4.setHeightForWidth(self.wholesaler_address.sizePolicy().hasHeightForWidth())
        self.wholesaler_address.setSizePolicy(sizePolicy4)
        self.wholesaler_address.setClearButtonEnabled(False)

        self.verticalLayout_84.addWidget(self.wholesaler_address)


        self.verticalLayout_77.addWidget(self.frame_113)

        self.frame_116 = QFrame(self.frame_109)
        self.frame_116.setObjectName(u"frame_116")
        self.frame_116.setFrameShape(QFrame.StyledPanel)
        self.frame_116.setFrameShadow(QFrame.Raised)
        self.verticalLayout_87 = QVBoxLayout(self.frame_116)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.wholesaler_id_number = QLineEdit(self.frame_116)
        self.wholesaler_id_number.setObjectName(u"wholesaler_id_number")
        sizePolicy4.setHeightForWidth(self.wholesaler_id_number.sizePolicy().hasHeightForWidth())
        self.wholesaler_id_number.setSizePolicy(sizePolicy4)
        self.wholesaler_id_number.setMaxLength(10)

        self.verticalLayout_87.addWidget(self.wholesaler_id_number)


        self.verticalLayout_77.addWidget(self.frame_116)

        self.frame_153 = QFrame(self.frame_109)
        self.frame_153.setObjectName(u"frame_153")
        self.frame_153.setFrameShape(QFrame.StyledPanel)
        self.frame_153.setFrameShadow(QFrame.Raised)
        self.verticalLayout_123 = QVBoxLayout(self.frame_153)
        self.verticalLayout_123.setObjectName(u"verticalLayout_123")
        self.departmentcombo1 = QComboBox(self.frame_153)
        self.departmentcombo1.addItem("")
        self.departmentcombo1.addItem("")
        self.departmentcombo1.setObjectName(u"departmentcombo1")

        self.verticalLayout_123.addWidget(self.departmentcombo1)


        self.verticalLayout_77.addWidget(self.frame_153)

        self.frame_154 = QFrame(self.frame_109)
        self.frame_154.setObjectName(u"frame_154")
        self.frame_154.setFrameShape(QFrame.StyledPanel)
        self.frame_154.setFrameShadow(QFrame.Raised)
        self.verticalLayout_124 = QVBoxLayout(self.frame_154)
        self.verticalLayout_124.setObjectName(u"verticalLayout_124")
        self.wholesaler_id_number_3 = QLineEdit(self.frame_154)
        self.wholesaler_id_number_3.setObjectName(u"wholesaler_id_number_3")
        sizePolicy4.setHeightForWidth(self.wholesaler_id_number_3.sizePolicy().hasHeightForWidth())
        self.wholesaler_id_number_3.setSizePolicy(sizePolicy4)
        self.wholesaler_id_number_3.setMaxLength(10)

        self.verticalLayout_124.addWidget(self.wholesaler_id_number_3)


        self.verticalLayout_77.addWidget(self.frame_154)

        self.frame_155 = QFrame(self.frame_109)
        self.frame_155.setObjectName(u"frame_155")
        self.frame_155.setFrameShape(QFrame.StyledPanel)
        self.frame_155.setFrameShadow(QFrame.Raised)
        self.verticalLayout_128 = QVBoxLayout(self.frame_155)
        self.verticalLayout_128.setObjectName(u"verticalLayout_128")
        self.illnessNameCombo = QComboBox(self.frame_155)
        self.illnessNameCombo.addItem("")
        self.illnessNameCombo.addItem("")
        self.illnessNameCombo.addItem("")
        self.illnessNameCombo.addItem("")
        self.illnessNameCombo.addItem("")
        self.illnessNameCombo.addItem("")
        self.illnessNameCombo.addItem("")
        self.illnessNameCombo.addItem("")
        self.illnessNameCombo.addItem("")
        self.illnessNameCombo.addItem("")
        self.illnessNameCombo.setObjectName(u"illnessNameCombo")

        self.verticalLayout_128.addWidget(self.illnessNameCombo)


        self.verticalLayout_77.addWidget(self.frame_155)


        self.horizontalLayout_37.addWidget(self.frame_109)


        self.verticalLayout_66.addWidget(self.frame_87)

        self.Wholesaler_RadioButton = QRadioButton(self.frame_85)
        self.Wholesaler_RadioButton.setObjectName(u"Wholesaler_RadioButton")
        self.Wholesaler_RadioButton.setStyleSheet(u"font: 12pt \"Century Gothic\";\n"
"")

        self.verticalLayout_66.addWidget(self.Wholesaler_RadioButton, 0, Qt.AlignVCenter)

        self.frame_118 = QFrame(self.frame_85)
        self.frame_118.setObjectName(u"frame_118")
        sizePolicy.setHeightForWidth(self.frame_118.sizePolicy().hasHeightForWidth())
        self.frame_118.setSizePolicy(sizePolicy)
        self.frame_118.setFrameShape(QFrame.NoFrame)
        self.frame_118.setFrameShadow(QFrame.Plain)
        self.verticalLayout_10 = QVBoxLayout(self.frame_118)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.wholesaler_clear_btn = QPushButton(self.frame_118)
        self.wholesaler_clear_btn.setObjectName(u"wholesaler_clear_btn")
        self.wholesaler_clear_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.wholesaler_clear_btn.setStyleSheet(u"font: 16pt \"Century Gothic\";")
        self.wholesaler_clear_btn.setFlat(True)

        self.verticalLayout_10.addWidget(self.wholesaler_clear_btn)

        self.wholesaler_add_btn = QPushButton(self.frame_118)
        self.wholesaler_add_btn.setObjectName(u"wholesaler_add_btn")
        self.wholesaler_add_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.wholesaler_add_btn.setStyleSheet(u"font: 16pt \"Century Gothic\";")
        self.wholesaler_add_btn.setFlat(True)

        self.verticalLayout_10.addWidget(self.wholesaler_add_btn)

        self.wholesaler_update_btn = QPushButton(self.frame_118)
        self.wholesaler_update_btn.setObjectName(u"wholesaler_update_btn")
        self.wholesaler_update_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.wholesaler_update_btn.setStyleSheet(u"font: 16pt \"Century Gothic\";")
        self.wholesaler_update_btn.setFlat(True)

        self.verticalLayout_10.addWidget(self.wholesaler_update_btn)


        self.verticalLayout_66.addWidget(self.frame_118)


        self.horizontalLayout_36.addWidget(self.frame_85)

        self.frame_119 = QFrame(self.frame_84)
        self.frame_119.setObjectName(u"frame_119")
        sizePolicy6.setHeightForWidth(self.frame_119.sizePolicy().hasHeightForWidth())
        self.frame_119.setSizePolicy(sizePolicy6)
        self.frame_119.setFrameShape(QFrame.StyledPanel)
        self.frame_119.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_89 = QVBoxLayout(self.frame_119)
        self.verticalLayout_89.setSpacing(0)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.verticalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.frame_120 = QFrame(self.frame_119)
        self.frame_120.setObjectName(u"frame_120")
        self.frame_120.setFrameShape(QFrame.StyledPanel)
        self.frame_120.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_120)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.frame_121 = QFrame(self.frame_120)
        self.frame_121.setObjectName(u"frame_121")
        self.frame_121.setFrameShape(QFrame.StyledPanel)
        self.frame_121.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_121)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.label_58 = QLabel(self.frame_121)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setStyleSheet(u"font: 16pt \"Century Gothic\";")
        self.label_58.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_39.addWidget(self.label_58)

        self.wholesaler_sort1_combo = QComboBox(self.frame_121)
        self.wholesaler_sort1_combo.addItem("")
        self.wholesaler_sort1_combo.setObjectName(u"wholesaler_sort1_combo")
        self.wholesaler_sort1_combo.setCursor(QCursor(Qt.PointingHandCursor))
        self.wholesaler_sort1_combo.setStyleSheet(u"font: 10pt \"Century Gothic\";\n"
"")

        self.horizontalLayout_39.addWidget(self.wholesaler_sort1_combo)


        self.horizontalLayout_38.addWidget(self.frame_121)

        self.frame_122 = QFrame(self.frame_120)
        self.frame_122.setObjectName(u"frame_122")
        self.frame_122.setFrameShape(QFrame.StyledPanel)
        self.frame_122.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_122)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.wholesaler_sort2_combo = QComboBox(self.frame_122)
        self.wholesaler_sort2_combo.setObjectName(u"wholesaler_sort2_combo")
        self.wholesaler_sort2_combo.setCursor(QCursor(Qt.PointingHandCursor))
        self.wholesaler_sort2_combo.setStyleSheet(u"font: 10pt \"Century Gothic\";\n"
"")

        self.horizontalLayout_40.addWidget(self.wholesaler_sort2_combo)

        self.wholesaler_search = QPushButton(self.frame_122)
        self.wholesaler_search.setObjectName(u"wholesaler_search")
        self.wholesaler_search.setCursor(QCursor(Qt.PointingHandCursor))
        self.wholesaler_search.setStyleSheet(u"font: 12pt \"Century Gothic\";")
        self.wholesaler_search.setFlat(True)

        self.horizontalLayout_40.addWidget(self.wholesaler_search)

        self.wholesaler_show_all_btn = QPushButton(self.frame_122)
        self.wholesaler_show_all_btn.setObjectName(u"wholesaler_show_all_btn")
        self.wholesaler_show_all_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.wholesaler_show_all_btn.setStyleSheet(u"font: 12pt \"Century Gothic\";")
        self.wholesaler_show_all_btn.setFlat(True)

        self.horizontalLayout_40.addWidget(self.wholesaler_show_all_btn)


        self.horizontalLayout_38.addWidget(self.frame_122)


        self.verticalLayout_89.addWidget(self.frame_120, 0, Qt.AlignTop)

        self.frame_123 = QFrame(self.frame_119)
        self.frame_123.setObjectName(u"frame_123")
        sizePolicy1.setHeightForWidth(self.frame_123.sizePolicy().hasHeightForWidth())
        self.frame_123.setSizePolicy(sizePolicy1)
        self.frame_123.setFrameShape(QFrame.StyledPanel)
        self.frame_123.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_123)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.tableWidget_3 = QTableWidget(self.frame_123)
        if (self.tableWidget_3.columnCount() < 8):
            self.tableWidget_3.setColumnCount(8)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(7, __qtablewidgetitem35)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setStyleSheet(u"font: 10pt \"Century Gothic\";\n"
"\n"
"")
        self.tableWidget_3.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_3.setSortingEnabled(False)

        self.horizontalLayout_49.addWidget(self.tableWidget_3)


        self.verticalLayout_89.addWidget(self.frame_123)


        self.horizontalLayout_36.addWidget(self.frame_119)


        self.verticalLayout_91.addWidget(self.frame_84)

        self.stackedWidget.addWidget(self.page_wholesaler)
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
        self.stackedWidget.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CheckMySymptomps | Dashboard", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.dashboard_btn.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.Hospital_btn.setText(QCoreApplication.translate("MainWindow", u"Hospital", None))
        self.inventory_btn.setText(QCoreApplication.translate("MainWindow", u"Diseases", None))
        self.sale_history_btn.setText(QCoreApplication.translate("MainWindow", u"SearchHistory", None))
        self.users_btn.setText(QCoreApplication.translate("MainWindow", u"Users", None))
        self.custom_querying.setText(QCoreApplication.translate("MainWindow", u"Custom Query", None))
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
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Custom Querying", None))
        self.query_RadioBtn.setText(QCoreApplication.translate("MainWindow", u"Enable Table Sorting", None))
        self.query_reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.query_header.setText(QCoreApplication.translate("MainWindow", u"Add Header", None))
        self.query_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.query1.setText(QCoreApplication.translate("MainWindow", u"Query 1", None))
        self.query2.setText(QCoreApplication.translate("MainWindow", u"Query 2", None))
        self.query3.setText(QCoreApplication.translate("MainWindow", u"Query 3", None))
        self.query4.setText(QCoreApplication.translate("MainWindow", u"Query 4", None))
        self.query5.setText(QCoreApplication.translate("MainWindow", u"Query 5", None))
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"Table", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Enter a Query", None))
        self.query_search.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.query_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Users", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Add User", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"User Name", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.users_add_btn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.users_contact_no.setPlaceholderText("")
        self.users_username.setPlaceholderText("")
        self.users_password.setPlaceholderText("")
        self.users_id_type_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"Admin", None))
        self.users_id_type_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"User", None))

        self.uses_clear_btn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.User_RadioBtn.setText(QCoreApplication.translate("MainWindow", u"Enable Table Sorting", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Change Profile Password", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"User ID", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"User Name", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"New Password", None))
        self.users_user_name.setPlaceholderText("")
        self.users_current_password.setPlaceholderText("")
        self.users_new_password.setPlaceholderText("")
        self.users_update_btn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.users_delete_btn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Users Profiles", None))
        ___qtablewidgetitem = self.tableWidget_5.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget_5.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.tableWidget_5.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"User Name", None));
        ___qtablewidgetitem3 = self.tableWidget_5.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Password", None));
        ___qtablewidgetitem4 = self.tableWidget_5.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Patient Search History", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"Update Search History", None))
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"Patient ID", None))
        self.sale_history_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.sale_history_checkbox.setText(QCoreApplication.translate("MainWindow", u"Enable Table Sorting", None))
        self.sale_history_deleteAll.setText(QCoreApplication.translate("MainWindow", u"Delete All", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Categories", None))
        self.sale_history_sort1_combo.setItemText(0, "")
        self.sale_history_sort1_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"ILLNESS", None))
        self.sale_history_sort1_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"Hospital", None))

        self.sale_history_search_btn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.sale_history_show_all_btn.setText(QCoreApplication.translate("MainWindow", u"Show All", None))
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"PatientID", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u" ILLNESS", None));
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Hospital Name", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Dept Name", None));
        ___qtablewidgetitem10 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Doctor Name", None));
        ___qtablewidgetitem11 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"Diseases", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Add New", None))
        self.new_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"Disease", None))
        self.new_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"Agent", None))

        self.label_89.setText(QCoreApplication.translate("MainWindow", u"Illnessname", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"Agents", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"Symptomps", None))
        self.new_chemical3_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"Fever", None))
        self.new_chemical3_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"Cough", None))
        self.new_chemical3_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"Head Ache", None))
        self.new_chemical3_combo.setItemText(3, QCoreApplication.translate("MainWindow", u"Body Pain", None))
        self.new_chemical3_combo.setItemText(4, QCoreApplication.translate("MainWindow", u"Itching", None))
        self.new_chemical3_combo.setItemText(5, QCoreApplication.translate("MainWindow", u"Cold", None))
        self.new_chemical3_combo.setItemText(6, QCoreApplication.translate("MainWindow", u"Tiredness", None))
        self.new_chemical3_combo.setItemText(7, QCoreApplication.translate("MainWindow", u"Fast HeartBeat", None))
        self.new_chemical3_combo.setItemText(8, QCoreApplication.translate("MainWindow", u"Vomiting", None))

        self.new_add.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Enable Table Sorting", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Delete Section", None))
        self.inventory_update_combo_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Disease", None))
        self.inventory_update_combo_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Agent", None))

        self.label_78.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.new_delete_btn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"Categories", None))
        self.new_show_all_btn.setText(QCoreApplication.translate("MainWindow", u"Show All", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Hospitals", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Hospitals", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Hospital Name", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"City", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"State", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Department", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Doctor Name", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"illness", None))
        self.wholesaler_name.setPlaceholderText("")
        self.wholesaler_phone_no.setPlaceholderText("")
        self.wholesaler_address.setPlaceholderText("")
        self.wholesaler_id_number.setPlaceholderText("")
        self.departmentcombo1.setItemText(0, QCoreApplication.translate("MainWindow", u"Virology Department", None))
        self.departmentcombo1.setItemText(1, QCoreApplication.translate("MainWindow", u"Bactiriology Department", None))

        self.wholesaler_id_number_3.setPlaceholderText("")
        self.illnessNameCombo.setItemText(0, QCoreApplication.translate("MainWindow", u"Corona", None))
        self.illnessNameCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"Sepisis", None))
        self.illnessNameCombo.setItemText(2, QCoreApplication.translate("MainWindow", u"Zoonosis", None))
        self.illnessNameCombo.setItemText(3, QCoreApplication.translate("MainWindow", u"HIV/AIDS", None))
        self.illnessNameCombo.setItemText(4, QCoreApplication.translate("MainWindow", u"Common cold", None))
        self.illnessNameCombo.setItemText(5, QCoreApplication.translate("MainWindow", u"Viral fever", None))
        self.illnessNameCombo.setItemText(6, QCoreApplication.translate("MainWindow", u"Zika", None))
        self.illnessNameCombo.setItemText(7, QCoreApplication.translate("MainWindow", u"Malaria", None))
        self.illnessNameCombo.setItemText(8, QCoreApplication.translate("MainWindow", u"Dengue", None))
        self.illnessNameCombo.setItemText(9, QCoreApplication.translate("MainWindow", u"Bird Flue", None))

        self.Wholesaler_RadioButton.setText(QCoreApplication.translate("MainWindow", u"Enable Table Sorting", None))
        self.wholesaler_clear_btn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.wholesaler_add_btn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.wholesaler_update_btn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Categories", None))
        self.wholesaler_sort1_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"Hospital", None))

        self.wholesaler_search.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.wholesaler_show_all_btn.setText(QCoreApplication.translate("MainWindow", u"Show All", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Welcome", None))
        self.user_name.setText(QCoreApplication.translate("MainWindow", u"User_Name", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Number of Hospitals", None))
        self.number_of_Hospitals.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Number of Cases", None))
        self.number_of_cases.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Number of Doctors", None))
        self.number_of_doctors.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"Number of Users", None))
        self.total_users.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"Number of Diseases", None))
        self.total_diseases.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Health and Illness @Anil kumar @Sumanth Hegde", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Ver - 1.000.3  ", None))
    # retranslateUi

