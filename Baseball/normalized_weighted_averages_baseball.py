# The weighted average formulas for the game of baseball

from dataset import *

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
def game_results(team_one_average_results, team_two_average_results):
    if team_one_average_results > team_two_average_results:
        results = team_one_input
    else: results = team_two_input
    print("The following team is going to win: " + results)
def input_function_team_one(team_one_function_input):
    if team_one_function_input == "ARI":
        team_one_batting_input, team_one_pitching_input = teams.batting.ARI, teams.pitching.ARI
    elif team_one_function_input == "ATL":
        team_one_batting_input, team_one_pitching_input = teams.batting.ATL, teams.pitching.ATL
    elif team_one_function_input == "BAL":
        team_one_batting_input, team_one_pitching_input = teams.batting.BAL, teams.pitching.BAL
    elif team_one_function_input == "BOS":
        team_one_batting_input, team_one_pitching_input = teams.batting.BOS, teams.pitching.BOS
    elif team_one_function_input == "CHC":
        team_one_batting_input, team_one_pitching_input = teams.batting.CHC, teams.pitching.CHC
    elif team_one_function_input == "CHW":
        team_one_batting_input, team_one_pitching_input = teams.batting.CHW, teams.pitching.CHW
    elif team_one_function_input == "CIN":
        team_one_batting_input, team_one_pitching_input = teams.batting.CIN, teams.pitching.CIN
    elif team_one_function_input == "CLE":
        team_one_batting_input, team_one_pitching_input = teams.batting.CLE, teams.pitching.CLE
    elif team_one_function_input == "COL":
        team_one_batting_input, team_one_pitching_input = teams.batting.COL, teams.pitching.COL
    elif team_one_function_input == "DET":
        team_one_batting_input, team_one_pitching_input = teams.batting.DET, teams.pitching.DET
    elif team_one_function_input == "HOU":
        team_one_batting_input, team_one_pitching_input = teams.batting.HOU, teams.pitching.HOU
    elif team_one_function_input == "KCR":
        team_one_batting_input, team_one_pitching_input = teams.batting.KCR, teams.pitching.KCR
    elif team_one_function_input == "LAA":
        team_one_batting_input, team_one_pitching_input = teams.batting.LAA, teams.pitching.LAA
    elif team_one_function_input == "LAD":
        team_one_batting_input, team_one_pitching_input = teams.batting.LAD, teams.pitching.LAD
    elif team_one_function_input == "MIA":
        team_one_batting_input, team_one_pitching_input = teams.batting.MIA, teams.pitching.MIA
    elif team_one_function_input == "MIL":
        team_one_batting_input, team_one_pitching_input = teams.batting.MIL, teams.pitching.MIL
    elif team_one_function_input == "MIN":
        team_one_batting_input, team_one_pitching_input = teams.batting.MIN, teams.pitching.MIN
    elif team_one_function_input == "NYM":
        team_one_batting_input, team_one_pitching_input = teams.batting.NYM, teams.pitching.NYM
    elif team_one_function_input == "NYY":
        team_one_batting_input, team_one_pitching_input = teams.batting.NYY, teams.pitching.NYY
    elif team_one_function_input == "OAK":
        team_one_batting_input, team_one_pitching_input = teams.batting.OAK, teams.pitching.OAK
    elif team_one_function_input == "PHI":
        team_one_batting_input, team_one_pitching_input = teams.batting.PHI, teams.pitching.PHI
    elif team_one_function_input == "PIT":
        team_one_batting_input, team_one_pitching_input = teams.batting.PIT, teams.pitching.PIT
    elif team_one_function_input == "SDP":
        team_one_batting_input, team_one_pitching_input = teams.batting.SDP, teams.pitching.SDP
    elif team_one_function_input == "SEA":
        team_one_batting_input, team_one_pitching_input = teams.batting.SEA, teams.pitching.SEA
    elif team_one_function_input == "SFG":
        team_one_batting_input, team_one_pitching_input = teams.batting.SFG, teams.pitching.SFG
    elif team_one_function_input == "STL":
        team_one_batting_input, team_one_pitching_input = teams.batting.STL, teams.pitching.STL
    elif team_one_function_input == "TBR":
        team_one_batting_input, team_one_pitching_input = teams.batting.TBR, teams.pitching.TBR
    elif team_one_function_input == "TEX":
        team_one_batting_input, team_one_pitching_input = teams.batting.TEX, teams.pitching.TEX
    elif team_one_function_input == "TOR":
        team_one_batting_input, team_one_pitching_input = teams.batting.TOR, teams.pitching.TOR
    elif team_one_function_input == "WSN":
        team_one_batting_input, team_one_pitching_input = teams.batting.WSN, teams.pitching.WSN
    return team_one_batting_input, team_one_pitching_input
def input_function_team_two(team_two_function_input):
    if team_two_function_input == "ARI":
        team_two_batting_input, team_two_pitching_input = teams.batting.ARI, teams.pitching.ARI
    elif team_two_function_input == "ATL":
        team_two_batting_input, team_two_pitching_input = teams.batting.ATL, teams.pitching.ATL
    elif team_two_function_input == "BAL":
        team_two_batting_input, team_two_pitching_input = teams.batting.BAL, teams.pitching.BAL
    elif team_two_function_input == "BOS":
        team_two_batting_input, team_two_pitching_input = teams.batting.BOS, teams.pitching.BOS
    elif team_two_function_input == "CHC":
        team_two_batting_input, team_two_pitching_input = teams.batting.CHC, teams.pitching.CHC
    elif team_two_function_input == "CHW":
        team_two_batting_input, team_two_pitching_input = teams.batting.CHW, teams.pitching.CHW
    elif team_two_function_input == "CIN":
        team_two_batting_input, team_two_pitching_input = teams.batting.CIN, teams.pitching.CIN
    elif team_two_function_input == "CLE":
        team_two_batting_input, team_two_pitching_input = teams.batting.CLE, teams.pitching.CLE
    elif team_two_function_input == "COL":
        team_two_batting_input, team_two_pitching_input = teams.batting.COL, teams.pitching.COL
    elif team_two_function_input == "DET":
        team_two_batting_input, team_two_pitching_input = teams.batting.DET, teams.pitching.DET
    elif team_two_function_input == "HOU":
        team_two_batting_input, team_two_pitching_input = teams.batting.HOU, teams.pitching.HOU
    elif team_two_function_input == "KCR":
        team_two_batting_input, team_two_pitching_input = teams.batting.KCR, teams.pitching.KCR
    elif team_two_function_input == "LAA":
        team_two_batting_input, team_two_pitching_input = teams.batting.LAA, teams.pitching.LAA
    elif team_two_function_input == "LAD":
        team_two_batting_input, team_two_pitching_input = teams.batting.LAD, teams.pitching.LAD
    elif team_two_function_input == "MIA":
        team_two_batting_input, team_two_pitching_input = teams.batting.MIA, teams.pitching.MIA
    elif team_two_function_input == "MIL":
        team_two_batting_input, team_two_pitching_input = teams.batting.MIL, teams.pitching.MIL
    elif team_two_function_input == "MIN":
        team_two_batting_input, team_two_pitching_input = teams.batting.MIN, teams.pitching.MIN
    elif team_two_function_input == "NYM":
        team_two_batting_input, team_two_pitching_input = teams.batting.NYM, teams.pitching.NYM
    elif team_two_function_input == "NYY":
        team_two_batting_input, team_two_pitching_input = teams.batting.NYY, teams.pitching.NYY
    elif team_two_function_input == "OAK":
        team_two_batting_input, team_two_pitching_input = teams.batting.OAK, teams.pitching.OAK
    elif team_two_function_input == "PHI":
        team_two_batting_input, team_two_pitching_input = teams.batting.PHI, teams.pitching.PHI
    elif team_two_function_input == "PIT":
        team_two_batting_input, team_two_pitching_input = teams.batting.PIT, teams.pitching.PIT
    elif team_two_function_input == "SDP":
        team_two_batting_input, team_two_pitching_input = teams.batting.SDP, teams.pitching.SDP
    elif team_two_function_input == "SEA":
        team_two_batting_input, team_two_pitching_input = teams.batting.SEA, teams.pitching.SEA
    elif team_two_function_input == "SFG":
        team_two_batting_input, team_two_pitching_input = teams.batting.SFG, teams.pitching.SFG
    elif team_two_function_input == "STL":
        team_two_batting_input, team_two_pitching_input = teams.batting.STL, teams.pitching.STL
    elif team_two_function_input == "TBR":
        team_two_batting_input, team_two_pitching_input = teams.batting.TBR, teams.pitching.TBR
    elif team_two_function_input == "TEX":
        team_two_batting_input, team_two_pitching_input = teams.batting.TEX, teams.pitching.TEX
    elif team_two_function_input == "TOR":
        team_two_batting_input, team_two_pitching_input = teams.batting.TOR, teams.pitching.TOR
    elif team_two_function_input == "WSN":
        team_two_batting_input, team_two_pitching_input = teams.batting.WSN, teams.pitching.WSN
    return team_two_batting_input, team_two_pitching_input

print("Enter Team 1 here: ")
team_one_input = input()
print("Enter Team 2 here: ")
team_two_input = input()

Statistics_used_for_normalization = normalized_batting_stats(Batting_df_all, Pitching_df_all)

team_one_chosen_batting = input_function_team_one(team_one_input)[0]
team_one_chosen_pitching = input_function_team_one(team_one_input)[1]
team_two_chosen_batting = input_function_team_one(team_two_input)[0]
team_two_chosen_pitching = input_function_team_one(team_two_input)[1]


# This sheet is going to be used to create the offence and defence weighted averages
# Note: change these functions to represent only dataframes as the variables -> ex. def offence(df): r_sum = np.sum(df[1])
# This is just to optimize the code.

team_one_average_results = team_one(team_one_chosen_batting, team_one_chosen_pitching)
team_two_average_results = team_two(team_two_chosen_batting, team_two_chosen_pitching)

Final_results = game_results(team_one_average_results, team_two_average_results)
