from extract_data_sportsipy import extract_year_stats
from sports_gui import Sports

from PyQt5.QtWidgets import QApplication

import sys
import os

CURRENT_YEAR = 2023

for year in range(2020, CURRENT_YEAR + 1):
    if not os.path.exists(f"Data/{year}.csv"):
        extract_year_stats(year)

app = QApplication(sys.argv)
main = Sports()
main.show()
exit_code = app.exec_()
sys.exit(exit_code)