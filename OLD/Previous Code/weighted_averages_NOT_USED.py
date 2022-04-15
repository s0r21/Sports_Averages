from dataset import pd, np
from dataset import ARI_batting_df, ARI_pitching_df, ATL_batting_df, ATL_pitching_df, BAL_pitching_df, BAL_batting_df,\
    BOS_batting_df, BOS_pitching_df, CHC_pitching_df, CHC_batting_df, CHW_pitching_df, CHW_batting_df, CIN_pitching_df,\
    CIN_batting_df, CLE_batting_df, CLE_pitching_df, COL_batting_df, COL_pitching_df, DET_batting_df, DET_pitching_df,\
    HOU_batting_df, HOU_pitching_df, KCR_pitching_df, KCR_batting_df, LAA_pitching_df, LAA_batting_df, LAD_pitching_df,\
    LAD_batting_df, MIA_batting_df, MIA_pitching_df, MIL_batting_df, MIL_pitching_df, MIN_pitching_df, MIN_batting_df,\
    NYM_batting_df, NYM_pitching_df, NYY_pitching_df, NYY_batting_df, OAK_pitching_df, OAK_batting_df, PHI_pitching_df,\
    PHI_batting_df, PIT_batting_df, PIT_pitching_df, SDP_pitching_df, SDP_batting_df, SEA_pitching_df, SEA_batting_df,\
    SFG_batting_df, SFG_pitching_df, STL_pitching_df, STL_batting_df, TBR_pitching_df, TBR_batting_df, TEX_pitching_df,\
    TEX_batting_df, TOR_batting_df, TOR_pitching_df, WSN_batting_df, WSN_pitching_df

print("Enter Team 1 here: ")
team_one_input = input()
print("Enter Team 2 here: ")
team_two_input = input()

def input_function_team_one(team_one_function_input):
    if team_one_function_input == "ARI":
        team_one_batting_input, team_one_pitching_input = ARI_batting_df, ARI_pitching_df
    elif team_one_function_input == "ATL":
        team_one_batting_input, team_one_pitching_input = ATL_batting_df, ATL_pitching_df
    elif team_one_function_input == "BAL":
        team_one_batting_input, team_one_pitching_input = BAL_batting_df, BAL_pitching_df
    elif team_one_function_input == "BOS":
        team_one_batting_input, team_one_pitching_input = BOS_batting_df, BOS_pitching_df
    elif team_one_function_input == "CHC":
        team_one_batting_input, team_one_pitching_input = CHC_batting_df, CHC_pitching_df
    elif team_one_function_input == "CHW":
        team_one_batting_input, team_one_pitching_input = CHW_batting_df, CHW_pitching_df
    elif team_one_function_input == "CIN":
        team_one_batting_input, team_one_pitching_input = CIN_batting_df, CIN_pitching_df
    elif team_one_function_input == "CLE":
        team_one_batting_input, team_one_pitching_input = CLE_batting_df, CLE_pitching_df
    elif team_one_function_input == "COL":
        team_one_batting_input, team_one_pitching_input = COL_batting_df, COL_pitching_df
    elif team_one_function_input == "DET":
        team_one_batting_input, team_one_pitching_input = DET_batting_df, DET_pitching_df
    elif team_one_function_input == "HOU":
        team_one_batting_input, team_one_pitching_input = HOU_batting_df, HOU_pitching_df
    elif team_one_function_input == "KCR":
        team_one_batting_input, team_one_pitching_input = KCR_batting_df, KCR_pitching_df
    elif team_one_function_input == "LAA":
        team_one_batting_input, team_one_pitching_input = LAA_batting_df, LAA_pitching_df
    elif team_one_function_input == "LAD":
        team_one_batting_input, team_one_pitching_input = LAD_batting_df, LAD_pitching_df
    elif team_one_function_input == "MIA":
        team_one_batting_input, team_one_pitching_input = MIA_batting_df, MIA_pitching_df
    elif team_one_function_input == "MIL":
        team_one_batting_input, team_one_pitching_input = MIL_batting_df, MIL_pitching_df
    elif team_one_function_input == "MIN":
        team_one_batting_input, team_one_pitching_input = MIN_batting_df, MIN_pitching_df
    elif team_one_function_input == "NYM":
        team_one_batting_input, team_one_pitching_input = NYM_batting_df, NYM_pitching_df
    elif team_one_function_input == "NYY":
        team_one_batting_input, team_one_pitching_input = NYY_batting_df, NYY_pitching_df
    elif team_one_function_input == "OAK":
        team_one_batting_input, team_one_pitching_input = OAK_batting_df, OAK_pitching_df
    elif team_one_function_input == "PHI":
        team_one_batting_input, team_one_pitching_input = PHI_batting_df, PHI_pitching_df
    elif team_one_function_input == "PIT":
        team_one_batting_input, team_one_pitching_input = PIT_batting_df, PIT_pitching_df
    elif team_one_function_input == "SDP":
        team_one_batting_input, team_one_pitching_input = SDP_batting_df, SDP_pitching_df
    elif team_one_function_input == "SEA":
        team_one_batting_input, team_one_pitching_input = SEA_batting_df, SEA_pitching_df
    elif team_one_function_input == "SFG":
        team_one_batting_input, team_one_pitching_input = SFG_batting_df, SFG_pitching_df
    elif team_one_function_input == "STL":
        team_one_batting_input, team_one_pitching_input = STL_batting_df, STL_pitching_df
    elif team_one_function_input == "TBR":
        team_one_batting_input, team_one_pitching_input = TBR_batting_df, TBR_pitching_df
    elif team_one_function_input == "TEX":
        team_one_batting_input, team_one_pitching_input = TEX_batting_df, TEX_pitching_df
    elif team_one_function_input == "TOR":
        team_one_batting_input, team_one_pitching_input = TOR_batting_df, TOR_pitching_df
    elif team_one_function_input == "WSN":
        team_one_batting_input, team_one_pitching_input = WSN_batting_df, WSN_pitching_df
    return team_one_batting_input, team_one_pitching_input
def input_function_team_two(team_two_function_input):
    if team_two_function_input == "ARI":
        team_two_batting_input, team_two_pitching_input = ARI_batting_df, ARI_pitching_df
    elif team_two_function_input == "ATL":
        team_two_batting_input, team_two_pitching_input = ATL_batting_df, ATL_pitching_df
    elif team_two_function_input == "BAL":
        team_two_batting_input, team_two_pitching_input = BAL_batting_df, BAL_pitching_df
    elif team_two_function_input == "BOS":
        team_two_batting_input, team_two_pitching_input = BOS_batting_df, BOS_pitching_df
    elif team_two_function_input == "CHC":
        team_two_batting_input, team_two_pitching_input = CHC_batting_df, CHC_pitching_df
    elif team_two_function_input == "CHW":
        team_two_batting_input, team_two_pitching_input = CHW_batting_df, CHW_pitching_df
    elif team_two_function_input == "CIN":
        team_two_batting_input, team_two_pitching_input = CIN_batting_df, CIN_pitching_df
    elif team_two_function_input == "CLE":
        team_two_batting_input, team_two_pitching_input = CLE_batting_df, CLE_pitching_df
    elif team_two_function_input == "COL":
        team_two_batting_input, team_two_pitching_input = COL_batting_df, COL_pitching_df
    elif team_two_function_input == "DET":
        team_two_batting_input, team_two_pitching_input = DET_batting_df, DET_pitching_df
    elif team_two_function_input == "HOU":
        team_two_batting_input, team_two_pitching_input = HOU_batting_df, HOU_pitching_df
    elif team_two_function_input == "KCR":
        team_two_batting_input, team_two_pitching_input = KCR_batting_df, KCR_pitching_df
    elif team_two_function_input == "LAA":
        team_two_batting_input, team_two_pitching_input = LAA_batting_df, LAA_pitching_df
    elif team_two_function_input == "LAD":
        team_two_batting_input, team_two_pitching_input = LAD_batting_df, LAD_pitching_df
    elif team_two_function_input == "MIA":
        team_two_batting_input, team_two_pitching_input = MIA_batting_df, MIA_pitching_df
    elif team_two_function_input == "MIL":
        team_two_batting_input, team_two_pitching_input = MIL_batting_df, MIL_pitching_df
    elif team_two_function_input == "MIN":
        team_two_batting_input, team_two_pitching_input = MIN_batting_df, MIN_pitching_df
    elif team_two_function_input == "NYM":
        team_two_batting_input, team_two_pitching_input = NYM_batting_df, NYM_pitching_df
    elif team_two_function_input == "NYY":
        team_two_batting_input, team_two_pitching_input = NYY_batting_df, NYY_pitching_df
    elif team_two_function_input == "OAK":
        team_two_batting_input, team_two_pitching_input = OAK_batting_df, OAK_pitching_df
    elif team_two_function_input == "PHI":
        team_two_batting_input, team_two_pitching_input = PHI_batting_df, PHI_pitching_df
    elif team_two_function_input == "PIT":
        team_two_batting_input, team_two_pitching_input = PIT_batting_df, PIT_pitching_df
    elif team_two_function_input == "SDP":
        team_two_batting_input, team_two_pitching_input = SDP_batting_df, SDP_pitching_df
    elif team_two_function_input == "SEA":
        team_two_batting_input, team_two_pitching_input = SEA_batting_df, SEA_pitching_df
    elif team_two_function_input == "SFG":
        team_two_batting_input, team_two_pitching_input = SFG_batting_df, SFG_pitching_df
    elif team_two_function_input == "STL":
        team_two_batting_input, team_two_pitching_input = STL_batting_df, STL_pitching_df
    elif team_two_function_input == "TBR":
        team_two_batting_input, team_two_pitching_input = TBR_batting_df, TBR_pitching_df
    elif team_two_function_input == "TEX":
        team_two_batting_input, team_two_pitching_input = TEX_batting_df, TEX_pitching_df
    elif team_two_function_input == "TOR":
        team_two_batting_input, team_two_pitching_input = TOR_batting_df, TOR_pitching_df
    elif team_two_function_input == "WSN":
        team_two_batting_input, team_two_pitching_input = WSN_batting_df, WSN_pitching_df
    return team_two_batting_input, team_two_pitching_input

team_one_chosen_batting = input_function_team_one(team_one_input)[0]
team_one_chosen_pitching = input_function_team_one(team_one_input)[1]
team_two_chosen_batting = input_function_team_one(team_two_input)[0]
team_two_chosen_pitching = input_function_team_one(team_two_input)[1]


# This sheet is going to be used to create the offence and defence weighted averages
# Note: change these functions to represent only dataframes as the variables -> ex. def offence(df): r_mean = np.mean(df[1])
# This is just to optimize the code.

def team_one(batting, pitching):
    R_mean = (batting.iloc[:,0]).astype(int).mean()
    H_mean = (batting.iloc[:,1]).astype(int).mean()
    two_B_mean = (batting.iloc[:,2]).astype(int).mean()
    three_B_mean = (batting.iloc[:,3]).astype(int).mean()
    RBI_mean = (batting.iloc[:,4]).astype(int).mean()
    SB_mean = (batting.iloc[:,5]).astype(int).mean()
    batting_final = (0.25*(H_mean)) + (0.2*(R_mean)) + (0.2*(three_B_mean)) +\
                    (0.15*(SB_mean)) + (0.1*(RBI_mean)) + (0.1*(two_B_mean))
    R_mean = (pitching.iloc[:,0]).astype(int).mean()
    H_mean = (pitching.iloc[:,1]).astype(int).mean()
    ER_mean = (pitching.iloc[:,2]).astype(int).mean()
    HR_mean = (pitching.iloc[:,3]).astype(int).mean()
    BB_mean = (pitching.iloc[:,4]).astype(int).mean()
    SO_mean = (pitching.iloc[:,5]).astype(int).mean()
    pitching_final = (0.25*(H_mean)) + (0.15*(R_mean)) + (0.15*(ER_mean)) + \
                     (0.05*(HR_mean)) + (0.05*(BB_mean)) - (0.35*(SO_mean))
    team_one_average = batting_final - pitching_final
    return team_one_average

team_one_average_results = team_one(team_one_chosen_batting, team_one_chosen_pitching)

def team_two(batting, pitching):
    R_mean = (batting.iloc[:,0]).astype(int).mean()
    H_mean = (batting.iloc[:,1]).astype(int).mean()
    two_B_mean = (batting.iloc[:,2]).astype(int).mean()
    three_B_mean = (batting.iloc[:,3]).astype(int).mean()
    RBI_mean = (batting.iloc[:,4]).astype(int).mean()
    SB_mean = (batting.iloc[:,5]).astype(int).mean()
    batting_final = (0.25*(H_mean)) + (0.2*(R_mean)) + (0.2*(three_B_mean)) +\
                    (0.15*(SB_mean)) + (0.1*(RBI_mean)) + (0.1*(two_B_mean))
    R_mean = (pitching.iloc[:,0]).astype(int).mean()
    H_mean = (pitching.iloc[:,1]).astype(int).mean()
    ER_mean = (pitching.iloc[:,2]).astype(int).mean()
    HR_mean = (pitching.iloc[:,3]).astype(int).mean()
    BB_mean = (pitching.iloc[:,4]).astype(int).mean()
    SO_mean = (pitching.iloc[:,5]).astype(int).mean()
    pitching_final = (0.25*(H_mean)) + (0.15*(R_mean)) + (0.15*(ER_mean)) + \
                     (0.05*(HR_mean)) + (0.05*(BB_mean)) - (0.35*(SO_mean))
    team_two_average = batting_final - pitching_final
    return team_two_average

team_two_average_results = team_two(team_two_chosen_batting, team_two_chosen_pitching)

def game_results(team_one_average_results, team_two_average_results):
    if team_one_average_results > team_two_average_results:
        results = team_one_input
    else: results = team_two_input
    print("The following team is going to win: " + results)

Final_results = game_results(team_one_average_results, team_two_average_results)
