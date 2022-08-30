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


class Course_Player (QMainWindow):

    def __init__(self, *args, **kwargs):
        super(Course_Player, self).__init__(*args, **kwargs)

        self.setWindowTitle("Course Player")
        self.setFixedWidth(1920)
        self.setFixedHeight(1080)

        label = QLabel("")

        # The `Qt` namespace has a lot of attributes to customise
        # widgets. See: http://doc.qt.io/qt-5/qt.html
        label.setAlignment(Qt.AlignCenter)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(label)

        # Code for 1 Youtube video and its QtWidget
        # ======================================================================================

        self.centralwid = QtWidgets.QWidget(self)
        self.centralwid.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.centralwid.setObjectName("centralwid")
        self.label_loading_browsers = QtWidgets.QLabel(self.centralwid)
        # ===================== HERE IS THE CODE FOR IFRAM YOUTUBE ============================
        self.vlayout = QtWidgets.QVBoxLayout()
        self.webview = QtWebEngineWidgets.QWebEngineView()
        self.webview.settings().setAttribute(
            QWebEngineSettings.FullScreenSupportEnabled, True)
        self.webview.settings().setAttribute(
            QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
        self.webview.settings().setAttribute(
            QWebEngineSettings.AllowRunningInsecureContent, True)
        self.webview.page().fullScreenRequested.connect(lambda request: request.accept())
        baseUrl = "local"
        htmlString = """
                        <iframe width="1900" height="950" src="https://www.youtube.com/embed/g8NVwN0_mks?rel=0&amp;showinfo=0" frameborder="0" allowfullscreen></iframe>
                                """

        self.webview.setHtml(htmlString, QUrl(baseUrl))
        self.vlayout.addWidget(self.webview)
        self.centralwid.setLayout(self.vlayout)


class LandingPage(QMainWindow):
    def __init__(self):
        super(LandingPage, self).__init__()
        uic.loadUi("./ui/landing_page.ui", self)

        # Finding the button
        # button1 -> Get Started
        # button7 -> Exit
        # button8 -> Share
        # button9 -> Course_1

        self.button1 = self.findChild(QPushButton, "pushButton")
        self.button1.clicked.connect(self.gotocp)

        self.button8 = self.findChild(QPushButton, "pushButton_8")
        self.button8.clicked.connect(self.share)

        self.button7 = self.findChild(QPushButton, "pushButton_7")
        self.button7.clicked.connect(self.exit)

        self.button9 = self.findChild(QPushButton, "course_no_1")
        self.button9.clicked.connect(self.goto_course_player)

    def share(self):
        url = QUrl("https://www.google.co.in/")
        QDesktopServices.openUrl(url)

    def gotocp(self):
        screen2 = CourseInfo()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def exit(self):
        sys.exit(app.exec())

    def goto_course_player(self):
        app = QApplication(sys.argv)
        window = Course_Player()
        window.show()
        app.exec_()

# *********************************************
#                  FRAME 2
# *********************************************


class CourseInfo(QMainWindow):
    def __init__(self):
        super(CourseInfo, self).__init__()
        uic.loadUi("./ui/course_info.ui", self)

        # On-clicking this button python will be executing the function gotorp and showing the app
        # button -> Start Reading
        # button1 -> terminal
        # button2 -> Quiz
        # button3 -> Back
        # button4 -> terminal game

        self.button = self.findChild(QPushButton, "pushButton")
        self.button.clicked.connect(self.gotorp)

        self.button2 = self.findChild(QPushButton, "pushButton_5")
        self.button2.clicked.connect(self.gotoq)

        self.button3 = self.findChild(QPushButton, "pushButton_3")
        self.button3.clicked.connect(self.back)

        self.button4 = self.findChild(QPushButton, "pushButton_4")
        self.button4.clicked.connect(self.terminalgame)

        self.button5 = self.findChild(QPushButton, "pushButton_2")
        self.button5.clicked.connect(self.share)
        # not sure what the error is but this left uncommented gives:
        # "AttributeError: 'NoneType' object has no attribute 'clicked'" when i click the start reading button on the landing page
        # self.button5 = self.findChild(QPushButton, "pushButton_2")
        # self.button5.clicked.connect(self.share)

    def gotorp(self):
        screen2 = ReadingPage()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex()+1)
        # print(widget.currentIndex()+1)

    def back(self):
        screen1 = LandingPage()
        widget.addWidget(screen1)
        widget.setCurrentIndex(widget.currentIndex()+1)
        # print(widget.currentIndex()+1)

    def gotoq(self):
        screen1 = QuizGame()
        widget.addWidget(screen1)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def terminalgame(self):
        screen1 = TerminalGame()
        widget.addWidget(screen1)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def share(self):
        url = QUrl("https://www.google.co.in/")
        QDesktopServices.openUrl(url)

# *********************************************
#                  FRAME 3
# *********************************************


class ReadingPage(QMainWindow):
    def __init__(self):
        super(ReadingPage, self).__init__()
        uic.loadUi("./ui/course_reading.ui", self)

        self.button = self.findChild(QPushButton, "pushButton")
        self.button.clicked.connect(self.back)

        # Course material
        self.text = self.findChild(QLabel, "Para1")
        # with open("./reading/file.txt") as f:
        #     __content = f.read()
        #     self.text.setText(__content)

        # HTML Embedding
        self.htmlView = QtWidgets.QTextBrowser(self)
        # Replace Label with TextBrowser
        containing_layout = self.text.parent().layout()
        containing_layout.replaceWidget(self.text, self.htmlView)
        # Loading HTML
        self.htmlView.setSource(
            QtCore.QUrl.fromLocalFile("./reading/course.html"))

    def back(self):
        screen1 = CourseInfo()
        widget.addWidget(screen1)
        widget.setCurrentIndex(widget.currentIndex()+1)


# *********************************************
#                  Terminal Game
# *********************************************

class TerminalGame(QMainWindow):
    def __init__(self):
        super(TerminalGame, self).__init__()
        uic.loadUi("./ui/terminal_game.ui", self)

        self.button = self.findChild(QPushButton, "pushButton")
        self.button.clicked.connect(self.back)

    def back(self):
        screen1 = CourseInfo()
        widget.addWidget(screen1)
        widget.setCurrentIndex(widget.currentIndex()+1)
        print(widget.currentIndex()+1)

# *********************************************
#                  Score Page
# *********************************************


class QuizScore(QMainWindow):
    def __init__(self, score):
        super(QuizScore, self).__init__()
        uic.loadUi("./ui/quiz_score.ui", self)
        self.QuestionText.setText(str(score))

        self.button = self.findChild(QPushButton, "pushButton")
        self.button.clicked.connect(self.back)

    def back(self):
        screen1 = CourseInfo()
        widget.addWidget(screen1)
        widget.setCurrentIndex(widget.currentIndex()+1)
        print(widget.currentIndex()+1)

# *********************************************
#                  Quiz Game
# *********************************************


class QuizGame(QMainWindow):
    def __init__(self):
        super(QuizGame, self).__init__()
        uic.loadUi("/ui/quiz_game.ui", self)

        self.button = self.findChild(QPushButton, "pushButton")
        self.button.clicked.connect(self.back)

        self.parameters = {
            "question": [],
            "answer1": [],
            "answer2": [],
            "answer3": [],
            "answer4": [],
            "correct": [],
            "score": [],
            "index": [],
            "hint": [],
            "pAnsExp": [],
            "questionNo": []
        }

        self.clear_parameters()
        self.preload_data(self.parameters["index"][-1])
        self.quiz()

    f = open('quiz/data.json')
    data = json.load(f)
    df = pd.DataFrame(data["results"])
    # load 1 instance of questions & answers at a time from the database

    def back(self):
        screen1 = CourseInfo()
        widget.addWidget(screen1)
        widget.setCurrentIndex(widget.currentIndex()+1)
        # print(widget.currentIndex()+1)

    def quiz(self):
        # Score
        score = self.parameters["score"][-1]
        self.ScoreCounter.setText(str(score))

        # Question
        question = self.parameters["question"][-1]
        questionNo = self.parameters["questionNo"][-1]
        self.QuestionText.setText(str(questionNo) + ". " + str(question))

        # Answers
        answer1 = self.parameters["answer1"][-1]
        self.Option1.setText(answer1)
        self.Option1.clicked.connect(lambda x: self.is_correct(self.Option1))

        answer2 = self.parameters["answer2"][-1]
        self.Option2.setText(answer2)
        self.Option2.clicked.connect(lambda x: self.is_correct(self.Option2))

        answer3 = self.parameters["answer3"][-1]
        self.Option3.setText(answer3)
        self.Option3.clicked.connect(lambda x: self.is_correct(self.Option3))

        answer4 = self.parameters["answer4"][-1]
        self.Option4.setText(answer4)
        self.Option4.clicked.connect(lambda x: self.is_correct(self.Option4))

        # Hint
        hint = self.parameters["hint"][-1]
        self.SHORTCheck.setText("")
        self.AnswerExplanation.setText(hint)

        self.NextQuestion.setEnabled(False)
        self.button = self.findChild(QPushButton, "NextQuestion")
        self.button.clicked.connect(self.next)

    def preload_data(self, idx):
        # idx parm: selected randomly time and again at function call
        question = self.df["question"][idx]
        correct = self.df["correct_answer"][idx]
        wrong = self.df["incorrect_answers"][idx]
        hint = self.df["hint"][idx]
        answerexp = self.df["AnswerExp"][idx]

        # store local values globally
        self.parameters["question"].append(question)
        self.parameters["correct"].append(correct)

        all_answers = wrong + [correct]
        random.shuffle(all_answers)

        self.parameters["answer1"].append(all_answers[0])
        self.parameters["answer2"].append(all_answers[1])
        self.parameters["answer3"].append(all_answers[2])
        self.parameters["answer4"].append(all_answers[3])
        self.parameters["hint"].append(hint)
        self.parameters["pAnsExp"].append(answerexp)

        # print correct answer to the terminal (for testing)
        print(self.parameters["question"][-1])
        print(self.parameters["correct"][-1])

    def clear_parameters(self):
        # clear the global dictionary of parameters
        for parm in self.parameters:
            if self.parameters[parm] != []:
                for i in range(0, len(self.parameters[parm])):
                    self.parameters[parm].pop()
        # populate with initial index & score values
        random_index = [x for x in range(7)]
        random.shuffle(random_index)
        self.parameters["index"] = random_index + self.parameters["index"]
        self.parameters["score"].append(0)
        self.parameters["questionNo"].append(1)

    def is_correct(self, btn):
        # a function to evaluate wether user answer is correct
        self.Option1.setEnabled(False)
        self.Option2.setEnabled(False)
        self.Option3.setEnabled(False)
        self.Option4.setEnabled(False)
        self.NextQuestion.setEnabled(True)

        if (btn.text() == self.parameters["correct"][-1]):
            # CORRECT ANSWER

            print(self.parameters["index"])
            print(len(self.parameters["index"]))

            if (len(self.parameters["index"]) != 0):
                # update score (+10 points)
                temp_score = self.parameters["score"][-1]
                self.parameters["score"].pop()
                self.parameters["score"].append(temp_score + 10)
                self.ScoreCounter.setText(str(self.parameters["score"][-1]))
                self.SHORTCheck.setText("Correct Answer!")
        else:
            self.SHORTCheck.setText("WRONG ANSWER!")
            ansexp = self.parameters["pAnsExp"][-1]
            self.AnswerExplanation.setText(ansexp)

    def next(self):
        self.Option1.setEnabled(True)
        self.Option2.setEnabled(True)
        self.Option3.setEnabled(True)
        self.Option4.setEnabled(True)
        self.NextQuestion.setEnabled(False)

        # if (len(self.parameters["index"]) > 1):
        if (self.parameters["questionNo"][-1] < 7):
            temp_no = self.parameters["questionNo"][-1]
            self.parameters["questionNo"].pop()
            self.parameters["questionNo"].append(temp_no + 1)
            print("Question No: ", self.parameters["questionNo"][-1])

            self.parameters["index"].pop()
            self.preload_data(self.parameters["index"][-1])
            self.ScoreCounter.setText(str(self.parameters["score"][-1]))
            self.QuestionText.setText(
                str(self.parameters["questionNo"][-1]) + ". " + self.parameters["question"][-1])
            self.Option1.setText(self.parameters["answer1"][-1])
            self.Option2.setText(self.parameters["answer2"][-1])
            self.Option3.setText(self.parameters["answer3"][-1])
            self.Option4.setText(self.parameters["answer4"][-1])

            hint = self.parameters["hint"][-1]
            self.SHORTCheck.setText("")
            self.AnswerExplanation.setText(hint)

        else:
            screen1 = QuizScore(self.parameters["score"][-1])
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
