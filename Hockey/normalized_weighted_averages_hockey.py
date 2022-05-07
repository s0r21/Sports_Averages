# The Main Script File to analyze each team and provide the results of who will win
from utils import *
from dataset import final_team_averages, todays_home_teams_df, todays_away_teams_df

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

class automated_method:
    def team_difference(team_one_average, team_two_average):
        return(abs(team_one_average - team_two_average))
    @staticmethod
    def automated_function_away_team():
        away_team_array = []
        for i in list(todays_away_teams_df.index):
            for x in list(todays_away_teams_df):
                if list(todays_away_teams_df.index)[i] == list(todays_home_teams_df.index)[i]:
                    away_team_array.append(final_team_averages.get(x))
        return away_team_array[0:max(list(todays_away_teams_df.index))+1]
    @staticmethod
    def automated_function_home_team():
        home_team_array = []
        for i in list(todays_home_teams_df.index):
            for x in list(todays_home_teams_df):
                if list(todays_home_teams_df.index)[i] == list(todays_away_teams_df.index)[i]:
                    home_team_array.append(final_team_averages.get(x))
        return home_team_array[0:max(list(todays_home_teams_df.index))+1]
    @staticmethod
    def final_data_frame_automated():
        column_names = ['Away_Team', 'Home_Team', 'Away_Avg', 'Home_Avg']
        score_df = pd.DataFrame(np.transpose([todays_away_teams_df, todays_home_teams_df,
                                              automated_method.automated_function_away_team(),
                                              automated_method.automated_function_home_team()]),
                                columns=column_names)
        score_df['{1: Away, 0: Home}'] = (score_df['Home_Avg'] < score_df['Away_Avg'])
        score_df['{1: Away, 0: Home}'] = score_df['{1: Away, 0: Home}'].astype(int)
        score_df['Difference'] = automated_method.team_difference(score_df['Home_Avg'], score_df['Away_Avg'])
        score_df.drop(['Away_Avg', 'Home_Avg'], axis=1, inplace=True)
        return score_df

Final_dataframe = automated_method.final_data_frame_automated()
file_name = create_directory('Output', 'todays_hockey_games.xlsx')
Final_dataframe.to_excel(file_name)
