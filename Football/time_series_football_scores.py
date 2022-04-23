# The Main Script File to analyze each team and provide the results of who will win

from dataset import teams_normalized_datasets, teams_datasets, team_array
from packages import *

print("Enter Team 1 here: ")
team_one_input = input()
print("Enter Team 2 here: ")
team_two_input = input()

def model_predict_results(team_array_position):
    df = teams_normalized_datasets.get(team_array[team_array_position])
    model = arma.auto_arima(df, seasonal=False, suppress_warnings=True)
    model_prediction = (model.predict(n_periods=1) + 1) * \
                       teams_datasets.get(team_array[team_array_position]).iloc[
                           max(teams_datasets.get(team_array[team_array_position]).index)]
    return model_prediction

class input_functionality:
    def input_function_team_one(team_one_function_input):
        for i in list(t_plus_one_scores.keys()):
            if i == team_one_function_input:
                team_one_result = t_plus_one_scores.get(i)
        return team_one_result
    def input_function_team_two(team_two_function_input):
        for i in list(t_plus_one_scores.keys()):
            if i == team_two_function_input:
                team_two_result = t_plus_one_scores.get(i)
        return team_two_result

def game_results(team_one_average_results, team_two_average_results):
     if team_one_average_results > team_two_average_results:
         results = team_one_input
     else:
         results = team_two_input
     print("The following team is going to win: " + results)

t_plus_one_scores = {
    'ARI': float(model_predict_results(0)),
    'ATL': float(model_predict_results(1)),
    'BUF': float(model_predict_results(2)),
    'MIA': float(model_predict_results(3)),
    'NWE': float(model_predict_results(4)),
    'NYJ': float(model_predict_results(5)),
    'TEN': float(model_predict_results(6)),
    'IND': float(model_predict_results(7)),
    'HOU': float(model_predict_results(8)),
    'JAX': float(model_predict_results(9)),
    'PIT': float(model_predict_results(10)),
    'BAL': float(model_predict_results(11)),
    'CLE': float(model_predict_results(12)),
    'CIN': float(model_predict_results(13)),
    'KAN': float(model_predict_results(14)),
    'LVR': float(model_predict_results(15)),
    'LAC': float(model_predict_results(16)),
    'DEN': float(model_predict_results(17)),
    'WSH': float(model_predict_results(18)),
    'NYG': float(model_predict_results(19)),
    'DAL': float(model_predict_results(20)),
    'PHI': float(model_predict_results(21)),
    'NOR': float(model_predict_results(22)),
    'TBB': float(model_predict_results(23)),
    'CAR': float(model_predict_results(24)),
    'GNB': float(model_predict_results(25)),
    'CHI': float(model_predict_results(26)),
    'MIN': float(model_predict_results(27)),
    'DET': float(model_predict_results(28)),
    'SEA': float(model_predict_results(29)),
    'LAR': float(model_predict_results(30)),
    'SFO': float(model_predict_results(31))
}

game_results(input_functionality.input_function_team_one(team_one_input),
             input_functionality.input_function_team_two(team_two_input))