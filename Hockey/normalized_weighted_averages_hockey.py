# The Main Script File to analyze each team and provide the results of who will win

from packages import pd, np
from dataset import final_team_averages

class Input_functionality:
    def input_function_team_one(team_one_function_input):
        for i in list(final_team_averages.keys()):
            if i == team_one_function_input:
                team_one_input = final_team_averages.get(i)
        return team_one_input
    def input_function_team_two(team_two_function_input):
        for i in list(final_team_averages.keys()):
            if i == team_two_function_input:
                team_two_input = final_team_averages.get(i)
        return team_two_input

def game_results(team_one_average_results, team_two_average_results):
    if team_one_average_results > team_two_average_results:
        results = team_one_input
    else: results = team_two_input
    print("The following team is going to win: " + results)

print("Enter Team 1 here: ")
team_one_input = input()
print("Enter Team 2 here: ")
team_two_input = input()

game_results(Input_functionality.input_function_team_one(team_one_input),
             Input_functionality.input_function_team_one(team_two_input))

