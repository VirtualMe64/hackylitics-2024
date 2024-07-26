from sportsipy.nfl.teams import Teams, Team
import pandas as pd

def extract_year_stats(year):
    # note: we had to fix sportsipy
    # created issue detailing solution (https://github.com/roclark/sportsipy/issues/791)
    teams = Teams(year)
    data_frame : pd.DataFrame = teams.dataframes
    data_frame.to_csv(f"Data/{year}.csv")

# starting year: 1970
# ending year: 2022
extract_year_stats(2023)