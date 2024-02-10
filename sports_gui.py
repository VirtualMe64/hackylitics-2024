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

        self.t1=QHBoxLayout()
        self.team1=QComboBox()
        for item in team_dict.keys():
            self.team1.addItem(item)
        self.t1.addWidget(self.team1)
        self.year1=QComboBox()
        for year in range(1999, 2024):
            self.year1.addItem(str(year))
        self.t1.addWidget(self.year1)
        self.stats.addLayout(self.t1)

        self.t2=QHBoxLayout()
        self.team2=QComboBox()
        for item in team_dict.keys():
            self.team2.addItem(item)
        self.t2.addWidget(self.team2)
        self.year2=QComboBox()
        for year in range(1999, 2024):
            self.year2.addItem(str(year))
        self.t2.addWidget(self.year2)
        self.stats.addLayout(self.t2)

        self.set_teams=QPushButton('Select Teams')
        self.set_teams.clicked.connect(self.team_select)
        self.stats.addWidget(self.set_teams)

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

        self.stat3=QLabel('Turnover Margin')
        self.stats.addWidget(self.stat3)
        self.stat3s=QSlider(Qt.Horizontal)
        self.stats.addWidget(self.stat3s)

        self.stat4=QLabel('Overall Win Percent')
        self.stats.addWidget(self.stat4)
        self.stat4s=QSlider(Qt.Horizontal)
        self.stats.addWidget(self.stat4s)

        self.stat5=QLabel('Field Goal Success Rate')
        self.stats.addWidget(self.stat5)
        self.stat5s=QSlider(Qt.Horizontal)
        self.stats.addWidget(self.stat5s)

        self.stat6=QLabel('Opponent Points Per Game')
        self.stats.addWidget(self.stat6)
        self.stat6s=QSlider(Qt.Horizontal)
        self.stats.addWidget(self.stat6s)

        self.stat7=QLabel('Opponent Yards Per Game')
        self.stats.addWidget(self.stat7)
        self.stat7s=QSlider(Qt.Horizontal)
        self.stats.addWidget(self.stat7s)

        self.generate=QPushButton('Generate')
        self.generate.clicked.connect(self.generate_statistics)
        self.predictions.addWidget(self.generate)

        self.winner=QLabel(f'Predicted winner: {"sammy"}')
        self.predictions.addWidget(self.winner)
        self.probability=QLabel(f'{"insert math here"}')
        self.predictions.addWidget(self.probability)


        self.overall.addLayout(self.stats)
        self.overall.addLayout(self.predictions)
        self.setLayout(self.overall)


    def team_select(self):
        team1=str(self.team1.currentText())
        team2=str(self.team2.currentText())
        code1=team_dict[team1]
        code2=team_dict[team2]
        print(code1+code2)

    def generate_statistics(self):
        #order: ppg, pass yds, rush yds, turnover, win %, fg success rate, opp ppg, opp ypg
        weights=[]
        weights.append(self.stat1s.value()/100)
        if self.passing.isChecked():
            weights.append(self.stat2s.value()/100)
            weights.append(0)
        elif self.rushing.isChecked():
            weights.append(0)
            weights.append(self.stat2s.value()/100)
        else:
            weights.append(self.stat2s.value()/100)
            weights.append(self.stat2s.value()/100)
        weights.append(self.stat3s.value()/100)
        weights.append(self.stat4s.value()/100)
        weights.append(self.stat5s.value()/100)
        weights.append(self.stat6s.value()/100)
        weights.append(self.stat7s.value()/100)
        print(weights)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Sports()
    main.show()
    exit_code = app.exec_()
    sys.exit(exit_code)
