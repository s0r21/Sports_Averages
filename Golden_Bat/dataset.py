# This script is to import the data

from packages import pd

# NOTE: Make sure to find (crtl+f) and replace 2021 with 2022 when the season starts.

# Arizona
ARI_batting = pd.read_html('https://www.baseball-reference.com/teams/ARI/2021.shtml#team_batting')
ARI_batting_df = pd.DataFrame(ARI_batting[(len(ARI_batting)-2)])
ARI_batting_df = ARI_batting_df.loc[0:12, ['R', 'H', '2B', '3B', 'RBI', 'SB']]
ARI_batting_df = ARI_batting_df.drop(labels = range(21,len(ARI_batting_df)),
                                     axis = 0)
ARI_batting_df = ARI_batting_df.loc[(ARI_batting_df['R'] != 'R')]

ARI_pitching = pd.read_html('https://www.baseball-reference.com/teams/ARI/2021.shtml#team_pitching')
ARI_pitching_df = pd.DataFrame(ARI_pitching[(len(ARI_batting)-1)])
ARI_pitching_df = ARI_pitching_df.loc[0:12, ['R', 'H', 'ER', 'HR', 'BB', 'SO']]
ARI_pitching_df = ARI_pitching_df.drop(labels = range(21,len(ARI_pitching_df)),
                                       axis = 0)
ARI_pitching_df = ARI_pitching_df.loc[(ARI_pitching_df['H'] != 'H')]

# Tampa Bay
TBR_batting = pd.read_html('https://www.baseball-reference.com/teams/TBR/2021.shtml#team_batting')
TBR_batting_df = pd.DataFrame(TBR_batting[(len(TBR_batting)-2)])
TBR_batting_df = TBR_batting_df.loc[0:12, ['R', 'H', '2B', '3B', 'RBI', 'SB']]
TBR_batting_df = TBR_batting_df.drop(labels = range(21,len(TBR_batting_df)),
                                     axis = 0)
TBR_batting_df = TBR_batting_df.loc[(TBR_batting_df['R'] != 'R')]

TBR_pitching = pd.read_html('https://www.baseball-reference.com/teams/TBR/2021.shtml#team_pitching')
TBR_pitching_df = pd.DataFrame(TBR_pitching[len(TBR_pitching)-1])
TBR_pitching_df = TBR_pitching_df.loc[0:12, ['R', 'H', 'ER', 'HR', 'BB', 'SO']]
TBR_pitching_df = TBR_pitching_df.drop(labels = range(21,len(TBR_pitching_df)),
                                       axis = 0)
TBR_pitching_df = TBR_pitching_df.loc[(TBR_pitching_df['H'] != 'H')]

# Houston
HOU_batting = pd.read_html('https://www.baseball-reference.com/teams/HOU/2021.shtml#team_batting')
HOU_batting_df = pd.DataFrame(HOU_batting[(len(HOU_batting)-2)])
HOU_batting_df = HOU_batting_df.loc[0:12, ['R', 'H', '2B', '3B', 'RBI', 'SB']]
HOU_batting_df = HOU_batting_df.drop(labels = range(21,len(HOU_batting_df)),
                                     axis = 0)
HOU_batting_df = HOU_batting_df.loc[(HOU_batting_df['R'] != 'R')]

HOU_pitching = pd.read_html('https://www.baseball-reference.com/teams/HOU/2021.shtml#team_pitching')
HOU_pitching_df = pd.DataFrame(HOU_pitching[len(HOU_pitching)-1])
HOU_pitching_df = HOU_pitching_df.loc[0:12, ['R', 'H', 'ER', 'HR', 'BB', 'SO']]
HOU_pitching_df = HOU_pitching_df.drop(labels = range(21,len(HOU_pitching_df)),
                                       axis = 0)
HOU_pitching_df = HOU_pitching_df.loc[(HOU_pitching_df['H'] != 'H')]

# NY Yankees
NYY_batting = pd.read_html('https://www.baseball-reference.com/teams/NYY/2021.shtml#team_batting')
NYY_batting_df = pd.DataFrame(NYY_batting[(len(NYY_batting)-2)])
NYY_batting_df = NYY_batting_df.loc[0:12, ['R', 'H', '2B', '3B', 'RBI', 'SB']]
NYY_batting_df = NYY_batting_df.drop(labels = range(21,len(NYY_batting_df)),
                                     axis = 0)
NYY_batting_df = NYY_batting_df.loc[(NYY_batting_df['R'] != 'R')]

NYY_pitching = pd.read_html('https://www.baseball-reference.com/teams/NYY/2021.shtml#team_pitching')
NYY_pitching_df = pd.DataFrame(NYY_pitching[len(NYY_pitching)-1])
NYY_pitching_df = NYY_pitching_df.loc[0:12, ['R', 'H', 'ER', 'HR', 'BB', 'SO']]
NYY_pitching_df = NYY_pitching_df.drop(labels = range(21,len(NYY_pitching_df)),
                                       axis = 0)
NYY_pitching_df = NYY_pitching_df.loc[(NYY_pitching_df['H'] != 'H')]

# Chi White Sox
CHW_batting = pd.read_html('https://www.baseball-reference.com/teams/CHW/2021.shtml#team_batting')
CHW_batting_df = pd.DataFrame(CHW_batting[(len(CHW_batting)-2)])
CHW_batting_df = CHW_batting_df.loc[0:12, ['R', 'H', '2B', '3B', 'RBI', 'SB']]
CHW_batting_df = CHW_batting_df.drop(labels = range(21,len(CHW_batting_df)),
                                     axis = 0)
CHW_batting_df = CHW_batting_df.loc[(CHW_batting_df['R'] != 'R')]

CHW_pitching = pd.read_html('https://www.baseball-reference.com/teams/CHW/2021.shtml#team_pitching')
CHW_pitching_df = pd.DataFrame(CHW_pitching[len(CHW_pitching)-1])
CHW_pitching_df = CHW_pitching_df.loc[0:12, ['R', 'H', 'ER', 'HR', 'BB', 'SO']]
CHW_pitching_df = CHW_pitching_df.drop(labels = range(21,len(CHW_pitching_df)),
                                       axis = 0)
CHW_pitching_df = CHW_pitching_df.loc[(CHW_pitching_df['H'] != 'H')]

# Boston
BOS_batting = pd.read_html('https://www.baseball-reference.com/teams/BOS/2021.shtml#team_batting')
BOS_batting_df = pd.DataFrame(BOS_batting[(len(BOS_batting)-2)])
BOS_batting_df = BOS_batting_df.loc[0:12, ['R', 'H', '2B', '3B', 'RBI', 'SB']]
BOS_batting_df = BOS_batting_df.drop(labels = range(21,len(BOS_batting_df)),
                                     axis = 0)
BOS_batting_df = BOS_batting_df.loc[(BOS_batting_df['R'] != 'R')]

BOS_pitching = pd.read_html('https://www.baseball-reference.com/teams/BOS/2021.shtml#team_pitching')
BOS_pitching_df = pd.DataFrame(BOS_pitching[len(BOS_pitching)-1])
BOS_pitching_df = BOS_pitching_df.loc[0:12, ['R', 'H', 'ER', 'HR', 'BB', 'SO']]
BOS_pitching_df = BOS_pitching_df.drop(labels = range(21,len(BOS_pitching_df)),
                                       axis = 0)
BOS_pitching_df = BOS_pitching_df.loc[(BOS_pitching_df['H'] != 'H')]

# Oakland
OAK_batting = pd.read_html('https://www.baseball-reference.com/teams/OAK/2021.shtml#team_batting')
OAK_batting_df = pd.DataFrame(OAK_batting[(len(OAK_batting)-2)])
OAK_batting_df = OAK_batting_df.loc[0:12, ['R', 'H', '2B', '3B', 'RBI', 'SB']]
OAK_batting_df = OAK_batting_df.drop(labels = range(21,len(OAK_batting_df)),
                                     axis = 0)
OAK_batting_df = OAK_batting_df.loc[(OAK_batting_df['R'] != 'R')]

OAK_pitching = pd.read_html('https://www.baseball-reference.com/teams/OAK/2021.shtml#team_pitching')
OAK_pitching_df = pd.DataFrame(OAK_pitching[len(OAK_pitching)-1])
OAK_pitching_df = OAK_pitching_df.loc[0:12, ['R', 'H', 'ER', 'HR', 'BB', 'SO']]
OAK_pitching_df = OAK_pitching_df.drop(labels = range(21,len(OAK_pitching_df)),
                                       axis = 0)
OAK_pitching_df = OAK_pitching_df.loc[(OAK_pitching_df['H'] != 'H')]

# Seattle
SEA_batting = pd.read_html('https://www.baseball-reference.com/teams/SEA/2021.shtml#team_batting')
SEA_batting_df = pd.DataFrame(SEA_batting[(len(SEA_batting)-2)])
SEA_batting_df = SEA_batting_df.loc[0:12, ['R', 'H', '2B', '3B', 'RBI', 'SB']]
SEA_batting_df = SEA_batting_df.drop(labels = range(21,len(SEA_batting_df)),
                                     axis = 0)
SEA_batting_df = SEA_batting_df.loc[(SEA_batting_df['R'] != 'R')]

SEA_pitching = pd.read_html('https://www.baseball-reference.com/teams/SEA/2021.shtml#team_pitching')
SEA_pitching_df = pd.DataFrame(SEA_pitching[len(SEA_pitching)-1])
SEA_pitching_df = SEA_pitching_df.loc[0:12, ['R', 'H', 'ER', 'HR', 'BB', 'SO']]
SEA_pitching_df = SEA_pitching_df.drop(labels = range(21,len(SEA_pitching_df)),
                                       axis = 0)
SEA_pitching_df = SEA_pitching_df.loc[(SEA_pitching_df['H'] != 'H')]

# Toronto
TOR_batting = pd.read_html('https://www.baseball-reference.com/teams/TOR/2021.shtml#team_batting')
TOR_batting_df = pd.DataFrame(TOR_batting[(len(TOR_batting)-2)])
TOR_batting_df = TOR_batting_df.loc[0:12, ['R', 'H', '2B', '3B', 'RBI', 'SB']]
TOR_batting_df = TOR_batting_df.drop(labels = range(21,len(TOR_batting_df)),
                                     axis = 0)
TOR_batting_df = TOR_batting_df.loc[(TOR_batting_df['R'] != 'R')]

TOR_pitching = pd.read_html('https://www.baseball-reference.com/teams/TOR/2021.shtml#team_pitching')
TOR_pitching_df = pd.DataFrame(TOR_pitching[len(TOR_pitching)-1])
TOR_pitching_df = TOR_pitching_df.loc[0:12, ['R', 'H', 'ER', 'HR', 'BB', 'SO']]
TOR_pitching_df = TOR_pitching_df.drop(labels = range(21,len(TOR_pitching_df)),
                                       axis = 0)
TOR_pitching_df = TOR_pitching_df.loc[(TOR_pitching_df['H'] != 'H')]

# Cleveland
CLE_batting = pd.read_html('https://www.baseball-reference.com/teams/CLE/2021.shtml#team_batting')
CLE_batting_df = pd.DataFrame(CLE_batting[(len(CLE_batting)-2)])
CLE_batting_df = CLE_batting_df.loc[0:12, ['R', 'H', '2B', '3B', 'RBI', 'SB']]
CLE_batting_df = CLE_batting_df.drop(labels = range(21,len(CLE_batting_df)),
                                     axis = 0)
CLE_batting_df = CLE_batting_df.loc[(CLE_batting_df['R'] != 'R')]

CLE_pitching = pd.read_html('https://www.baseball-reference.com/teams/CLE/2021.shtml#team_pitching')
CLE_pitching_df = pd.DataFrame(CLE_pitching[len(CLE_pitching)-1])
CLE_pitching_df = CLE_pitching_df.loc[0:12, ['R', 'H', 'ER', 'HR', 'BB', 'SO']]
CLE_pitching_df = CLE_pitching_df.drop(labels = range(21,len(CLE_pitching_df)),
                                       axis = 0)
CLE_pitching_df = CLE_pitching_df.loc[(CLE_pitching_df['H'] != 'H')]

#LA Angels
LAA_batting = pd.read_html('https://www.baseball-reference.com/teams/LAA/2021.shtml#team_batting')
LAA_batting_df = pd.DataFrame(LAA_batting[(len(LAA_batting)-2)])
LAA_batting_df = LAA_batting_df.loc[0:12, ['R', 'H', '2B', '3B', 'RBI', 'SB']]
LAA_batting_df = LAA_batting_df.drop(labels = range(21,len(LAA_batting_df)),
                                     axis = 0)
LAA_batting_df = LAA_batting_df.loc[(LAA_batting_df['R'] != 'R')]

LAA_pitching = pd.read_html('https://www.baseball-reference.com/teams/LAA/2021.shtml#team_pitching')
LAA_pitching_df = pd.DataFrame(LAA_pitching[len(LAA_pitching)-1])
LAA_pitching_df = LAA_pitching_df.loc[0:12, ['R', 'H', 'ER', 'HR', 'BB', 'SO']]
LAA_pitching_df = LAA_pitching_df.drop(labels = range(21,len(LAA_pitching_df)),
                                       axis = 0)
LAA_pitching_df = LAA_pitching_df.loc[(LAA_pitching_df['H'] != 'H')]

# Detroit
DET_batting = pd.read_html('https://www.baseball-reference.com/teams/DET/2021.shtml#team_batting')
DET_batting_df = pd.DataFrame(DET_batting[(len(DET_batting)-2)])
DET_batting_df = DET_batting_df.loc[0:12, ['R', 'H', '2B', '3B', 'RBI', 'SB']]
DET_batting_df = DET_batting_df.drop(labels = range(21,len(DET_batting_df)),
                                     axis = 0)
DET_batting_df = DET_batting_df.loc[(DET_batting_df['R'] != 'R')]


DET_pitching = pd.read_html('https://www.baseball-reference.com/teams/DET/2021.shtml#team_pitching')
DET_pitching_df = pd.DataFrame(DET_pitching[len(DET_pitching)-1])
DET_pitching_df = DET_pitching_df.loc[0:12, ['R', 'H', 'ER', 'HR', 'BB', 'SO']]
DET_pitching_df = DET_pitching_df.drop(labels = range(21,len(DET_pitching_df)),
                                       axis = 0)
DET_pitching_df = DET_pitching_df.loc[(DET_pitching_df['H'] != 'H')]

# Kansas City
KCR_batting = pd.read_html('https://www.baseball-reference.com/teams/KCR/2021.shtml#team_batting')
KCR_batting_df = pd.DataFrame(KCR_batting[(len(KCR_batting)-2)])
KCR_batting_df = KCR_batting_df.loc[0:12, ['R', 'H', '2B', '3B', 'RBI', 'SB']]
KCR_batting_df = KCR_batting_df.drop(labels = range(21,len(KCR_batting_df)),
                                     axis = 0)
KCR_batting_df = KCR_batting_df.loc[(KCR_batting_df['R'] != 'R')]


KCR_pitching = pd.read_html('https://www.baseball-reference.com/teams/KCR/2021.shtml#team_pitching')
KCR_pitching_df = pd.DataFrame(KCR_pitching[len(KCR_pitching)-1])
KCR_pitching_df = KCR_pitching_df.loc[0:12, ['R', 'H', 'ER', 'HR', 'BB', 'SO']]
KCR_pitching_df = KCR_pitching_df.drop(labels = range(21,len(KCR_pitching_df)),
                                       axis = 0)
KCR_pitching_df = KCR_pitching_df.loc[(KCR_pitching_df['H'] != 'H')]

# Minnesota
MIN_batting = pd.read_html('https://www.baseball-reference.com/teams/MIN/2021.shtml#team_batting')
MIN_batting_df = pd.DataFrame(MIN_batting[(len(MIN_batting)-2)])
MIN_batting_df = MIN_batting_df.loc[0:12, ['R', 'H', '2B', '3B', 'RBI', 'SB']]
MIN_batting_df = MIN_batting_df.drop(labels = range(21,len(MIN_batting_df)),
                                     axis = 0)
MIN_batting_df = MIN_batting_df.loc[(MIN_batting_df['R'] != 'R')]

MIN_pitching = pd.read_html('https://www.baseball-reference.com/teams/MIN/2021.shtml#team_pitching')
MIN_pitching_df = pd.DataFrame(MIN_pitching[len(MIN_pitching)-1])
MIN_pitching_df = MIN_pitching_df.loc[0:12, ['R', 'H', 'ER', 'HR', 'BB', 'SO']]
MIN_pitching_df = MIN_pitching_df.drop(labels = range(21,len(MIN_pitching_df)),
                                       axis = 0)
MIN_pitching_df = MIN_pitching_df.loc[(MIN_pitching_df['H'] != 'H')]

# Texas
TEX_batting = pd.read_html('https://www.baseball-reference.com/teams/TEX/2021.shtml#team_batting')
TEX_batting_df = pd.DataFrame(TEX_batting[(len(TEX_batting)-2)])
TEX_batting_df = TEX_batting_df.loc[0:12, ['R', 'H', '2B', '3B', 'RBI', 'SB']]
TEX_batting_df = TEX_batting_df.drop(labels = range(21,len(TEX_batting_df)),
                                     axis = 0)
TEX_batting_df = TEX_batting_df.loc[(TEX_batting_df['R'] != 'R')]

TEX_pitching = pd.read_html('https://www.baseball-reference.com/teams/TEX/2021.shtml#team_pitching')
TEX_pitching_df = pd.DataFrame(TEX_pitching[len(TEX_pitching)-1])
TEX_pitching_df = TEX_pitching_df.loc[0:12, ['R', 'H', 'ER', 'HR', 'BB', 'SO']]
TEX_pitching_df = TEX_pitching_df.drop(labels = range(21,len(TEX_pitching_df)),
                                       axis = 0)
TEX_pitching_df = TEX_pitching_df.loc[(TEX_pitching_df['H'] != 'H')]

# Baltimore
BAL_batting = pd.read_html('https://www.baseball-reference.com/teams/BAL/2021.shtml#team_batting')
BAL_batting_df = pd.DataFrame(BAL_batting[(len(BAL_batting)-2)])
BAL_batting_df = BAL_batting_df.loc[0:12, ['R', 'H', '2B', '3B', 'RBI', 'SB']]
BAL_batting_df = BAL_batting_df.drop(labels = range(21,len(BAL_batting_df)),
                                     axis = 0)
BAL_batting_df = BAL_batting_df.loc[(BAL_batting_df['R'] != 'R')]

BAL_pitching = pd.read_html('https://www.baseball-reference.com/teams/BAL/2021.shtml#team_pitching')
BAL_pitching_df = pd.DataFrame(BAL_pitching[len(BAL_pitching)-1])
BAL_pitching_df = BAL_pitching_df.loc[0:12, ['R', 'H', 'ER', 'HR', 'BB', 'SO']]
BAL_pitching_df = BAL_pitching_df.drop(labels = range(21,len(BAL_pitching_df)),
                                       axis = 0)
BAL_pitching_df = BAL_pitching_df.loc[(BAL_pitching_df['H'] != 'H')]

# SF Giants
SFG_batting = pd.read_html('https://www.baseball-reference.com/teams/SFG/2021.shtml#team_batting')
SFG_batting_df = pd.DataFrame(SFG_batting[(len(SFG_batting)-2)])
SFG_batting_df = SFG_batting_df.loc[0:12, ['R', 'H', '2B', '3B', 'RBI', 'SB']]
SFG_batting_df = SFG_batting_df.drop(labels = range(21,len(SFG_batting_df)),
                                     axis = 0)
SFG_batting_df = SFG_batting_df.loc[(SFG_batting_df['R'] != 'R')]

SFG_pitching = pd.read_html('https://www.baseball-reference.com/teams/SFG/2021.shtml#team_pitching')
SFG_pitching_df = pd.DataFrame(SFG_pitching[len(SFG_pitching)-1])
SFG_pitching_df = SFG_pitching_df.loc[0:12, ['R', 'H', 'ER', 'HR', 'BB', 'SO']]
SFG_pitching_df = SFG_pitching_df.drop(labels = range(21,len(SFG_pitching_df)),
                                       axis = 0)
SFG_pitching_df = SFG_pitching_df.loc[(SFG_pitching_df['H'] != 'H')]

# LA Dodgers
LAD_batting = pd.read_html('https://www.baseball-reference.com/teams/LAD/2021.shtml#team_batting')
LAD_batting_df = pd.DataFrame(LAD_batting[(len(LAD_batting)-2)])
LAD_batting_df = LAD_batting_df.loc[0:12, ['R', 'H', '2B', '3B', 'RBI', 'SB']]
LAD_batting_df = LAD_batting_df.drop(labels = range(21,len(LAD_batting_df)),
                                     axis = 0)
LAD_batting_df = LAD_batting_df.loc[(LAD_batting_df['R'] != 'R')]

LAD_pitching = pd.read_html('https://www.baseball-reference.com/teams/LAD/2021.shtml#team_pitching')
LAD_pitching_df = pd.DataFrame(LAD_pitching[len(LAD_pitching)-1])
LAD_pitching_df = LAD_pitching_df.loc[0:12, ['R', 'H', 'ER', 'HR', 'BB', 'SO']]
LAD_pitching_df = LAD_pitching_df.drop(labels = range(21,len(LAD_pitching_df)),
                                       axis = 0)
LAD_pitching_df = LAD_pitching_df.loc[(LAD_pitching_df['H'] != 'H')]

# Milwauke
MIL_batting = pd.read_html('https://www.baseball-reference.com/teams/MIL/2021.shtml#team_batting')
MIL_batting_df = pd.DataFrame(MIL_batting[(len(MIL_batting)-2)])
MIL_batting_df = MIL_batting_df.loc[0:12, ['R', 'H', '2B', '3B', 'RBI', 'SB']]
MIL_batting_df = MIL_batting_df.drop(labels = range(21,len(MIL_batting_df)),
                                     axis = 0)
MIL_batting_df = MIL_batting_df.loc[(MIL_batting_df['R'] != 'R')]

MIL_pitching = pd.read_html('https://www.baseball-reference.com/teams/MIL/2021.shtml#team_pitching')
MIL_pitching_df = pd.DataFrame(MIL_pitching[len(MIL_pitching)-1])
MIL_pitching_df = MIL_pitching_df.loc[0:12, ['R', 'H', 'ER', 'HR', 'BB', 'SO']]
MIL_pitching_df = MIL_pitching_df.drop(labels = range(21,len(MIL_pitching_df)),
                                       axis = 0)
MIL_pitching_df = MIL_pitching_df.loc[(MIL_pitching_df['H'] != 'H')]

# Cincinnati
CIN_batting = pd.read_html('https://www.baseball-reference.com/teams/CIN/2021.shtml#team_batting')
CIN_batting_df = pd.DataFrame(CIN_batting[(len(CIN_batting)-2)])
CIN_batting_df = CIN_batting_df.loc[0:12, ['R', 'H', '2B', '3B', 'RBI', 'SB']]
CIN_batting_df = CIN_batting_df.drop(labels = range(21,len(CIN_batting_df)),
                                     axis = 0)
CIN_batting_df = CIN_batting_df.loc[(CIN_batting_df['R'] != 'R')]

CIN_pitching = pd.read_html('https://www.baseball-reference.com/teams/CIN/2021.shtml#team_pitching')
CIN_pitching_df = pd.DataFrame(CIN_pitching[len(CIN_pitching)-1])
CIN_pitching_df = CIN_pitching_df.loc[0:12, ['R', 'H', 'ER', 'HR', 'BB', 'SO']]
CIN_pitching_df = CIN_pitching_df.drop(labels = range(21,len(CIN_pitching_df)),
                                       axis = 0)
CIN_pitching_df = CIN_pitching_df.loc[(CIN_pitching_df['H'] != 'H')]

# Atlanta
ATL_batting = pd.read_html('https://www.baseball-reference.com/teams/ATL/2021.shtml#team_batting')
ATL_batting_df = pd.DataFrame(ATL_batting[(len(ATL_batting)-2)])
ATL_batting_df = ATL_batting_df.loc[0:12, ['R', 'H', '2B', '3B', 'RBI', 'SB']]
ATL_batting_df = ATL_batting_df.drop(labels = range(21,len(ATL_batting_df)),
                                     axis = 0)
ATL_batting_df = ATL_batting_df.loc[(ATL_batting_df['R'] != 'R')]

ATL_pitching = pd.read_html('https://www.baseball-reference.com/teams/ATL/2021.shtml#team_pitching')
ATL_pitching_df = pd.DataFrame(ATL_pitching[len(ATL_pitching)-1])
ATL_pitching_df = ATL_pitching_df.loc[0:12, ['R', 'H', 'ER', 'HR', 'BB', 'SO']]
ATL_pitching_df = ATL_pitching_df.drop(labels = range(21,len(ATL_pitching_df)),
                                       axis = 0)
ATL_pitching_df = ATL_pitching_df.loc[(ATL_pitching_df['H'] != 'H')]

# San Diego
SDP_batting = pd.read_html('https://www.baseball-reference.com/teams/SDP/2021.shtml#team_batting')
SDP_batting_df = pd.DataFrame(SDP_batting[(len(SDP_batting)-2)])
SDP_batting_df = SDP_batting_df.loc[0:12, ['R', 'H', '2B', '3B', 'RBI', 'SB']]
SDP_batting_df = SDP_batting_df.drop(labels = range(21,len(SDP_batting_df)),
                                     axis = 0)
SDP_batting_df = SDP_batting_df.loc[(SDP_batting_df['R'] != 'R')]

SDP_pitching = pd.read_html('https://www.baseball-reference.com/teams/SDP/2021.shtml#team_pitching')
SDP_pitching_df = pd.DataFrame(SDP_pitching[len(SDP_pitching)-1])
SDP_pitching_df = SDP_pitching_df.loc[0:12, ['R', 'H', 'ER', 'HR', 'BB', 'SO']]
SDP_pitching_df = SDP_pitching_df.drop(labels = range(21,len(SDP_pitching_df)),
                                       axis = 0)
SDP_pitching_df = SDP_pitching_df.loc[(SDP_pitching_df['H'] != 'H')]

# St. Louis
STL_batting = pd.read_html('https://www.baseball-reference.com/teams/STL/2021.shtml#team_batting')
STL_batting_df = pd.DataFrame(STL_batting[(len(STL_batting)-2)])
STL_batting_df = STL_batting_df.loc[0:12, ['R', 'H', '2B', '3B', 'RBI', 'SB']]
STL_batting_df = STL_batting_df.drop(labels = range(21,len(STL_batting_df)),
                                     axis = 0)
STL_batting_df = STL_batting_df.loc[(STL_batting_df['R'] != 'R')]

STL_pitching = pd.read_html('https://www.baseball-reference.com/teams/STL/2021.shtml#team_pitching')
STL_pitching_df = pd.DataFrame(STL_pitching[len(STL_pitching)-1])
STL_pitching_df = STL_pitching_df.loc[0:12, ['R', 'H', 'ER', 'HR', 'BB', 'SO']]
STL_pitching_df = STL_pitching_df.drop(labels = range(21,len(STL_pitching_df)),
                                       axis = 0)
STL_pitching_df = STL_pitching_df.loc[(STL_pitching_df['H'] != 'H')]

# Philadelphia
PHI_batting = pd.read_html('https://www.baseball-reference.com/teams/PHI/2021.shtml#team_batting')
PHI_batting_df = pd.DataFrame(PHI_batting[(len(PHI_batting)-2)])
PHI_batting_df = PHI_batting_df.loc[0:12, ['R', 'H', '2B', '3B', 'RBI', 'SB']]
PHI_batting_df = PHI_batting_df.drop(labels = range(21,len(PHI_batting_df)),
                                     axis = 0)
PHI_batting_df = PHI_batting_df.loc[(PHI_batting_df['R'] != 'R')]

PHI_pitching = pd.read_html('https://www.baseball-reference.com/teams/PHI/2021.shtml#team_pitching')
PHI_pitching_df = pd.DataFrame(PHI_pitching[len(PHI_pitching)-1])
PHI_pitching_df = PHI_pitching_df.loc[0:12, ['R', 'H', 'ER', 'HR', 'BB', 'SO']]
PHI_pitching_df = PHI_pitching_df.drop(labels = range(21,len(PHI_pitching_df)),
                                       axis = 0)
PHI_pitching_df = PHI_pitching_df.loc[(PHI_pitching_df['H'] != 'H')]

# NY Mets
NYM_batting = pd.read_html('https://www.baseball-reference.com/teams/NYM/2021.shtml#team_batting')
NYM_batting_df = pd.DataFrame(NYM_batting[(len(NYM_batting)-2)])
NYM_batting_df = NYM_batting_df.loc[0:12, ['R', 'H', '2B', '3B', 'RBI', 'SB']]
NYM_batting_df = NYM_batting_df.drop(labels = range(21,len(NYM_batting_df)),
                                     axis = 0)
NYM_batting_df = NYM_batting_df.loc[(NYM_batting_df['R'] != 'R')]

NYM_pitching = pd.read_html('https://www.baseball-reference.com/teams/NYM/2021.shtml#team_pitching')
NYM_pitching_df = pd.DataFrame(NYM_pitching[len(NYM_pitching)-1])
NYM_pitching_df = NYM_pitching_df.loc[0:12, ['R', 'H', 'ER', 'HR', 'BB', 'SO']]
NYM_pitching_df = NYM_pitching_df.drop(labels = range(21,len(NYM_pitching_df)),
                                       axis = 0)
NYM_pitching_df = NYM_pitching_df.loc[(NYM_pitching_df['H'] != 'H')]

# Colorado
COL_batting = pd.read_html('https://www.baseball-reference.com/teams/COL/2021.shtml#team_batting')
COL_batting_df = pd.DataFrame(COL_batting[(len(COL_batting)-2)])
COL_batting_df = COL_batting_df.loc[0:12, ['R', 'H', '2B', '3B', 'RBI', 'SB']]
COL_batting_df = COL_batting_df.drop(labels = range(21,len(COL_batting_df)),
                                     axis = 0)
COL_batting_df = COL_batting_df.loc[(COL_batting_df['R'] != 'R')]

COL_pitching = pd.read_html('https://www.baseball-reference.com/teams/COL/2021.shtml#team_pitching')
COL_pitching_df = pd.DataFrame(COL_pitching[len(COL_pitching)-1])
COL_pitching_df = COL_pitching_df.loc[0:12, ['R', 'H', 'ER', 'HR', 'BB', 'SO']]
COL_pitching_df = COL_pitching_df.drop(labels = range(21,len(COL_pitching_df)),
                                       axis = 0)
COL_pitching_df = COL_pitching_df.loc[(COL_pitching_df['H'] != 'H')]

# Washington
WSN_batting = pd.read_html('https://www.baseball-reference.com/teams/WSN/2021.shtml#team_batting')
WSN_batting_df = pd.DataFrame(WSN_batting[(len(WSN_batting)-2)])
WSN_batting_df = WSN_batting_df.loc[0:12, ['R', 'H', '2B', '3B', 'RBI', 'SB']]
WSN_batting_df = WSN_batting_df.drop(labels = range(21,len(WSN_batting_df)),
                                     axis = 0)
WSN_batting_df = WSN_batting_df.loc[(WSN_batting_df['R'] != 'R')]

WSN_pitching = pd.read_html('https://www.baseball-reference.com/teams/WSN/2021.shtml#team_pitching')
WSN_pitching_df = pd.DataFrame(WSN_pitching[len(WSN_pitching)-1])
WSN_pitching_df = WSN_pitching_df.loc[0:12, ['R', 'H', 'ER', 'HR', 'BB', 'SO']]
WSN_pitching_df = WSN_pitching_df.drop(labels = range(21,len(WSN_pitching_df)),
                                       axis = 0)
WSN_pitching_df = WSN_pitching_df.loc[(WSN_pitching_df['H'] != 'H')]

# Chi Cubs
CHC_batting = pd.read_html('https://www.baseball-reference.com/teams/CHC/2021.shtml#team_batting')
CHC_batting_df = pd.DataFrame(CHC_batting[(len(CHC_batting)-2)])
CHC_batting_df = CHC_batting_df.loc[0:12, ['R', 'H', '2B', '3B', 'RBI', 'SB']]
CHC_batting_df = CHC_batting_df.drop(labels = range(21,len(CHC_batting_df)),
                                     axis = 0)
CHC_batting_df = CHC_batting_df.loc[(CHC_batting_df['R'] != 'R')]

CHC_pitching = pd.read_html('https://www.baseball-reference.com/teams/CHC/2021.shtml#team_pitching')
CHC_pitching_df = pd.DataFrame(CHC_pitching[len(CHC_pitching)-1])
CHC_pitching_df = CHC_pitching_df.loc[0:12, ['R', 'H', 'ER', 'HR', 'BB', 'SO']]
CHC_pitching_df = CHC_pitching_df.drop(labels = range(21,len(CHC_pitching_df)),
                                       axis = 0)
CHC_pitching_df = CHC_pitching_df.loc[(CHC_pitching_df['H'] != 'H')]

# Miami
MIA_batting = pd.read_html('https://www.baseball-reference.com/teams/MIA/2021.shtml#team_batting')
MIA_batting_df = pd.DataFrame(MIA_batting[(len(MIA_batting)-2)])
MIA_batting_df = MIA_batting_df.loc[0:12, ['R', 'H', '2B', '3B', 'RBI', 'SB']]
MIA_batting_df = MIA_batting_df.drop(labels = range(21,len(MIA_batting_df)),
                                     axis = 0)
MIA_batting_df = MIA_batting_df.loc[(MIA_batting_df['R'] != 'R')]

MIA_pitching = pd.read_html('https://www.baseball-reference.com/teams/MIA/2021.shtml#team_pitching')
MIA_pitching_df = pd.DataFrame(MIA_pitching[len(MIA_pitching)-1])
MIA_pitching_df = MIA_pitching_df.loc[0:12, ['R', 'H', 'ER', 'HR', 'BB', 'SO']]
MIA_pitching_df = MIA_pitching_df.drop(labels = range(21,len(MIA_pitching_df)),
                                       axis = 0)
MIA_pitching_df = MIA_pitching_df.loc[(MIA_pitching_df['H'] != 'H')]

# Pittsburgh
PIT_batting = pd.read_html('https://www.baseball-reference.com/teams/PIT/2021.shtml#team_batting')
PIT_batting_df = pd.DataFrame(PIT_batting[(len(PIT_batting)-2)])
PIT_batting_df = PIT_batting_df.loc[0:12, ['R', 'H', '2B', '3B', 'RBI', 'SB']]
PIT_batting_df = PIT_batting_df.drop(labels = range(21,len(PIT_batting_df)),
                                     axis = 0)
PIT_batting_df = PIT_batting_df.loc[(PIT_batting_df['R'] != 'R')]

PIT_pitching = pd.read_html('https://www.baseball-reference.com/teams/PIT/2021.shtml#team_pitching')
PIT_pitching_df = pd.DataFrame(PIT_pitching[len(PIT_pitching)-1])
PIT_pitching_df = PIT_pitching_df.loc[0:12, ['R', 'H', 'ER', 'HR', 'BB', 'SO']]
PIT_pitching_df = PIT_pitching_df.drop(labels = range(21,len(PIT_pitching_df)),
                                       axis = 0)
PIT_pitching_df = PIT_pitching_df.loc[(PIT_pitching_df['H'] != 'H')]