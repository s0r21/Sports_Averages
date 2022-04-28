# The Main Script File to analyze each team and provide the results of who will win

from dataset import teams_normalized_datasets, teams_datasets, team_array
from packages import *

print("Enter Team 1 here: ")
team_one_input = input()
print("Enter Team 2 here: ")
team_two_input = input()

class models:
    def model_results(team_array_position):
        df = teams_normalized_datasets.get(team_array[team_array_position])
        model = arma.auto_arima(df, seasonal=False, suppress_warnings=True,
                                trend=True, with_intercept=True)
        return model
    def model_predict_results(team_array_position):
        if (models.model_results(team_array_position).predict(n_periods=1)) > 0:
            model_prediction = teams_datasets.get(team_array[team_array_position]).iloc[
                                   max(teams_datasets.get(team_array[team_array_position]).index)] * \
                               (1 + models.model_results(team_array_position).predict(n_periods=1))
        elif (models.model_results(team_array_position).predict(n_periods=1)) < 0:
            model_prediction = teams_datasets.get(team_array[team_array_position]).iloc[
                max(teams_datasets.get(team_array[team_array_position]).index)] / \
                               (1 + models.model_results(team_array_position).predict(n_periods=1))
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

arma_models = {
    'ARI': models.model_results(0),
    'ATL': models.model_results(1),
    'BUF': models.model_results(2),
    'MIA': models.model_results(3),
    'NWE': models.model_results(4),
    'NYJ': models.model_results(5),
    'TEN': models.model_results(6),
    'IND': models.model_results(7),
    'HOU': models.model_results(8),
    'JAX': models.model_results(9),
    'PIT': models.model_results(10),
    'BAL': models.model_results(11),
    'CLE': models.model_results(12),
    'CIN': models.model_results(13),
    'KAN': models.model_results(14),
    'LVR': models.model_results(15),
    'LAC': models.model_results(16),
    'DEN': models.model_results(17),
    'WSH': models.model_results(18),
    'NYG': models.model_results(19),
    'DAL': models.model_results(20),
    'PHI': models.model_results(21),
    'NOR': models.model_results(22),
    'TBB': models.model_results(23),
    'CAR': models.model_results(24),
    'GNB': models.model_results(25),
    'CHI': models.model_results(26),
    'MIN': models.model_results(27),
    'DET': models.model_results(28),
    'SEA': models.model_results(29),
    'LAR': models.model_results(30),
    'SFO': models.model_results(31)
}
t_plus_one_scores = {
    'ARI': float(models.model_predict_results(0)),
    'ATL': float(models.model_predict_results(1)),
    'BUF': float(models.model_predict_results(2)),
    'MIA': float(models.model_predict_results(3)),
    'NWE': float(models.model_predict_results(4)),
    'NYJ': float(models.model_predict_results(5)),
    'TEN': float(models.model_predict_results(6)),
    'IND': float(models.model_predict_results(7)),
    'HOU': float(models.model_predict_results(8)),
    'JAX': float(models.model_predict_results(9)),
    'PIT': float(models.model_predict_results(10)),
    'BAL': float(models.model_predict_results(11)),
    'CLE': float(models.model_predict_results(12)),
    'CIN': float(models.model_predict_results(13)),
    'KAN': float(models.model_predict_results(14)),
    'LVR': float(models.model_predict_results(15)),
    'LAC': float(models.model_predict_results(16)),
    'DEN': float(models.model_predict_results(17)),
    'WSH': float(models.model_predict_results(18)),
    'NYG': float(models.model_predict_results(19)),
    'DAL': float(models.model_predict_results(20)),
    'PHI': float(models.model_predict_results(21)),
    'NOR': float(models.model_predict_results(22)),
    'TBB': float(models.model_predict_results(23)),
    'CAR': float(models.model_predict_results(24)),
    'GNB': float(models.model_predict_results(25)),
    'CHI': float(models.model_predict_results(26)),
    'MIN': float(models.model_predict_results(27)),
    'DET': float(models.model_predict_results(28)),
    'SEA': float(models.model_predict_results(29)),
    'LAR': float(models.model_predict_results(30)),
    'SFO': float(models.model_predict_results(31))
}

game_results(input_functionality.input_function_team_one(team_one_input),
             input_functionality.input_function_team_two(team_two_input))