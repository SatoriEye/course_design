import sys
import os
import time
from PyQt5.QtGui import QFont, QPixmap
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp, QDate, QDateTime

def date_init(date):
    with open("../data/time_period.txt", 'r') as f:
        data = str(f.read())
        data = data.split(".")
        date['year'] = data[0]
        date['month'] = data[1]
        date['day'] = data[2]
    return date
def write_date(input_date):
    date["year"] = str(input_date.year())
    date["month"] = str(input_date.month())
    date["day"] = str(input_date.day())


def file_operate(event):
    f = open("../data/time_period.txt", 'w')
    f.write(date['year'])
    f.write('.')
    f.write(date['month'])
    f.write(".")
    f.write(date["day"])
    f.close()
    event.accept()

date = {"year": "", "month": "", "day": ""}
class TimeLineSurface(QWidget):
    def __init__(self):
        super(TimeLineSurface, self).__init__()
        self.InitUI()
    def InitUI(self):
        date_init(date)
        self.win = QMainWindow()
        self.win.setGeometry(100, 100, 400, 200)
        self.cal = QDateTimeEdit(QDateTime.currentDateTime(), self.win)
        self.cal.resize(200, 30)
        self.cal.move(20, 20)
        self.cal.setDisplayFormat("yyyy-MM-dd")
        self.cal.dateChanged.connect(write_date)
        # 使用说明
        self.label = QPushButton(self.win)
        self.label.resize(200, 40)
        self.label.setText(
            "设定完毕")
        self.label.setFont(QFont("微软雅黑", 10, QFont.Bold))
        self.label.setStyleSheet("color:darkblue")
        self.label.move(50, 100)
        self.label.clicked.connect(file_operate)










