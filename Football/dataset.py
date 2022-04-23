# This page is to create the dataset needed to predict football (american) games.

from packages import pd, np

team_array_for_website = ['CRD', 'ATL', 'BUF', 'MIA', 'NWE',
                          'NYJ', 'OTI', 'CLT', 'HTX', 'JAX',
                          'PIT', 'RAV', 'CLE', 'CIN', 'KAN',
                          'RAI', 'SDG', 'DEN', 'WAS', 'NYG',
                          'DAL', 'PHI', 'NOR', 'TAM', 'CAR',
                          'GNB', 'CHI', 'MIN', 'DET', 'SEA',
                          'RAM', 'SFO']

team_array = ['ARI', 'ATL', 'BUF', 'MIA', 'NWE',
              'NYJ', 'TEN', 'IND', 'HOU', 'JAX',
              'PIT', 'BAL', 'CLE', 'CIN', 'KAN',
              'LVR', 'LAC', 'DEN', 'WSH', 'NYG',
              'DAL', 'PHI', 'NOR', 'TBB', 'CAR',
              'GNB', 'CHI', 'MIN', 'DET', 'SEA',
              'LAR', 'SFO']

season_year = 2021

def webscrape_data_manipulation_function(team_array_position):
    latest_season = pd.read_html('https://www.pro-football-reference.com/teams/'
                                 + str.lower(team_array_for_website[team_array_position]) + '/'
                                 + str(season_year) + '.htm#passing')[1]
    latest_season_minus_1 = pd.read_html('https://www.pro-football-reference.com/teams/'
                                         + str.lower(team_array_for_website[team_array_position])
                                         + '/' + str(season_year-1) + '.htm#passing')[1]
    latest_season_minus_2 = pd.read_html('https://www.pro-football-reference.com/teams/'
                                         + str.lower(team_array_for_website[team_array_position])
                                         + '/' + str(season_year-2) + '.htm#passing')[1]
    latest_season_minus_3 = pd.read_html('https://www.pro-football-reference.com/teams/'
                                         + str.lower(team_array_for_website[team_array_position])
                                         + '/' + str(season_year-3) + '.htm#passing')[1]
    latest_season_minus_4 = pd.read_html('https://www.pro-football-reference.com/teams/'
                                         + str.lower(team_array_for_website[team_array_position])
                                         + '/' + str(season_year-4) + '.htm#passing')[1]
    df = pd.concat([pd.DataFrame(latest_season_minus_4), pd.DataFrame(latest_season_minus_3),
                    pd.DataFrame(latest_season_minus_2), pd.DataFrame(latest_season_minus_1),
                    pd.DataFrame(latest_season)])
    df = df.get(('Score', 'Tm'))
    df = pd.DataFrame(df).dropna().reset_index(drop=True)
    return df

def normalization(df):
    normalized_values = np.log(df.shift(1) / df)
    normalized_values = normalized_values.dropna()
    normalized_values = normalized_values.replace([np.inf, -np.inf], 0)
    return normalized_values


teams_datasets = {
    'ARI': webscrape_data_manipulation_function(0),
    'ATL': webscrape_data_manipulation_function(1),
    'BUF': webscrape_data_manipulation_function(2),
    'MIA': webscrape_data_manipulation_function(3),
    'NWE': webscrape_data_manipulation_function(4),
    'NYJ': webscrape_data_manipulation_function(5),
    'TEN': webscrape_data_manipulation_function(6),
    'IND': webscrape_data_manipulation_function(7),
    'HOU': webscrape_data_manipulation_function(8),
    'JAX': webscrape_data_manipulation_function(9),
    'PIT': webscrape_data_manipulation_function(10),
    'BAL': webscrape_data_manipulation_function(11),
    'CLE': webscrape_data_manipulation_function(12),
    'CIN': webscrape_data_manipulation_function(13),
    'KAN': webscrape_data_manipulation_function(14),
    'LVR': webscrape_data_manipulation_function(15),
    'LAC': webscrape_data_manipulation_function(16),
    'DEN': webscrape_data_manipulation_function(17),
    'WSH': webscrape_data_manipulation_function(18),
    'NYG': webscrape_data_manipulation_function(19),
    'DAL': webscrape_data_manipulation_function(20),
    'PHI': webscrape_data_manipulation_function(21),
    'NOR': webscrape_data_manipulation_function(22),
    'TBB': webscrape_data_manipulation_function(23),
    'CAR': webscrape_data_manipulation_function(24),
    'GNB': webscrape_data_manipulation_function(25),
    'CHI': webscrape_data_manipulation_function(26),
    'MIN': webscrape_data_manipulation_function(27),
    'DET': webscrape_data_manipulation_function(28),
    'SEA': webscrape_data_manipulation_function(29),
    'LAR': webscrape_data_manipulation_function(30),
    'SFO': webscrape_data_manipulation_function(31)
}
teams_normalized_datasets = {
    'ARI': normalization(teams_datasets.get(team_array[0])),
    'ATL': normalization(teams_datasets.get(team_array[1])),
    'BUF': normalization(teams_datasets.get(team_array[2])),
    'MIA': normalization(teams_datasets.get(team_array[3])),
    'NWE': normalization(teams_datasets.get(team_array[4])),
    'NYJ': normalization(teams_datasets.get(team_array[5])),
    'TEN': normalization(teams_datasets.get(team_array[6])),
    'IND': normalization(teams_datasets.get(team_array[7])),
    'HOU': normalization(teams_datasets.get(team_array[8])),
    'JAX': normalization(teams_datasets.get(team_array[9])),
    'PIT': normalization(teams_datasets.get(team_array[10])),
    'BAL': normalization(teams_datasets.get(team_array[11])),
    'CLE': normalization(teams_datasets.get(team_array[12])),
    'CIN': normalization(teams_datasets.get(team_array[13])),
    'KAN': normalization(teams_datasets.get(team_array[14])),
    'LVR': normalization(teams_datasets.get(team_array[15])),
    'LAC': normalization(teams_datasets.get(team_array[16])),
    'DEN': normalization(teams_datasets.get(team_array[17])),
    'WSH': normalization(teams_datasets.get(team_array[18])),
    'NYG': normalization(teams_datasets.get(team_array[19])),
    'DAL': normalization(teams_datasets.get(team_array[20])),
    'PHI': normalization(teams_datasets.get(team_array[21])),
    'NOR': normalization(teams_datasets.get(team_array[22])),
    'TBB': normalization(teams_datasets.get(team_array[23])),
    'CAR': normalization(teams_datasets.get(team_array[24])),
    'GNB': normalization(teams_datasets.get(team_array[25])),
    'CHI': normalization(teams_datasets.get(team_array[26])),
    'MIN': normalization(teams_datasets.get(team_array[27])),
    'DET': normalization(teams_datasets.get(team_array[28])),
    'SEA': normalization(teams_datasets.get(team_array[29])),
    'LAR': normalization(teams_datasets.get(team_array[30])),
    'SFO': normalization(teams_datasets.get(team_array[31]))
}