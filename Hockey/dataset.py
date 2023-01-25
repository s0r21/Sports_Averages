from utils import *

# Directory & File Name Function
class position_functions:
    def offence_function(df):
        offence = 0.65 * (np.sum(df.loc[0]) + 0.35 * (np.sum(df.loc[1])))
        time_delay
        return offence

    def defence_function(df):
        defence = 0.35 * (np.sum(df.loc[0])) + 0.25 * (np.sum(df.loc[1])) + 0.4 * (np.sum(df.loc[2]))
        time_delay
        return defence

    def goalie_function(df):
        goalie = np.sum(df)
        return goalie
class dataframe_manipulation:
    def offence_dataframe(df, offence_defence_table_number):
        team_df = df[offence_defence_table_number].loc[:len(df[offence_defence_table_number]).__index__()-1,
                  [('Scoring', 'G'), ('Unnamed: 17_level_0', 'S')]]
        time_delay
        return team_df

    def defence_dataframe(df, offence_defence_table_number):
        defence_df = pd.DataFrame(df[offence_defence_table_number])
        team_defence_df = defence_df.loc[:len(df[offence_defence_table_number]).__index__()-1,
                          [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT'),
                           ('Unnamed: 26_level_0', 'FOW'), ('Unnamed: 27_level_0', 'FOL')]]
        team_defence_df['Unnamed: 26_level_0', 'XXX'] = team_defence_df['Unnamed: 26_level_0', 'FOW'] -\
                                                        team_defence_df['Unnamed: 27_level_0', 'FOL']
        team_defence_df.drop(columns=[('Unnamed: 26_level_0', 'FOW'), ('Unnamed: 27_level_0', 'FOL')])
        time_delay
        return team_defence_df

    def goalie_dataframe(df, goalie_table_number):
        team_goalie_df = df[goalie_table_number].loc[0:2, [('Goalie Stats', 'GA')]]
        time_delay
        return team_goalie_df

    def concat_teams(dictionary):
        for i in list(dictionary.keys()):
            df = pd.concat(dictionary.get(i))
            time_delay
            return df

def webscrape_function(team_name, season_year):
    df = pd.read_html('https://www.hockey-reference.com/teams/' + team_name + '/' + season_year + '.html')
    time.sleep(t)
    return df
def normalization_function(df):
    normalized_value = ( df - pd.DataFrame.mean(df) ) / pd.DataFrame.std(df)
    return normalized_value
team_array = ['CAR', 'FLA', 'TBL', 'NSH',
              'DAL', 'CHI', 'CBJ', 'DET',
              'PIT', 'WSH', 'BOS', 'NYI',
              'NYR', 'PHI', 'NJD', 'BUF',
              'TOR', 'EDM', 'WPG', 'MTL',
              'CGY', 'OTT', 'VAN', 'COL',
              'VEG', 'MIN', 'STL', 'ARI',
              'SJS', 'LAK', 'ANA', 'SEA']
team_abbrev = {
    'Boston': 'BOS',
    'Buffalo': 'BUF',
    'Detroit': 'DET',
    'Florida': 'FLA',
    'Montreal': 'MTL',
    'Ottawa': 'OTT',
    'Tampa Bay': 'TBL',
    'Toronto': 'TOR',
    'Carolina': 'CAR',
    'Columbus': 'CBJ',
    'N.Y. Islanders': 'NYI',
    'N.Y. Rangers': 'NYR',
    'New Jersey': 'NJD',
    'Philadelphia': 'PHI',
    'Pittsburgh': 'PIT',
    'Washington': 'WSH',
    'Arizona': 'ARI',
    'Chicago': 'CHI',
    'Colorado': 'COL',
    'Dallas': 'DAL',
    'Minnesota': 'MIN',
    'Nashville': 'NSH',
    'St. Louis': 'STL',
    'Winnipeg': 'WPG',
    'Anaheim': 'ANA',
    'Calgary': 'CGY',
    'Edmonton': 'EDM',
    'Los Angeles': 'LAK',
    'San Jose': 'SJS',
    'Seattle': 'SEA',
    'Vancouver': 'VAN',
    'Vegas': 'VEG'
}

class todays_games:
    todays_date = date.today().strftime("%Y%m%d")
    link_to_todays_games = pd.read_html('https://www.cbssports.com/nhl/schedule/' + todays_date)
    @staticmethod
    def home_teams():
        todays_home_teams_df = todays_games.link_to_todays_games[0]['Home'].map(team_abbrev)
        return todays_home_teams_df
    @staticmethod
    def away_teams():
        todays_away_teams_df = todays_games.link_to_todays_games[0]['Away'].map(team_abbrev)
        return todays_away_teams_df


# Variables to declare the column numbers, season year, and number of players to use for the weighted average.
season_year = '2022'
injury_table_number = 0
no_injury_table = None # in case a team has no injuries
first_offence_defence_table_number = 4
second_offence_defence_table_number = 3
first_goalie_table_number = 5
second_goalie_table_number = 4

# Webscraping the team data
team_datasets = {
    'CAR_df' : webscrape_function(team_array[0], season_year=season_year),
    'FLA_df' : webscrape_function(team_array[1], season_year=season_year),
    'TBL_df' : webscrape_function(team_array[2], season_year=season_year),
    'NSH_df' : webscrape_function(team_array[3], season_year=season_year),
    'DAL_df' : webscrape_function(team_array[4], season_year=season_year),
    'CHI_df' : webscrape_function(team_array[5], season_year=season_year),
    'CBJ_df' : webscrape_function(team_array[6], season_year=season_year),
    'DET_df' : webscrape_function(team_array[7], season_year=season_year),
    'PIT_df' : webscrape_function(team_array[8], season_year=season_year),
    'WSH_df' : webscrape_function(team_array[9], season_year=season_year),
    'BOS_df' : webscrape_function(team_array[10], season_year=season_year),
    'NYI_df' : webscrape_function(team_array[11], season_year=season_year),
    'NYR_df' : webscrape_function(team_array[12], season_year=season_year),
    'PHI_df' : webscrape_function(team_array[13], season_year=season_year),
    'NJD_df' : webscrape_function(team_array[14], season_year=season_year),
    'BUF_df' : webscrape_function(team_array[15], season_year=season_year),
    'TOR_df' : webscrape_function(team_array[16], season_year=season_year),
    'EDM_df' : webscrape_function(team_array[17], season_year=season_year),
    'WPG_df' : webscrape_function(team_array[18], season_year=season_year),
    'MTL_df' : webscrape_function(team_array[19], season_year=season_year),
    'CGY_df' : webscrape_function(team_array[20], season_year=season_year),
    'OTT_df' : webscrape_function(team_array[21], season_year=season_year),
    'VAN_df' : webscrape_function(team_array[22], season_year=season_year),
    'COL_df' : webscrape_function(team_array[23], season_year=season_year),
    'VEG_df' : webscrape_function(team_array[24], season_year=season_year),
    'MIN_df' : webscrape_function(team_array[25], season_year=season_year),
    'STL_df' : webscrape_function(team_array[26], season_year=season_year),
    'ARI_df' : webscrape_function(team_array[27], season_year=season_year),
    'SJS_df' : webscrape_function(team_array[28], season_year=season_year),
    'LAK_df' : webscrape_function(team_array[29], season_year=season_year),
    'ANA_df' : webscrape_function(team_array[30], season_year=season_year),
    'SEA_df' : webscrape_function(team_array[31], season_year=season_year)
}
# Normalization of the data & final weighted averages
final_team_averages = {
    'CAR': float(position_functions.offence_function(normalization_function(
        dataframe_manipulation.offence_dataframe(team_datasets.get('CAR_df'), first_offence_defence_table_number))) +\
           position_functions.defence_function(normalization_function(
               dataframe_manipulation.defence_dataframe(team_datasets.get('CAR_df'), first_offence_defence_table_number))) +\
           position_functions.goalie_function(normalization_function(
               dataframe_manipulation.goalie_dataframe(team_datasets.get('CAR_df'), first_goalie_table_number)))),

    'FLA': float(position_functions.offence_function(normalization_function(
        dataframe_manipulation.offence_dataframe(team_datasets.get('FLA_df'), first_offence_defence_table_number))) +\
           position_functions.defence_function(normalization_function(
               dataframe_manipulation.defence_dataframe(team_datasets.get('FLA_df'), first_offence_defence_table_number))) +\
           position_functions.goalie_function(normalization_function(
               dataframe_manipulation.goalie_dataframe(team_datasets.get('FLA_df'), first_goalie_table_number)))),

    'TBL': float(position_functions.offence_function(normalization_function(
        dataframe_manipulation.offence_dataframe(team_datasets.get('TBL_df'), second_offence_defence_table_number))) +\
           position_functions.defence_function(normalization_function(
               dataframe_manipulation.defence_dataframe(team_datasets.get('TBL_df'), second_offence_defence_table_number))) +\
           position_functions.goalie_function(normalization_function(
               dataframe_manipulation.goalie_dataframe(team_datasets.get('TBL_df'), second_goalie_table_number)))),

    'NSH': float(position_functions.offence_function(normalization_function(
        dataframe_manipulation.offence_dataframe(team_datasets.get('NSH_df'), first_offence_defence_table_number))) +\
           position_functions.defence_function(normalization_function(
               dataframe_manipulation.defence_dataframe(team_datasets.get('NSH_df'), first_offence_defence_table_number))) +\
           position_functions.goalie_function(normalization_function(
               dataframe_manipulation.goalie_dataframe(team_datasets.get('NSH_df'), first_goalie_table_number)))),

    'DAL': float(position_functions.offence_function(normalization_function(
        dataframe_manipulation.offence_dataframe(team_datasets.get('DAL_df'), first_offence_defence_table_number))) +\
           position_functions.defence_function(normalization_function(
               dataframe_manipulation.defence_dataframe(team_datasets.get('DAL_df'), first_offence_defence_table_number))) +\
           position_functions.goalie_function(normalization_function(
               dataframe_manipulation.goalie_dataframe(team_datasets.get('DAL_df'), first_goalie_table_number)))),

    'CHI': float(position_functions.offence_function(normalization_function(
        dataframe_manipulation.offence_dataframe(team_datasets.get('CHI_df'), first_offence_defence_table_number))) +\
           position_functions.defence_function(normalization_function(
               dataframe_manipulation.defence_dataframe(team_datasets.get('CHI_df'), first_offence_defence_table_number))) +\
           position_functions.goalie_function(normalization_function(
               dataframe_manipulation.goalie_dataframe(team_datasets.get('CHI_df'), first_goalie_table_number)))),

    'CBJ': float(position_functions.offence_function(normalization_function(
        dataframe_manipulation.offence_dataframe(team_datasets.get('CBJ_df'), first_offence_defence_table_number))) + \
                 position_functions.defence_function(normalization_function(
                     dataframe_manipulation.defence_dataframe(team_datasets.get('CBJ_df'),
                                                              first_offence_defence_table_number))) + \
                 position_functions.goalie_function(normalization_function(
                     dataframe_manipulation.goalie_dataframe(team_datasets.get('CBJ_df'), first_goalie_table_number)))),

    'DET': float(position_functions.offence_function(normalization_function(
        dataframe_manipulation.offence_dataframe(team_datasets.get('DET_df'), first_offence_defence_table_number))) +\
           position_functions.defence_function(normalization_function(
               dataframe_manipulation.defence_dataframe(team_datasets.get('DET_df'), first_offence_defence_table_number))) +\
           position_functions.goalie_function(normalization_function(
               dataframe_manipulation.goalie_dataframe(team_datasets.get('DET_df'), first_goalie_table_number)))),

    'WSH': float(position_functions.offence_function(normalization_function(
        dataframe_manipulation.offence_dataframe(team_datasets.get('WSH_df'), first_offence_defence_table_number))) +\
           position_functions.defence_function(normalization_function(
               dataframe_manipulation.defence_dataframe(team_datasets.get('WSH_df'), first_offence_defence_table_number))) +\
           position_functions.goalie_function(normalization_function(
               dataframe_manipulation.goalie_dataframe(team_datasets.get('WSH_df'), first_goalie_table_number)))),

    'PIT': float(position_functions.offence_function(normalization_function(
        dataframe_manipulation.offence_dataframe(team_datasets.get('PIT_df'), first_offence_defence_table_number))) +\
           position_functions.defence_function(normalization_function(
               dataframe_manipulation.defence_dataframe(team_datasets.get('PIT_df'), first_offence_defence_table_number))) +\
           position_functions.goalie_function(normalization_function(
               dataframe_manipulation.goalie_dataframe(team_datasets.get('PIT_df'), first_goalie_table_number)))),

    'BOS': float(position_functions.offence_function(normalization_function(
        dataframe_manipulation.offence_dataframe(team_datasets.get('BOS_df'), first_offence_defence_table_number))) +\
           position_functions.defence_function(normalization_function(
               dataframe_manipulation.defence_dataframe(team_datasets.get('BOS_df'), first_offence_defence_table_number))) +\
           position_functions.goalie_function(normalization_function(
               dataframe_manipulation.goalie_dataframe(team_datasets.get('BOS_df'), first_goalie_table_number)))),

    'NYI': float(position_functions.offence_function(normalization_function(
        dataframe_manipulation.offence_dataframe(team_datasets.get('NYI_df'), first_offence_defence_table_number))) +\
           position_functions.defence_function(normalization_function(
               dataframe_manipulation.defence_dataframe(team_datasets.get('NYI_df'), first_offence_defence_table_number))) +\
           position_functions.goalie_function(normalization_function(
               dataframe_manipulation.goalie_dataframe(team_datasets.get('NYI_df'), first_goalie_table_number)))),

    'NYR': float(position_functions.offence_function(normalization_function(
        dataframe_manipulation.offence_dataframe(team_datasets.get('NYR_df'), first_offence_defence_table_number))) +\
           position_functions.defence_function(normalization_function(
               dataframe_manipulation.defence_dataframe(team_datasets.get('NYR_df'), first_offence_defence_table_number))) +\
           position_functions.goalie_function(normalization_function(
               dataframe_manipulation.goalie_dataframe(team_datasets.get('NYR_df'), first_goalie_table_number)))),

    'PHI': float(position_functions.offence_function(normalization_function(
        dataframe_manipulation.offence_dataframe(team_datasets.get('PHI_df'), first_offence_defence_table_number))) +\
           position_functions.defence_function(normalization_function(
               dataframe_manipulation.defence_dataframe(team_datasets.get('PHI_df'), first_offence_defence_table_number))) +\
           position_functions.goalie_function(normalization_function(
               dataframe_manipulation.goalie_dataframe(team_datasets.get('PHI_df'), first_goalie_table_number)))),

    'NJD': float(position_functions.offence_function(normalization_function(
        dataframe_manipulation.offence_dataframe(team_datasets.get('NJD_df'), first_offence_defence_table_number))) +\
           position_functions.defence_function(normalization_function(
               dataframe_manipulation.defence_dataframe(team_datasets.get('NJD_df'), first_offence_defence_table_number))) +\
           position_functions.goalie_function(normalization_function(
               dataframe_manipulation.goalie_dataframe(team_datasets.get('NJD_df'), first_goalie_table_number)))),

    'BUF': float(position_functions.offence_function(normalization_function(
        dataframe_manipulation.offence_dataframe(team_datasets.get('BUF_df'), first_offence_defence_table_number))) +\
           position_functions.defence_function(normalization_function(
               dataframe_manipulation.defence_dataframe(team_datasets.get('BUF_df'), first_offence_defence_table_number))) +\
           position_functions.goalie_function(normalization_function(
               dataframe_manipulation.goalie_dataframe(team_datasets.get('BUF_df'), first_goalie_table_number)))),

    'TOR': float(position_functions.offence_function(normalization_function(
        dataframe_manipulation.offence_dataframe(team_datasets.get('TOR_df'), first_offence_defence_table_number))) +\
           position_functions.defence_function(normalization_function(
               dataframe_manipulation.defence_dataframe(team_datasets.get('TOR_df'), first_offence_defence_table_number))) +\
           position_functions.goalie_function(normalization_function(
               dataframe_manipulation.goalie_dataframe(team_datasets.get('TOR_df'), first_goalie_table_number)))),

    'EDM': float(position_functions.offence_function(normalization_function(
        dataframe_manipulation.offence_dataframe(team_datasets.get('EDM_df'), first_offence_defence_table_number))) +\
           position_functions.defence_function(normalization_function(
               dataframe_manipulation.defence_dataframe(team_datasets.get('EDM_df'), first_offence_defence_table_number))) +\
           position_functions.goalie_function(normalization_function(
               dataframe_manipulation.goalie_dataframe(team_datasets.get('EDM_df'), first_goalie_table_number)))),

    'WPG': float(position_functions.offence_function(normalization_function(
        dataframe_manipulation.offence_dataframe(team_datasets.get('WPG_df'), first_offence_defence_table_number))) +\
           position_functions.defence_function(normalization_function(
               dataframe_manipulation.defence_dataframe(team_datasets.get('WPG_df'), first_offence_defence_table_number))) +\
           position_functions.goalie_function(normalization_function(
               dataframe_manipulation.goalie_dataframe(team_datasets.get('WPG_df'), first_goalie_table_number)))),

    'MTL': float(position_functions.offence_function(normalization_function(
        dataframe_manipulation.offence_dataframe(team_datasets.get('MTL_df'), first_offence_defence_table_number))) +\
           position_functions.defence_function(normalization_function(
               dataframe_manipulation.defence_dataframe(team_datasets.get('MTL_df'), first_offence_defence_table_number))) +\
           position_functions.goalie_function(normalization_function(
               dataframe_manipulation.goalie_dataframe(team_datasets.get('MTL_df'), first_goalie_table_number)))),

    'CGY': float(position_functions.offence_function(normalization_function(
        dataframe_manipulation.offence_dataframe(team_datasets.get('CGY_df'), first_offence_defence_table_number))) +\
           position_functions.defence_function(normalization_function(
               dataframe_manipulation.defence_dataframe(team_datasets.get('CGY_df'), first_offence_defence_table_number))) +\
           position_functions.goalie_function(normalization_function(
               dataframe_manipulation.goalie_dataframe(team_datasets.get('CGY_df'), first_goalie_table_number)))),

    'OTT': float(position_functions.offence_function(normalization_function(
        dataframe_manipulation.offence_dataframe(team_datasets.get('OTT_df'), first_offence_defence_table_number))) +\
           position_functions.defence_function(normalization_function(
               dataframe_manipulation.defence_dataframe(team_datasets.get('OTT_df'), first_offence_defence_table_number))) +\
           position_functions.goalie_function(normalization_function(
               dataframe_manipulation.goalie_dataframe(team_datasets.get('OTT_df'), first_goalie_table_number)))),

    'VAN': float(position_functions.offence_function(normalization_function(
        dataframe_manipulation.offence_dataframe(team_datasets.get('VAN_df'), first_offence_defence_table_number))) +\
           position_functions.defence_function(normalization_function(
               dataframe_manipulation.defence_dataframe(team_datasets.get('VAN_df'), first_offence_defence_table_number))) +\
           position_functions.goalie_function(normalization_function(
               dataframe_manipulation.goalie_dataframe(team_datasets.get('VAN_df'), first_goalie_table_number)))),

    'COL': float(position_functions.offence_function(normalization_function(
        dataframe_manipulation.offence_dataframe(team_datasets.get('COL_df'), first_offence_defence_table_number))) +\
           position_functions.defence_function(normalization_function(
               dataframe_manipulation.defence_dataframe(team_datasets.get('COL_df'), first_offence_defence_table_number))) +\
           position_functions.goalie_function(normalization_function(
               dataframe_manipulation.goalie_dataframe(team_datasets.get('COL_df'), first_goalie_table_number)))),

    'VEG': float(position_functions.offence_function(normalization_function(
        dataframe_manipulation.offence_dataframe(team_datasets.get('VEG_df'), first_offence_defence_table_number))) +\
           position_functions.defence_function(normalization_function(
               dataframe_manipulation.defence_dataframe(team_datasets.get('VEG_df'), first_offence_defence_table_number))) +\
           position_functions.goalie_function(normalization_function(
               dataframe_manipulation.goalie_dataframe(team_datasets.get('VEG_df'), first_goalie_table_number)))),

    'MIN': float(position_functions.offence_function(normalization_function(
        dataframe_manipulation.offence_dataframe(team_datasets.get('MIN_df'), second_offence_defence_table_number))) +\
           position_functions.defence_function(normalization_function(
               dataframe_manipulation.defence_dataframe(team_datasets.get('MIN_df'), second_offence_defence_table_number))) +\
           position_functions.goalie_function(normalization_function(
               dataframe_manipulation.goalie_dataframe(team_datasets.get('MIN_df'), second_goalie_table_number)))),

    'STL': float(position_functions.offence_function(normalization_function(
        dataframe_manipulation.offence_dataframe(team_datasets.get('STL_df'), first_offence_defence_table_number))) +\
           position_functions.defence_function(normalization_function(
               dataframe_manipulation.defence_dataframe(team_datasets.get('STL_df'), first_offence_defence_table_number))) +\
           position_functions.goalie_function(normalization_function(
               dataframe_manipulation.goalie_dataframe(team_datasets.get('STL_df'), first_goalie_table_number)))),

    'ARI': float(position_functions.offence_function(normalization_function(
        dataframe_manipulation.offence_dataframe(team_datasets.get('ARI_df'), first_offence_defence_table_number))) +\
           position_functions.defence_function(normalization_function(
               dataframe_manipulation.defence_dataframe(team_datasets.get('ARI_df'), first_offence_defence_table_number))) +\
           position_functions.goalie_function(normalization_function(
               dataframe_manipulation.goalie_dataframe(team_datasets.get('ARI_df'), first_goalie_table_number)))),

    'SJS': float(position_functions.offence_function(normalization_function(
        dataframe_manipulation.offence_dataframe(team_datasets.get('SJS_df'), first_offence_defence_table_number))) +\
           position_functions.defence_function(normalization_function(
               dataframe_manipulation.defence_dataframe(team_datasets.get('SJS_df'), first_offence_defence_table_number))) +\
           position_functions.goalie_function(normalization_function(
               dataframe_manipulation.goalie_dataframe(team_datasets.get('SJS_df'), first_goalie_table_number)))),

    'LAK': float(position_functions.offence_function(normalization_function(
        dataframe_manipulation.offence_dataframe(team_datasets.get('LAK_df'), first_offence_defence_table_number))) +\
           position_functions.defence_function(normalization_function(
               dataframe_manipulation.defence_dataframe(team_datasets.get('LAK_df'), first_offence_defence_table_number))) +\
           position_functions.goalie_function(normalization_function(
               dataframe_manipulation.goalie_dataframe(team_datasets.get('LAK_df'), first_goalie_table_number)))),

    'ANA': float(position_functions.offence_function(normalization_function(
        dataframe_manipulation.offence_dataframe(team_datasets.get('ANA_df'), first_offence_defence_table_number))) +\
           position_functions.defence_function(normalization_function(
               dataframe_manipulation.defence_dataframe(team_datasets.get('ANA_df'), first_offence_defence_table_number))) +\
           position_functions.goalie_function(normalization_function(
               dataframe_manipulation.goalie_dataframe(team_datasets.get('ANA_df'), first_goalie_table_number)))),

    'SEA': float(position_functions.offence_function(normalization_function(
        dataframe_manipulation.offence_dataframe(team_datasets.get('SEA_df'), first_offence_defence_table_number))) +\
           position_functions.defence_function(normalization_function(
               dataframe_manipulation.defence_dataframe(team_datasets.get('SEA_df'), first_offence_defence_table_number))) +\
           position_functions.goalie_function(normalization_function(
               dataframe_manipulation.goalie_dataframe(team_datasets.get('SEA_df'), first_goalie_table_number))))

}

todays_home_teams_df = todays_games.home_teams()
todays_away_teams_df = todays_games.away_teams()