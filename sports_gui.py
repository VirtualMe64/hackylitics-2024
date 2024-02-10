import sys
import pandas as pd
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QSlider,
    QComboBox,
    QRadioButton
)
from PyQt5.QtCore import *


team_dict={
'Washington Commanders':'WAS',
'New York Jets': 'NYJ',
'Atlanta Falcons': 'ATL',
'Cleveland Browns': 'CLE',
'New York Giants': 'NYG',
'Kansas City Chiefs': 'KC',
'Chicago Bears': 'CHI',
'Baltimore Ravens': 'BAL',
'Indianapolis Colts': 'IND',
'Seattle Seahawks': 'SEA',
'Denver Broncos': 'DEN',
'Los Angeles Chargers': 'LAC',
'New England Patriots': 'NE',
'Pittsburgh Steelers': 'PIT',
'Minnesota Vikings': 'MIN',
'New Orleans Saints': 'NO',
'Cincinnati Bengals': 'CIN',
'Tampa Bay Buccaneers': 'TB',
'Houston Texans': 'HOU',
'Jacksonville Jaguars': 'JAX',
'Tennessee Titans': 'TEN',
'Buffalo Bills': 'BUF',
'Philadelphia Eagles': 'PHI',
'Carolina Panthers':'CAR',
'Arizona Cardinals': 'ARI',
'Dallas Cowboys': 'DAL',
'Detroit Lions': 'DET',
'Los Angeles Rams': 'LA',
'Miami Dolphins': 'MIA',
'Green Bay Packers': 'GB',
'San Francisco 49ers': 'SF',
'Las Vegas Raiders': 'LV'
}

class Sports(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Who Will Win the Super Bowl?')
        self.overall=QHBoxLayout()
        self.stats=QVBoxLayout()
        self.predictions=QVBoxLayout()

        self.team1=QComboBox()
        for item in team_dict.keys():
            self.team1.addItem(item)
        self.stats.addWidget(self.team1)

        self.team2=QComboBox()
        for item in team_dict.keys():
            self.team2.addItem(item)
        self.stats.addWidget(self.team2)

        self.stat1=QLabel('Points Per Game')
        self.stats.addWidget(self.stat1)
        self.stat1s=QSlider(Qt.Horizontal)
        self.stats.addWidget(self.stat1s)

        self.stat2=QLabel('Yards Per Game')
        self.stats.addWidget(self.stat2)
        self.yard_proportion=QHBoxLayout()
        self.rushing=QRadioButton('Rushing')
        self.yard_proportion.addWidget(self.rushing)
        self.passing=QRadioButton('Passing')
        self.yard_proportion.addWidget(self.passing)
        self.both=QRadioButton('Both')
        self.yard_proportion.addWidget(self.both)
        self.stats.addLayout(self.yard_proportion)
        self.stat2s=QSlider(Qt.Horizontal)
        self.stats.addWidget(self.stat2s)

        Self.

        self.winner=QLabel(f'Predicted winner: {"sammy"}')
        self.predictions.addWidget(self.winner)
        self.probability=QLabel(f'{"insert math here"}')
        self.predictions.addWidget(self.probability)


        self.overall.addLayout(self.stats)
        self.overall.addLayout(self.predictions)
        self.setLayout(self.overall)


    def team_select(self):
        pass




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Sports()
    main.show()
    exit_code = app.exec_()
    sys.exit(exit_code)
