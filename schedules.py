from nfl_data_py import import_schedules
import pandas as pd

dfs = []

for year in range(2000, 2024):
    print(year)
    dfs.append(import_schedules([year]))

pd.concat(dfs).to_csv("schedules.csv")