import pandas as pd
import math

data = pd.read_csv("Data/stats.csv")

# ppg, pass yds, rush yds, turnover, win %, fg success rate, opp ppg, opp ypg
stats = ['points', 'rush_yards', 'pass_yards', 'turnover_margin', 'won_game', 'field_goal_rate', 'opp_points', 'opp_yards']

def sigmoid(x):
   return 1 / (1 + math.exp(-x))

def make_prediction(team1 : tuple[str, int], team2 : tuple[str, int], weights : list[int]):
   team1_stats = data[(data['team'] == team1[0]) & (data['year'] == team1[1])][stats]
   team2_stats = data[(data['team'] == team2[0]) & (data['year'] == team2[1])][stats]

   total = 0
   for i, weight in enumerate(weights):
      stat = stats[i]
      total += weight * (team1_stats[stat].values[0] - team2_stats[stat].values[0])
      
   return sigmoid(total)

if __name__ == '__main__':
   print(make_prediction(('ARI', 2020), ('CLE', 2020), [1, 1, 1, 1, 1, 1, 1, 1]))
