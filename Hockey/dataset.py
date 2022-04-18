from packages import pd, np

def offence_function(df):
    offence = 0.7 * ( np.sum(df.loc[0]) + 0.3 * (np.sum(df.loc[1]) - np.sum(df.loc[2])) )
    return offence
def defence_function(df):
    defence = 0.1 * (np.sum(df.loc[0])) + 0.1 * (np.sum(df.loc[1])) + 0.8 * (np.sum(df.loc[2]))
    return defence
def goalie_function(df):
    goalie = np.sum(df)
    return goalie
def normalization_function(df):
    normalized_value = ( df - pd.DataFrame.mean(df) ) / pd.DataFrame.std(df)
    return normalized_value

def offence_injury_function(df, offence_list):
    team_injury_df = pd.DataFrame(df[injury_table_number])
    team_injury_array = np.array(team_injury_df['Player']).astype(str)
    dataset = offence_list[~offence_list.isin(team_injury_array)]
    dataset.dropna(subset=[('Unnamed: 1_level_0', 'Player')], inplace = True)
    return dataset
def defence_injury_function(df, defence_list):
    team_injury_df = pd.DataFrame(df[injury_table_number])
    team_injury_array = np.array(team_injury_df['Player']).astype(str)
    dataset = defence_list[~defence_list.isin(team_injury_array)]
    dataset.dropna(subset=[('Unnamed: 1_level_0', 'Player')], inplace = True)
    return dataset
def goalie_injury_function(df, goalie_list):
    team_injury_df = pd.DataFrame(df[injury_table_number])
    team_injury_array = np.array(team_injury_df['Player']).astype(str)
    dataset = goalie_list[~goalie_list.isin(team_injury_array)]
    dataset.dropna(subset=[('Unnamed: 1_level_0', 'Player')], inplace = True)
    return dataset
def offence_dataframe(df, offence_defence_table_number):
    team_df = df[offence_defence_table_number].loc[0:df_cutoff_value,
              [('Scoring', 'G'), ('Unnamed: 26_level_0', 'FOW'), ('Unnamed: 27_level_0', 'FOL')]]
    return team_df
def defence_dataframe(df, offence_defence_table_number):
    defence_df = pd.DataFrame(df[offence_defence_table_number])
    team_defence_df = defence_df.loc[0:df_cutoff_value, [('Unnamed: 24_level_0', 'BLK'),
                                                         ('Unnamed: 25_level_0', 'HIT')]]
    return team_defence_df
def goalie_dataframe(df, goalie_table_number):
    team_goalie_df = df[goalie_table_number].loc[0:2, [('Goalie Stats', 'GA')]]
    return team_goalie_df
def webscrape_function(team_name, season_year):
    df = pd.read_html('https://www.hockey-reference.com/teams/' + team_name + '/' + season_year + '.html')
    return df
def concat_teams(dictionary):
    for i in list(dictionary.keys()):
        df = pd.concat(dictionary.get(i))
        return df

team_array = ['CAR', 'FLA', 'TBL', 'NSH',
              'DAL', 'CHI', 'CBJ', 'DET',
              'PIT', 'WSH', 'BOS', 'NYI',
              'NYR', 'PHI', 'NJD', 'BUF',
              'TOR', 'EDM', 'WPG', 'MTL',
              'CGY', 'OTT', 'VAN', 'COL',
              'VEG', 'MIN', 'STL', 'ARI',
              'SJS', 'LAK', 'ANA', 'SEA'
]

season_year = '2022'
injury_table_number = 0
no_injury_table = None # in case a team has no injuries
first_offence_defence_table_number = 4
second_offence_defence_table_number = 3
first_goalie_table_number = 5
second_goalie_table_number = 4
df_cutoff_value = 12

# Webscraping the team data
class team_datasets:
    CAR_df = webscrape_function(team_array[0], season_year=season_year)
    FLA_df = webscrape_function(team_array[1], season_year=season_year)
    TBL_df = webscrape_function(team_array[2], season_year=season_year)
    NSH_df = webscrape_function(team_array[3], season_year=season_year)
    DAL_df = webscrape_function(team_array[4], season_year=season_year)
    CHI_df = webscrape_function(team_array[5], season_year=season_year)
    CBJ_df = webscrape_function(team_array[6], season_year=season_year)
    DET_df = webscrape_function(team_array[7], season_year=season_year)
    PIT_df = webscrape_function(team_array[8], season_year=season_year)
    WSH_df = webscrape_function(team_array[9], season_year=season_year)
    BOS_df = webscrape_function(team_array[10], season_year=season_year)
    NYI_df = webscrape_function(team_array[11], season_year=season_year)
    NYR_df = webscrape_function(team_array[12], season_year=season_year)
    PHI_df = webscrape_function(team_array[13], season_year=season_year)
    NJD_df = webscrape_function(team_array[14], season_year=season_year)
    BUF_df = webscrape_function(team_array[15], season_year=season_year)
    TOR_df = webscrape_function(team_array[16], season_year=season_year)
    EDM_df = webscrape_function(team_array[17], season_year=season_year)
    WPG_df = webscrape_function(team_array[18], season_year=season_year)
    MTL_df = webscrape_function(team_array[19], season_year=season_year)
    CGY_df = webscrape_function(team_array[20], season_year=season_year)
    OTT_df = webscrape_function(team_array[21], season_year=season_year)
    VAN_df = webscrape_function(team_array[22], season_year=season_year)
    COL_df = webscrape_function(team_array[23], season_year=season_year)
    VEG_df = webscrape_function(team_array[24], season_year=season_year)
    MIN_df = webscrape_function(team_array[25], season_year=season_year)
    STL_df = webscrape_function(team_array[26], season_year=season_year)
    ARI_df = webscrape_function(team_array[27], season_year=season_year)
    SJS_df = webscrape_function(team_array[28], season_year=season_year)
    LAK_df = webscrape_function(team_array[29], season_year=season_year)
    ANA_df = webscrape_function(team_array[30], season_year=season_year)
    SEA_df = webscrape_function(team_array[31], season_year=season_year)

# Normalization of the data & final weighted averages
final_team_averages = {
    'CAR': float(offence_function(normalization_function(offence_dataframe(team_datasets.CAR_df, first_offence_defence_table_number))) +\
           defence_function(normalization_function(defence_dataframe(team_datasets.CAR_df, first_offence_defence_table_number))) +\
           goalie_function(normalization_function(goalie_dataframe(team_datasets.CAR_df, first_goalie_table_number)))),

    'FLA': float(offence_function(normalization_function(offence_dataframe(team_datasets.FLA_df, first_offence_defence_table_number))) +\
           defence_function(normalization_function(defence_dataframe(team_datasets.FLA_df, first_offence_defence_table_number))) +\
           goalie_function(normalization_function(goalie_dataframe(team_datasets.FLA_df, first_goalie_table_number)))),

    'TBL': float(offence_function(normalization_function(offence_dataframe(team_datasets.TBL_df, second_offence_defence_table_number))) +\
           defence_function(normalization_function(defence_dataframe(team_datasets.TBL_df, second_offence_defence_table_number))) +\
           goalie_function(normalization_function(goalie_dataframe(team_datasets.TBL_df, second_goalie_table_number)))),

    'NSH': float(offence_function(normalization_function(offence_dataframe(team_datasets.NSH_df, first_offence_defence_table_number))) +\
           defence_function(normalization_function(defence_dataframe(team_datasets.NSH_df, first_offence_defence_table_number))) +\
           goalie_function(normalization_function(goalie_dataframe(team_datasets.NSH_df, first_goalie_table_number)))),

    'DAL': float(offence_function(normalization_function(offence_dataframe(team_datasets.DAL_df, first_offence_defence_table_number))) +\
           defence_function(normalization_function(defence_dataframe(team_datasets.DAL_df, first_offence_defence_table_number))) +\
           goalie_function(normalization_function(goalie_dataframe(team_datasets.DAL_df, first_goalie_table_number)))),

    'CHI': float(offence_function(normalization_function(offence_dataframe(team_datasets.CHI_df, first_offence_defence_table_number))) +\
           defence_function(normalization_function(defence_dataframe(team_datasets.CHI_df, first_offence_defence_table_number))) +\
           goalie_function(normalization_function(goalie_dataframe(team_datasets.CHI_df, first_goalie_table_number)))),

    'DET': float(offence_function(normalization_function(offence_dataframe(team_datasets.DET_df, first_offence_defence_table_number))) +\
           defence_function(normalization_function(defence_dataframe(team_datasets.DET_df, first_offence_defence_table_number))) +\
           goalie_function(normalization_function(goalie_dataframe(team_datasets.DET_df, first_goalie_table_number)))),

    'WSH': float(offence_function(normalization_function(offence_dataframe(team_datasets.WSH_df, first_offence_defence_table_number))) +\
           defence_function(normalization_function(defence_dataframe(team_datasets.WSH_df, first_offence_defence_table_number))) +\
           goalie_function(normalization_function(goalie_dataframe(team_datasets.WSH_df, first_goalie_table_number)))),

    'PIT': float(offence_function(normalization_function(offence_dataframe(team_datasets.PIT_df, first_offence_defence_table_number))) +\
           defence_function(normalization_function(defence_dataframe(team_datasets.PIT_df, first_offence_defence_table_number))) +\
           goalie_function(normalization_function(goalie_dataframe(team_datasets.PIT_df, first_goalie_table_number)))),

    'BOS': float(offence_function(normalization_function(offence_dataframe(team_datasets.BOS_df, first_offence_defence_table_number))) +\
           defence_function(normalization_function(defence_dataframe(team_datasets.BOS_df, first_offence_defence_table_number))) +\
           goalie_function(normalization_function(goalie_dataframe(team_datasets.BOS_df, first_goalie_table_number)))),

    'NYI': float(offence_function(normalization_function(offence_dataframe(team_datasets.NYI_df, first_offence_defence_table_number))) +\
           defence_function(normalization_function(defence_dataframe(team_datasets.NYI_df, first_offence_defence_table_number))) +\
           goalie_function(normalization_function(goalie_dataframe(team_datasets.NYI_df, first_goalie_table_number)))),

    'NYR': float(offence_function(normalization_function(offence_dataframe(team_datasets.NYR_df, first_offence_defence_table_number))) +\
           defence_function(normalization_function(defence_dataframe(team_datasets.NYR_df, first_offence_defence_table_number))) +\
           goalie_function(normalization_function(goalie_dataframe(team_datasets.NYR_df, first_goalie_table_number)))),

    'PHI': float(offence_function(normalization_function(offence_dataframe(team_datasets.PHI_df, first_offence_defence_table_number))) +\
           defence_function(normalization_function(defence_dataframe(team_datasets.PHI_df, first_offence_defence_table_number))) +\
           goalie_function(normalization_function(goalie_dataframe(team_datasets.PHI_df, first_goalie_table_number)))),

    'NJD': float(offence_function(normalization_function(offence_dataframe(team_datasets.NJD_df, first_offence_defence_table_number))) +\
           defence_function(normalization_function(defence_dataframe(team_datasets.NJD_df, first_offence_defence_table_number))) +\
           goalie_function(normalization_function(goalie_dataframe(team_datasets.NJD_df, first_goalie_table_number)))),

    'BUF': float(offence_function(normalization_function(offence_dataframe(team_datasets.BUF_df, first_offence_defence_table_number))) +\
           defence_function(normalization_function(defence_dataframe(team_datasets.BUF_df, first_offence_defence_table_number))) +\
           goalie_function(normalization_function(goalie_dataframe(team_datasets.BUF_df, first_goalie_table_number)))),

    'TOR': float(offence_function(normalization_function(offence_dataframe(team_datasets.TOR_df, first_offence_defence_table_number))) +\
           defence_function(normalization_function(defence_dataframe(team_datasets.TOR_df, first_offence_defence_table_number))) +\
           goalie_function(normalization_function(goalie_dataframe(team_datasets.TOR_df, first_goalie_table_number)))),

    'EDM': float(offence_function(normalization_function(offence_dataframe(team_datasets.EDM_df, first_offence_defence_table_number))) +\
           defence_function(normalization_function(defence_dataframe(team_datasets.EDM_df, first_offence_defence_table_number))) +\
           goalie_function(normalization_function(goalie_dataframe(team_datasets.EDM_df, first_goalie_table_number)))),

    'WPG': float(offence_function(normalization_function(offence_dataframe(team_datasets.WPG_df, first_offence_defence_table_number))) +\
           defence_function(normalization_function(defence_dataframe(team_datasets.WPG_df, first_offence_defence_table_number))) +\
           goalie_function(normalization_function(goalie_dataframe(team_datasets.WPG_df, first_goalie_table_number)))),

    'MTL': float(offence_function(normalization_function(offence_dataframe(team_datasets.MTL_df, first_offence_defence_table_number))) +\
           defence_function(normalization_function(defence_dataframe(team_datasets.MTL_df, first_offence_defence_table_number))) +\
           goalie_function(normalization_function(goalie_dataframe(team_datasets.MTL_df, first_goalie_table_number)))),

    'CGY': float(offence_function(normalization_function(offence_dataframe(team_datasets.CGY_df, first_offence_defence_table_number))) +\
           defence_function(normalization_function(defence_dataframe(team_datasets.CGY_df, first_offence_defence_table_number))) +\
           goalie_function(normalization_function(goalie_dataframe(team_datasets.CGY_df, first_goalie_table_number)))),

    'OTT': float(offence_function(normalization_function(offence_dataframe(team_datasets.OTT_df, first_offence_defence_table_number))) +\
           defence_function(normalization_function(defence_dataframe(team_datasets.OTT_df, first_offence_defence_table_number))) +\
           goalie_function(normalization_function(goalie_dataframe(team_datasets.OTT_df, first_goalie_table_number)))),

    'VAN': float(offence_function(normalization_function(offence_dataframe(team_datasets.VAN_df, first_offence_defence_table_number))) +\
           defence_function(normalization_function(defence_dataframe(team_datasets.VAN_df, first_offence_defence_table_number))) +\
           goalie_function(normalization_function(goalie_dataframe(team_datasets.VAN_df, first_goalie_table_number)))),

    'COL': float(offence_function(normalization_function(offence_dataframe(team_datasets.COL_df, first_offence_defence_table_number))) +\
           defence_function(normalization_function(defence_dataframe(team_datasets.COL_df, first_offence_defence_table_number))) +\
           goalie_function(normalization_function(goalie_dataframe(team_datasets.COL_df, first_goalie_table_number)))),

    'VEG': float(offence_function(normalization_function(offence_dataframe(team_datasets.VEG_df, first_offence_defence_table_number))) +\
           defence_function(normalization_function(defence_dataframe(team_datasets.VEG_df, first_offence_defence_table_number))) +\
           goalie_function(normalization_function(goalie_dataframe(team_datasets.VEG_df, first_goalie_table_number)))),

    'MIN': float(offence_function(normalization_function(offence_dataframe(team_datasets.MIN_df, first_offence_defence_table_number))) +\
           defence_function(normalization_function(defence_dataframe(team_datasets.MIN_df, first_offence_defence_table_number))) +\
           goalie_function(normalization_function(goalie_dataframe(team_datasets.MIN_df, first_goalie_table_number)))),

    'STL': float(offence_function(normalization_function(offence_dataframe(team_datasets.STL_df, first_offence_defence_table_number))) +\
           defence_function(normalization_function(defence_dataframe(team_datasets.STL_df, first_offence_defence_table_number))) +\
           goalie_function(normalization_function(goalie_dataframe(team_datasets.STL_df, first_goalie_table_number)))),

    'ARI': float(offence_function(normalization_function(offence_dataframe(team_datasets.ARI_df, first_offence_defence_table_number))) +\
           defence_function(normalization_function(defence_dataframe(team_datasets.ARI_df, first_offence_defence_table_number))) +\
           goalie_function(normalization_function(goalie_dataframe(team_datasets.ARI_df, first_goalie_table_number)))),

    'SJS': float(offence_function(normalization_function(offence_dataframe(team_datasets.SJS_df, first_offence_defence_table_number))) +\
           defence_function(normalization_function(defence_dataframe(team_datasets.SJS_df, first_offence_defence_table_number))) +\
           goalie_function(normalization_function(goalie_dataframe(team_datasets.SJS_df, first_goalie_table_number)))),

    'LAK': float(offence_function(normalization_function(offence_dataframe(team_datasets.LAK_df, first_offence_defence_table_number))) +\
           defence_function(normalization_function(defence_dataframe(team_datasets.LAK_df, first_offence_defence_table_number))) +\
           goalie_function(normalization_function(goalie_dataframe(team_datasets.LAK_df, first_goalie_table_number)))),

    'ANA': float(offence_function(normalization_function(offence_dataframe(team_datasets.ANA_df, first_offence_defence_table_number))) +\
           defence_function(normalization_function(defence_dataframe(team_datasets.ANA_df, first_offence_defence_table_number))) +\
           goalie_function(normalization_function(goalie_dataframe(team_datasets.ANA_df, first_goalie_table_number)))),

    'SEA': float(offence_function(normalization_function(offence_dataframe(team_datasets.SEA_df, first_offence_defence_table_number))) +\
           defence_function(normalization_function(defence_dataframe(team_datasets.SEA_df, first_offence_defence_table_number))) +\
           goalie_function(normalization_function(goalie_dataframe(team_datasets.SEA_df, first_goalie_table_number))))

}

