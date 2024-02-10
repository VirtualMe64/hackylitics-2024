import sys
import pandas as pd
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QSlider
)
from PyQt5.QtCore import *

import datetime

class Sports(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Who Will Win the Super Bowl?')
        self.overall=QHBoxLayout()
        self.stats=QVBoxLayout()
        self.predictions=QVBoxLayout()

        self.stat1=QLabel('Stat 1')
        self.stats.addWidget(self.stat1)
        self.stat1s=QSlider(Qt.Horizontal)
        self.stats.addWidget(self.stat1s)

        self.overall.addLayout(self.stats)
        self.setLayout(self.overall)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Sports()
    main.show()
    exit_code = app.exec_()
    sys.exit(exit_code)
