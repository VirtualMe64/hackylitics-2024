import sys
import pandas as pd
from PyQT5.QTWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QLabel
)

import datetime

class Sports(QWidget):
    def __init__(self):
        super().__init__

        self.setWindowTitle('Who Will Win the Super Bowl?')
