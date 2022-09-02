from unicodedata import name
from PyQt5.Qt import QUrl, QDesktopServices
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QFrame, QStackedWidget, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineSettings
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
import json
import pandas as pd
import random
import sys
import os


# for Opening links in a new window with QWebEngineView - landing_page - "Enjoyed using it? share"
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage

# *********************************************
#                  FRAME 1
# *********************************************


class LandingPage(QMainWindow):
    def __init__(self):
        super(LandingPage, self).__init__()
        uic.loadUi("./ui/landing_page.ui", self)

        self.setWindowTitle("StudyBlu")
        # Finding the button
        # button7  -> Exit
        # button8  -> Share
        # button9  -> Course_1
        # button10 -> Course_2
        # button11 -> Course_3

<<<<<<< Updated upstream
        # self.button1 = self.findChild(QPushButton, "pushButton")
        # self.button1.clicked.connect(self.gotocp)
=======
        self.shareButton = self.findChild(QPushButton, "pushButton_8")
        self.shareButton.clicked.connect(self.share)
>>>>>>> Stashed changes

        self.backButton = self.findChild(QPushButton, "pushButton_7")
        self.backButton.clicked.connect(self.exit)

<<<<<<< Updated upstream
        # self.button7 = self.findChild(QPushButton, "pushButton_7")
        # self.button7.clicked.connect(self.exit)

        self.button9 = self.findChild(QPushButton, "course_no_1")
        self.button9.clicked.connect(lambda: self.goto_rp(1))

        self.button10 = self.findChild(QPushButton, "course_no_2")
        self.button10.clicked.connect(lambda: self.goto_rp(2))

        self.button11 = self.findChild(QPushButton, "course_no_3")
        self.button11.clicked.connect(lambda: self.goto_rp(3))
=======
        for i in range(1, 4):
            self.findChild(QPushButton, f"course_no_{i}")\
                .clicked.connect(lambda: self.goto_rp(i))
>>>>>>> Stashed changes

    def share(self):
        url = QUrl("https://www.kavach.org.in/")
        QDesktopServices.openUrl(url)

    def exit(self):
        sys.exit(app.exec())

    def goto_rp(self, courseNumber=1):
        screen2 = ReadingPage(courseNumber)
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex()+1)

# *********************************************
#                  FRAME 2
# *********************************************


class ReadingPage(QMainWindow):
    def __init__(self, courseNumber):
        super(ReadingPage, self).__init__()
        uic.loadUi("./ui/course_reading.ui", self)

        self.button = self.findChild(QPushButton, "pushButton")
        self.button.clicked.connect(self.back)

        # Course material
        self.text = self.findChild(QLabel, "Para1")

        # HTML Embedding
        self.htmlV = QtWebEngineWidgets.QWebEngineView(self)
        containing_layout = self.text.parent().layout()
        containing_layout.replaceWidget(self.text, self.htmlV)
        # Loading HTML
        with open(f"./reading/course_{courseNumber}.html", "r", encoding="utf-8") as f:
            html = f.read()
        self.htmlV.setHtml(html, QtCore.QUrl("local"))

    def back(self):
        screen1 = LandingPage()
        widget.addWidget(screen1)
        widget.setCurrentIndex(widget.currentIndex()+1)


if __name__ == '__main__':
    # Initialize the program
    app = QApplication(sys.argv)
    widget = QStackedWidget()
    mainwindow = LandingPage()
    widget.addWidget(mainwindow)
    # fixed sizing causes window to be un resizable and the values used are too big
    # widget.setFixedHeight(1000)
    # widget.setFixedWidth(1900)
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting...")
