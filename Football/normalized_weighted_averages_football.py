# The Main Script File to analyze each team and provide the results of who will win

from dataset import Appended_qb_df, Appended_rb_df, Appended_def_df
from packages import np

def normalization(df):
    column_average = np.mean(df)
    column_std = np.std(df)
    normalized_values = ((df - column_average) / column_std)
    return normalized_values

def qb_weighted(df,y):
    x = (0.4 * (df.iloc[y,0] - df.iloc[y,1])) + (0.6 * df.iloc[y,2])
    return x

def rb_weighted(df,y):
    x = (0.4 * df.iloc[y,0] ) + (0.6 * df.iloc[y,1] )
    return x

def def_weighted(df,y):
    x = (0.5 * df.iloc[y,0]) + (0.5 * df.iloc[y,1])
    return x

def Offence(QB,RB):
    x = QB + RB
    return x

def Team_total(offence, defence):
    x = offence - defence
    return x

normalized_qb_df = normalization(Appended_qb_df)
normalized_rb_df = normalization(Appended_rb_df)
normalized_def_df = normalization(Appended_def_df)

print("Enter Team 1 here: ")
team_one_input = input()
print("Enter Team 2 here: ")
team_two_input = input()

def input_function_team_one(team_one_function_input):
    if team_one_function_input == 'ARI':
        y = 0
        x = Team_total(Offence(qb_weighted(normalized_qb_df,y),rb_weighted(normalized_rb_df,y)),
                       def_weighted(normalized_def_df,y))
    elif team_one_function_input == 'ATL':
        y = 1
        x = Team_total(Offence(qb_weighted(normalized_qb_df,y),rb_weighted(normalized_rb_df,y)),
                       def_weighted(normalized_def_df,y))
    elif team_one_function_input == 'BUF':
        y = 2
        x = Team_total(Offence(qb_weighted(normalized_qb_df,y),rb_weighted(normalized_rb_df,y)),
                       def_weighted(normalized_def_df,y))
    elif team_one_function_input == 'MIA':
        y = 3
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_one_function_input == 'NWE':
        y = 4
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_one_function_input == 'NYJ':
        y = 5
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_one_function_input == 'TEN':
        y = 6
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_one_function_input == 'IND':
        y = 7
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_one_function_input == 'HOU':
        y = 8
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_one_function_input == 'JAX':
        y = 9
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_one_function_input == 'PIT':
        y = 10
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_one_function_input == 'BAL':
        y = 11
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_one_function_input == 'CLE':
        y = 12
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_one_function_input == 'CIN':
        y = 13
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_one_function_input == 'KAN':
        y = 14
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_one_function_input == 'LVR':
        y = 15
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_one_function_input == 'LAC':
        y = 16
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_one_function_input == 'DEN':
        y = 17
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_one_function_input == 'WSH':
        y = 18
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_one_function_input == 'NYG':
        y = 19
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_one_function_input == 'DAL':
        y = 20
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_one_function_input == 'PHI':
        y = 21
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_one_function_input == 'NOR':
        y = 22
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_one_function_input == 'TBB':
        y = 23
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_one_function_input == 'CAR':
        y = 24
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_one_function_input == 'GNB':
        y = 25
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_one_function_input == 'CHI':
        y = 26
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_one_function_input == 'MIN':
        y = 27
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_one_function_input == 'DET':
        y = 28
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_one_function_input == 'SEA':
        y = 29
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_one_function_input == 'LAR':
        y = 30
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_one_function_input == 'SFO':
        y = 31
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    return x
def input_function_team_two(team_two_function_input):
    if team_two_function_input == 'ARI':
        y = 0
        x = Team_total(Offence(qb_weighted(normalized_qb_df,y),rb_weighted(normalized_rb_df,y)),
                       def_weighted(normalized_def_df,y))
    elif team_two_function_input == 'ATL':
        y = 1
        x = Team_total(Offence(qb_weighted(normalized_qb_df,y),rb_weighted(normalized_rb_df,y)),
                       def_weighted(normalized_def_df,y))
    elif team_two_function_input == 'BUF':
        y = 2
        x = Team_total(Offence(qb_weighted(normalized_qb_df,y),rb_weighted(normalized_rb_df,y)),
                       def_weighted(normalized_def_df,y))
    elif team_two_function_input == 'MIA':
        y = 3
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_two_function_input == 'NWE':
        y = 4
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_two_function_input == 'NYJ':
        y = 5
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_two_function_input == 'TEN':
        y = 6
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_two_function_input == 'IND':
        y = 7
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_two_function_input == 'HOU':
        y = 8
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_two_function_input == 'JAX':
        y = 9
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_two_function_input == 'PIT':
        y = 10
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_two_function_input == 'BAL':
        y = 11
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_two_function_input == 'CLE':
        y = 12
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_two_function_input == 'CIN':
        y = 13
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_two_function_input == 'KAN':
        y = 14
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_two_function_input == 'LVR':
        y = 15
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_two_function_input == 'LAC':
        y = 16
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_two_function_input == 'DEN':
        y = 17
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_two_function_input == 'WSH':
        y = 18
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_two_function_input == 'NYG':
        y = 19
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_two_function_input == 'DAL':
        y = 20
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_two_function_input == 'PHI':
        y = 21
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_two_function_input == 'NOR':
        y = 22
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_two_function_input == 'TBB':
        y = 23
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_two_function_input == 'CAR':
        y = 24
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_two_function_input == 'GNB':
        y = 25
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_two_function_input == 'CHI':
        y = 26
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_two_function_input == 'MIN':
        y = 27
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_two_function_input == 'DET':
        y = 28
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_two_function_input == 'SEA':
        y = 29
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_two_function_input == 'LAR':
        y = 30
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    elif team_two_function_input == 'SFO':
        y = 31
        x = Team_total(Offence(qb_weighted(normalized_qb_df, y), rb_weighted(normalized_rb_df, y)),
                       def_weighted(normalized_def_df, y))
    return x

def game_results(team_one_average_results, team_two_average_results):
     if team_one_average_results > team_two_average_results:
         results = team_one_input
     else:
         results = team_two_input
     print("The following team is going to win: " + results)

game_results(input_function_team_one(team_one_input), input_function_team_two(team_two_input))