# The weighted average formulas for the game of baseball
from dataset import *
from packages import *

# Concatenating all the datasets into one
Batting_df_all = pd.concat([teams.batting.ARI, teams.batting.ATL, teams.batting.BAL, teams.batting.BOS,
                            teams.batting.CHC, teams.batting.CHW, teams.batting.CIN, teams.batting.CLE,
                            teams.batting.COL, teams.batting.DET, teams.batting.HOU, teams.batting.KCR,
                            teams.batting.LAA, teams.batting.LAD, teams.batting.MIA, teams.batting.MIL,
                            teams.batting.MIN, teams.batting.NYM, teams.batting.NYY, teams.batting.OAK,
                            teams.batting.PHI, teams.batting.PIT, teams.batting.SDP, teams.batting.SEA,
                            teams.batting.SFG, teams.batting.STL, teams.batting.TBR, teams.batting.TEX,
                            teams.batting.TOR, teams.batting.WSN
                            ]).reset_index().drop(columns = 'index')
Pitching_df_all = pd.concat([teams.pitching.ARI, teams.pitching.ATL, teams.pitching.BAL, teams.pitching.BOS,
                            teams.pitching.CHC, teams.pitching.CHW, teams.pitching.CIN, teams.pitching.CLE,
                            teams.pitching.COL, teams.pitching.DET, teams.pitching.HOU, teams.pitching.KCR,
                            teams.pitching.LAA, teams.pitching.LAD, teams.pitching.MIA, teams.pitching.MIL,
                            teams.pitching.MIN, teams.pitching.NYM, teams.pitching.NYY, teams.pitching.OAK,
                            teams.pitching.PHI, teams.pitching.PIT, teams.pitching.SDP, teams.pitching.SEA,
                            teams.pitching.SFG, teams.pitching.STL, teams.pitching.TBR, teams.pitching.TEX,
                            teams.pitching.TOR, teams.pitching.WSN
                            ]).reset_index().drop(columns = 'index')

# Normalization Function
def normalized_batting_stats(all_batting_df, all_pitching_df):
    batting_stats = []
    pitching_stats = []
# Batting Mean & SD
    R_mean_batting = all_batting_df.iloc[:, 0].astype(float).mean()
    H_mean_batting = all_batting_df.iloc[:, 1].astype(float).mean()
    two_B_mean_batting = all_batting_df.iloc[:, 2].astype(float).mean()
    three_B_mean_batting = all_batting_df.iloc[:, 3].astype(float).mean()
    RBI_mean_batting = all_batting_df.iloc[:, 4].astype(float).mean()
    SB_mean_batting = all_batting_df.iloc[:, 5].astype(float).mean()
    R_SD_batting = all_batting_df.iloc[:, 0].astype(float).std()
    H_SD_batting = all_batting_df.iloc[:, 1].astype(float).std()
    two_B_SD_batting = all_batting_df.iloc[:, 2].astype(float).std()
    three_B_SD_batting = all_batting_df.iloc[:, 3].astype(float).std()
    RBI_SD_batting = all_batting_df.iloc[:, 4].astype(float).std()
    SB_SD_batting = all_batting_df.iloc[:, 5].astype(float).std()
    batting_stats = [R_mean_batting, H_mean_batting, two_B_mean_batting, three_B_mean_batting, RBI_mean_batting,
                     SB_mean_batting, R_SD_batting, H_SD_batting, two_B_SD_batting, three_B_SD_batting, RBI_SD_batting,
                     SB_SD_batting]
# Pitching Mean & SD
    R_sum_pitching_mean = (all_pitching_df.iloc[:, 0]).astype(int).mean()
    H_sum_pitching_mean = (all_pitching_df.iloc[:, 1]).astype(int).mean()
    ER_sum_pitching_mean = (all_pitching_df.iloc[:, 2]).astype(int).mean()
    HR_sum_pitching_mean = (all_pitching_df.iloc[:, 3]).astype(int).mean()
    BB_sum_pitching_mean = (all_pitching_df.iloc[:, 4]).astype(int).mean()
    So_sum_pitching_mean = (all_pitching_df.iloc[:, 5]).astype(int).mean()
    R_sum_pitching_SD = (all_pitching_df.iloc[:, 0]).astype(int).std()
    H_sum_pitching_SD = (all_pitching_df.iloc[:, 1]).astype(int).std()
    ER_sum_pitching_SD = (all_pitching_df.iloc[:, 2]).astype(int).std()
    HR_sum_pitching_SD = (all_pitching_df.iloc[:, 3]).astype(int).std()
    BB_sum_pitching_SD = (all_pitching_df.iloc[:, 4]).astype(int).std()
    So_sum_pitching_SD = (all_pitching_df.iloc[:, 5]).astype(int).std()
    pitching_stats = [R_sum_pitching_mean, H_sum_pitching_mean, ER_sum_pitching_mean, HR_sum_pitching_mean, BB_sum_pitching_mean,
                      So_sum_pitching_mean, R_sum_pitching_SD, H_sum_pitching_SD, ER_sum_pitching_SD, HR_sum_pitching_SD,
                      BB_sum_pitching_SD, So_sum_pitching_SD]
    return [batting_stats, pitching_stats]

# Class to represent the team stats
class team_stats:
    def team_one(batting, pitching):
        R_sum_batting = (((batting.iloc[:,0]).astype(int) - Statistics_used_for_normalization[0][0]) / Statistics_used_for_normalization[0][6]).mean()
        H_sum_batting = (((batting.iloc[:,1]).astype(int) - Statistics_used_for_normalization[0][1]) / Statistics_used_for_normalization[0][7]).mean()
        two_B_sum_batting = (((batting.iloc[:,2]).astype(int) - Statistics_used_for_normalization[0][2]) / Statistics_used_for_normalization[0][8]).mean()
        three_B_sum_batting = (((batting.iloc[:,3]).astype(int) - Statistics_used_for_normalization[0][3]) / Statistics_used_for_normalization[0][9]).mean()
        RBI_sum_batting = (((batting.iloc[:,4]).astype(int) - Statistics_used_for_normalization[0][4]) / Statistics_used_for_normalization[0][10]).mean()
        SB_sum_batting = (((batting.iloc[:,5]).astype(int) - Statistics_used_for_normalization[0][5]) / Statistics_used_for_normalization[0][11]).mean()
        batting_final = (0.25*(H_sum_batting)) + (0.2*(R_sum_batting)) + (0.2*(three_B_sum_batting)) +\
                        (0.15*(SB_sum_batting)) + (0.1*(RBI_sum_batting)) + (0.1*(two_B_sum_batting))
        R_sum_pitching = (((pitching.iloc[:,0]).astype(int) - Statistics_used_for_normalization[1][0]) / Statistics_used_for_normalization[1][6]).mean()
        H_sum_pitching = (((pitching.iloc[:,1]).astype(int) - Statistics_used_for_normalization[1][1]) / Statistics_used_for_normalization[1][7]).mean()
        ER_sum_pitching = (((pitching.iloc[:,2]).astype(int) - Statistics_used_for_normalization[1][2]) / Statistics_used_for_normalization[1][8]).mean()
        HR_sum_pitching = (((pitching.iloc[:,3]).astype(int) - Statistics_used_for_normalization[1][3]) / Statistics_used_for_normalization[1][9]).mean()
        BB_sum_pitching = (((pitching.iloc[:,4]).astype(int) - Statistics_used_for_normalization[1][4]) / Statistics_used_for_normalization[1][10]).mean()
        So_sum_pitching = (((pitching.iloc[:,5]).astype(int) - Statistics_used_for_normalization[1][5]) / Statistics_used_for_normalization[1][11]).mean()
        pitching_final = (0.15*(H_sum_pitching)) + (0.15*(R_sum_pitching)) + (0.15*(ER_sum_pitching)) + \
                         (0.05*(HR_sum_pitching)) + (0.05*(BB_sum_pitching)) - (0.45*(So_sum_pitching))
        team_one_average = batting_final - pitching_final
        return team_one_average
    def team_two(batting, pitching):
        R_sum_batting = (((batting.iloc[:,0]).astype(int) - Statistics_used_for_normalization[0][0]) / Statistics_used_for_normalization[0][6]).mean()
        H_sum_batting = (((batting.iloc[:,1]).astype(int) - Statistics_used_for_normalization[0][1]) / Statistics_used_for_normalization[0][7]).mean()
        two_B_sum_batting = (((batting.iloc[:,2]).astype(int) - Statistics_used_for_normalization[0][2]) / Statistics_used_for_normalization[0][8]).mean()
        three_B_sum_batting = (((batting.iloc[:,3]).astype(int) - Statistics_used_for_normalization[0][3]) / Statistics_used_for_normalization[0][9]).mean()
        RBI_sum_batting = (((batting.iloc[:,4]).astype(int) - Statistics_used_for_normalization[0][4]) / Statistics_used_for_normalization[0][10]).mean()
        SB_sum_batting = (((batting.iloc[:,5]).astype(int) - Statistics_used_for_normalization[0][5]) / Statistics_used_for_normalization[0][11]).mean()
        batting_final = (0.25*(H_sum_batting)) + (0.2*(R_sum_batting)) + (0.2*(three_B_sum_batting)) +\
                        (0.15*(SB_sum_batting)) + (0.1*(RBI_sum_batting)) + (0.1*(two_B_sum_batting))
        R_sum_pitching = (((pitching.iloc[:,0]).astype(int) - Statistics_used_for_normalization[1][0]) / Statistics_used_for_normalization[1][6]).mean()
        H_sum_pitching = (((pitching.iloc[:,1]).astype(int) - Statistics_used_for_normalization[1][1]) / Statistics_used_for_normalization[1][7]).mean()
        ER_sum_pitching = (((pitching.iloc[:,2]).astype(int) - Statistics_used_for_normalization[1][2]) / Statistics_used_for_normalization[1][8]).mean()
        HR_sum_pitching = (((pitching.iloc[:,3]).astype(int) - Statistics_used_for_normalization[1][3]) / Statistics_used_for_normalization[1][9]).mean()
        BB_sum_pitching = (((pitching.iloc[:,4]).astype(int) - Statistics_used_for_normalization[1][4]) / Statistics_used_for_normalization[1][10]).mean()
        So_sum_pitching = (((pitching.iloc[:,5]).astype(int) - Statistics_used_for_normalization[1][5]) / Statistics_used_for_normalization[1][11]).mean()
        pitching_final = (0.15*(H_sum_pitching)) + (0.15*(R_sum_pitching)) + (0.15*(ER_sum_pitching)) + \
                         (0.05*(HR_sum_pitching)) + (0.05*(BB_sum_pitching)) - (0.45*(So_sum_pitching))
        team_two_average = batting_final - pitching_final
        return team_two_average
    def team_difference(team_one_average, team_two_average):
        return(abs(team_one_average - team_two_average))

# Class to collect the data from the chosen teams
class Input_functionality:
    def input_function_team_one(team_one_function_input):
        for i in list(Batting_all_teams.keys()):
            if i == team_one_function_input:
                team_one_batting_input, team_one_pitching_input = Batting_all_teams.get(i), Pitching_all_teams.get(i)
        return team_one_batting_input, team_one_pitching_input
    def input_function_team_two(team_two_function_input):
        for i in list(Batting_all_teams.keys()):
            if i == team_two_function_input:
                team_two_batting_input, team_two_pitching_input = Batting_all_teams.get(i), Pitching_all_teams.get(i)
        return team_two_batting_input, team_two_pitching_input

class automated_method:
    @staticmethod
    def automated_function_away_team():
        away_team_array = []
        for i in list(todays_away_teams_df.index):
            for x in list(todays_away_teams_df):
                if list(todays_away_teams_df.index)[i] == list(todays_home_teams_df.index)[i]:
                    away_team_array.append(team_stats.team_two(Batting_all_teams.get(x), Pitching_all_teams.get(x)))
        return away_team_array[0:max(list(todays_away_teams_df.index))+1]
    @staticmethod
    def automated_function_home_team():
        home_team_array = []
        for i in list(todays_home_teams_df.index):
            for x in list(todays_home_teams_df):
                if list(todays_home_teams_df.index)[i] == list(todays_away_teams_df.index)[i]:
                    home_team_array.append(team_stats.team_one(Batting_all_teams.get(x), Pitching_all_teams.get(x)))
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
        score_df['Difference'] = team_stats.team_difference(score_df['Home_Avg'], score_df['Away_Avg'])
        score_df.drop(['Away_Avg', 'Home_Avg'], axis=1, inplace=True)
        return score_df

class manual_input:
    # Manual Input Function
    @staticmethod
    def input_team_one():
        team_one_input = input("Enter Team 1 here: ")
        return team_one_input
    @staticmethod
    def input_team_two():
        team_two_input = input("Enter Team 2 here: ")
        return team_two_input
    @staticmethod
    def manual_input_function():
        team_one_chosen_batting = Input_functionality.input_function_team_one(manual_input.input_team_one())[0]
        team_one_chosen_pitching = Input_functionality.input_function_team_one(manual_input.input_team_one())[1]
        team_two_chosen_batting = Input_functionality.input_function_team_one(manual_input.input_team_two())[0]
        team_two_chosen_pitching = Input_functionality.input_function_team_one(manual_input.input_team_two())[1]
        team_one_average_results = team_stats.team_one(team_one_chosen_batting, team_one_chosen_pitching)
        team_two_average_results = team_stats.team_two(team_two_chosen_batting, team_two_chosen_pitching)
        Final_results = manual_input.game_results(team_one_average_results, team_two_average_results)
        return Final_results
    # Function to tell me who is going to win based on average comparison
    def game_results(team_one_average_results, team_two_average_results):
        if team_one_average_results > team_two_average_results:
            results = manual_input.input_team_one()
        else:
            results = manual_input.input_team_two()
        print("The following team is going to win: " + results)
        print("Team has an Avg. advantage of: ",
              team_stats.team_difference(team_one_average_results, team_two_average_results))

# Created a dictionary for the teams and datasets per team
Batting_all_teams = {
    "ARI": teams.batting.ARI,"ATL": teams.batting.ATL,"BAL": teams.batting.BAL,"BOS": teams.batting.BOS,
    "CHC": teams.batting.CHC,"CHW": teams.batting.CHW,"CIN": teams.batting.CIN,"CLE": teams.batting.CLE,
    "COL": teams.batting.COL,"DET": teams.batting.DET,"HOU": teams.batting.HOU,"KCR": teams.batting.KCR,
    "LAA": teams.batting.LAA,"LAD": teams.batting.LAD,"MIA": teams.batting.MIA,"MIL": teams.batting.MIL,
    "MIN": teams.batting.MIN,"NYM": teams.batting.NYM,"NYY": teams.batting.NYY,"OAK": teams.batting.OAK,
    "PHI": teams.batting.PHI,"PIT": teams.batting.PIT,"SDP": teams.batting.SDP,"SEA": teams.batting.SEA,
    "SFG": teams.batting.SFG,"STL": teams.batting.STL,"TBR": teams.batting.TBR,"TEX": teams.batting.TEX,
    "TOR": teams.batting.TOR,"WSN": teams.batting.WSN
}

Pitching_all_teams = {
    "ARI": teams.pitching.ARI,"ATL": teams.pitching.ATL,"BAL": teams.pitching.BAL,"BOS": teams.pitching.BOS,
    "CHC": teams.pitching.CHC,"CHW": teams.pitching.CHW,"CIN": teams.pitching.CIN,"CLE": teams.pitching.CLE,
    "COL": teams.pitching.COL,"DET": teams.pitching.DET,"HOU": teams.pitching.HOU,"KCR": teams.pitching.KCR,
    "LAA": teams.pitching.LAA,"LAD": teams.pitching.LAD,"MIA": teams.pitching.MIA,"MIL": teams.pitching.MIL,
    "MIN": teams.pitching.MIN,"NYM": teams.pitching.NYM,"NYY": teams.pitching.NYY,"OAK": teams.pitching.OAK,
    "PHI": teams.pitching.PHI,"PIT": teams.pitching.PIT,"SDP": teams.pitching.SDP,"SEA": teams.pitching.SEA,
    "SFG": teams.pitching.SFG,"STL": teams.pitching.STL,"TBR": teams.pitching.TBR,"TEX": teams.pitching.TEX,
    "TOR": teams.pitching.TOR,"WSN": teams.pitching.WSN
}

# Normalization of the stats
Statistics_used_for_normalization = normalized_batting_stats(Batting_df_all, Pitching_df_all)

Final_dataframe = automated_method.final_data_frame_automated()
Final_dataframe.to_excel('C:/Users/t0ys0r/OneDrive\Desktop/Degenerate Behaviour/Baseball/Todays_Games.xlsx',
                  sheet_name='Todays_Games')