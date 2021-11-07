# The weighted average formulas for the game of baseball

from dataset import ARI_batting_df, ARI_pitching_df, ATL_batting_df, ATL_pitching_df, BAL_pitching_df, BAL_batting_df,\
    BOS_batting_df, BOS_pitching_df, CHC_pitching_df, CHC_batting_df, CHW_pitching_df, CHW_batting_df, CIN_pitching_df,\
    CIN_batting_df, CLE_batting_df, CLE_pitching_df, COL_batting_df, COL_pitching_df, DET_batting_df, DET_pitching_df,\
    HOU_batting_df, HOU_pitching_df, KCR_pitching_df, KCR_batting_df, LAA_pitching_df, LAA_batting_df, LAD_pitching_df,\
    LAD_batting_df, MIA_batting_df, MIA_pitching_df, MIL_batting_df, MIL_pitching_df, MIN_pitching_df, MIN_batting_df,\
    NYM_batting_df, NYM_pitching_df, NYY_pitching_df, NYY_batting_df, OAK_pitching_df, OAK_batting_df, PHI_pitching_df,\
    PHI_batting_df, PIT_batting_df, PIT_pitching_df, SDP_pitching_df, SDP_batting_df, SEA_pitching_df, SEA_batting_df,\
    SFG_batting_df, SFG_pitching_df, STL_pitching_df, STL_batting_df, TBR_pitching_df, TBR_batting_df, TEX_pitching_df,\
    TEX_batting_df, TOR_batting_df, TOR_pitching_df, WSN_batting_df, WSN_pitching_df

Batting_df_all = ARI_batting_df.append(ATL_batting_df).append(BAL_batting_df).append(BOS_batting_df).append(CHC_batting_df)\
    .append(CHW_batting_df).append(CIN_batting_df).append(CLE_batting_df).append(COL_batting_df).append(DET_batting_df)\
    .append(HOU_batting_df).append(KCR_batting_df).append(LAA_batting_df).append(LAD_batting_df).append(MIA_batting_df)\
    .append(MIL_batting_df).append(MIN_batting_df).append(NYM_batting_df).append(NYY_batting_df).append(OAK_batting_df)\
    .append(PHI_batting_df).append(PIT_batting_df).append(SDP_batting_df).append(SEA_batting_df).append(SFG_batting_df)\
    .append(STL_batting_df).append(TBR_batting_df).append(TEX_batting_df).append(TOR_batting_df).append(WSN_batting_df)\
    .reset_index().drop(columns = 'index')
Pitching_df_all = ARI_pitching_df.append(ATL_pitching_df).append(BAL_pitching_df).append(BOS_pitching_df).append(CHC_pitching_df)\
    .append(CHW_pitching_df).append(CIN_pitching_df).append(CLE_pitching_df).append(COL_pitching_df).append(DET_pitching_df)\
    .append(HOU_pitching_df).append(KCR_pitching_df).append(LAA_pitching_df).append(LAD_pitching_df).append(MIA_pitching_df)\
    .append(MIL_pitching_df).append(MIN_pitching_df).append(NYM_pitching_df).append(NYY_pitching_df).append(OAK_pitching_df)\
    .append(PHI_pitching_df).append(PIT_pitching_df).append(SDP_pitching_df).append(SEA_pitching_df).append(SFG_pitching_df)\
    .append(STL_pitching_df).append(TBR_pitching_df).append(TEX_pitching_df).append(TOR_pitching_df).append(WSN_pitching_df)\
    .reset_index().drop(columns = 'index')

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

Statistics_used_for_normalization = normalized_batting_stats(Batting_df_all, Pitching_df_all)

# NOTE: try to sum it instead of averaging the weighted averages (since you already normalized it).

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
# Note: change these functions to represent only dataframes as the variables -> ex. def offence(df): r_sum = np.sum(df[1])
# This is just to optimize the code.

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

team_one_average_results = team_one(team_one_chosen_batting, team_one_chosen_pitching)

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

team_two_average_results = team_two(team_two_chosen_batting, team_two_chosen_pitching)

def game_results(team_one_average_results, team_two_average_results):
    if team_one_average_results > team_two_average_results:
        results = team_one_input
    else: results = team_two_input
    print("The following team is going to win: " + results)

Final_results = game_results(team_one_average_results, team_two_average_results)
