# This page is to create the dataset needed to predict football (american) games.

from packages import pd, np

# Injuries_dataset = pd.read_html('https://www.pro-football-reference.com/players/injuries.htm#injuries')
# Injuries_dataset = pd.DataFrame(Injuries_dataset[0])
# Injuries_dataset = Injuries_dataset[Injuries_dataset['Practice Status'] != 'Full Participation In Practice']
# Injuries_array = np.array(Injuries_dataset['Player']).astype(str)
#
# def injury_function(dataset):
#     dataset = dataset[~dataset.isin(Injuries_array)]
#     dataset.dropna(subset=[('Unnamed: 1_level_0', 'Player')], inplace = True)
#     return dataset

# Buffalo Bills
    # QB - Offence
BUF_raw_df = pd.read_html('https://www.pro-football-reference.com/teams/buf/2021.htm#passing')
BUF_qb_df = pd.DataFrame(BUF_raw_df[0])
BUF_qb_df = np.transpose(pd.DataFrame(BUF_qb_df))
BUF_qb_df = np.transpose(BUF_qb_df.loc[[('Passing', 'Cmp'), ('Passing', 'Att'), ('Passing', 'TD')], :])
BUF_qb_df = np.transpose(BUF_qb_df.loc[0])
BUF_qb_final_sum = (0.4 * np.sum(BUF_qb_df[('Passing', 'Att')] - BUF_qb_df[('Passing', 'Cmp')])) + (0.6 * BUF_qb_df[('Passing', 'TD')])

    # RB - Offence
BUF_rb_df = pd.DataFrame(BUF_raw_df[0])
BUF_rb_df = np.transpose(pd.DataFrame(BUF_rb_df))
BUF_rb_df = np.transpose(BUF_rb_df.loc[[('Rushing', 'Y/A'), ('Rushing', 'TD')], :])
BUF_rb_df = np.transpose(BUF_rb_df.loc[0])
BUF_rb_final_sum = np.sum( (0.4 * BUF_rb_df.loc[('Rushing', 'Y/A')] ) + (0.6 * BUF_rb_df.loc[('Rushing', 'TD')] ) )

    # Defense
BUF_def = pd.DataFrame(BUF_raw_df[1])
BUF_def = np.transpose(pd.DataFrame(BUF_def))
BUF_def = np.transpose(BUF_def.loc[[('Defense', 'PassY'), ('Defense', 'RushY')], :])
BUF_def = np.transpose(BUF_def.loc[0])
BUF_def_final_sum = np.sum( (0.5 * BUF_def.loc[('Defense', 'PassY')] ) + (0.5 * BUF_def.loc[('Defense', 'RushY')] ) )

# Miami Dolphins
    # QB - Offence
MIA_raw_df = pd.read_html('https://www.pro-football-reference.com/teams/mia/2021.htm#passing')
MIA_qb_df = pd.DataFrame(MIA_raw_df[0])
MIA_qb_df = np.transpose(pd.DataFrame(MIA_qb_df))
MIA_qb_df = np.transpose(MIA_qb_df.loc[[('Passing', 'Cmp'), ('Passing', 'Att'), ('Passing', 'TD')], :])
MIA_qb_df = np.transpose(MIA_qb_df.loc[0])
MIA_qb_final_sum = (0.4 * np.sum(MIA_qb_df[('Passing', 'Att')] - MIA_qb_df[('Passing', 'Cmp')])) + (0.6 * MIA_qb_df[('Passing', 'TD')])

 # RB - Offence
MIA_rb_df = pd.DataFrame(MIA_raw_df[0])
MIA_rb_df = np.transpose(pd.DataFrame(MIA_rb_df))
MIA_rb_df = np.transpose(MIA_rb_df.loc[[('Rushing', 'Y/A'), ('Rushing', 'TD')], :])
MIA_rb_df = np.transpose(MIA_rb_df.loc[0])
MIA_rb_final_sum = np.sum( (0.4 * MIA_rb_df.loc[('Rushing', 'Y/A')] ) + (0.6 * MIA_rb_df.loc[('Rushing', 'TD')] ) )

 # Defense
MIA_def = pd.DataFrame(MIA_raw_df[1])
MIA_def = np.transpose(pd.DataFrame(MIA_def))
MIA_def = np.transpose(MIA_def.loc[[('Defense', 'PassY'), ('Defense', 'RushY')], :])
MIA_def = np.transpose(MIA_def.loc[0])
MIA_def_final_sum = np.sum( (0.5 * MIA_def.loc[('Defense', 'PassY')] ) + (0.5 * MIA_def.loc[('Defense', 'RushY')] ) )

# New England Patriots
    # QB - Offence
NWE_raw_df = pd.read_html('https://www.pro-football-reference.com/teams/nwe/2021.htm#passing')
NWE_qb_df = pd.DataFrame(NWE_raw_df[0])
NWE_qb_df = np.transpose(pd.DataFrame(NWE_qb_df))
NWE_qb_df = np.transpose(NWE_qb_df.loc[[('Passing', 'Cmp'), ('Passing', 'Att'), ('Passing', 'TD')], :])
NWE_qb_df = np.transpose(NWE_qb_df.loc[0])
NWE_qb_final_sum = (0.4 * np.sum(NWE_qb_df[('Passing', 'Att')] - NWE_qb_df[('Passing', 'Cmp')])) + (0.6 * NWE_qb_df[('Passing', 'TD')])

 # RB - Offence
NWE_rb_df = pd.DataFrame(NWE_raw_df[0])
NWE_rb_df = np.transpose(pd.DataFrame(NWE_rb_df))
NWE_rb_df = np.transpose(NWE_rb_df.loc[[('Rushing', 'Y/A'), ('Rushing', 'TD')], :])
NWE_rb_df = np.transpose(NWE_rb_df.loc[0])
NWE_rb_final_sum = np.sum( (0.4 * NWE_rb_df.loc[('Rushing', 'Y/A')] ) + (0.6 * NWE_rb_df.loc[('Rushing', 'TD')] ) )

 # Defense
NWE_def = pd.DataFrame(NWE_raw_df[1])
NWE_def = np.transpose(pd.DataFrame(NWE_def))
NWE_def = np.transpose(NWE_def.loc[[('Defense', 'PassY'), ('Defense', 'RushY')], :])
NWE_def = np.transpose(NWE_def.loc[0])
NWE_def_final_sum = np.sum( (0.5 * NWE_def.loc[('Defense', 'PassY')] ) + (0.5 * NWE_def.loc[('Defense', 'RushY')] ) )

# New York Jets
    # QB - Offence
NYJ_raw_df = pd.read_html('https://www.pro-football-reference.com/teams/nyj/2021.htm#passing')
NYJ_qb_df = pd.DataFrame(NYJ_raw_df[0])
NYJ_qb_df = np.transpose(pd.DataFrame(NYJ_qb_df))
NYJ_qb_df = np.transpose(NYJ_qb_df.loc[[('Passing', 'Cmp'), ('Passing', 'Att'), ('Passing', 'TD')], :])
NYJ_qb_df = np.transpose(NYJ_qb_df.loc[0])
NYJ_qb_final_sum = (0.4 * np.sum(NYJ_qb_df[('Passing', 'Att')] - NYJ_qb_df[('Passing', 'Cmp')])) + (0.6 * NYJ_qb_df[('Passing', 'TD')])

 # RB - Offence
NYJ_rb_df = pd.DataFrame(NYJ_raw_df[0])
NYJ_rb_df = np.transpose(pd.DataFrame(NYJ_rb_df))
NYJ_rb_df = np.transpose(NYJ_rb_df.loc[[('Rushing', 'Y/A'), ('Rushing', 'TD')], :])
NYJ_rb_df = np.transpose(NYJ_rb_df.loc[0])
NYJ_rb_final_sum = np.sum( (0.4 * NYJ_rb_df.loc[('Rushing', 'Y/A')] ) + (0.6 * NYJ_rb_df.loc[('Rushing', 'TD')] ) )

 # Defense
NYJ_def = pd.DataFrame(NYJ_raw_df[1])
NYJ_def = np.transpose(pd.DataFrame(NYJ_def))
NYJ_def = np.transpose(NYJ_def.loc[[('Defense', 'PassY'), ('Defense', 'RushY')], :])
NYJ_def = np.transpose(NYJ_def.loc[0])
NYJ_def_final_sum = np.sum( (0.5 * NYJ_def.loc[('Defense', 'PassY')] ) + (0.5 * NYJ_def.loc[('Defense', 'RushY')] ) )

# Pittsburgh Steelers
    # QB - Offence
PIT_raw_df = pd.read_html('https://www.pro-football-reference.com/teams/pit/2021.htm#passing')
PIT_qb_df = pd.DataFrame(PIT_raw_df[0])
PIT_qb_df = np.transpose(pd.DataFrame(PIT_qb_df))
PIT_qb_df = np.transpose(PIT_qb_df.loc[[('Passing', 'Cmp'), ('Passing', 'Att'), ('Passing', 'TD')], :])
PIT_qb_df = np.transpose(PIT_qb_df.loc[0])
PIT_qb_final_sum = (0.4 * np.sum(PIT_qb_df[('Passing', 'Att')] - PIT_qb_df[('Passing', 'Cmp')])) + (0.6 * PIT_qb_df[('Passing', 'TD')])

 # RB - Offence
PIT_rb_df = pd.DataFrame(PIT_raw_df[0])
PIT_rb_df = np.transpose(pd.DataFrame(PIT_rb_df))
PIT_rb_df = np.transpose(PIT_rb_df.loc[[('Rushing', 'Y/A'), ('Rushing', 'TD')], :])
PIT_rb_df = np.transpose(PIT_rb_df.loc[0])
PIT_rb_final_sum = np.sum( (0.4 * PIT_rb_df.loc[('Rushing', 'Y/A')] ) + (0.6 * PIT_rb_df.loc[('Rushing', 'TD')] ) )

 # Defense
PIT_def = pd.DataFrame(PIT_raw_df[1])
PIT_def = np.transpose(pd.DataFrame(PIT_def))
PIT_def = np.transpose(PIT_def.loc[[('Defense', 'PassY'), ('Defense', 'RushY')], :])
PIT_def = np.transpose(PIT_def.loc[0])
PIT_def_final_sum = np.sum( (0.5 * PIT_def.loc[('Defense', 'PassY')] ) + (0.5 * PIT_def.loc[('Defense', 'RushY')] ) )

# Baltimore Ravens
    # QB - Offence
BAL_raw_df = pd.read_html('https://www.pro-football-reference.com/teams/rav/2021.htm#passing')
BAL_qb_df = pd.DataFrame(BAL_raw_df[0])
BAL_qb_df = np.transpose(pd.DataFrame(BAL_qb_df))
BAL_qb_df = np.transpose(BAL_qb_df.loc[[('Passing', 'Cmp'), ('Passing', 'Att'), ('Passing', 'TD')], :])
BAL_qb_df = np.transpose(BAL_qb_df.loc[0])
BAL_qb_final_sum = (0.4 * np.sum(BAL_qb_df[('Passing', 'Att')] - BAL_qb_df[('Passing', 'Cmp')])) + (0.6 * BAL_qb_df[('Passing', 'TD')])

 # RB - Offence
BAL_rb_df = pd.DataFrame(BAL_raw_df[0])
BAL_rb_df = np.transpose(pd.DataFrame(BAL_rb_df))
BAL_rb_df = np.transpose(BAL_rb_df.loc[[('Rushing', 'Y/A'), ('Rushing', 'TD')], :])
BAL_rb_df = np.transpose(BAL_rb_df.loc[0])
BAL_rb_final_sum = np.sum( (0.4 * BAL_rb_df.loc[('Rushing', 'Y/A')] ) + (0.6 * BAL_rb_df.loc[('Rushing', 'TD')] ) )

 # Defense
BAL_def = pd.DataFrame(BAL_raw_df[1])
BAL_def = np.transpose(pd.DataFrame(BAL_def))
BAL_def = np.transpose(BAL_def.loc[[('Defense', 'PassY'), ('Defense', 'RushY')], :])
BAL_def = np.transpose(BAL_def.loc[0])
BAL_def_final_sum = np.sum( (0.5 * BAL_def.loc[('Defense', 'PassY')] ) + (0.5 * BAL_def.loc[('Defense', 'RushY')] ) )

# Cleveland Browns
    # QB - Offence
CLE_raw_df = pd.read_html('https://www.pro-football-reference.com/teams/cle/2021.htm#passing')
CLE_qb_df = pd.DataFrame(CLE_raw_df[0])
CLE_qb_df = np.transpose(pd.DataFrame(CLE_qb_df))
CLE_qb_df = np.transpose(CLE_qb_df.loc[[('Passing', 'Cmp'), ('Passing', 'Att'), ('Passing', 'TD')], :])
CLE_qb_df = np.transpose(CLE_qb_df.loc[0])
CLE_qb_final_sum = (0.4 * np.sum(CLE_qb_df[('Passing', 'Att')] - CLE_qb_df[('Passing', 'Cmp')])) + (0.6 * CLE_qb_df[('Passing', 'TD')])

 # RB - Offence
CLE_rb_df = pd.DataFrame(CLE_raw_df[0])
CLE_rb_df = np.transpose(pd.DataFrame(CLE_rb_df))
CLE_rb_df = np.transpose(CLE_rb_df.loc[[('Rushing', 'Y/A'), ('Rushing', 'TD')], :])
CLE_rb_df = np.transpose(CLE_rb_df.loc[0])
CLE_rb_final_sum = np.sum( (0.4 * CLE_rb_df.loc[('Rushing', 'Y/A')] ) + (0.6 * CLE_rb_df.loc[('Rushing', 'TD')] ) )

 # Defense
CLE_def = pd.DataFrame(CLE_raw_df[1])
CLE_def = np.transpose(pd.DataFrame(CLE_def))
CLE_def = np.transpose(CLE_def.loc[[('Defense', 'PassY'), ('Defense', 'RushY')], :])
CLE_def = np.transpose(CLE_def.loc[0])
CLE_def_final_sum = np.sum( (0.5 * CLE_def.loc[('Defense', 'PassY')] ) + (0.5 * CLE_def.loc[('Defense', 'RushY')] ) )

# Buffalo Bills
    # QB - Offence
CIN_raw_df = pd.read_html('https://www.pro-football-reference.com/teams/cin/2021.htm#passing')
CIN_qb_df = pd.DataFrame(CIN_raw_df[0])
CIN_qb_df = np.transpose(pd.DataFrame(CIN_qb_df))
CIN_qb_df = np.transpose(CIN_qb_df.loc[[('Passing', 'Cmp'), ('Passing', 'Att'), ('Passing', 'TD')], :])
CIN_qb_df = np.transpose(CIN_qb_df.loc[0])
CIN_qb_final_sum = (0.4 * np.sum(CIN_qb_df[('Passing', 'Att')] - CIN_qb_df[('Passing', 'Cmp')])) + (0.6 * CIN_qb_df[('Passing', 'TD')])

 # RB - Offence
CIN_rb_df = pd.DataFrame(CIN_raw_df[0])
CIN_rb_df = np.transpose(pd.DataFrame(CIN_rb_df))
CIN_rb_df = np.transpose(CIN_rb_df.loc[[('Rushing', 'Y/A'), ('Rushing', 'TD')], :])
CIN_rb_df = np.transpose(CIN_rb_df.loc[0])
CIN_rb_final_sum = np.sum( (0.4 * CIN_rb_df.loc[('Rushing', 'Y/A')] ) + (0.6 * CIN_rb_df.loc[('Rushing', 'TD')] ) )

 # Defense
CIN_def = pd.DataFrame(CIN_raw_df[1])
CIN_def = np.transpose(pd.DataFrame(CIN_def))
CIN_def = np.transpose(CIN_def.loc[[('Defense', 'PassY'), ('Defense', 'RushY')], :])
CIN_def = np.transpose(CIN_def.loc[0])
CIN_def_final_sum = np.sum( (0.5 * CIN_def.loc[('Defense', 'PassY')] ) + (0.5 * CIN_def.loc[('Defense', 'RushY')] ) )

# Tennessee Titans
    # QB - Offence
TEN_raw_df = pd.read_html('https://www.pro-football-reference.com/teams/oti/2021.htm#passing')
TEN_qb_df = pd.DataFrame(TEN_raw_df[0])
TEN_qb_df = np.transpose(pd.DataFrame(TEN_qb_df))
TEN_qb_df = np.transpose(TEN_qb_df.loc[[('Passing', 'Cmp'), ('Passing', 'Att'), ('Passing', 'TD')], :])
TEN_qb_df = np.transpose(TEN_qb_df.loc[0])
TEN_qb_final_sum = (0.4 * np.sum(TEN_qb_df[('Passing', 'Att')] - TEN_qb_df[('Passing', 'Cmp')])) + (0.6 * TEN_qb_df[('Passing', 'TD')])

 # RB - Offence
TEN_rb_df = pd.DataFrame(TEN_raw_df[0])
TEN_rb_df = np.transpose(pd.DataFrame(TEN_rb_df))
TEN_rb_df = np.transpose(TEN_rb_df.loc[[('Rushing', 'Y/A'), ('Rushing', 'TD')], :])
TEN_rb_df = np.transpose(TEN_rb_df.loc[0])
TEN_rb_final_sum = np.sum( (0.4 * TEN_rb_df.loc[('Rushing', 'Y/A')] ) + (0.6 * TEN_rb_df.loc[('Rushing', 'TD')] ) )

 # Defense
TEN_def = pd.DataFrame(TEN_raw_df[1])
TEN_def = np.transpose(pd.DataFrame(TEN_def))
TEN_def = np.transpose(TEN_def.loc[[('Defense', 'PassY'), ('Defense', 'RushY')], :])
TEN_def = np.transpose(TEN_def.loc[0])
TEN_def_final_sum = np.sum( (0.5 * TEN_def.loc[('Defense', 'PassY')] ) + (0.5 * TEN_def.loc[('Defense', 'RushY')] ) )

# Indianapolis Colts
    # QB - Offence
IND_raw_df = pd.read_html('https://www.pro-football-reference.com/teams/clt/2021.htm#passing')
IND_qb_df = pd.DataFrame(IND_raw_df[0])
IND_qb_df = np.transpose(pd.DataFrame(IND_qb_df))
IND_qb_df = np.transpose(IND_qb_df.loc[[('Passing', 'Cmp'), ('Passing', 'Att'), ('Passing', 'TD')], :])
IND_qb_df = np.transpose(IND_qb_df.loc[0])
IND_qb_final_sum = (0.4 * np.sum(IND_qb_df[('Passing', 'Att')] - IND_qb_df[('Passing', 'Cmp')])) + (0.6 * IND_qb_df[('Passing', 'TD')])

 # RB - Offence
IND_rb_df = pd.DataFrame(IND_raw_df[0])
IND_rb_df = np.transpose(pd.DataFrame(IND_rb_df))
IND_rb_df = np.transpose(IND_rb_df.loc[[('Rushing', 'Y/A'), ('Rushing', 'TD')], :])
IND_rb_df = np.transpose(IND_rb_df.loc[0])
IND_rb_final_sum = np.sum( (0.4 * TEN_rb_df.loc[('Rushing', 'Y/A')] ) + (0.6 * TEN_rb_df.loc[('Rushing', 'TD')] ) )

 # Defense
IND_def = pd.DataFrame(IND_raw_df[1])
IND_def = np.transpose(pd.DataFrame(IND_def))
IND_def = np.transpose(IND_def.loc[[('Defense', 'PassY'), ('Defense', 'RushY')], :])
IND_def = np.transpose(IND_def.loc[0])
IND_def_final_sum = np.sum( (0.5 * IND_def.loc[('Defense', 'PassY')] ) + (0.5 * IND_def.loc[('Defense', 'RushY')] ) )

# HOUSTAN TEXANS
    # QB - Offence
HOU_raw_df = pd.read_html('https://www.pro-football-reference.com/teams/htx/2021.htm#passing')
HOU_qb_df = pd.DataFrame(HOU_raw_df[0])
HOU_qb_df = np.transpose(pd.DataFrame(HOU_qb_df))
HOU_qb_df = np.transpose(HOU_qb_df.loc[[('Passing', 'Cmp'), ('Passing', 'Att'), ('Passing', 'TD')], :])
HOU_qb_df = np.transpose(HOU_qb_df.loc[0])
HOU_qb_final_sum = (0.4 * np.sum(HOU_qb_df[('Passing', 'Att')] - HOU_qb_df[('Passing', 'Cmp')])) + (0.6 * HOU_qb_df[('Passing', 'TD')])

 # RB - Offence
HOU_rb_df = pd.DataFrame(HOU_raw_df[0])
HOU_rb_df = np.transpose(pd.DataFrame(HOU_rb_df))
HOU_rb_df = np.transpose(HOU_rb_df.loc[[('Rushing', 'Y/A'), ('Rushing', 'TD')], :])
HOU_rb_df = np.transpose(HOU_rb_df.loc[0])
HOU_rb_final_sum = np.sum( (0.4 * HOU_rb_df.loc[('Rushing', 'Y/A')] ) + (0.6 * HOU_rb_df.loc[('Rushing', 'TD')] ) )

 # Defense
HOU_def = pd.DataFrame(HOU_raw_df[1])
HOU_def = np.transpose(pd.DataFrame(HOU_def))
HOU_def = np.transpose(HOU_def.loc[[('Defense', 'PassY'), ('Defense', 'RushY')], :])
HOU_def = np.transpose(HOU_def.loc[0])
HOU_def_final_sum = np.sum( (0.5 * HOU_def.loc[('Defense', 'PassY')] ) + (0.5 * HOU_def.loc[('Defense', 'RushY')] ) )

# JACKSONVILLE JAGUARS
    # QB - Offence
JAX_raw_df = pd.read_html('https://www.pro-football-reference.com/teams/jax/2021.htm#passing')
JAX_qb_df = pd.DataFrame(JAX_raw_df[0])
JAX_qb_df = np.transpose(pd.DataFrame(JAX_qb_df))
JAX_qb_df = np.transpose(JAX_qb_df.loc[[('Passing', 'Cmp'), ('Passing', 'Att'), ('Passing', 'TD')], :])
JAX_qb_df = np.transpose(JAX_qb_df.loc[0])
JAX_qb_final_sum = (0.4 * np.sum(JAX_qb_df[('Passing', 'Att')] - JAX_qb_df[('Passing', 'Cmp')])) + (0.6 * JAX_qb_df[('Passing', 'TD')])

 # RB - Offence
JAX_rb_df = pd.DataFrame(JAX_raw_df[0])
JAX_rb_df = np.transpose(pd.DataFrame(JAX_rb_df))
JAX_rb_df = np.transpose(JAX_rb_df.loc[[('Rushing', 'Y/A'), ('Rushing', 'TD')], :])
JAX_rb_df = np.transpose(JAX_rb_df.loc[0])
JAX_rb_final_sum = np.sum( (0.4 * JAX_rb_df.loc[('Rushing', 'Y/A')] ) + (0.6 * JAX_rb_df.loc[('Rushing', 'TD')] ) )

 # Defense
JAX_def = pd.DataFrame(JAX_raw_df[1])
JAX_def = np.transpose(pd.DataFrame(JAX_def))
JAX_def = np.transpose(JAX_def.loc[[('Defense', 'PassY'), ('Defense', 'RushY')], :])
JAX_def = np.transpose(JAX_def.loc[0])
JAX_def_final_sum = np.sum( (0.5 * JAX_def.loc[('Defense', 'PassY')] ) + (0.5 * JAX_def.loc[('Defense', 'RushY')] ) )

# KANSAS CITY CHIEFS
    # QB - Offence
KAN_raw_df = pd.read_html('https://www.pro-football-reference.com/teams/kan/2021.htm#passing')
KAN_qb_df = pd.DataFrame(KAN_raw_df[0])
KAN_qb_df = np.transpose(pd.DataFrame(KAN_qb_df))
KAN_qb_df = np.transpose(KAN_qb_df.loc[[('Passing', 'Cmp'), ('Passing', 'Att'), ('Passing', 'TD')], :])
KAN_qb_df = np.transpose(KAN_qb_df.loc[0])
KAN_qb_final_sum = (0.4 * np.sum(KAN_qb_df[('Passing', 'Att')] - KAN_qb_df[('Passing', 'Cmp')])) + (0.6 * KAN_qb_df[('Passing', 'TD')])

 # RB - Offence
KAN_rb_df = pd.DataFrame(KAN_raw_df[0])
KAN_rb_df = np.transpose(pd.DataFrame(KAN_rb_df))
KAN_rb_df = np.transpose(KAN_rb_df.loc[[('Rushing', 'Y/A'), ('Rushing', 'TD')], :])
KAN_rb_df = np.transpose(KAN_rb_df.loc[0])
KAN_rb_final_sum = np.sum( (0.4 * KAN_rb_df.loc[('Rushing', 'Y/A')] ) + (0.6 * KAN_rb_df.loc[('Rushing', 'TD')] ) )

 # Defense
KAN_def = pd.DataFrame(KAN_raw_df[1])
KAN_def = np.transpose(pd.DataFrame(KAN_def))
KAN_def = np.transpose(KAN_def.loc[[('Defense', 'PassY'), ('Defense', 'RushY')], :])
KAN_def = np.transpose(KAN_def.loc[0])
KAN_def_final_sum = np.sum( (0.5 * KAN_def.loc[('Defense', 'PassY')] ) + (0.5 * KAN_def.loc[('Defense', 'RushY')] ) )

# LAS VEGAS RAIDERS
    # QB - Offence
LVR_raw_df = pd.read_html('https://www.pro-football-reference.com/teams/rai/2021.htm#passing')
LVR_qb_df = pd.DataFrame(LVR_raw_df[0])
LVR_qb_df = np.transpose(pd.DataFrame(LVR_qb_df))
LVR_qb_df = np.transpose(LVR_qb_df.loc[[('Passing', 'Cmp'), ('Passing', 'Att'), ('Passing', 'TD')], :])
LVR_qb_df = np.transpose(LVR_qb_df.loc[0])
LVR_qb_final_sum = (0.4 * np.sum(LVR_qb_df[('Passing', 'Att')] - LVR_qb_df[('Passing', 'Cmp')])) + (0.6 * LVR_qb_df[('Passing', 'TD')])

 # RB - Offence
LVR_rb_df = pd.DataFrame(LVR_raw_df[0])
LVR_rb_df = np.transpose(pd.DataFrame(LVR_rb_df))
LVR_rb_df = np.transpose(LVR_rb_df.loc[[('Rushing', 'Y/A'), ('Rushing', 'TD')], :])
LVR_rb_df = np.transpose(LVR_rb_df.loc[0])
LVR_rb_final_sum = np.sum( (0.4 * LVR_rb_df.loc[('Rushing', 'Y/A')] ) + (0.6 * LVR_rb_df.loc[('Rushing', 'TD')] ) )

 # Defense
LVR_def = pd.DataFrame(LVR_raw_df[1])
LVR_def = np.transpose(pd.DataFrame(LVR_def))
LVR_def = np.transpose(LVR_def.loc[[('Defense', 'PassY'), ('Defense', 'RushY')], :])
LVR_def = np.transpose(LVR_def.loc[0])
LVR_def_final_sum = np.sum( (0.5 * LVR_def.loc[('Defense', 'PassY')] ) + (0.5 * LVR_def.loc[('Defense', 'RushY')] ) )

# LOS ANGELES CHARGERS
    # QB - Offence
LAC_raw_df = pd.read_html('https://www.pro-football-reference.com/teams/sdg/2021.htm#passing')
LAC_qb_df = pd.DataFrame(LAC_raw_df[0])
LAC_qb_df = np.transpose(pd.DataFrame(LAC_qb_df))
LAC_qb_df = np.transpose(LAC_qb_df.loc[[('Passing', 'Cmp'), ('Passing', 'Att'), ('Passing', 'TD')], :])
LAC_qb_df = np.transpose(LAC_qb_df.loc[0])
LAC_qb_final_sum = (0.4 * np.sum(LAC_qb_df[('Passing', 'Att')] - LAC_qb_df[('Passing', 'Cmp')])) + (0.6 * LAC_qb_df[('Passing', 'TD')])

 # RB - Offence
LAC_rb_df = pd.DataFrame(LAC_raw_df[0])
LAC_rb_df = np.transpose(pd.DataFrame(LAC_rb_df))
LAC_rb_df = np.transpose(LAC_rb_df.loc[[('Rushing', 'Y/A'), ('Rushing', 'TD')], :])
LAC_rb_df = np.transpose(LAC_rb_df.loc[0])
LAC_rb_final_sum = np.sum( (0.4 * LAC_rb_df.loc[('Rushing', 'Y/A')] ) + (0.6 * LAC_rb_df.loc[('Rushing', 'TD')] ) )

 # Defense
LAC_def = pd.DataFrame(LAC_raw_df[1])
LAC_def = np.transpose(pd.DataFrame(LAC_def))
LAC_def = np.transpose(LAC_def.loc[[('Defense', 'PassY'), ('Defense', 'RushY')], :])
LAC_def = np.transpose(LAC_def.loc[0])
LAC_def_final_sum = np.sum( (0.5 * LAC_def.loc[('Defense', 'PassY')] ) + (0.5 * LAC_def.loc[('Defense', 'RushY')] ) )

# DENVER BRONCOS
    # QB - Offence
DEN_raw_df = pd.read_html('https://www.pro-football-reference.com/teams/den/2021.htm#passing')
DEN_qb_df = pd.DataFrame(DEN_raw_df[0])
DEN_qb_df = np.transpose(pd.DataFrame(DEN_qb_df))
DEN_qb_df = np.transpose(DEN_qb_df.loc[[('Passing', 'Cmp'), ('Passing', 'Att'), ('Passing', 'TD')], :])
DEN_qb_df = np.transpose(DEN_qb_df.loc[0])
DEN_qb_final_sum = (0.4 * np.sum(DEN_qb_df[('Passing', 'Att')] - DEN_qb_df[('Passing', 'Cmp')])) + (0.6 * DEN_qb_df[('Passing', 'TD')])

 # RB - Offence
DEN_rb_df = pd.DataFrame(DEN_raw_df[0])
DEN_rb_df = np.transpose(pd.DataFrame(DEN_rb_df))
DEN_rb_df = np.transpose(DEN_rb_df.loc[[('Rushing', 'Y/A'), ('Rushing', 'TD')], :])
DEN_rb_df = np.transpose(DEN_rb_df.loc[0])
DEN_rb_final_sum = np.sum( (0.4 * DEN_rb_df.loc[('Rushing', 'Y/A')] ) + (0.6 * DEN_rb_df.loc[('Rushing', 'TD')] ) )

 # Defense
DEN_def = pd.DataFrame(DEN_raw_df[1])
DEN_def = np.transpose(pd.DataFrame(DEN_def))
DEN_def = np.transpose(DEN_def.loc[[('Defense', 'PassY'), ('Defense', 'RushY')], :])
DEN_def = np.transpose(DEN_def.loc[0])
DEN_def_final_sum = np.sum( (0.5 * DEN_def.loc[('Defense', 'PassY')] ) + (0.5 * DEN_def.loc[('Defense', 'RushY')] ) )

# WASHINGTON FOOTBALL TEAM
    # QB - Offence
WSH_raw_df = pd.read_html('https://www.pro-football-reference.com/teams/was/2021.htm#passing')
WSH_qb_df = pd.DataFrame(WSH_raw_df[0])
WSH_qb_df = np.transpose(pd.DataFrame(WSH_qb_df))
WSH_qb_df = np.transpose(WSH_qb_df.loc[[('Passing', 'Cmp'), ('Passing', 'Att'), ('Passing', 'TD')], :])
WSH_qb_df = np.transpose(WSH_qb_df.loc[0])
WSH_qb_final_sum = (0.4 * np.sum(WSH_qb_df[('Passing', 'Att')] - WSH_qb_df[('Passing', 'Cmp')])) + (0.6 * WSH_qb_df[('Passing', 'TD')])

 # RB - Offence
WSH_rb_df = pd.DataFrame(WSH_raw_df[0])
WSH_rb_df = np.transpose(pd.DataFrame(WSH_rb_df))
WSH_rb_df = np.transpose(WSH_rb_df.loc[[('Rushing', 'Y/A'), ('Rushing', 'TD')], :])
WSH_rb_df = np.transpose(WSH_rb_df.loc[0])
WSH_rb_final_sum = np.sum( (0.4 * WSH_rb_df.loc[('Rushing', 'Y/A')] ) + (0.6 * WSH_rb_df.loc[('Rushing', 'TD')] ) )

 # Defense
WSH_def = pd.DataFrame(WSH_raw_df[1])
WSH_def = np.transpose(pd.DataFrame(WSH_def))
WSH_def = np.transpose(WSH_def.loc[[('Defense', 'PassY'), ('Defense', 'RushY')], :])
WSH_def = np.transpose(WSH_def.loc[0])
WSH_def_final_sum = np.sum( (0.5 * WSH_def.loc[('Defense', 'PassY')] ) + (0.5 * WSH_def.loc[('Defense', 'RushY')] ) )

 # Final Weighted Average
WSH_Avg = ((WSH_qb_final_sum + WSH_rb_final_sum) - WSH_def_final_sum)

# NEW YORK GIANTS
    # QB - Offence
NYG_raw_df = pd.read_html('https://www.pro-football-reference.com/teams/nyg/2021.htm#passing')
NYG_qb_df = pd.DataFrame(NYG_raw_df[0])
NYG_qb_df = np.transpose(pd.DataFrame(NYG_qb_df))
NYG_qb_df = np.transpose(NYG_qb_df.loc[[('Passing', 'Cmp'), ('Passing', 'Att'), ('Passing', 'TD')], :])
NYG_qb_df = np.transpose(NYG_qb_df.loc[0])
NYG_qb_final_sum = (0.4 * np.sum(NYG_qb_df[('Passing', 'Att')] - NYG_qb_df[('Passing', 'Cmp')])) + (0.6 * NYG_qb_df[('Passing', 'TD')])

 # RB - Offence
NYG_rb_df = pd.DataFrame(NYG_raw_df[0])
NYG_rb_df = np.transpose(pd.DataFrame(NYG_rb_df))
NYG_rb_df = np.transpose(NYG_rb_df.loc[[('Rushing', 'Y/A'), ('Rushing', 'TD')], :])
NYG_rb_df = np.transpose(NYG_rb_df.loc[0])
NYG_rb_final_sum = np.sum( (0.4 * NYG_rb_df.loc[('Rushing', 'Y/A')] ) + (0.6 * NYG_rb_df.loc[('Rushing', 'TD')] ) )

 # Defense
NYG_def = pd.DataFrame(NYG_raw_df[1])
NYG_def = np.transpose(pd.DataFrame(NYG_def))
NYG_def = np.transpose(NYG_def.loc[[('Defense', 'PassY'), ('Defense', 'RushY')], :])
NYG_def = np.transpose(NYG_def.loc[0])
NYG_def_final_sum = np.sum( (0.5 * NYG_def.loc[('Defense', 'PassY')] ) + (0.5 * NYG_def.loc[('Defense', 'RushY')] ) )

# DALLAS COWBOYS
    # QB - Offence
DAL_raw_df = pd.read_html('https://www.pro-football-reference.com/teams/dal/2021.htm#passing')
DAL_qb_df = pd.DataFrame(DAL_raw_df[0])
DAL_qb_df = np.transpose(pd.DataFrame(DAL_qb_df))
DAL_qb_df = np.transpose(DAL_qb_df.loc[[('Passing', 'Cmp'), ('Passing', 'Att'), ('Passing', 'TD')], :])
DAL_qb_df = np.transpose(DAL_qb_df.loc[0])
DAL_qb_final_sum = (0.4 * np.sum(DAL_qb_df[('Passing', 'Att')] - DAL_qb_df[('Passing', 'Cmp')])) + (0.6 * DAL_qb_df[('Passing', 'TD')])

 # RB - Offence
DAL_rb_df = pd.DataFrame(DAL_raw_df[0])
DAL_rb_df = np.transpose(pd.DataFrame(DAL_rb_df))
DAL_rb_df = np.transpose(DAL_rb_df.loc[[('Rushing', 'Y/A'), ('Rushing', 'TD')], :])
DAL_rb_df = np.transpose(DAL_rb_df.loc[0])
DAL_rb_final_sum = np.sum( (0.4 * DAL_rb_df.loc[('Rushing', 'Y/A')] ) + (0.6 * DAL_rb_df.loc[('Rushing', 'TD')] ) )

 # Defense
DAL_def = pd.DataFrame(DAL_raw_df[1])
DAL_def = np.transpose(pd.DataFrame(DAL_def))
DAL_def = np.transpose(DAL_def.loc[[('Defense', 'PassY'), ('Defense', 'RushY')], :])
DAL_def = np.transpose(DAL_def.loc[0])
DAL_def_final_sum = np.sum( (0.5 * DAL_def.loc[('Defense', 'PassY')] ) + (0.5 * DAL_def.loc[('Defense', 'RushY')] ) )

# PHILIDELPHIA EAGLES
    # QB - Offence
PHI_raw_df = pd.read_html('https://www.pro-football-reference.com/teams/phi/2021.htm#passing')
PHI_qb_df = pd.DataFrame(PHI_raw_df[0])
PHI_qb_df = np.transpose(pd.DataFrame(PHI_qb_df))
PHI_qb_df = np.transpose(PHI_qb_df.loc[[('Passing', 'Cmp'), ('Passing', 'Att'), ('Passing', 'TD')], :])
PHI_qb_df = np.transpose(PHI_qb_df.loc[0])
PHI_qb_final_sum = (0.4 * np.sum(PHI_qb_df[('Passing', 'Att')] - PHI_qb_df[('Passing', 'Cmp')])) + (0.6 * PHI_qb_df[('Passing', 'TD')])

 # RB - Offence
PHI_rb_df = pd.DataFrame(PHI_raw_df[0])
PHI_rb_df = np.transpose(pd.DataFrame(PHI_rb_df))
PHI_rb_df = np.transpose(PHI_rb_df.loc[[('Rushing', 'Y/A'), ('Rushing', 'TD')], :])
PHI_rb_df = np.transpose(PHI_rb_df.loc[0])
PHI_rb_final_sum = np.sum( (0.4 * PHI_rb_df.loc[('Rushing', 'Y/A')] ) + (0.6 * PHI_rb_df.loc[('Rushing', 'TD')] ) )

 # Defense
PHI_def = pd.DataFrame(PHI_raw_df[1])
PHI_def = np.transpose(pd.DataFrame(PHI_def))
PHI_def = np.transpose(PHI_def.loc[[('Defense', 'PassY'), ('Defense', 'RushY')], :])
PHI_def = np.transpose(PHI_def.loc[0])
PHI_def_final_sum = np.sum( (0.5 * PHI_def.loc[('Defense', 'PassY')] ) + (0.5 * PHI_def.loc[('Defense', 'RushY')] ) )

# NEW ORLEANS SAINTS
    # QB - Offence
NOR_raw_df = pd.read_html('https://www.pro-football-reference.com/teams/nor/2021.htm#passing')
NOR_qb_df = pd.DataFrame(NOR_raw_df[0])
NOR_qb_df = np.transpose(pd.DataFrame(NOR_qb_df))
NOR_qb_df = np.transpose(NOR_qb_df.loc[[('Passing', 'Cmp'), ('Passing', 'Att'), ('Passing', 'TD')], :])
NOR_qb_df = np.transpose(NOR_qb_df.loc[0])
NOR_qb_final_sum = (0.4 * np.sum(NOR_qb_df[('Passing', 'Att')] - NOR_qb_df[('Passing', 'Cmp')])) + (0.6 * NOR_qb_df[('Passing', 'TD')])

 # RB - Offence
NOR_rb_df = pd.DataFrame(NOR_raw_df[0])
NOR_rb_df = np.transpose(pd.DataFrame(NOR_rb_df))
NOR_rb_df = np.transpose(NOR_rb_df.loc[[('Rushing', 'Y/A'), ('Rushing', 'TD')], :])
NOR_rb_df = np.transpose(NOR_rb_df.loc[0])
NOR_rb_final_sum = np.sum( (0.4 * NOR_rb_df.loc[('Rushing', 'Y/A')] ) + (0.6 * NOR_rb_df.loc[('Rushing', 'TD')] ) )

 # Defense
NOR_def = pd.DataFrame(NOR_raw_df[1])
NOR_def = np.transpose(pd.DataFrame(NOR_def))
NOR_def = np.transpose(NOR_def.loc[[('Defense', 'PassY'), ('Defense', 'RushY')], :])
NOR_def = np.transpose(NOR_def.loc[0])
NOR_def_final_sum = np.sum( (0.5 * NOR_def.loc[('Defense', 'PassY')] ) + (0.5 * NOR_def.loc[('Defense', 'RushY')] ) )

# TAMPA BAY BUCCANEERS
    # QB - Offence
TBB_raw_df = pd.read_html('https://www.pro-football-reference.com/teams/tam/2021.htm#passing')
TBB_qb_df = pd.DataFrame(TBB_raw_df[0])
TBB_qb_df = np.transpose(pd.DataFrame(TBB_qb_df))
TBB_qb_df = np.transpose(TBB_qb_df.loc[[('Passing', 'Cmp'), ('Passing', 'Att'), ('Passing', 'TD')], :])
TBB_qb_df = np.transpose(TBB_qb_df.loc[0])
TBB_qb_final_sum = (0.4 * np.sum(TBB_qb_df[('Passing', 'Att')] - TBB_qb_df[('Passing', 'Cmp')])) + (0.6 * TBB_qb_df[('Passing', 'TD')])

 # RB - Offence
TBB_rb_df = pd.DataFrame(TBB_raw_df[0])
TBB_rb_df = np.transpose(pd.DataFrame(TBB_rb_df))
TBB_rb_df = np.transpose(TBB_rb_df.loc[[('Rushing', 'Y/A'), ('Rushing', 'TD')], :])
TBB_rb_df = np.transpose(TBB_rb_df.loc[0])
TBB_rb_final_sum = np.sum( (0.4 * TBB_rb_df.loc[('Rushing', 'Y/A')] ) + (0.6 * TBB_rb_df.loc[('Rushing', 'TD')] ) )

 # Defense
TBB_def = pd.DataFrame(TBB_raw_df[1])
TBB_def = np.transpose(pd.DataFrame(TBB_def))
TBB_def = np.transpose(TBB_def.loc[[('Defense', 'PassY'), ('Defense', 'RushY')], :])
TBB_def = np.transpose(TBB_def.loc[0])
TBB_def_final_sum = np.sum( (0.5 * TBB_def.loc[('Defense', 'PassY')] ) + (0.5 * TBB_def.loc[('Defense', 'RushY')] ) )

# CAROLINA PANTHERS
    # QB - Offence
CAR_raw_df = pd.read_html('https://www.pro-football-reference.com/teams/car/2021.htm#passing')
CAR_qb_df = pd.DataFrame(CAR_raw_df[0])
CAR_qb_df = np.transpose(pd.DataFrame(CAR_qb_df))
CAR_qb_df = np.transpose(CAR_qb_df.loc[[('Passing', 'Cmp'), ('Passing', 'Att'), ('Passing', 'TD')], :])
CAR_qb_df = np.transpose(CAR_qb_df.loc[0])
CAR_qb_final_sum = (0.4 * np.sum(CAR_qb_df[('Passing', 'Att')] - CAR_qb_df[('Passing', 'Cmp')])) + (0.6 * CAR_qb_df[('Passing', 'TD')])

 # RB - Offence
CAR_rb_df = pd.DataFrame(CAR_raw_df[0])
CAR_rb_df = np.transpose(pd.DataFrame(CAR_rb_df))
CAR_rb_df = np.transpose(CAR_rb_df.loc[[('Rushing', 'Y/A'), ('Rushing', 'TD')], :])
CAR_rb_df = np.transpose(CAR_rb_df.loc[0])
CAR_rb_final_sum = np.sum( (0.4 * CAR_rb_df.loc[('Rushing', 'Y/A')] ) + (0.6 * CAR_rb_df.loc[('Rushing', 'TD')] ) )

 # Defense
CAR_def = pd.DataFrame(CAR_raw_df[1])
CAR_def = np.transpose(pd.DataFrame(CAR_def))
CAR_def = np.transpose(CAR_def.loc[[('Defense', 'PassY'), ('Defense', 'RushY')], :])
CAR_def = np.transpose(CAR_def.loc[0])
CAR_def_final_sum = np.sum( (0.5 * CAR_def.loc[('Defense', 'PassY')] ) + (0.5 * CAR_def.loc[('Defense', 'RushY')] ) )

# ATLANTA FALCONS
    # QB - Offence
ATL_raw_df = pd.read_html('https://www.pro-football-reference.com/teams/atl/2021.htm#passing')
ATL_qb_df = pd.DataFrame(ATL_raw_df[0])
ATL_qb_df = np.transpose(pd.DataFrame(ATL_qb_df))
ATL_qb_df = np.transpose(ATL_qb_df.loc[[('Passing', 'Cmp'), ('Passing', 'Att'), ('Passing', 'TD')], :])
ATL_qb_df = np.transpose(ATL_qb_df.loc[0])
ATL_qb_final_sum = (0.4 * np.sum(ATL_qb_df[('Passing', 'Att')] - ATL_qb_df[('Passing', 'Cmp')])) + (0.6 * ATL_qb_df[('Passing', 'TD')])

 # RB - Offence
ATL_rb_df = pd.DataFrame(ATL_raw_df[0])
ATL_rb_df = np.transpose(pd.DataFrame(ATL_rb_df))
ATL_rb_df = np.transpose(ATL_rb_df.loc[[('Rushing', 'Y/A'), ('Rushing', 'TD')], :])
ATL_rb_df = np.transpose(ATL_rb_df.loc[0])
ATL_rb_final_sum = np.sum( (0.4 * ATL_rb_df.loc[('Rushing', 'Y/A')] ) + (0.6 * ATL_rb_df.loc[('Rushing', 'TD')] ) )

 # Defense
ATL_def = pd.DataFrame(ATL_raw_df[1])
ATL_def = np.transpose(pd.DataFrame(ATL_def))
ATL_def = np.transpose(ATL_def.loc[[('Defense', 'PassY'), ('Defense', 'RushY')], :])
ATL_def = np.transpose(ATL_def.loc[0])
ATL_def_final_sum = np.sum( (0.5 * ATL_def.loc[('Defense', 'PassY')] ) + (0.5 * ATL_def.loc[('Defense', 'RushY')] ) )

# GREEN BAY PACKERS
    # QB - Offence
GNB_raw_df = pd.read_html('https://www.pro-football-reference.com/teams/gnb/2021.htm#passing')
GNB_qb_df = pd.DataFrame(GNB_raw_df[0])
GNB_qb_df = np.transpose(pd.DataFrame(GNB_qb_df))
GNB_qb_df = np.transpose(GNB_qb_df.loc[[('Passing', 'Cmp'), ('Passing', 'Att'), ('Passing', 'TD')], :])
GNB_qb_df = np.transpose(GNB_qb_df.loc[0])
GNB_qb_final_sum = (0.4 * np.sum(GNB_qb_df[('Passing', 'Att')] - GNB_qb_df[('Passing', 'Cmp')])) + (0.6 * GNB_qb_df[('Passing', 'TD')])

 # RB - Offence
GNB_rb_df = pd.DataFrame(GNB_raw_df[0])
GNB_rb_df = np.transpose(pd.DataFrame(GNB_rb_df))
GNB_rb_df = np.transpose(GNB_rb_df.loc[[('Rushing', 'Y/A'), ('Rushing', 'TD')], :])
GNB_rb_df = np.transpose(GNB_rb_df.loc[0])
GNB_rb_final_sum = np.sum( (0.4 * GNB_rb_df.loc[('Rushing', 'Y/A')] ) + (0.6 * GNB_rb_df.loc[('Rushing', 'TD')] ) )

 # Defense
GNB_def = pd.DataFrame(GNB_raw_df[1])
GNB_def = np.transpose(pd.DataFrame(GNB_def))
GNB_def = np.transpose(GNB_def.loc[[('Defense', 'PassY'), ('Defense', 'RushY')], :])
GNB_def = np.transpose(GNB_def.loc[0])
GNB_def_final_sum = np.sum( (0.5 * GNB_def.loc[('Defense', 'PassY')] ) + (0.5 * GNB_def.loc[('Defense', 'RushY')] ) )

# CHICAGO BEARS
    # QB - Offence
CHI_raw_df = pd.read_html('https://www.pro-football-reference.com/teams/chi/2021.htm#passing')
CHI_qb_df = pd.DataFrame(CHI_raw_df[0])
CHI_qb_df = np.transpose(pd.DataFrame(CHI_qb_df))
CHI_qb_df = np.transpose(CHI_qb_df.loc[[('Passing', 'Cmp'), ('Passing', 'Att'), ('Passing', 'TD')], :])
CHI_qb_df = np.transpose(CHI_qb_df.loc[0])
CHI_qb_final_sum = (0.4 * np.sum(CHI_qb_df[('Passing', 'Att')] - CHI_qb_df[('Passing', 'Cmp')])) + (0.6 * CHI_qb_df[('Passing', 'TD')])

 # RB - Offence
CHI_rb_df = pd.DataFrame(CHI_raw_df[0])
CHI_rb_df = np.transpose(pd.DataFrame(CHI_rb_df))
CHI_rb_df = np.transpose(CHI_rb_df.loc[[('Rushing', 'Y/A'), ('Rushing', 'TD')], :])
CHI_rb_df = np.transpose(CHI_rb_df.loc[0])
CHI_rb_final_sum = np.sum( (0.4 * CHI_rb_df.loc[('Rushing', 'Y/A')] ) + (0.6 * CHI_rb_df.loc[('Rushing', 'TD')] ) )

 # Defense
CHI_def = pd.DataFrame(CHI_raw_df[1])
CHI_def = np.transpose(pd.DataFrame(CHI_def))
CHI_def = np.transpose(CHI_def.loc[[('Defense', 'PassY'), ('Defense', 'RushY')], :])
CHI_def = np.transpose(CHI_def.loc[0])
CHI_def_final_sum = np.sum( (0.5 * CHI_def.loc[('Defense', 'PassY')] ) + (0.5 * CHI_def.loc[('Defense', 'RushY')] ) )

# MINNESOTA VIKINGS
    # QB - Offence
MIN_raw_df = pd.read_html('https://www.pro-football-reference.com/teams/min/2021.htm#passing')
MIN_qb_df = pd.DataFrame(MIN_raw_df[0])
MIN_qb_df = np.transpose(pd.DataFrame(MIN_qb_df))
MIN_qb_df = np.transpose(MIN_qb_df.loc[[('Passing', 'Cmp'), ('Passing', 'Att'), ('Passing', 'TD')], :])
MIN_qb_df = np.transpose(MIN_qb_df.loc[0])
MIN_qb_final_sum = (0.4 * np.sum(MIN_qb_df[('Passing', 'Att')] - MIN_qb_df[('Passing', 'Cmp')])) + (0.6 * MIN_qb_df[('Passing', 'TD')])

 # RB - Offence
MIN_rb_df = pd.DataFrame(MIN_raw_df[0])
MIN_rb_df = np.transpose(pd.DataFrame(MIN_rb_df))
MIN_rb_df = np.transpose(MIN_rb_df.loc[[('Rushing', 'Y/A'), ('Rushing', 'TD')], :])
MIN_rb_df = np.transpose(MIN_rb_df.loc[0])
MIN_rb_final_sum = np.sum( (0.4 * MIN_rb_df.loc[('Rushing', 'Y/A')] ) + (0.6 * MIN_rb_df.loc[('Rushing', 'TD')] ) )

 # Defense
MIN_def = pd.DataFrame(MIN_raw_df[1])
MIN_def = np.transpose(pd.DataFrame(MIN_def))
MIN_def = np.transpose(MIN_def.loc[[('Defense', 'PassY'), ('Defense', 'RushY')], :])
MIN_def = np.transpose(MIN_def.loc[0])
MIN_def_final_sum = np.sum( (0.5 * MIN_def.loc[('Defense', 'PassY')] ) + (0.5 * MIN_def.loc[('Defense', 'RushY')] ) )

# DETROIT LIONS
    # QB - Offence
DET_raw_df = pd.read_html('https://www.pro-football-reference.com/teams/det/2021.htm#passing')
DET_qb_df = pd.DataFrame(DET_raw_df[0])
DET_qb_df = np.transpose(pd.DataFrame(DET_qb_df))
DET_qb_df = np.transpose(DET_qb_df.loc[[('Passing', 'Cmp'), ('Passing', 'Att'), ('Passing', 'TD')], :])
DET_qb_df = np.transpose(DET_qb_df.loc[0])
DET_qb_final_sum = (0.4 * np.sum(DET_qb_df[('Passing', 'Att')] - DET_qb_df[('Passing', 'Cmp')])) + (0.6 * DET_qb_df[('Passing', 'TD')])

 # RB - Offence
DET_rb_df = pd.DataFrame(DET_raw_df[0])
DET_rb_df = np.transpose(pd.DataFrame(DET_rb_df))
DET_rb_df = np.transpose(DET_rb_df.loc[[('Rushing', 'Y/A'), ('Rushing', 'TD')], :])
DET_rb_df = np.transpose(DET_rb_df.loc[0])
DET_rb_final_sum = np.sum( (0.4 * DET_rb_df.loc[('Rushing', 'Y/A')] ) + (0.6 * DET_rb_df.loc[('Rushing', 'TD')] ) )

 # Defense
DET_def = pd.DataFrame(DET_raw_df[1])
DET_def = np.transpose(pd.DataFrame(DET_def))
DET_def = np.transpose(DET_def.loc[[('Defense', 'PassY'), ('Defense', 'RushY')], :])
DET_def = np.transpose(DET_def.loc[0])
DET_def_final_sum = np.sum( (0.5 * DET_def.loc[('Defense', 'PassY')] ) + (0.5 * DET_def.loc[('Defense', 'RushY')] ) )

# SEATTLE SEAHAWKS
    # QB - Offence
SEA_raw_df = pd.read_html('https://www.pro-football-reference.com/teams/sea/2021.htm#passing')
SEA_qb_df = pd.DataFrame(SEA_raw_df[0])
SEA_qb_df = np.transpose(pd.DataFrame(SEA_qb_df))
SEA_qb_df = np.transpose(SEA_qb_df.loc[[('Passing', 'Cmp'), ('Passing', 'Att'), ('Passing', 'TD')], :])
SEA_qb_df = np.transpose(SEA_qb_df.loc[0])
SEA_qb_final_sum = (0.4 * np.sum(SEA_qb_df[('Passing', 'Att')] - SEA_qb_df[('Passing', 'Cmp')])) + (0.6 * SEA_qb_df[('Passing', 'TD')])

 # RB - Offence
SEA_rb_df = pd.DataFrame(SEA_raw_df[0])
SEA_rb_df = np.transpose(pd.DataFrame(SEA_rb_df))
SEA_rb_df = np.transpose(SEA_rb_df.loc[[('Rushing', 'Y/A'), ('Rushing', 'TD')], :])
SEA_rb_df = np.transpose(SEA_rb_df.loc[0])
SEA_rb_final_sum = np.sum( (0.4 * SEA_rb_df.loc[('Rushing', 'Y/A')] ) + (0.6 * SEA_rb_df.loc[('Rushing', 'TD')] ) )

 # Defense
SEA_def = pd.DataFrame(SEA_raw_df[1])
SEA_def = np.transpose(pd.DataFrame(SEA_def))
SEA_def = np.transpose(SEA_def.loc[[('Defense', 'PassY'), ('Defense', 'RushY')], :])
SEA_def = np.transpose(SEA_def.loc[0])
SEA_def_final_sum = np.sum( (0.5 * SEA_def.loc[('Defense', 'PassY')] ) + (0.5 * SEA_def.loc[('Defense', 'RushY')] ) )

# LOS ANGELES RAMS
    # QB - Offence
LAR_raw_df = pd.read_html('https://www.pro-football-reference.com/teams/ram/2021.htm#passing')
LAR_qb_df = pd.DataFrame(LAR_raw_df[0])
LAR_qb_df = np.transpose(pd.DataFrame(LAR_qb_df))
LAR_qb_df = np.transpose(LAR_qb_df.loc[[('Passing', 'Cmp'), ('Passing', 'Att'), ('Passing', 'TD')], :])
LAR_qb_df = np.transpose(LAR_qb_df.loc[0])
LAR_qb_final_sum = (0.4 * np.sum(LAR_qb_df[('Passing', 'Att')] - LAR_qb_df[('Passing', 'Cmp')])) + (0.6 * LAR_qb_df[('Passing', 'TD')])

 # RB - Offence
LAR_rb_df = pd.DataFrame(LAR_raw_df[0])
LAR_rb_df = np.transpose(pd.DataFrame(LAR_rb_df))
LAR_rb_df = np.transpose(LAR_rb_df.loc[[('Rushing', 'Y/A'), ('Rushing', 'TD')], :])
LAR_rb_df = np.transpose(LAR_rb_df.loc[0])
LAR_rb_final_sum = np.sum( (0.4 * LAR_rb_df.loc[('Rushing', 'Y/A')] ) + (0.6 * LAR_rb_df.loc[('Rushing', 'TD')] ) )

 # Defense
LAR_def = pd.DataFrame(LAR_raw_df[1])
LAR_def = np.transpose(pd.DataFrame(LAR_def))
LAR_def = np.transpose(LAR_def.loc[[('Defense', 'PassY'), ('Defense', 'RushY')], :])
LAR_def = np.transpose(LAR_def.loc[0])
LAR_def_final_sum = np.sum( (0.5 * LAR_def.loc[('Defense', 'PassY')] ) + (0.5 * LAR_def.loc[('Defense', 'RushY')] ) )

# ARIZONA CARDINALS
    # QB - Offence
ARI_raw_df = pd.read_html('https://www.pro-football-reference.com/teams/ram/2021.htm#passing')
ARI_qb_df = pd.DataFrame(ARI_raw_df[0])
ARI_qb_df = np.transpose(pd.DataFrame(ARI_qb_df))
ARI_qb_df = np.transpose(ARI_qb_df.loc[[('Passing', 'Cmp'), ('Passing', 'Att'), ('Passing', 'TD')], :])
ARI_qb_df = np.transpose(ARI_qb_df.loc[0])
ARI_qb_final_sum = (0.4 * np.sum(ARI_qb_df[('Passing', 'Att')] - ARI_qb_df[('Passing', 'Cmp')])) + (0.6 * ARI_qb_df[('Passing', 'TD')])

 # RB - Offence
ARI_rb_df = pd.DataFrame(ARI_raw_df[0])
ARI_rb_df = np.transpose(pd.DataFrame(ARI_rb_df))
ARI_rb_df = np.transpose(ARI_rb_df.loc[[('Rushing', 'Y/A'), ('Rushing', 'TD')], :])
ARI_rb_df = np.transpose(ARI_rb_df.loc[0])
ARI_rb_final_sum = np.sum( (0.4 * ARI_rb_df.loc[('Rushing', 'Y/A')] ) + (0.6 * ARI_rb_df.loc[('Rushing', 'TD')] ) )

 # Defense
ARI_def = pd.DataFrame(ARI_raw_df[1])
ARI_def = np.transpose(pd.DataFrame(ARI_def))
ARI_def = np.transpose(ARI_def.loc[[('Defense', 'PassY'), ('Defense', 'RushY')], :])
ARI_def = np.transpose(ARI_def.loc[0])
ARI_def_final_sum = np.sum( (0.5 * ARI_def.loc[('Defense', 'PassY')] ) + (0.5 * ARI_def.loc[('Defense', 'RushY')] ) )


# SAN FRANCISCO 49ERS
    # QB - Offence
SFO_raw_df = pd.read_html('https://www.pro-football-reference.com/teams/sfo/2021.htm#passing')
SFO_qb_df = pd.DataFrame(SFO_raw_df[0])
SFO_qb_df = np.transpose(pd.DataFrame(SFO_qb_df))
SFO_qb_df = np.transpose(SFO_qb_df.loc[[('Passing', 'Cmp'), ('Passing', 'Att'), ('Passing', 'TD')], :])
SFO_qb_df = np.transpose(SFO_qb_df.loc[0])
SFO_qb_final_sum = (0.4 * np.sum(SFO_qb_df[('Passing', 'Att')] - SFO_qb_df[('Passing', 'Cmp')])) + (0.6 * SFO_qb_df[('Passing', 'TD')])

 # RB - Offence
SFO_rb_df = pd.DataFrame(SFO_raw_df[0])
SFO_rb_df = np.transpose(pd.DataFrame(SFO_rb_df))
SFO_rb_df = np.transpose(SFO_rb_df.loc[[('Rushing', 'Y/A'), ('Rushing', 'TD')], :])
SFO_rb_df = np.transpose(SFO_rb_df.loc[0])
SFO_rb_final_sum = np.sum( (0.4 * SFO_rb_df.loc[('Rushing', 'Y/A')] ) + (0.6 * SFO_rb_df.loc[('Rushing', 'TD')] ) )

 # Defense
SFO_def = pd.DataFrame(SFO_raw_df[1])
SFO_def = np.transpose(pd.DataFrame(SFO_def))
SFO_def = np.transpose(SFO_def.loc[[('Defense', 'PassY'), ('Defense', 'RushY')], :])
SFO_def = np.transpose(SFO_def.loc[0])
SFO_def_final_sum = np.sum( (0.5 * SFO_def.loc[('Defense', 'PassY')] ) + (0.5 * SFO_def.loc[('Defense', 'RushY')] ) )

# Appended qb_dfs
Appended_qb_df = np.transpose(pd.concat([ ARI_qb_df, ATL_qb_df, BUF_qb_df, MIA_qb_df, NWE_qb_df,
                                          NYJ_qb_df, TEN_qb_df, IND_qb_df, HOU_qb_df, JAX_qb_df,
                                          PIT_qb_df, BAL_qb_df, CLE_qb_df, CIN_qb_df, KAN_qb_df,
                                          LVR_qb_df, LAC_qb_df, DEN_qb_df, WSH_qb_df, NYG_qb_df,
                                          DAL_qb_df, PHI_qb_df, NOR_qb_df, TBB_qb_df, CAR_qb_df,
                                          GNB_qb_df, CHI_qb_df, MIN_qb_df, DET_qb_df, SEA_qb_df,
                                          LAR_qb_df, SFO_qb_df], axis = 1))

Appended_rb_df = np.transpose(pd.concat([ ARI_rb_df, ATL_rb_df, BUF_rb_df, MIA_rb_df, NWE_rb_df,
                                          NYJ_rb_df, TEN_rb_df, IND_rb_df, HOU_rb_df, JAX_rb_df,
                                          PIT_rb_df, BAL_rb_df, CLE_rb_df, CIN_rb_df, KAN_rb_df,
                                          LVR_rb_df, LAC_rb_df, DEN_rb_df, WSH_rb_df, NYG_rb_df,
                                          DAL_rb_df, PHI_rb_df, NOR_rb_df, TBB_rb_df, CAR_rb_df,
                                          GNB_rb_df, CHI_rb_df, MIN_rb_df, DET_rb_df, SEA_rb_df,
                                          LAR_rb_df, SFO_rb_df], axis = 1))

Appended_def_df = np.transpose(pd.concat([ ARI_def, ATL_def, BUF_def, MIA_def, NWE_def,
                                           NYJ_def, TEN_def, IND_def, HOU_def, JAX_def,
                                           PIT_def, BAL_def, CLE_def, CIN_def, KAN_def,
                                           LVR_def, LAC_def, DEN_def, WSH_def, NYG_def,
                                           DAL_def, PHI_def, NOR_def, TBB_def, CAR_def,
                                           GNB_def, CHI_def, MIN_def, DET_def, SEA_def,
                                           LAR_def, SFO_def], axis = 1))

