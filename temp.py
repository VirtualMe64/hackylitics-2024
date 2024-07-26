import pandas as pd

dfs = []
for i in range(2000, 2024):
    df = pd.read_csv(f"Data/{i}.csv")
    df['year'] = i
    dfs.append(df)

data = pd.concat(dfs)
data.to_csv("stats.csv")