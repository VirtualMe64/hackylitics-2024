import pandas as pd
import math

data = pd.read_csv("Data/stats.csv")
schedule = pd.read_csv("./schedules.csv")

# ppg, pass yds, rush yds, turnover, win %, fg success rate, opp ppg, opp ypg
stats = ['points', 'rush_yards', 'pass_yards', 'turnover_margin', 'won_game', 'field_goal_rate', 'opp_points', 'opp_yards']
data['opp_points'] = data['opp_points'] * -1
data['opp_yards'] = data['opp_yards'] * -1

def sigmoid(x):
   return 1 / (1 + math.exp(-x))

def make_prediction(team1 : tuple[str, int], team2 : tuple[str, int], weights : list[int]):
   weights = [x / sum(weights) for x in weights]

   team1_stats = data[(data['team'] == team1[0]) & (data['year'] == team1[1])][stats]
   team2_stats = data[(data['team'] == team2[0]) & (data['year'] == team2[1])][stats]

   total = 0
   for i, weight in enumerate(weights):
      stat = stats[i]
      total += weight * (team1_stats[stat].values[0] - team2_stats[stat].values[0])   
   
   return sigmoid(total)

def evaluate_predictions(weights):
   superbowls = schedule[schedule['game_type'] == 'SB']
   superbowls = superbowls[superbowls['season'] < 2023].reset_index(drop=True)
   correct = 0
   total = 0
   for i, sb in superbowls.iterrows():
      season = 2000 + i
      team1 = sb['away_team']
      team2 = sb['home_team']
      winner = sb['home_score'] > sb['away_score']
      prediction = make_prediction((team1, season), (team2, season), weights)
      right = winner == (prediction > 0.5)
      total += 1
      correct += 1 if right else 0
   return correct / float(total)

if __name__ == '__main__':
   #print(make_prediction(('ARI', 2020), ('CLE', 2020), [1, 1, 1, 1, 1, 1, 1, 1]))
   print(evaluate_predictions([1, 1, 1, 1, 1, 1, 1, 1]))