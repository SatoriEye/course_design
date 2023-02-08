import sys
import os
from PyQt5.QtGui import QFont, QPixmap
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5 import Qt

class MainSurface(QWidget):
    def __init__(self):
        super(MainWindowSurface, self).__init__()
        self.initUI()
    def initUI(self):
