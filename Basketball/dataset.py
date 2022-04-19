from packages import pd, np

# Injury Table
Injury = pd.read_html('https://www.basketball-reference.com/friv/injuries.fcgi#injuries')
Injury_df = pd.DataFrame(Injury[0])
Injury_array = np.array(Injury_df['Player']).astype(str)

def injury_function(dataset):
    dataset = dataset[~dataset.isin(Injury_df)]
    dataset.dropna(subset=[('Unnamed: 1')], inplace = True)
    return dataset

# Boston
BOS_Dataset = pd.read_html('https://www.basketball-reference.com/teams/BOS/2022.html#advanced')
BOS_Dataset = pd.DataFrame(BOS_Dataset[1])
BOS_Dataset = injury_function(BOS_Dataset)
BOS_Dataset = BOS_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB',
                                     'DRB', 'STL', 'BLK', 'PF', 'TOV']].fillna(0)
BOS_Offence = BOS_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB']]

BOS_Defence = BOS_Dataset.loc[0:12, ['DRB', 'STL', 'BLK', 'PF', 'TOV']]

# Brooklyn
BRK_Dataset = pd.read_html('https://www.basketball-reference.com/teams/BRK/2022.html#advanced')
BRK_Dataset = pd.DataFrame(BRK_Dataset[1])
BRK_Dataset = injury_function(BRK_Dataset)
BRK_Dataset = BRK_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB',
                                  'DRB', 'STL', 'BLK', 'PF', 'TOV']].fillna(0)
BRK_Offence = BRK_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB']]

BRK_Defence = BRK_Dataset.loc[0:12, ['DRB', 'STL', 'BLK', 'PF', 'TOV']]

# Toronto
TOR_Dataset = pd.read_html('https://www.basketball-reference.com/teams/TOR/2022.html#advanced')
TOR_Dataset = pd.DataFrame(TOR_Dataset[1])
TOR_Dataset = injury_function(TOR_Dataset)
TOR_Dataset = TOR_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB',
                                  'DRB', 'STL', 'BLK', 'PF', 'TOV']].fillna(0)
TOR_Offence = TOR_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB']]

TOR_Defence = TOR_Dataset.loc[0:12, ['DRB', 'STL', 'BLK', 'PF', 'TOV']]

# Philidelphia
PHI_Dataset = pd.read_html('https://www.basketball-reference.com/teams/PHI/2022.html#advanced')
PHI_Dataset = pd.DataFrame(PHI_Dataset[1])
PHI_Dataset = injury_function(PHI_Dataset)
PHI_Dataset = PHI_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB',
                                  'DRB', 'STL', 'BLK', 'PF', 'TOV']].fillna(0)
PHI_Offence = PHI_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB']]

PHI_Defence = PHI_Dataset.loc[0:12, ['DRB', 'STL', 'BLK', 'PF', 'TOV']]

# New York Knicks
NYK_Dataset = pd.read_html('https://www.basketball-reference.com/teams/NYK/2022.html#advanced')
NYK_Dataset = pd.DataFrame(NYK_Dataset[1])
NYK_Dataset = injury_function(NYK_Dataset)
NYK_Dataset = NYK_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB',
                                  'DRB', 'STL', 'BLK', 'PF', 'TOV']].fillna(0)
NYK_Offence = NYK_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB']]

NYK_Defence = NYK_Dataset.loc[0:12, ['DRB', 'STL', 'BLK', 'PF', 'TOV']]

# Minnesota
MIN_Dataset = pd.read_html('https://www.basketball-reference.com/teams/MIN/2022.html#advanced')
MIN_Dataset = pd.DataFrame(MIN_Dataset[1])
MIN_Dataset = injury_function(MIN_Dataset)
MIN_Dataset = MIN_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB',
                                  'DRB', 'STL', 'BLK', 'PF', 'TOV']].fillna(0)
MIN_Offence = MIN_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB']]

MIN_Defence = MIN_Dataset.loc[0:12, ['DRB', 'STL', 'BLK', 'PF', 'TOV']]

# Oklahoma
OKC_Dataset = pd.read_html('https://www.basketball-reference.com/teams/OKC/2022.html#advanced')
OKC_Dataset = pd.DataFrame(OKC_Dataset[1])
OKC_Dataset = injury_function(OKC_Dataset)
OKC_Dataset = OKC_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB',
                                  'DRB', 'STL', 'BLK', 'PF', 'TOV']].fillna(0)
OKC_Offence = OKC_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB']]

OKC_Defence = OKC_Dataset.loc[0:12, ['DRB', 'STL', 'BLK', 'PF', 'TOV']]

# Denver
DEN_Dataset = pd.read_html('https://www.basketball-reference.com/teams/DEN/2022.html#advanced')
DEN_Dataset = pd.DataFrame(DEN_Dataset[1])
DEN_Dataset = injury_function(DEN_Dataset)
DEN_Dataset = DEN_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB',
                                  'DRB', 'STL', 'BLK', 'PF', 'TOV']].fillna(0)
DEN_Offence = DEN_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB']]

DEN_Defence = DEN_Dataset.loc[0:12, ['DRB', 'STL', 'BLK', 'PF', 'TOV']]

# Portland
POR_Dataset = pd.read_html('https://www.basketball-reference.com/teams/POR/2022.html#advanced')
POR_Dataset = pd.DataFrame(POR_Dataset[1])
POR_Dataset = injury_function(POR_Dataset)
POR_Dataset = POR_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB',
                                  'DRB', 'STL', 'BLK', 'PF', 'TOV']].fillna(0)
POR_Offence = POR_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB']]

POR_Defence = POR_Dataset.loc[0:12, ['DRB', 'STL', 'BLK', 'PF', 'TOV']]

# Utah
UTA_Dataset = pd.read_html('https://www.basketball-reference.com/teams/UTA/2022.html#advanced')
UTA_Dataset = pd.DataFrame(UTA_Dataset[1])
UTA_Dataset = injury_function(UTA_Dataset)
UTA_Dataset = UTA_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB',
                                  'DRB', 'STL', 'BLK', 'PF', 'TOV']].fillna(0)
UTA_Offence = UTA_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB']]

UTA_Defence = UTA_Dataset.loc[0:12, ['DRB', 'STL', 'BLK', 'PF', 'TOV']]

# Chicago
CHI_Dataset = pd.read_html('https://www.basketball-reference.com/teams/CHI/2022.html#advanced')
CHI_Dataset = pd.DataFrame(CHI_Dataset[1])
CHI_Dataset = injury_function(CHI_Dataset)
CHI_Dataset = CHI_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB',
                                  'DRB', 'STL', 'BLK', 'PF', 'TOV']].fillna(0)
CHI_Offence = CHI_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB']]

CHI_Defence = CHI_Dataset.loc[0:12, ['DRB', 'STL', 'BLK', 'PF', 'TOV']]

# Cleveland
CLE_Dataset = pd.read_html('https://www.basketball-reference.com/teams/CLE/2022.html#advanced')
CLE_Dataset = pd.DataFrame(CLE_Dataset[1])
CLE_Dataset = injury_function(CLE_Dataset)
CLE_Dataset = CLE_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB',
                                  'DRB', 'STL', 'BLK', 'PF', 'TOV']].fillna(0)
CLE_Offence = CLE_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB']]

CLE_Defence = CLE_Dataset.loc[0:12, ['DRB', 'STL', 'BLK', 'PF', 'TOV']]

# Detroit
DET_Dataset = pd.read_html('https://www.basketball-reference.com/teams/DET/2022.html#advanced')
DET_Dataset = pd.DataFrame(DET_Dataset[1])
DET_Dataset = injury_function(DET_Dataset)
DET_Dataset = DET_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB',
                                  'DRB', 'STL', 'BLK', 'PF', 'TOV']].fillna(0)
DET_Offence = DET_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB']]

DET_Defence = DET_Dataset.loc[0:12, ['DRB', 'STL', 'BLK', 'PF', 'TOV']]

# Indiana
IND_Dataset = pd.read_html('https://www.basketball-reference.com/teams/IND/2022.html#advanced')
IND_Dataset = pd.DataFrame(IND_Dataset[1])
IND_Dataset = injury_function(IND_Dataset)
IND_Dataset = IND_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB',
                                  'DRB', 'STL', 'BLK', 'PF', 'TOV']].fillna(0)
IND_Offence = IND_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB']]

IND_Defence = IND_Dataset.loc[0:12, ['DRB', 'STL', 'BLK', 'PF', 'TOV']]

# Milwaukee
MIL_Dataset = pd.read_html('https://www.basketball-reference.com/teams/MIL/2022.html#advanced')
MIL_Dataset = pd.DataFrame(MIL_Dataset[1])
MIL_Dataset = injury_function(MIL_Dataset)
MIL_Dataset = MIL_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB',
                                  'DRB', 'STL', 'BLK', 'PF', 'TOV']].fillna(0)
MIL_Offence = MIL_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB']]

MIL_Defence = MIL_Dataset.loc[0:12, ['DRB', 'STL', 'BLK', 'PF', 'TOV']]

# Los Angeles Lakers
LAL_Dataset = pd.read_html('https://www.basketball-reference.com/teams/LAL/2022.html#advanced')
LAL_Dataset = pd.DataFrame(LAL_Dataset[1])
LAL_Dataset = injury_function(LAL_Dataset)
LAL_Dataset = LAL_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB',
                                  'DRB', 'STL', 'BLK', 'PF', 'TOV']].fillna(0)
LAL_Offence = LAL_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB']]

LAL_Defence = LAL_Dataset.loc[0:12, ['DRB', 'STL', 'BLK', 'PF', 'TOV']]

# Los Angeles Clippers
LAC_Dataset = pd.read_html('https://www.basketball-reference.com/teams/LAC/2022.html#advanced')
LAC_Dataset = pd.DataFrame(LAC_Dataset[1])
LAC_Dataset = injury_function(LAC_Dataset)
LAC_Dataset = LAC_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB',
                                  'DRB', 'STL', 'BLK', 'PF', 'TOV']].fillna(0)
LAC_Offence = LAC_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB']]

LAC_Defence = LAC_Dataset.loc[0:12, ['DRB', 'STL', 'BLK', 'PF', 'TOV']]

# Golden State
GSW_Dataset = pd.read_html('https://www.basketball-reference.com/teams/GSW/2022.html#advanced')
GSW_Dataset = pd.DataFrame(GSW_Dataset[1])
GSW_Dataset = injury_function(GSW_Dataset)
GSW_Dataset = GSW_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB',
                                  'DRB', 'STL', 'BLK', 'PF', 'TOV']].fillna(0)
GSW_Offence = GSW_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB']]

GSW_Defence = GSW_Dataset.loc[0:12, ['DRB', 'STL', 'BLK', 'PF', 'TOV']]

# Phoenix
PHO_Dataset = pd.read_html('https://www.basketball-reference.com/teams/PHO/2022.html#advanced')
PHO_Dataset = pd.DataFrame(PHO_Dataset[1])
PHO_Dataset = injury_function(PHO_Dataset)
PHO_Dataset = PHO_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB',
                                  'DRB', 'STL', 'BLK', 'PF', 'TOV']].fillna(0)
PHO_Offence = PHO_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB']]

PHO_Defence = PHO_Dataset.loc[0:12, ['DRB', 'STL', 'BLK', 'PF', 'TOV']]

# Sacramento
SAC_Dataset = pd.read_html('https://www.basketball-reference.com/teams/SAC/2022.html#advanced')
SAC_Dataset = pd.DataFrame(SAC_Dataset[1])
SAC_Dataset = injury_function(SAC_Dataset)
SAC_Dataset = SAC_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB',
                                  'DRB', 'STL', 'BLK', 'PF', 'TOV']].fillna(0)
SAC_Offence = SAC_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB']]

SAC_Defence = SAC_Dataset.loc[0:12, ['DRB', 'STL', 'BLK', 'PF', 'TOV']]

# Washington
WAS_Dataset = pd.read_html('https://www.basketball-reference.com/teams/WAS/2022.html#advanced')
WAS_Dataset = pd.DataFrame(WAS_Dataset[1])
WAS_Dataset = injury_function(WAS_Dataset)
WAS_Dataset = WAS_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB',
                                  'DRB', 'STL', 'BLK', 'PF', 'TOV']].fillna(0)
WAS_Offence = WAS_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB']]

WAS_Defence = WAS_Dataset.loc[0:12, ['DRB', 'STL', 'BLK', 'PF', 'TOV']]

# Atlanta
ATL_Dataset = pd.read_html('https://www.basketball-reference.com/teams/ATL/2022.html#advanced')
ATL_Dataset = pd.DataFrame(ATL_Dataset[1])
ATL_Dataset = injury_function(ATL_Dataset)
ATL_Dataset = ATL_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB',
                                  'DRB', 'STL', 'BLK', 'PF', 'TOV']].fillna(0)
ATL_Offence = ATL_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB']]

ATL_Defence = ATL_Dataset.loc[0:12, ['DRB', 'STL', 'BLK', 'PF', 'TOV']]

# Orlando
ORL_Dataset = pd.read_html('https://www.basketball-reference.com/teams/ORL/2022.html#advanced')
ORL_Dataset = pd.DataFrame(ORL_Dataset[1])
ORL_Dataset = injury_function(ORL_Dataset)
ORL_Dataset = ORL_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB',
                                  'DRB', 'STL', 'BLK', 'PF', 'TOV']].fillna(0)
ORL_Offence = ORL_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB']]

ORL_Defence = ORL_Dataset.loc[0:12, ['DRB', 'STL', 'BLK', 'PF', 'TOV']]

# Miami
MIA_Dataset = pd.read_html('https://www.basketball-reference.com/teams/MIA/2022.html#advanced')
MIA_Dataset = pd.DataFrame(MIA_Dataset[1])
MIA_Dataset = injury_function(MIA_Dataset)
MIA_Dataset = MIA_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB',
                                  'DRB', 'STL', 'BLK', 'PF', 'TOV']].fillna(0)
MIA_Offence = MIA_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB']]

MIA_Defence = MIA_Dataset.loc[0:12, ['DRB', 'STL', 'BLK', 'PF', 'TOV']]

# Charlotte
CHO_Dataset = pd.read_html('https://www.basketball-reference.com/teams/CHO/2022.html#advanced')
CHO_Dataset = pd.DataFrame(CHO_Dataset[1])
CHO_Dataset = injury_function(CHO_Dataset)
CHO_Dataset = CHO_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB',
                                  'DRB', 'STL', 'BLK', 'PF', 'TOV']].fillna(0)
CHO_Offence = CHO_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB']]

CHO_Defence = CHO_Dataset.loc[0:12, ['DRB', 'STL', 'BLK', 'PF', 'TOV']]

# Memphis
MEM_Dataset = pd.read_html('https://www.basketball-reference.com/teams/MEM/2022.html#advanced')
MEM_Dataset = pd.DataFrame(MEM_Dataset[1])
MEM_Dataset = injury_function(MEM_Dataset)
MEM_Dataset = MEM_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB',
                                  'DRB', 'STL', 'BLK', 'PF', 'TOV']].fillna(0)
MEM_Offence = MEM_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB']]

MEM_Defence = MEM_Dataset.loc[0:12, ['DRB', 'STL', 'BLK', 'PF', 'TOV']]

# New Orleans
NOP_Dataset = pd.read_html('https://www.basketball-reference.com/teams/NOP/2022.html#advanced')
NOP_Dataset = pd.DataFrame(NOP_Dataset[1])
NOP_Dataset = injury_function(NOP_Dataset)
NOP_Dataset = NOP_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB',
                                  'DRB', 'STL', 'BLK', 'PF', 'TOV']].fillna(0)
NOP_Offence = NOP_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB']]

NOP_Defence = NOP_Dataset.loc[0:12, ['DRB', 'STL', 'BLK', 'PF', 'TOV']]

# Houston
HOU_Dataset = pd.read_html('https://www.basketball-reference.com/teams/HOU/2022.html#advanced')
HOU_Dataset = pd.DataFrame(HOU_Dataset[1])
HOU_Dataset = injury_function(HOU_Dataset)
HOU_Dataset = HOU_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB',
                                  'DRB', 'STL', 'BLK', 'PF', 'TOV']].fillna(0)
HOU_Offence = HOU_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB']]

HOU_Defence = HOU_Dataset.loc[0:12, ['DRB', 'STL', 'BLK', 'PF', 'TOV']]

# San Antonio
SAS_Dataset = pd.read_html('https://www.basketball-reference.com/teams/SAS/2022.html#advanced')
SAS_Dataset = pd.DataFrame(SAS_Dataset[1])
SAS_Dataset = injury_function(SAS_Dataset)
SAS_Dataset = SAS_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB',
                                  'DRB', 'STL', 'BLK', 'PF', 'TOV']].fillna(0)
SAS_Offence = SAS_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB']]

SAS_Defence = SAS_Dataset.loc[0:12, ['DRB', 'STL', 'BLK', 'PF', 'TOV']]

# Dallas
DAL_Dataset = pd.read_html('https://www.basketball-reference.com/teams/DAL/2022.html#advanced')
DAL_Dataset = pd.DataFrame(DAL_Dataset[1])
DAL_Dataset = injury_function(DAL_Dataset)
DAL_Dataset = DAL_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB',
                                  'DRB', 'STL', 'BLK', 'PF', 'TOV']].fillna(0)
DAL_Offence = DAL_Dataset.loc[0:12, ['FG', 'FGA', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB']]

DAL_Defence = DAL_Dataset.loc[0:12, ['DRB', 'STL', 'BLK', 'PF', 'TOV']]

# Full Offence Dataset
Offence_Dataframe = pd.DataFrame(BOS_Offence).append(BRK_Offence).append(TOR_Offence).append(PHI_Offence).\
    append(NYK_Offence).append(MIN_Offence).append(OKC_Offence).append(DEN_Offence).append(POR_Offence).\
    append(UTA_Offence).append(CHI_Offence).append(CLE_Offence).append(DET_Offence).append(IND_Offence).\
    append(MIL_Offence).append(LAL_Offence).append(LAC_Offence).append(GSW_Offence).append(PHO_Offence).\
    append(SAC_Offence).append(WAS_Offence).append(ATL_Offence).append(ORL_Offence).append(MIA_Offence).\
    append(CHO_Offence).append(MEM_Offence).append(NOP_Offence).append(HOU_Offence).append(SAS_Offence).\
    append(DAL_Offence)

# Full Defence Dataset
Defence_Dataframe = pd.DataFrame(BOS_Defence).append(BRK_Defence).append(TOR_Defence).append(PHI_Defence).\
    append(NYK_Defence).append(MIN_Defence).append(OKC_Defence).append(DEN_Defence).append(POR_Defence).\
    append(UTA_Defence).append(CHI_Defence).append(CLE_Defence).append(DET_Defence).append(IND_Defence).\
    append(MIL_Defence).append(LAL_Defence).append(LAC_Defence).append(GSW_Defence).append(PHO_Defence).\
    append(SAC_Defence).append(WAS_Defence).append(ATL_Defence).append(ORL_Defence).append(MIA_Defence).\
    append(CHO_Defence).append(MEM_Defence).append(NOP_Defence).append(HOU_Defence).append(SAS_Defence).\
    append(DAL_Defence)

# Offence Mean
FG_Mean = float(np.mean(Offence_Dataframe.loc[:, ['FG']]))
ThreeP_Mean = float((np.mean(Offence_Dataframe.loc[:, ['3P']])))
TwoP_Mean = float((np.mean(Offence_Dataframe.loc[:, ['2P']])))
FT_Mean = float((np.mean(Offence_Dataframe.loc[:, ['FT']])))
ORB_Mean = float((np.mean(Offence_Dataframe.loc[:, ['ORB']])))

# Offence Standard Deviation
FG_Std = float(np.std(Offence_Dataframe.loc[:, ['FG']]))
ThreeP_Std = float((np.std(Offence_Dataframe.loc[:, ['3P']])))
TwoP_Std = float((np.std(Offence_Dataframe.loc[:, ['2P']])))
FT_Std = float((np.std(Offence_Dataframe.loc[:, ['FT']])))
ORB_Std = float((np.std(Offence_Dataframe.loc[:, ['ORB']])))

# Defence Mean
DRB_Mean = float((np.mean(Defence_Dataframe.loc[:, ['DRB']])))
STL_Mean = float((np.mean(Defence_Dataframe.loc[:, ['STL']])))
BLK_Mean = float((np.mean(Defence_Dataframe.loc[:, ['BLK']])))
PF_Mean = float((np.mean(Defence_Dataframe.loc[:, ['PF']])))
TOV_Mean = float((np.mean(Defence_Dataframe.loc[:, ['TOV']])))

# Defence Standard Deviation
DRB_Std = float((np.std(Defence_Dataframe.loc[:, ['DRB']])))
STL_Std = float((np.std(Defence_Dataframe.loc[:, ['STL']])))
BLK_Std = float((np.std(Defence_Dataframe.loc[:, ['BLK']])))
PF_Std = float((np.std(Defence_Dataframe.loc[:, ['PF']])))
TOV_Std = float((np.std(Defence_Dataframe.loc[:, ['TOV']])))

# Boston Offence Normalized
BOS_FG_Normalized = float(np.sum(((BOS_Offence.loc[:,['FG']] - FG_Mean) / FG_Std)))
BOS_ThreeP_Normalized = float(np.sum(((BOS_Offence.loc[:,['3P']] - ThreeP_Mean) / ThreeP_Std)))
BOS_TwoP_Normalized = float(np.sum(((BOS_Offence.loc[:,['2P']] - TwoP_Mean) / TwoP_Std)))
BOS_FT_Normalized = float(np.sum(((BOS_Offence.loc[:,['FT']] - FT_Mean) / FT_Std)))
BOS_ORB_Normalized = float(np.sum(((BOS_Offence.loc[:,['ORB']] - ORB_Mean) / ORB_Std)))

# Boston Defence Normalized
BOS_DRB_Normalized = float(np.sum(((BOS_Defence.loc[:,['DRB']] - DRB_Mean) / DRB_Std)))
BOS_STL_Normalized = float(np.sum(((BOS_Defence.loc[:,['STL']] - STL_Mean) / STL_Std)))
BOS_BLK_Normalized = float(np.sum(((BOS_Defence.loc[:,['BLK']] - BLK_Mean) / BLK_Std)))
BOS_PF_Normalized = float(np.sum(((BOS_Defence.loc[:,['PF']] - PF_Mean) / PF_Std)))
BOS_TOV_Normalized = float(np.sum(((BOS_Defence.loc[:,['TOV']] - TOV_Mean) / TOV_Std)))

# Brooklyn Offence Normalized
BRK_FG_Normalized = float(np.sum(((BRK_Offence.loc[:,['FG']] - FG_Mean) / FG_Std)))
BRK_ThreeP_Normalized = float(np.sum(((BRK_Offence.loc[:,['3P']] - ThreeP_Mean) / ThreeP_Std)))
BRK_TwoP_Normalized = float(np.sum(((BRK_Offence.loc[:,['2P']] - TwoP_Mean) / TwoP_Std)))
BRK_FT_Normalized = float(np.sum(((BRK_Offence.loc[:,['FT']] - FT_Mean) / FT_Std)))
BRK_ORB_Normalized = float(np.sum(((BRK_Offence.loc[:,['ORB']] - ORB_Mean) / ORB_Std)))

# Brooklyn Defence Normalized
BRK_DRB_Normalized = float(np.sum(((BRK_Defence.loc[:,['DRB']] - DRB_Mean) / DRB_Std)))
BRK_STL_Normalized = float(np.sum(((BRK_Defence.loc[:,['STL']] - STL_Mean) / STL_Std)))
BRK_BLK_Normalized = float(np.sum(((BRK_Defence.loc[:,['BLK']] - BLK_Mean) / BLK_Std)))
BRK_PF_Normalized = float(np.sum(((BRK_Defence.loc[:,['PF']] - PF_Mean) / PF_Std)))
BRK_TOV_Normalized = float(np.sum(((BRK_Defence.loc[:,['TOV']] - TOV_Mean) / TOV_Std)))

# Toronto Offence Normalized
TOR_FG_Normalized = float(np.sum(((TOR_Offence.loc[:,['FG']] - FG_Mean) / FG_Std)))
TOR_ThreeP_Normalized = float(np.sum(((TOR_Offence.loc[:,['3P']] - ThreeP_Mean) / ThreeP_Std)))
TOR_TwoP_Normalized = float(np.sum(((TOR_Offence.loc[:,['2P']] - TwoP_Mean) / TwoP_Std)))
TOR_ORB_Normalized = float(np.sum(((TOR_Offence.loc[:,['ORB']] - ORB_Mean) / ORB_Std)))
TOR_FT_Normalized = float(np.sum(((TOR_Offence.loc[:,['FT']] - FT_Mean) / FT_Std)))

# Toronto Defence Normalized
TOR_DRB_Normalized = float(np.sum(((TOR_Defence.loc[:,['DRB']] - DRB_Mean) / DRB_Std)))
TOR_STL_Normalized = float(np.sum(((TOR_Defence.loc[:,['STL']] - STL_Mean) / STL_Std)))
TOR_BLK_Normalized = float(np.sum(((TOR_Defence.loc[:,['BLK']] - BLK_Mean) / BLK_Std)))
TOR_PF_Normalized = float(np.sum(((TOR_Defence.loc[:,['PF']] - PF_Mean) / PF_Std)))
TOR_TOV_Normalized = float(np.sum(((TOR_Defence.loc[:,['TOV']] - TOV_Mean) / TOV_Std)))

# Philidelphia Offence Normalized
PHI_FG_Normalized = float(np.sum(((PHI_Offence.loc[:, ['FG']] - FG_Mean) / FG_Std)))
PHI_ThreeP_Normalized = float(np.sum(((PHI_Offence.loc[:, ['3P']] - ThreeP_Mean) / ThreeP_Std)))
PHI_TwoP_Normalized = float(np.sum(((PHI_Offence.loc[:, ['2P']] - TwoP_Mean) / TwoP_Std)))
PHI_ORB_Normalized = float(np.sum(((PHI_Offence.loc[:, ['ORB']] - ORB_Mean) / ORB_Std)))
PHI_FT_Normalized = float(np.sum(((PHI_Offence.loc[:, ['FT']] - FT_Mean) / FT_Std)))

# Philidelphia Defence Normalized
PHI_DRB_Normalized = float(np.sum(((PHI_Defence.loc[:, ['DRB']] - DRB_Mean) / DRB_Std)))
PHI_STL_Normalized = float(np.sum(((PHI_Defence.loc[:, ['STL']] - STL_Mean) / STL_Std)))
PHI_BLK_Normalized = float(np.sum(((PHI_Defence.loc[:, ['BLK']] - BLK_Mean) / BLK_Std)))
PHI_PF_Normalized = float(np.sum(((PHI_Defence.loc[:, ['PF']] - PF_Mean) / PF_Std)))
PHI_TOV_Normalized = float(np.sum(((PHI_Defence.loc[:, ['TOV']] - TOV_Mean) / TOV_Std)))

# New York Knicks Offence Normalized
NYK_FG_Normalized = float(np.sum(((NYK_Offence.loc[:, ['FG']] - FG_Mean) / FG_Std)))
NYK_ThreeP_Normalized = float(np.sum(((NYK_Offence.loc[:, ['3P']] - ThreeP_Mean) / ThreeP_Std)))
NYK_TwoP_Normalized = float(np.sum(((NYK_Offence.loc[:, ['2P']] - TwoP_Mean) / TwoP_Std)))
NYK_ORB_Normalized = float(np.sum(((NYK_Offence.loc[:, ['ORB']] - ORB_Mean) / ORB_Std)))
NYK_FT_Normalized = float(np.sum(((NYK_Offence.loc[:, ['FT']] - FT_Mean) / FT_Std)))

# New York Knicks Defence Normalized
NYK_DRB_Normalized = float(np.sum(((NYK_Defence.loc[:, ['DRB']] - DRB_Mean) / DRB_Std)))
NYK_STL_Normalized = float(np.sum(((NYK_Defence.loc[:, ['STL']] - STL_Mean) / STL_Std)))
NYK_BLK_Normalized = float(np.sum(((NYK_Defence.loc[:, ['BLK']] - BLK_Mean) / BLK_Std)))
NYK_PF_Normalized = float(np.sum(((NYK_Defence.loc[:, ['PF']] - PF_Mean) / PF_Std)))
NYK_TOV_Normalized = float(np.sum(((NYK_Defence.loc[:, ['TOV']] - TOV_Mean) / TOV_Std)))

# Minnesota Offence Normalized
MIN_FG_Normalized = float(np.sum(((MIN_Offence.loc[:, ['FG']] - FG_Mean) / FG_Std)))
MIN_ThreeP_Normalized = float(np.sum(((MIN_Offence.loc[:, ['3P']] - ThreeP_Mean) / ThreeP_Std)))
MIN_TwoP_Normalized = float(np.sum(((MIN_Offence.loc[:, ['2P']] - TwoP_Mean) / TwoP_Std)))
MIN_ORB_Normalized = float(np.sum(((MIN_Offence.loc[:, ['ORB']] - ORB_Mean) / ORB_Std)))
MIN_FT_Normalized = float(np.sum(((MIN_Offence.loc[:, ['FT']] - FT_Mean) / FT_Std)))

# Minnesota Defence Normalized
MIN_DRB_Normalized = float(np.sum(((MIN_Defence.loc[:, ['DRB']] - DRB_Mean) / DRB_Std)))
MIN_STL_Normalized = float(np.sum(((MIN_Defence.loc[:, ['STL']] - STL_Mean) / STL_Std)))
MIN_BLK_Normalized = float(np.sum(((MIN_Defence.loc[:, ['BLK']] - BLK_Mean) / BLK_Std)))
MIN_PF_Normalized = float(np.sum(((MIN_Defence.loc[:, ['PF']] - PF_Mean) / PF_Std)))
MIN_TOV_Normalized = float(np.sum(((MIN_Defence.loc[:, ['TOV']] - TOV_Mean) / TOV_Std)))

# Oklahoma Offence Normalized
OKC_FG_Normalized = float(np.sum(((OKC_Offence.loc[:, ['FG']] - FG_Mean) / FG_Std)))
OKC_ThreeP_Normalized = float(np.sum(((OKC_Offence.loc[:, ['3P']] - ThreeP_Mean) / ThreeP_Std)))
OKC_TwoP_Normalized = float(np.sum(((OKC_Offence.loc[:, ['2P']] - TwoP_Mean) / TwoP_Std)))
OKC_ORB_Normalized = float(np.sum(((OKC_Offence.loc[:, ['ORB']] - ORB_Mean) / ORB_Std)))
OKC_FT_Normalized = float(np.sum(((OKC_Offence.loc[:, ['FT']] - FT_Mean) / FT_Std)))

# Oklahoma Defence Normalized
OKC_DRB_Normalized = float(np.sum(((OKC_Defence.loc[:, ['DRB']] - DRB_Mean) / DRB_Std)))
OKC_STL_Normalized = float(np.sum(((OKC_Defence.loc[:, ['STL']] - STL_Mean) / STL_Std)))
OKC_BLK_Normalized = float(np.sum(((OKC_Defence.loc[:, ['BLK']] - BLK_Mean) / BLK_Std)))
OKC_PF_Normalized = float(np.sum(((OKC_Defence.loc[:, ['PF']] - PF_Mean) / PF_Std)))
OKC_TOV_Normalized = float(np.sum(((OKC_Defence.loc[:, ['TOV']] - TOV_Mean) / TOV_Std)))

# Denver Offence Normalized
DEN_FG_Normalized = float(np.sum(((DEN_Offence.loc[:, ['FG']] - FG_Mean) / FG_Std)))
DEN_ThreeP_Normalized = float(np.sum(((DEN_Offence.loc[:, ['3P']] - ThreeP_Mean) / ThreeP_Std)))
DEN_TwoP_Normalized = float(np.sum(((DEN_Offence.loc[:, ['2P']] - TwoP_Mean) / TwoP_Std)))
DEN_ORB_Normalized = float(np.sum(((DEN_Offence.loc[:, ['ORB']] - ORB_Mean) / ORB_Std)))
DEN_FT_Normalized = float(np.sum(((DEN_Offence.loc[:, ['FT']] - FT_Mean) / FT_Std)))

# Denver Defence Normalized
DEN_DRB_Normalized = float(np.sum(((DEN_Defence.loc[:, ['DRB']] - DRB_Mean) / DRB_Std)))
DEN_STL_Normalized = float(np.sum(((DEN_Defence.loc[:, ['STL']] - STL_Mean) / STL_Std)))
DEN_BLK_Normalized = float(np.sum(((DEN_Defence.loc[:, ['BLK']] - BLK_Mean) / BLK_Std)))
DEN_PF_Normalized = float(np.sum(((DEN_Defence.loc[:, ['PF']] - PF_Mean) / PF_Std)))
DEN_TOV_Normalized = float(np.sum(((DEN_Defence.loc[:, ['TOV']] - TOV_Mean) / TOV_Std)))

# Portland Offence Normalized
POR_FG_Normalized = float(np.sum(((POR_Offence.loc[:, ['FG']] - FG_Mean) / FG_Std)))
POR_ThreeP_Normalized = float(np.sum(((POR_Offence.loc[:, ['3P']] - ThreeP_Mean) / ThreeP_Std)))
POR_TwoP_Normalized = float(np.sum(((POR_Offence.loc[:, ['2P']] - TwoP_Mean) / TwoP_Std)))
POR_ORB_Normalized = float(np.sum(((POR_Offence.loc[:, ['ORB']] - ORB_Mean) / ORB_Std)))
POR_FT_Normalized = float(np.sum(((POR_Offence.loc[:, ['FT']] - FT_Mean) / FT_Std)))

# Portland Defence Normalized
POR_DRB_Normalized = float(np.sum(((POR_Defence.loc[:, ['DRB']] - DRB_Mean) / DRB_Std)))
POR_STL_Normalized = float(np.sum(((POR_Defence.loc[:, ['STL']] - STL_Mean) / STL_Std)))
POR_BLK_Normalized = float(np.sum(((POR_Defence.loc[:, ['BLK']] - BLK_Mean) / BLK_Std)))
POR_PF_Normalized = float(np.sum(((POR_Defence.loc[:, ['PF']] - PF_Mean) / PF_Std)))
POR_TOV_Normalized = float(np.sum(((POR_Defence.loc[:, ['TOV']] - TOV_Mean) / TOV_Std)))

# Utah Offence Normalized
UTA_FG_Normalized = float(np.sum(((UTA_Offence.loc[:, ['FG']] - FG_Mean) / FG_Std)))
UTA_ThreeP_Normalized = float(np.sum(((UTA_Offence.loc[:, ['3P']] - ThreeP_Mean) / ThreeP_Std)))
UTA_TwoP_Normalized = float(np.sum(((UTA_Offence.loc[:, ['2P']] - TwoP_Mean) / TwoP_Std)))
UTA_ORB_Normalized = float(np.sum(((UTA_Offence.loc[:, ['ORB']] - ORB_Mean) / ORB_Std)))
UTA_FT_Normalized = float(np.sum(((UTA_Offence.loc[:, ['FT']] - FT_Mean) / FT_Std)))

# Utah Defence Normalized
UTA_DRB_Normalized = float(np.sum(((UTA_Defence.loc[:, ['DRB']] - DRB_Mean) / DRB_Std)))
UTA_STL_Normalized = float(np.sum(((UTA_Defence.loc[:, ['STL']] - STL_Mean) / STL_Std)))
UTA_BLK_Normalized = float(np.sum(((UTA_Defence.loc[:, ['BLK']] - BLK_Mean) / BLK_Std)))
UTA_PF_Normalized = float(np.sum(((UTA_Defence.loc[:, ['PF']] - PF_Mean) / PF_Std)))
UTA_TOV_Normalized = float(np.sum(((UTA_Defence.loc[:, ['TOV']] - TOV_Mean) / TOV_Std)))

# Chicago Offence Normalized
CHI_FG_Normalized = float(np.sum(((CHI_Offence.loc[:, ['FG']] - FG_Mean) / FG_Std)))
CHI_ThreeP_Normalized = float(np.sum(((CHI_Offence.loc[:, ['3P']] - ThreeP_Mean) / ThreeP_Std)))
CHI_TwoP_Normalized = float(np.sum(((CHI_Offence.loc[:, ['2P']] - TwoP_Mean) / TwoP_Std)))
CHI_ORB_Normalized = float(np.sum(((CHI_Offence.loc[:, ['ORB']] - ORB_Mean) / ORB_Std)))
CHI_FT_Normalized = float(np.sum(((CHI_Offence.loc[:, ['FT']] - FT_Mean) / FT_Std)))

# Chicago Defence Normalized
CHI_DRB_Normalized = float(np.sum(((CHI_Defence.loc[:, ['DRB']] - DRB_Mean) / DRB_Std)))
CHI_STL_Normalized = float(np.sum(((CHI_Defence.loc[:, ['STL']] - STL_Mean) / STL_Std)))
CHI_BLK_Normalized = float(np.sum(((CHI_Defence.loc[:, ['BLK']] - BLK_Mean) / BLK_Std)))
CHI_PF_Normalized = float(np.sum(((CHI_Defence.loc[:, ['PF']] - PF_Mean) / PF_Std)))
CHI_TOV_Normalized = float(np.sum(((CHI_Defence.loc[:, ['TOV']] - TOV_Mean) / TOV_Std)))

# Cleveland Offence Normalized
CLE_FG_Normalized = float(np.sum(((CLE_Offence.loc[:, ['FG']] - FG_Mean) / FG_Std)))
CLE_ThreeP_Normalized = float(np.sum(((CLE_Offence.loc[:, ['3P']] - ThreeP_Mean) / ThreeP_Std)))
CLE_TwoP_Normalized = float(np.sum(((CLE_Offence.loc[:, ['2P']] - TwoP_Mean) / TwoP_Std)))
CLE_ORB_Normalized = float(np.sum(((CLE_Offence.loc[:, ['ORB']] - ORB_Mean) / ORB_Std)))
CLE_FT_Normalized = float(np.sum(((CLE_Offence.loc[:, ['FT']] - FT_Mean) / FT_Std)))

# Cleveland Defence Normalized
CLE_DRB_Normalized = float(np.sum(((CLE_Defence.loc[:, ['DRB']] - DRB_Mean) / DRB_Std)))
CLE_STL_Normalized = float(np.sum(((CLE_Defence.loc[:, ['STL']] - STL_Mean) / STL_Std)))
CLE_BLK_Normalized = float(np.sum(((CLE_Defence.loc[:, ['BLK']] - BLK_Mean) / BLK_Std)))
CLE_PF_Normalized = float(np.sum(((CLE_Defence.loc[:, ['PF']] - PF_Mean) / PF_Std)))
CLE_TOV_Normalized = float(np.sum(((CLE_Defence.loc[:, ['TOV']] - TOV_Mean) / TOV_Std)))

# Detroit Offence Normalized
DET_FG_Normalized = float(np.sum(((DET_Offence.loc[:, ['FG']] - FG_Mean) / FG_Std)))
DET_ThreeP_Normalized = float(np.sum(((DET_Offence.loc[:, ['3P']] - ThreeP_Mean) / ThreeP_Std)))
DET_TwoP_Normalized = float(np.sum(((DET_Offence.loc[:, ['2P']] - TwoP_Mean) / TwoP_Std)))
DET_ORB_Normalized = float(np.sum(((DET_Offence.loc[:, ['ORB']] - ORB_Mean) / ORB_Std)))
DET_FT_Normalized = float(np.sum(((DET_Offence.loc[:, ['FT']] - FT_Mean) / FT_Std)))

# Detroit Defence Normalized
DET_DRB_Normalized = float(np.sum(((DET_Defence.loc[:, ['DRB']] - DRB_Mean) / DRB_Std)))
DET_STL_Normalized = float(np.sum(((DET_Defence.loc[:, ['STL']] - STL_Mean) / STL_Std)))
DET_BLK_Normalized = float(np.sum(((DET_Defence.loc[:, ['BLK']] - BLK_Mean) / BLK_Std)))
DET_PF_Normalized = float(np.sum(((DET_Defence.loc[:, ['PF']] - PF_Mean) / PF_Std)))
DET_TOV_Normalized = float(np.sum(((DET_Defence.loc[:, ['TOV']] - TOV_Mean) / TOV_Std)))

# Indiana Offence Normalized
IND_FG_Normalized = float(np.sum(((IND_Offence.loc[:, ['FG']] - FG_Mean) / FG_Std)))
IND_ThreeP_Normalized = float(np.sum(((IND_Offence.loc[:, ['3P']] - ThreeP_Mean) / ThreeP_Std)))
IND_TwoP_Normalized = float(np.sum(((IND_Offence.loc[:, ['2P']] - TwoP_Mean) / TwoP_Std)))
IND_ORB_Normalized = float(np.sum(((IND_Offence.loc[:, ['ORB']] - ORB_Mean) / ORB_Std)))
IND_FT_Normalized = float(np.sum(((IND_Offence.loc[:, ['FT']] - FT_Mean) / FT_Std)))

# Indiana Defence Normalized
IND_DRB_Normalized = float(np.sum(((IND_Defence.loc[:, ['DRB']] - DRB_Mean) / DRB_Std)))
IND_STL_Normalized = float(np.sum(((IND_Defence.loc[:, ['STL']] - STL_Mean) / STL_Std)))
IND_BLK_Normalized = float(np.sum(((IND_Defence.loc[:, ['BLK']] - BLK_Mean) / BLK_Std)))
IND_PF_Normalized = float(np.sum(((IND_Defence.loc[:, ['PF']] - PF_Mean) / PF_Std)))
IND_TOV_Normalized = float(np.sum(((IND_Defence.loc[:, ['TOV']] - TOV_Mean) / TOV_Std)))

# Milwaukee Offence Normalized
MIL_FG_Normalized = float(np.sum(((MIL_Offence.loc[:, ['FG']] - FG_Mean) / FG_Std)))
MIL_ThreeP_Normalized = float(np.sum(((MIL_Offence.loc[:, ['3P']] - ThreeP_Mean) / ThreeP_Std)))
MIL_TwoP_Normalized = float(np.sum(((MIL_Offence.loc[:, ['2P']] - TwoP_Mean) / TwoP_Std)))
MIL_ORB_Normalized = float(np.sum(((MIL_Offence.loc[:, ['ORB']] - ORB_Mean) / ORB_Std)))
MIL_FT_Normalized = float(np.sum(((MIL_Offence.loc[:, ['FT']] - FT_Mean) / FT_Std)))

# Milwaukee Defence Normalized
MIL_DRB_Normalized = float(np.sum(((MIL_Defence.loc[:, ['DRB']] - DRB_Mean) / DRB_Std)))
MIL_STL_Normalized = float(np.sum(((MIL_Defence.loc[:, ['STL']] - STL_Mean) / STL_Std)))
MIL_BLK_Normalized = float(np.sum(((MIL_Defence.loc[:, ['BLK']] - BLK_Mean) / BLK_Std)))
MIL_PF_Normalized = float(np.sum(((MIL_Defence.loc[:, ['PF']] - PF_Mean) / PF_Std)))
MIL_TOV_Normalized = float(np.sum(((MIL_Defence.loc[:, ['TOV']] - TOV_Mean) / TOV_Std)))

# Los Angeles Lakers Offence Normalized
LAL_FG_Normalized = float(np.sum(((LAL_Offence.loc[:, ['FG']] - FG_Mean) / FG_Std)))
LAL_ThreeP_Normalized = float(np.sum(((LAL_Offence.loc[:, ['3P']] - ThreeP_Mean) / ThreeP_Std)))
LAL_TwoP_Normalized = float(np.sum(((LAL_Offence.loc[:, ['2P']] - TwoP_Mean) / TwoP_Std)))
LAL_ORB_Normalized = float(np.sum(((LAL_Offence.loc[:, ['ORB']] - ORB_Mean) / ORB_Std)))
LAL_FT_Normalized = float(np.sum(((LAL_Offence.loc[:, ['FT']] - FT_Mean) / FT_Std)))

# Los Angeles Lakers Defence Normalized
LAL_DRB_Normalized = float(np.sum(((LAL_Defence.loc[:, ['DRB']] - DRB_Mean) / DRB_Std)))
LAL_STL_Normalized = float(np.sum(((LAL_Defence.loc[:, ['STL']] - STL_Mean) / STL_Std)))
LAL_BLK_Normalized = float(np.sum(((LAL_Defence.loc[:, ['BLK']] - BLK_Mean) / BLK_Std)))
LAL_PF_Normalized = float(np.sum(((LAL_Defence.loc[:, ['PF']] - PF_Mean) / PF_Std)))
LAL_TOV_Normalized = float(np.sum(((LAL_Defence.loc[:, ['TOV']] - TOV_Mean) / TOV_Std)))

# Los Angeles Clippers Offence Normalized
LAC_FG_Normalized = float(np.sum(((LAC_Offence.loc[:, ['FG']] - FG_Mean) / FG_Std)))
LAC_ThreeP_Normalized = float(np.sum(((LAC_Offence.loc[:, ['3P']] - ThreeP_Mean) / ThreeP_Std)))
LAC_TwoP_Normalized = float(np.sum(((LAC_Offence.loc[:, ['2P']] - TwoP_Mean) / TwoP_Std)))
LAC_ORB_Normalized = float(np.sum(((LAC_Offence.loc[:, ['ORB']] - ORB_Mean) / ORB_Std)))
LAC_FT_Normalized = float(np.sum(((LAC_Offence.loc[:, ['FT']] - FT_Mean) / FT_Std)))

# Los Angeles Clippers Defence Normalized
LAC_DRB_Normalized = float(np.sum(((LAC_Defence.loc[:, ['DRB']] - DRB_Mean) / DRB_Std)))
LAC_STL_Normalized = float(np.sum(((LAC_Defence.loc[:, ['STL']] - STL_Mean) / STL_Std)))
LAC_BLK_Normalized = float(np.sum(((LAC_Defence.loc[:, ['BLK']] - BLK_Mean) / BLK_Std)))
LAC_PF_Normalized = float(np.sum(((LAC_Defence.loc[:, ['PF']] - PF_Mean) / PF_Std)))
LAC_TOV_Normalized = float(np.sum(((LAC_Defence.loc[:, ['TOV']] - TOV_Mean) / TOV_Std)))

# Golden State Offence Normalized
GSW_FG_Normalized = float(np.sum(((GSW_Offence.loc[:, ['FG']] - FG_Mean) / FG_Std)))
GSW_ThreeP_Normalized = float(np.sum(((GSW_Offence.loc[:, ['3P']] - ThreeP_Mean) / ThreeP_Std)))
GSW_TwoP_Normalized = float(np.sum(((GSW_Offence.loc[:, ['2P']] - TwoP_Mean) / TwoP_Std)))
GSW_ORB_Normalized = float(np.sum(((GSW_Offence.loc[:, ['ORB']] - ORB_Mean) / ORB_Std)))
GSW_FT_Normalized = float(np.sum(((GSW_Offence.loc[:, ['FT']] - FT_Mean) / FT_Std)))

# Golden State Defence Normalized
GSW_DRB_Normalized = float(np.sum(((GSW_Defence.loc[:, ['DRB']] - DRB_Mean) / DRB_Std)))
GSW_STL_Normalized = float(np.sum(((GSW_Defence.loc[:, ['STL']] - STL_Mean) / STL_Std)))
GSW_BLK_Normalized = float(np.sum(((GSW_Defence.loc[:, ['BLK']] - BLK_Mean) / BLK_Std)))
GSW_PF_Normalized = float(np.sum(((GSW_Defence.loc[:, ['PF']] - PF_Mean) / PF_Std)))
GSW_TOV_Normalized = float(np.sum(((GSW_Defence.loc[:, ['TOV']] - TOV_Mean) / TOV_Std)))

# Phoenix Offence Normalized
PHO_FG_Normalized = float(np.sum(((PHO_Offence.loc[:, ['FG']] - FG_Mean) / FG_Std)))
PHO_ThreeP_Normalized = float(np.sum(((PHO_Offence.loc[:, ['3P']] - ThreeP_Mean) / ThreeP_Std)))
PHO_TwoP_Normalized = float(np.sum(((PHO_Offence.loc[:, ['2P']] - TwoP_Mean) / TwoP_Std)))
PHO_ORB_Normalized = float(np.sum(((PHO_Offence.loc[:, ['ORB']] - ORB_Mean) / ORB_Std)))
PHO_FT_Normalized = float(np.sum(((PHO_Offence.loc[:, ['FT']] - FT_Mean) / FT_Std)))

# Phoenix Defence Normalized
PHO_DRB_Normalized = float(np.sum(((PHO_Defence.loc[:, ['DRB']] - DRB_Mean) / DRB_Std)))
PHO_STL_Normalized = float(np.sum(((PHO_Defence.loc[:, ['STL']] - STL_Mean) / STL_Std)))
PHO_BLK_Normalized = float(np.sum(((PHO_Defence.loc[:, ['BLK']] - BLK_Mean) / BLK_Std)))
PHO_PF_Normalized = float(np.sum(((PHO_Defence.loc[:, ['PF']] - PF_Mean) / PF_Std)))
PHO_TOV_Normalized = float(np.sum(((PHO_Defence.loc[:, ['TOV']] - TOV_Mean) / TOV_Std)))

# Sacramento Offence Normalized
SAC_FG_Normalized = float(np.sum(((SAC_Offence.loc[:, ['FG']] - FG_Mean) / FG_Std)))
SAC_ThreeP_Normalized = float(np.sum(((SAC_Offence.loc[:, ['3P']] - ThreeP_Mean) / ThreeP_Std)))
SAC_TwoP_Normalized = float(np.sum(((SAC_Offence.loc[:, ['2P']] - TwoP_Mean) / TwoP_Std)))
SAC_ORB_Normalized = float(np.sum(((SAC_Offence.loc[:, ['ORB']] - ORB_Mean) / ORB_Std)))
SAC_FT_Normalized = float(np.sum(((SAC_Offence.loc[:, ['FT']] - FT_Mean) / FT_Std)))

# Sacramento Defence Normalized
SAC_DRB_Normalized = float(np.sum(((SAC_Defence.loc[:, ['DRB']] - DRB_Mean) / DRB_Std)))
SAC_STL_Normalized = float(np.sum(((SAC_Defence.loc[:, ['STL']] - STL_Mean) / STL_Std)))
SAC_BLK_Normalized = float(np.sum(((SAC_Defence.loc[:, ['BLK']] - BLK_Mean) / BLK_Std)))
SAC_PF_Normalized = float(np.sum(((SAC_Defence.loc[:, ['PF']] - PF_Mean) / PF_Std)))
SAC_TOV_Normalized = float(np.sum(((SAC_Defence.loc[:, ['TOV']] - TOV_Mean) / TOV_Std)))

# Washington Offence Normalized
WAS_FG_Normalized = float(np.sum(((WAS_Offence.loc[:, ['FG']] - FG_Mean) / FG_Std)))
WAS_ThreeP_Normalized = float(np.sum(((WAS_Offence.loc[:, ['3P']] - ThreeP_Mean) / ThreeP_Std)))
WAS_TwoP_Normalized = float(np.sum(((WAS_Offence.loc[:, ['2P']] - TwoP_Mean) / TwoP_Std)))
WAS_ORB_Normalized = float(np.sum(((WAS_Offence.loc[:, ['ORB']] - ORB_Mean) / ORB_Std)))
WAS_FT_Normalized = float(np.sum(((WAS_Offence.loc[:, ['FT']] - FT_Mean) / FT_Std)))

# Washington Defence Normalized
WAS_DRB_Normalized = float(np.sum(((WAS_Defence.loc[:, ['DRB']] - DRB_Mean) / DRB_Std)))
WAS_STL_Normalized = float(np.sum(((WAS_Defence.loc[:, ['STL']] - STL_Mean) / STL_Std)))
WAS_BLK_Normalized = float(np.sum(((WAS_Defence.loc[:, ['BLK']] - BLK_Mean) / BLK_Std)))
WAS_PF_Normalized = float(np.sum(((WAS_Defence.loc[:, ['PF']] - PF_Mean) / PF_Std)))
WAS_TOV_Normalized = float(np.sum(((WAS_Defence.loc[:, ['TOV']] - TOV_Mean) / TOV_Std)))

# Atlanta Offence Normalized
ATL_FG_Normalized = float(np.sum(((ATL_Offence.loc[:, ['FG']] - FG_Mean) / FG_Std)))
ATL_ThreeP_Normalized = float(np.sum(((ATL_Offence.loc[:, ['3P']] - ThreeP_Mean) / ThreeP_Std)))
ATL_TwoP_Normalized = float(np.sum(((ATL_Offence.loc[:, ['2P']] - TwoP_Mean) / TwoP_Std)))
ATL_ORB_Normalized = float(np.sum(((ATL_Offence.loc[:, ['ORB']] - ORB_Mean) / ORB_Std)))
ATL_FT_Normalized = float(np.sum(((ATL_Offence.loc[:, ['FT']] - FT_Mean) / FT_Std)))

# Atlanta Defence Normalized
ATL_DRB_Normalized = float(np.sum(((ATL_Defence.loc[:, ['DRB']] - DRB_Mean) / DRB_Std)))
ATL_STL_Normalized = float(np.sum(((ATL_Defence.loc[:, ['STL']] - STL_Mean) / STL_Std)))
ATL_BLK_Normalized = float(np.sum(((ATL_Defence.loc[:, ['BLK']] - BLK_Mean) / BLK_Std)))
ATL_PF_Normalized = float(np.sum(((ATL_Defence.loc[:, ['PF']] - PF_Mean) / PF_Std)))
ATL_TOV_Normalized = float(np.sum(((ATL_Defence.loc[:, ['TOV']] - TOV_Mean) / TOV_Std)))

# Orlando Offence Normalized
ORL_FG_Normalized = float(np.sum(((ORL_Offence.loc[:, ['FG']] - FG_Mean) / FG_Std)))
ORL_ThreeP_Normalized = float(np.sum(((ORL_Offence.loc[:, ['3P']] - ThreeP_Mean) / ThreeP_Std)))
ORL_TwoP_Normalized = float(np.sum(((ORL_Offence.loc[:, ['2P']] - TwoP_Mean) / TwoP_Std)))
ORL_ORB_Normalized = float(np.sum(((ORL_Offence.loc[:, ['ORB']] - ORB_Mean) / ORB_Std)))
ORL_FT_Normalized = float(np.sum(((ORL_Offence.loc[:, ['FT']] - FT_Mean) / FT_Std)))

# Orlando Defence Normalized
ORL_DRB_Normalized = float(np.sum(((ORL_Defence.loc[:, ['DRB']] - DRB_Mean) / DRB_Std)))
ORL_STL_Normalized = float(np.sum(((ORL_Defence.loc[:, ['STL']] - STL_Mean) / STL_Std)))
ORL_BLK_Normalized = float(np.sum(((ORL_Defence.loc[:, ['BLK']] - BLK_Mean) / BLK_Std)))
ORL_PF_Normalized = float(np.sum(((ORL_Defence.loc[:, ['PF']] - PF_Mean) / PF_Std)))
ORL_TOV_Normalized = float(np.sum(((ORL_Defence.loc[:, ['TOV']] - TOV_Mean) / TOV_Std)))

# Miami Offence Normalized
MIA_FG_Normalized = float(np.sum(((MIA_Offence.loc[:, ['FG']] - FG_Mean) / FG_Std)))
MIA_ThreeP_Normalized = float(np.sum(((MIA_Offence.loc[:, ['3P']] - ThreeP_Mean) / ThreeP_Std)))
MIA_TwoP_Normalized = float(np.sum(((MIA_Offence.loc[:, ['2P']] - TwoP_Mean) / TwoP_Std)))
MIA_ORB_Normalized = float(np.sum(((MIA_Offence.loc[:, ['ORB']] - ORB_Mean) / ORB_Std)))
MIA_FT_Normalized = float(np.sum(((MIA_Offence.loc[:, ['FT']] - FT_Mean) / FT_Std)))

# Miami Defence Normalized
MIA_DRB_Normalized = float(np.sum(((MIA_Defence.loc[:, ['DRB']] - DRB_Mean) / DRB_Std)))
MIA_STL_Normalized = float(np.sum(((MIA_Defence.loc[:, ['STL']] - STL_Mean) / STL_Std)))
MIA_BLK_Normalized = float(np.sum(((MIA_Defence.loc[:, ['BLK']] - BLK_Mean) / BLK_Std)))
MIA_PF_Normalized = float(np.sum(((MIA_Defence.loc[:, ['PF']] - PF_Mean) / PF_Std)))
MIA_TOV_Normalized = float(np.sum(((MIA_Defence.loc[:, ['TOV']] - TOV_Mean) / TOV_Std)))

# Charlotte Offence Normalized
CHO_FG_Normalized = float(np.sum(((CHO_Offence.loc[:, ['FG']] - FG_Mean) / FG_Std)))
CHO_ThreeP_Normalized = float(np.sum(((CHO_Offence.loc[:, ['3P']] - ThreeP_Mean) / ThreeP_Std)))
CHO_TwoP_Normalized = float(np.sum(((CHO_Offence.loc[:, ['2P']] - TwoP_Mean) / TwoP_Std)))
CHO_ORB_Normalized = float(np.sum(((CHO_Offence.loc[:, ['ORB']] - ORB_Mean) / ORB_Std)))
CHO_FT_Normalized = float(np.sum(((CHO_Offence.loc[:, ['FT']] - FT_Mean) / FT_Std)))

# Charlotte Defence Normalized
CHO_DRB_Normalized = float(np.sum(((CHO_Defence.loc[:, ['DRB']] - DRB_Mean) / DRB_Std)))
CHO_STL_Normalized = float(np.sum(((CHO_Defence.loc[:, ['STL']] - STL_Mean) / STL_Std)))
CHO_BLK_Normalized = float(np.sum(((CHO_Defence.loc[:, ['BLK']] - BLK_Mean) / BLK_Std)))
CHO_PF_Normalized = float(np.sum(((CHO_Defence.loc[:, ['PF']] - PF_Mean) / PF_Std)))
CHO_TOV_Normalized = float(np.sum(((CHO_Defence.loc[:, ['TOV']] - TOV_Mean) / TOV_Std)))

# Memphis Offence Normalized
MEM_FG_Normalized = float(np.sum(((MEM_Offence.loc[:, ['FG']] - FG_Mean) / FG_Std)))
MEM_ThreeP_Normalized = float(np.sum(((MEM_Offence.loc[:, ['3P']] - ThreeP_Mean) / ThreeP_Std)))
MEM_TwoP_Normalized = float(np.sum(((MEM_Offence.loc[:, ['2P']] - TwoP_Mean) / TwoP_Std)))
MEM_ORB_Normalized = float(np.sum(((MEM_Offence.loc[:, ['ORB']] - ORB_Mean) / ORB_Std)))
MEM_FT_Normalized = float(np.sum(((MEM_Offence.loc[:, ['FT']] - FT_Mean) / FT_Std)))

# Memphis Defence Normalized
MEM_DRB_Normalized = float(np.sum(((MEM_Defence.loc[:, ['DRB']] - DRB_Mean) / DRB_Std)))
MEM_STL_Normalized = float(np.sum(((MEM_Defence.loc[:, ['STL']] - STL_Mean) / STL_Std)))
MEM_BLK_Normalized = float(np.sum(((MEM_Defence.loc[:, ['BLK']] - BLK_Mean) / BLK_Std)))
MEM_PF_Normalized = float(np.sum(((MEM_Defence.loc[:, ['PF']] - PF_Mean) / PF_Std)))
MEM_TOV_Normalized = float(np.sum(((MEM_Defence.loc[:, ['TOV']] - TOV_Mean) / TOV_Std)))

# New Orleans Offence Normalized
NOP_FG_Normalized = float(np.sum(((NOP_Offence.loc[:, ['FG']] - FG_Mean) / FG_Std)))
NOP_ThreeP_Normalized = float(np.sum(((NOP_Offence.loc[:, ['3P']] - ThreeP_Mean) / ThreeP_Std)))
NOP_TwoP_Normalized = float(np.sum(((NOP_Offence.loc[:, ['2P']] - TwoP_Mean) / TwoP_Std)))
NOP_ORB_Normalized = float(np.sum(((NOP_Offence.loc[:, ['ORB']] - ORB_Mean) / ORB_Std)))
NOP_FT_Normalized = float(np.sum(((NOP_Offence.loc[:, ['FT']] - FT_Mean) / FT_Std)))

# New Orleans Defence Normalized
NOP_DRB_Normalized = float(np.sum(((NOP_Defence.loc[:, ['DRB']] - DRB_Mean) / DRB_Std)))
NOP_STL_Normalized = float(np.sum(((NOP_Defence.loc[:, ['STL']] - STL_Mean) / STL_Std)))
NOP_BLK_Normalized = float(np.sum(((NOP_Defence.loc[:, ['BLK']] - BLK_Mean) / BLK_Std)))
NOP_PF_Normalized = float(np.sum(((NOP_Defence.loc[:, ['PF']] - PF_Mean) / PF_Std)))
NOP_TOV_Normalized = float(np.sum(((NOP_Defence.loc[:, ['TOV']] - TOV_Mean) / TOV_Std)))

# Houston Offence Normalized
HOU_FG_Normalized = float(np.sum(((HOU_Offence.loc[:, ['FG']] - FG_Mean) / FG_Std)))
HOU_ThreeP_Normalized = float(np.sum(((HOU_Offence.loc[:, ['3P']] - ThreeP_Mean) / ThreeP_Std)))
HOU_TwoP_Normalized = float(np.sum(((HOU_Offence.loc[:, ['2P']] - TwoP_Mean) / TwoP_Std)))
HOU_ORB_Normalized = float(np.sum(((HOU_Offence.loc[:, ['ORB']] - ORB_Mean) / ORB_Std)))
HOU_FT_Normalized = float(np.sum(((HOU_Offence.loc[:, ['FT']] - FT_Mean) / FT_Std)))

# Houston Defence Normalized
HOU_DRB_Normalized = float(np.sum(((HOU_Defence.loc[:, ['DRB']] - DRB_Mean) / DRB_Std)))
HOU_STL_Normalized = float(np.sum(((HOU_Defence.loc[:, ['STL']] - STL_Mean) / STL_Std)))
HOU_BLK_Normalized = float(np.sum(((HOU_Defence.loc[:, ['BLK']] - BLK_Mean) / BLK_Std)))
HOU_PF_Normalized = float(np.sum(((HOU_Defence.loc[:, ['PF']] - PF_Mean) / PF_Std)))
HOU_TOV_Normalized = float(np.sum(((HOU_Defence.loc[:, ['TOV']] - TOV_Mean) / TOV_Std)))

# San Antonio Offence Normalized
SAS_FG_Normalized = float(np.sum(((SAS_Offence.loc[:, ['FG']] - FG_Mean) / FG_Std)))
SAS_ThreeP_Normalized = float(np.sum(((SAS_Offence.loc[:, ['3P']] - ThreeP_Mean) / ThreeP_Std)))
SAS_TwoP_Normalized = float(np.sum(((SAS_Offence.loc[:, ['2P']] - TwoP_Mean) / TwoP_Std)))
SAS_ORB_Normalized = float(np.sum(((SAS_Offence.loc[:, ['ORB']] - ORB_Mean) / ORB_Std)))
SAS_FT_Normalized = float(np.sum(((SAS_Offence.loc[:, ['FT']] - FT_Mean) / FT_Std)))

# San Antonio Defence Normalized
SAS_DRB_Normalized = float(np.sum(((SAS_Defence.loc[:, ['DRB']] - DRB_Mean) / DRB_Std)))
SAS_STL_Normalized = float(np.sum(((SAS_Defence.loc[:, ['STL']] - STL_Mean) / STL_Std)))
SAS_BLK_Normalized = float(np.sum(((SAS_Defence.loc[:, ['BLK']] - BLK_Mean) / BLK_Std)))
SAS_PF_Normalized = float(np.sum(((SAS_Defence.loc[:, ['PF']] - PF_Mean) / PF_Std)))
SAS_TOV_Normalized = float(np.sum(((SAS_Defence.loc[:, ['TOV']] - TOV_Mean) / TOV_Std)))

# Dallas Offence Normalized
DAL_FG_Normalized = float(np.sum(((DAL_Offence.loc[:, ['FG']] - FG_Mean) / FG_Std)))
DAL_ThreeP_Normalized = float(np.sum(((DAL_Offence.loc[:, ['3P']] - ThreeP_Mean) / ThreeP_Std)))
DAL_TwoP_Normalized = float(np.sum(((DAL_Offence.loc[:, ['2P']] - TwoP_Mean) / TwoP_Std)))
DAL_ORB_Normalized = float(np.sum(((DAL_Offence.loc[:, ['ORB']] - ORB_Mean) / ORB_Std)))
DAL_FT_Normalized = float(np.sum(((DAL_Offence.loc[:, ['FT']] - FT_Mean) / FT_Std)))

# Dallas Defence Normalized
DAL_DRB_Normalized = float(np.sum(((DAL_Defence.loc[:, ['DRB']] - DRB_Mean) / DRB_Std)))
DAL_STL_Normalized = float(np.sum(((DAL_Defence.loc[:, ['STL']] - STL_Mean) / STL_Std)))
DAL_BLK_Normalized = float(np.sum(((DAL_Defence.loc[:, ['BLK']] - BLK_Mean) / BLK_Std)))
DAL_PF_Normalized = float(np.sum(((DAL_Defence.loc[:, ['PF']] - PF_Mean) / PF_Std)))
DAL_TOV_Normalized = float(np.sum(((DAL_Defence.loc[:, ['TOV']] - TOV_Mean) / TOV_Std)))

# Normalized Weighted Averages:

def offence_function(ThreeP, TwoP, FG, FT, ORB):
    final_result = ( 0.5 * ThreeP) + ( 0.25 * TwoP ) + \
                   ( 0.1 * FG ) + ( 0.1 * FT ) + ( 0.05 * ORB )
    return final_result

def defence_function(Stl, Blk, Drb, Pf, Tov):
    final_result = ( 0.2 * Stl ) + ( 0.1 * Blk ) + \
                   ( 0.1 * Drb ) - ((0.3 * Pf) + (0.3 * Tov))
    return final_result

# Boston Offence Normalized
BOS_Offence_Weighted_Avg = offence_function(BOS_ThreeP_Normalized,
                                            BOS_TwoP_Normalized,
                                            BOS_FG_Normalized,
                                            BOS_FT_Normalized,
                                            BOS_ORB_Normalized)

# Boston Defence Normalized
BOS_Defence_Weighted_Avg = defence_function(BOS_STL_Normalized,
                                            BOS_BLK_Normalized,
                                            BOS_DRB_Normalized,
                                            BOS_PF_Normalized,
                                            BOS_TOV_Normalized)

# Brooklyn Offence Normalized
BRK_Offence_Weighted_Avg = offence_function(BRK_ThreeP_Normalized,
                                            BRK_TwoP_Normalized,
                                            BRK_FG_Normalized,
                                            BRK_FT_Normalized,
                                            BRK_ORB_Normalized)

# Brooklyn Defence Normalized
BRK_Defence_Weighted_Avg = defence_function(BRK_STL_Normalized,
                                            BRK_BLK_Normalized,
                                            BRK_DRB_Normalized,
                                            BRK_PF_Normalized,
                                            BRK_TOV_Normalized)

# Toronto Offence Normalized
TOR_Offence_Weighted_Avg = offence_function(TOR_ThreeP_Normalized,
                                            TOR_TwoP_Normalized,
                                            TOR_FG_Normalized,
                                            TOR_FT_Normalized,
                                            TOR_ORB_Normalized)

# Toronto Defence Normalized
TOR_Defence_Weighted_Avg = defence_function(TOR_STL_Normalized,
                                            TOR_BLK_Normalized,
                                            TOR_DRB_Normalized,
                                            TOR_PF_Normalized,
                                            TOR_TOV_Normalized)

# Philidelphia Offence Normalized
PHI_Offence_Weighted_Avg = offence_function(PHI_ThreeP_Normalized,
                                            PHI_TwoP_Normalized,
                                            PHI_FG_Normalized,
                                            PHI_FT_Normalized,
                                            PHI_ORB_Normalized)

# Philidelphia Defence Normalized
PHI_Defence_Weighted_Avg = defence_function(PHI_STL_Normalized,
                                            PHI_BLK_Normalized,
                                            PHI_DRB_Normalized,
                                            PHI_PF_Normalized,
                                            PHI_TOV_Normalized)

# New York Knicks Offence Normalized
NYK_Offence_Weighted_Avg = offence_function(NYK_ThreeP_Normalized,
                                            NYK_TwoP_Normalized,
                                            NYK_FG_Normalized,
                                            NYK_FT_Normalized,
                                            NYK_ORB_Normalized)

# New York Knicks Defence Normalized
NYK_Defence_Weighted_Avg = defence_function(NYK_STL_Normalized,
                                            NYK_BLK_Normalized,
                                            NYK_DRB_Normalized,
                                            NYK_PF_Normalized,
                                            NYK_TOV_Normalized)

# Minnesota Offence Normalized
MIN_Offence_Weighted_Avg = offence_function(MIN_ThreeP_Normalized,
                                            MIN_TwoP_Normalized,
                                            MIN_FG_Normalized,
                                            MIN_FT_Normalized,
                                            MIN_ORB_Normalized)

# Minnesota Defence Normalized
MIN_Defence_Weighted_Avg = defence_function(MIN_STL_Normalized,
                                            MIN_BLK_Normalized,
                                            MIN_DRB_Normalized,
                                            MIN_PF_Normalized,
                                            MIN_TOV_Normalized)

# Oklahoma Offence Normalized
OKC_Offence_Weighted_Avg = offence_function(OKC_ThreeP_Normalized,
                                            OKC_TwoP_Normalized,
                                            OKC_FG_Normalized,
                                            OKC_FT_Normalized,
                                            OKC_ORB_Normalized)

# Oklahoma Defence Normalized
OKC_Defence_Weighted_Avg = defence_function(OKC_STL_Normalized,
                                            OKC_BLK_Normalized,
                                            OKC_DRB_Normalized,
                                            OKC_PF_Normalized,
                                            OKC_TOV_Normalized)

# Denver Offence Normalized
DEN_Offence_Weighted_Avg = offence_function(DEN_ThreeP_Normalized,
                                            DEN_TwoP_Normalized,
                                            DEN_FG_Normalized,
                                            DEN_FT_Normalized,
                                            DEN_ORB_Normalized)

# Denver Defence Normalized
DEN_Defence_Weighted_Avg = defence_function(DEN_STL_Normalized,
                                            DEN_BLK_Normalized,
                                            DEN_DRB_Normalized,
                                            DEN_PF_Normalized,
                                            DEN_TOV_Normalized)

# Portland Offence Normalized
POR_Offence_Weighted_Avg = offence_function(POR_ThreeP_Normalized,
                                            POR_TwoP_Normalized,
                                            POR_FG_Normalized,
                                            POR_FT_Normalized,
                                            POR_ORB_Normalized)

# Portland Defence Normalized
POR_Defence_Weighted_Avg = defence_function(POR_STL_Normalized,
                                            POR_BLK_Normalized,
                                            POR_DRB_Normalized,
                                            POR_PF_Normalized,
                                            POR_TOV_Normalized)

# Utah Offence Normalized
UTA_Offence_Weighted_Avg = offence_function(UTA_ThreeP_Normalized,
                                            UTA_TwoP_Normalized,
                                            UTA_FG_Normalized,
                                            UTA_FT_Normalized,
                                            UTA_ORB_Normalized)

# Utah Defence Normalized
UTA_Defence_Weighted_Avg = defence_function(UTA_STL_Normalized,
                                            UTA_BLK_Normalized,
                                            UTA_DRB_Normalized,
                                            UTA_PF_Normalized,
                                            UTA_TOV_Normalized)

# Chicago Offence Normalized
CHI_Offence_Weighted_Avg = offence_function(CHI_ThreeP_Normalized,
                                            CHI_TwoP_Normalized,
                                            CHI_FG_Normalized,
                                            CHI_FT_Normalized,
                                            CHI_ORB_Normalized)

# Chicago Defence Normalized
CHI_Defence_Weighted_Avg = defence_function(CHI_STL_Normalized,
                                            CHI_BLK_Normalized,
                                            CHI_DRB_Normalized,
                                            CHI_PF_Normalized,
                                            CHI_TOV_Normalized)

# Cleveland Offence Normalized
CLE_Offence_Weighted_Avg = offence_function(CLE_ThreeP_Normalized,
                                            CLE_TwoP_Normalized,
                                            CLE_FG_Normalized,
                                            CLE_FT_Normalized,
                                            CLE_ORB_Normalized)

# Cleveland Defence Normalized
CLE_Defence_Weighted_Avg = defence_function(CLE_STL_Normalized,
                                            CLE_BLK_Normalized,
                                            CLE_DRB_Normalized,
                                            CLE_PF_Normalized,
                                            CLE_TOV_Normalized)

# Detroit Offence Normalized
DET_Offence_Weighted_Avg = offence_function(DET_ThreeP_Normalized,
                                            DET_TwoP_Normalized,
                                            DET_FG_Normalized,
                                            DET_FT_Normalized,
                                            DET_ORB_Normalized)

# Detroit Defence Normalized
DET_Defence_Weighted_Avg = defence_function(DET_STL_Normalized,
                                            DET_BLK_Normalized,
                                            DET_DRB_Normalized,
                                            DET_PF_Normalized,
                                            DET_TOV_Normalized)

# Indiana Offence Normalized
IND_Offence_Weighted_Avg = offence_function(IND_ThreeP_Normalized,
                                            IND_TwoP_Normalized,
                                            IND_FG_Normalized,
                                            IND_FT_Normalized,
                                            IND_ORB_Normalized)

# Indiana Defence Normalized
IND_Defence_Weighted_Avg = defence_function(IND_STL_Normalized,
                                            IND_BLK_Normalized,
                                            IND_DRB_Normalized,
                                            IND_PF_Normalized,
                                            IND_TOV_Normalized)

# Milwaukee Offence Normalized
MIL_Offence_Weighted_Avg = offence_function(MIL_ThreeP_Normalized,
                                            MIL_TwoP_Normalized,
                                            MIL_FG_Normalized,
                                            MIL_FT_Normalized,
                                            MIL_ORB_Normalized)

# Milwaukee Defence Normalized
MIL_Defence_Weighted_Avg = defence_function(MIL_STL_Normalized,
                                            MIL_BLK_Normalized,
                                            MIL_DRB_Normalized,
                                            MIL_PF_Normalized,
                                            MIL_TOV_Normalized)

# Los Angeles Lakers Offence Normalized
LAL_Offence_Weighted_Avg = offence_function(LAL_ThreeP_Normalized,
                                            LAL_TwoP_Normalized,
                                            LAL_FG_Normalized,
                                            LAL_FT_Normalized,
                                            LAL_ORB_Normalized)

# Los Angeles Lakers Defence Normalized
LAL_Defence_Weighted_Avg = defence_function(LAL_STL_Normalized,
                                            LAL_BLK_Normalized,
                                            LAL_DRB_Normalized,
                                            LAL_PF_Normalized,
                                            LAL_TOV_Normalized)

# Los Angeles Clippers Offence Normalized
LAC_Offence_Weighted_Avg = offence_function(LAC_ThreeP_Normalized,
                                            LAC_TwoP_Normalized,
                                            LAC_FG_Normalized,
                                            LAC_FT_Normalized,
                                            LAC_ORB_Normalized)

# Los Angeles Clippers Defence Normalized
LAC_Defence_Weighted_Avg = defence_function(LAC_STL_Normalized,
                                            LAC_BLK_Normalized,
                                            LAC_DRB_Normalized,
                                            LAC_PF_Normalized,
                                            LAC_TOV_Normalized)

# Golden State Offence Normalized
GSW_Offence_Weighted_Avg = offence_function(GSW_ThreeP_Normalized,
                                            GSW_TwoP_Normalized,
                                            GSW_FG_Normalized,
                                            GSW_FT_Normalized,
                                            GSW_ORB_Normalized)

# Golden State Defence Normalized
GSW_Defence_Weighted_Avg = defence_function(GSW_STL_Normalized,
                                            GSW_BLK_Normalized,
                                            GSW_DRB_Normalized,
                                            GSW_PF_Normalized,
                                            GSW_TOV_Normalized)

# Phoenix Offence Normalized
PHO_Offence_Weighted_Avg = offence_function(PHO_ThreeP_Normalized,
                                            PHO_TwoP_Normalized,
                                            PHO_FG_Normalized,
                                            PHO_FT_Normalized,
                                            PHO_ORB_Normalized)

# Phoenix Defence Normalized
PHO_Defence_Weighted_Avg = defence_function(PHO_STL_Normalized,
                                            PHO_BLK_Normalized,
                                            PHO_DRB_Normalized,
                                            PHO_PF_Normalized,
                                            PHO_TOV_Normalized)

# Sacramento Offence Normalized
SAC_Offence_Weighted_Avg = offence_function(SAC_ThreeP_Normalized,
                                            SAC_TwoP_Normalized,
                                            SAC_FG_Normalized,
                                            SAC_FT_Normalized,
                                            SAC_ORB_Normalized)

# Sacramento Defence Normalized
SAC_Defence_Weighted_Avg = defence_function(SAC_STL_Normalized,
                                            SAC_BLK_Normalized,
                                            SAC_DRB_Normalized,
                                            SAC_PF_Normalized,
                                            SAC_TOV_Normalized)

# Washington Offence Normalized
WAS_Offence_Weighted_Avg = offence_function(WAS_ThreeP_Normalized,
                                            WAS_TwoP_Normalized,
                                            WAS_FG_Normalized,
                                            WAS_FT_Normalized,
                                            WAS_ORB_Normalized)

# Washington Defence Normalized
WAS_Defence_Weighted_Avg = defence_function(WAS_STL_Normalized,
                                            WAS_BLK_Normalized,
                                            WAS_DRB_Normalized,
                                            WAS_PF_Normalized,
                                            WAS_TOV_Normalized)

# Atlanta Offence Normalized
ATL_Offence_Weighted_Avg = offence_function(ATL_ThreeP_Normalized,
                                            ATL_TwoP_Normalized,
                                            ATL_FG_Normalized,
                                            ATL_FT_Normalized,
                                            ATL_ORB_Normalized)

# Atlanta Defence Normalized
ATL_Defence_Weighted_Avg = defence_function(ATL_STL_Normalized,
                                            ATL_BLK_Normalized,
                                            ATL_DRB_Normalized,
                                            ATL_PF_Normalized,
                                            ATL_TOV_Normalized)

# Orlando Offence Normalized
ORL_Offence_Weighted_Avg = offence_function(ORL_ThreeP_Normalized,
                                            ORL_TwoP_Normalized,
                                            ORL_FG_Normalized,
                                            ORL_FT_Normalized,
                                            ORL_ORB_Normalized)

# Orlando Defence Normalized
ORL_Defence_Weighted_Avg = defence_function(ORL_STL_Normalized,
                                            ORL_BLK_Normalized,
                                            ORL_DRB_Normalized,
                                            ORL_PF_Normalized,
                                            ORL_TOV_Normalized)

# Miami Offence Normalized
MIA_Offence_Weighted_Avg = offence_function(MIA_ThreeP_Normalized,
                                            MIA_TwoP_Normalized,
                                            MIA_FG_Normalized,
                                            MIA_FT_Normalized,
                                            MIA_ORB_Normalized)

# Miami Defence Normalized
MIA_Defence_Weighted_Avg = defence_function(MIA_STL_Normalized,
                                            MIA_BLK_Normalized,
                                            MIA_DRB_Normalized,
                                            MIA_PF_Normalized,
                                            MIA_TOV_Normalized)

# Charlotte Offence Normalized
CHO_Offence_Weighted_Avg = offence_function(CHO_ThreeP_Normalized,
                                            CHO_TwoP_Normalized,
                                            CHO_FG_Normalized,
                                            CHO_FT_Normalized,
                                            CHO_ORB_Normalized)

# Charlotte Defence Normalized
CHO_Defence_Weighted_Avg = defence_function(CHO_STL_Normalized,
                                            CHO_BLK_Normalized,
                                            CHO_DRB_Normalized,
                                            CHO_PF_Normalized,
                                            CHO_TOV_Normalized)
# Memphis Offence Normalized
MEM_Offence_Weighted_Avg = offence_function(MEM_ThreeP_Normalized,
                                            MEM_TwoP_Normalized,
                                            MEM_FG_Normalized,
                                            MEM_FT_Normalized,
                                            MEM_ORB_Normalized)

# Memphis Defence Normalized
MEM_Defence_Weighted_Avg = defence_function(MEM_STL_Normalized,
                                            MEM_BLK_Normalized,
                                            MEM_DRB_Normalized,
                                            MEM_PF_Normalized,
                                            MEM_TOV_Normalized)

# New Orleans Offence Normalized
NOP_Offence_Weighted_Avg = offence_function(NOP_ThreeP_Normalized,
                                            NOP_TwoP_Normalized,
                                            NOP_FG_Normalized,
                                            NOP_FT_Normalized,
                                            NOP_ORB_Normalized)

# New Orleans Defence Normalized
NOP_Defence_Weighted_Avg = defence_function(NOP_STL_Normalized,
                                            NOP_BLK_Normalized,
                                            NOP_DRB_Normalized,
                                            NOP_PF_Normalized,
                                            NOP_TOV_Normalized)

# Houston Offence Normalized
HOU_Offence_Weighted_Avg = offence_function(HOU_ThreeP_Normalized,
                                            HOU_TwoP_Normalized,
                                            HOU_FG_Normalized,
                                            HOU_FT_Normalized,
                                            HOU_ORB_Normalized)

# Houston Defence Normalized
HOU_Defence_Weighted_Avg = defence_function(HOU_STL_Normalized,
                                            HOU_BLK_Normalized,
                                            HOU_DRB_Normalized,
                                            HOU_PF_Normalized,
                                            HOU_TOV_Normalized)

# San Antonio Offence Normalized
SAS_Offence_Weighted_Avg = offence_function(SAS_ThreeP_Normalized,
                                            SAS_TwoP_Normalized,
                                            SAS_FG_Normalized,
                                            SAS_FT_Normalized,
                                            SAS_ORB_Normalized)

# San Antonio Defence Normalized
SAS_Defence_Weighted_Avg = defence_function(SAS_STL_Normalized,
                                            SAS_BLK_Normalized,
                                            SAS_DRB_Normalized,
                                            SAS_PF_Normalized,
                                            SAS_TOV_Normalized)

# Dallas Offence Normalized
DAL_Offence_Weighted_Avg = offence_function(DAL_ThreeP_Normalized,
                                            DAL_TwoP_Normalized,
                                            DAL_FG_Normalized,
                                            DAL_FT_Normalized,
                                            DAL_ORB_Normalized)
# Dallas Defence Normalized
DAL_Defence_Weighted_Avg = defence_function(DAL_STL_Normalized,
                                            DAL_BLK_Normalized,
                                            DAL_DRB_Normalized,
                                            DAL_PF_Normalized,
                                            DAL_TOV_Normalized)