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
from PyQt5.QtGui import QFont
from make_prediction import make_prediction, evaluate_predictions




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

        custom_font=QFont()
        custom_font.setPointSize(15)
        QApplication.setFont(custom_font)

        self.setWindowTitle('Who Will Win the Super Bowl?')
        self.overall=QHBoxLayout()
        self.stats=QVBoxLayout()
        self.predictions=QVBoxLayout()

        self.t1=QHBoxLayout()
        self.team1=QComboBox()
        for item in sorted(list(team_dict.keys())):
            self.team1.addItem(item)
        self.team1.setCurrentIndex(15)
        self.t1.addWidget(self.team1)
        self.year1=QComboBox()
        for year in range(2000, 2024):
            self.year1.addItem(str(year))
        self.year1.setCurrentIndex(23)
        self.t1.addWidget(self.year1)
        self.stats.addLayout(self.t1)

        self.t2=QHBoxLayout()
        self.team2=QComboBox()
        for item in sorted(list(team_dict.keys())):
            self.team2.addItem(item)
        self.team2.setCurrentIndex(27)
        self.t2.addWidget(self.team2)
        self.year2=QComboBox()
        for year in range(2000, 2024):
            self.year2.addItem(str(year))
        self.year2.setCurrentIndex(23)
        self.t2.addWidget(self.year2)
        self.stats.addLayout(self.t2)

        self.stat1=QLabel('Points Per Game')
        self.stats.addWidget(self.stat1)
        self.stat1s=QSlider(Qt.Horizontal)
        self.stat1s.setSliderPosition(50)
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
        self.stat2s.setSliderPosition(50)
        self.stats.addWidget(self.stat2s)

        self.stat3=QLabel('Turnover Margin')
        self.stats.addWidget(self.stat3)
        self.stat3s=QSlider(Qt.Horizontal)
        self.stat3s.setSliderPosition(50)
        self.stats.addWidget(self.stat3s)

        self.stat4=QLabel('Overall Win Percent')
        self.stats.addWidget(self.stat4)
        self.stat4s=QSlider(Qt.Horizontal)
        self.stat4s.setSliderPosition(50)
        self.stats.addWidget(self.stat4s)

        self.stat5=QLabel('Field Goal Success Rate')
        self.stats.addWidget(self.stat5)
        self.stat5s=QSlider(Qt.Horizontal)
        self.stat5s.setSliderPosition(50)
        self.stats.addWidget(self.stat5s)

        self.stat6=QLabel('Opponent Points Per Game')
        self.stats.addWidget(self.stat6)
        self.stat6s=QSlider(Qt.Horizontal)
        self.stat6s.setSliderPosition(50)
        self.stats.addWidget(self.stat6s)

        self.stat7=QLabel('Opponent Yards Per Game')
        self.stats.addWidget(self.stat7)
        self.stat7s=QSlider(Qt.Horizontal)
        self.stat7s.setSliderPosition(50)
        self.stats.addWidget(self.stat7s)

        self.generate=QPushButton('Generate')
        self.generate.clicked.connect(self.generate_statistics)
        self.predictions.addWidget(self.generate)

        self.matchup=QLabel('Matchup:')
        self.predictions.addWidget(self.matchup)
        self.winner=QLabel('Predicted winner:')
        self.predictions.addWidget(self.winner)
        self.probability=QLabel('Win probability:')
        self.predictions.addWidget(self.probability)
        self.past=QLabel('Accuracy:')
        self.predictions.addWidget(self.past)

        self.overall.addLayout(self.stats)
        self.overall.addLayout(self.predictions)
        self.setLayout(self.overall)

    def generate_statistics(self):
        #order: ppg, pass yds, rush yds, turnover, win %, fg success rate, opp ppg, opp ypg
        team1=str(self.team1.currentText())
        team2=str(self.team2.currentText())
        year1=int(self.year1.currentText())
        year2=int(self.year2.currentText())
        code1=team_dict[team1]
        code2=team_dict[team2]
        self.matchup.setText(f'{year1} {team1} vs. {year2} {team2}')
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
        t1winprob=make_prediction((code1, year1),(code2,year2),weights)
        past_accuracy = evaluate_predictions(weights)
        self.past.setText(f"Past accuracy: {past_accuracy*100}%")
        if t1winprob>=.5:
            self.winner.setText(f'Predicted winner: {year1} {team1}')
            self.probability.setText(f'Win probability: {t1winprob*100}%')
        else:
            self.winner.setText(f'Predicted winner: {year2} {team2}')
            self.probability.setText(f'Win probability: {(1-t1winprob)*100}%')






if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Sports()
    main.show()
    exit_code = app.exec_()
    sys.exit(exit_code)
