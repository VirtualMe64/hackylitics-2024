from nfl_data_py import import_schedules
import pandas as pd

def generate_schedules(start_year, end_year):
    dfs = []

    for year in range(start_year, end_year):
        dfs.append(import_schedules([year]))

    pd.concat(dfs).to_csv("schedules.csv")

if __name__ == "__main__":
    generate_schedules(2000, 2023)