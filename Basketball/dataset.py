from packages import pd, np

# Injury Table
Injury = pd.read_html('https://www.basketball-reference.com/friv/injuries.fcgi#injuries')
Injury_df = pd.DataFrame(Injury[0])
Injury_array = np.array(Injury_df['Player']).astype(str)

def injury_function(dataset):
    dataset = dataset[~dataset.isin(Injury_df)]
    dataset.dropna(subset=[('Unnamed: 1')], inplace = True)
    return dataset

season_year = '2022'

team_array = [
    'BOS', 'BRK', 'TOR', 'PHI',
    'NYK', 'MIN', 'OKC', 'DEN',
    'POR', 'UTA', 'CHI', 'CLE',
    'DET', 'IND', 'MIL', 'LAL',
    'LAC', 'GSW', 'PHO', 'SAC',
    'WAS', 'ATL', 'ORL', 'MIA',
    'CHO', 'MEM', 'NOP', 'HOU',
    'SAS', 'DAL'
]

offence_variables_for_average = [
    'FG', '3P', '2P',
    'FT', 'ORB'
]

defence_variables_for_average = [
    'STL', 'BLK', 'DRB',
    'PF', 'TOV'
]

def webscrape_dataset_function(team_array, season_year):
    df = pd.read_html('https://www.basketball-reference.com/teams/' + team_array + '/' + season_year + '.html#advanced')
    team_table_number = 1
    df = pd.DataFrame(df[team_table_number])
    df = injury_function(df)
    df = df.loc[0:12, ['FG', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB',
                       'DRB', 'STL', 'BLK', 'PF', 'TOV']].fillna(0)
    return df

def offence_dataset(df):
    df = df.loc[0:12, offence_variables_for_average]
    return df

def defence_dataset(df):
    df = df.loc[0:12, defence_variables_for_average]
    return df

# Normalized Weighted Averages:

def normalization(df,variable):
    variable_normalzied = float(np.sum(((df.loc[:, [variable]] - pd.DataFrame.mean(df.loc[:, [variable]])) /
                                        pd.DataFrame.std(df.loc[:, [variable]]))))
    return variable_normalzied

def offence_function(FG, ThreeP, TwoP, FT, ORB):
    final_result = ( 0.1 * FG ) + ( 0.5 * ThreeP) + ( 0.25 * TwoP ) + \
                    + ( 0.1 * FT ) + ( 0.05 * ORB )
    return final_result

def defence_function(Stl, Blk, Drb, Pf, Tov):
    final_result = ( 0.2 * Stl ) + ( 0.1 * Blk ) + \
                   ( 0.1 * Drb ) - ((0.3 * Pf) + (0.3 * Tov))
    return final_result

team_dataset_offence = {
    'BOS': offence_dataset(webscrape_dataset_function(team_array[0],season_year=season_year)),
    'BRK': offence_dataset(webscrape_dataset_function(team_array[1],season_year=season_year)),
    'TOR': offence_dataset(webscrape_dataset_function(team_array[2],season_year=season_year)),
    'PHI': offence_dataset(webscrape_dataset_function(team_array[3],season_year=season_year)),
    'NYK': offence_dataset(webscrape_dataset_function(team_array[4],season_year=season_year)),
    'MIN': offence_dataset(webscrape_dataset_function(team_array[5],season_year=season_year)),
    'OKC': offence_dataset(webscrape_dataset_function(team_array[6],season_year=season_year)),
    'DEN': offence_dataset(webscrape_dataset_function(team_array[7],season_year=season_year)),
    'POR': offence_dataset(webscrape_dataset_function(team_array[8],season_year=season_year)),
    'UTA': offence_dataset(webscrape_dataset_function(team_array[9],season_year=season_year)),
    'CHI': offence_dataset(webscrape_dataset_function(team_array[10],season_year=season_year)),
    'CLE': offence_dataset(webscrape_dataset_function(team_array[11],season_year=season_year)),
    'DET': offence_dataset(webscrape_dataset_function(team_array[12],season_year=season_year)),
    'IND': offence_dataset(webscrape_dataset_function(team_array[13],season_year=season_year)),
    'MIL': offence_dataset(webscrape_dataset_function(team_array[14],season_year=season_year)),
    'LAL': offence_dataset(webscrape_dataset_function(team_array[15],season_year=season_year)),
    'LAC': offence_dataset(webscrape_dataset_function(team_array[16],season_year=season_year)),
    'GSW': offence_dataset(webscrape_dataset_function(team_array[17],season_year=season_year)),
    'PHO': offence_dataset(webscrape_dataset_function(team_array[18],season_year=season_year)),
    'SAC': offence_dataset(webscrape_dataset_function(team_array[19],season_year=season_year)),
    'WAS': offence_dataset(webscrape_dataset_function(team_array[20],season_year=season_year)),
    'ATL': offence_dataset(webscrape_dataset_function(team_array[21],season_year=season_year)),
    'ORL': offence_dataset(webscrape_dataset_function(team_array[22],season_year=season_year)),
    'MIA': offence_dataset(webscrape_dataset_function(team_array[23],season_year=season_year)),
    'CHO': offence_dataset(webscrape_dataset_function(team_array[24],season_year=season_year)),
    'MEM': offence_dataset(webscrape_dataset_function(team_array[25],season_year=season_year)),
    'NOP': offence_dataset(webscrape_dataset_function(team_array[26],season_year=season_year)),
    'HOU': offence_dataset(webscrape_dataset_function(team_array[27],season_year=season_year)),
    'SAS': offence_dataset(webscrape_dataset_function(team_array[28],season_year=season_year)),
    'DAL': offence_dataset(webscrape_dataset_function(team_array[29],season_year=season_year))
}
team_dataset_defence = {
    'BOS': defence_dataset(webscrape_dataset_function(team_array[0],season_year=season_year)),
    'BRK': defence_dataset(webscrape_dataset_function(team_array[1],season_year=season_year)),
    'TOR': defence_dataset(webscrape_dataset_function(team_array[2],season_year=season_year)),
    'PHI': defence_dataset(webscrape_dataset_function(team_array[3],season_year=season_year)),
    'NYK': defence_dataset(webscrape_dataset_function(team_array[4],season_year=season_year)),
    'MIN': defence_dataset(webscrape_dataset_function(team_array[5],season_year=season_year)),
    'OKC': defence_dataset(webscrape_dataset_function(team_array[6],season_year=season_year)),
    'DEN': defence_dataset(webscrape_dataset_function(team_array[7],season_year=season_year)),
    'POR': defence_dataset(webscrape_dataset_function(team_array[8],season_year=season_year)),
    'UTA': defence_dataset(webscrape_dataset_function(team_array[9],season_year=season_year)),
    'CHI': defence_dataset(webscrape_dataset_function(team_array[10],season_year=season_year)),
    'CLE': defence_dataset(webscrape_dataset_function(team_array[11],season_year=season_year)),
    'DET': defence_dataset(webscrape_dataset_function(team_array[12],season_year=season_year)),
    'IND': defence_dataset(webscrape_dataset_function(team_array[13],season_year=season_year)),
    'MIL': defence_dataset(webscrape_dataset_function(team_array[14],season_year=season_year)),
    'LAL': defence_dataset(webscrape_dataset_function(team_array[15],season_year=season_year)),
    'LAC': defence_dataset(webscrape_dataset_function(team_array[16],season_year=season_year)),
    'GSW': defence_dataset(webscrape_dataset_function(team_array[17],season_year=season_year)),
    'PHO': defence_dataset(webscrape_dataset_function(team_array[18],season_year=season_year)),
    'SAC': defence_dataset(webscrape_dataset_function(team_array[19],season_year=season_year)),
    'WAS': defence_dataset(webscrape_dataset_function(team_array[20],season_year=season_year)),
    'ATL': defence_dataset(webscrape_dataset_function(team_array[21],season_year=season_year)),
    'ORL': defence_dataset(webscrape_dataset_function(team_array[22],season_year=season_year)),
    'MIA': defence_dataset(webscrape_dataset_function(team_array[23],season_year=season_year)),
    'CHO': defence_dataset(webscrape_dataset_function(team_array[24],season_year=season_year)),
    'MEM': defence_dataset(webscrape_dataset_function(team_array[25],season_year=season_year)),
    'NOP': defence_dataset(webscrape_dataset_function(team_array[26],season_year=season_year)),
    'HOU': defence_dataset(webscrape_dataset_function(team_array[27],season_year=season_year)),
    'SAS': defence_dataset(webscrape_dataset_function(team_array[28],season_year=season_year)),
    'DAL': defence_dataset(webscrape_dataset_function(team_array[29],season_year=season_year))
}
team_final_result = {
    'BOS': offence_function(normalization(team_dataset_offence.get(team_array[0]),offence_variables_for_average[0]),
                            normalization(team_dataset_offence.get(team_array[0]),offence_variables_for_average[1]),
                            normalization(team_dataset_offence.get(team_array[0]),offence_variables_for_average[2]),
                            normalization(team_dataset_offence.get(team_array[0]),offence_variables_for_average[3]),
                            normalization(team_dataset_offence.get(team_array[0]),offence_variables_for_average[4])) +
           defence_function(normalization(team_dataset_defence.get(team_array[0]),defence_variables_for_average[0]),
                            normalization(team_dataset_defence.get(team_array[0]),defence_variables_for_average[1]),
                            normalization(team_dataset_defence.get(team_array[0]),defence_variables_for_average[2]),
                            normalization(team_dataset_defence.get(team_array[0]),defence_variables_for_average[3]),
                            normalization(team_dataset_defence.get(team_array[0]),defence_variables_for_average[4])),
    'BRK': offence_function(normalization(team_dataset_offence.get(team_array[1]),offence_variables_for_average[0]),
                            normalization(team_dataset_offence.get(team_array[1]),offence_variables_for_average[1]),
                            normalization(team_dataset_offence.get(team_array[1]),offence_variables_for_average[2]),
                            normalization(team_dataset_offence.get(team_array[1]),offence_variables_for_average[3]),
                            normalization(team_dataset_offence.get(team_array[1]),offence_variables_for_average[4])) +
           defence_function(normalization(team_dataset_defence.get(team_array[1]),defence_variables_for_average[0]),
                            normalization(team_dataset_defence.get(team_array[1]),defence_variables_for_average[1]),
                            normalization(team_dataset_defence.get(team_array[1]),defence_variables_for_average[2]),
                            normalization(team_dataset_defence.get(team_array[1]),defence_variables_for_average[3]),
                            normalization(team_dataset_defence.get(team_array[1]),defence_variables_for_average[4])),
    'TOR': offence_function(normalization(team_dataset_offence.get(team_array[2]),offence_variables_for_average[0]),
                            normalization(team_dataset_offence.get(team_array[2]),offence_variables_for_average[1]),
                            normalization(team_dataset_offence.get(team_array[2]),offence_variables_for_average[2]),
                            normalization(team_dataset_offence.get(team_array[2]),offence_variables_for_average[3]),
                            normalization(team_dataset_offence.get(team_array[2]),offence_variables_for_average[4])) +
           defence_function(normalization(team_dataset_defence.get(team_array[2]),defence_variables_for_average[0]),
                            normalization(team_dataset_defence.get(team_array[2]),defence_variables_for_average[1]),
                            normalization(team_dataset_defence.get(team_array[2]),defence_variables_for_average[2]),
                            normalization(team_dataset_defence.get(team_array[2]),defence_variables_for_average[3]),
                            normalization(team_dataset_defence.get(team_array[2]),defence_variables_for_average[4])),
    'PHI': offence_function(normalization(team_dataset_offence.get(team_array[3]),offence_variables_for_average[0]),
                            normalization(team_dataset_offence.get(team_array[3]),offence_variables_for_average[1]),
                            normalization(team_dataset_offence.get(team_array[3]),offence_variables_for_average[2]),
                            normalization(team_dataset_offence.get(team_array[3]),offence_variables_for_average[3]),
                            normalization(team_dataset_offence.get(team_array[3]),offence_variables_for_average[4])) +
           defence_function(normalization(team_dataset_defence.get(team_array[3]),defence_variables_for_average[0]),
                            normalization(team_dataset_defence.get(team_array[3]),defence_variables_for_average[1]),
                            normalization(team_dataset_defence.get(team_array[3]),defence_variables_for_average[2]),
                            normalization(team_dataset_defence.get(team_array[3]),defence_variables_for_average[3]),
                            normalization(team_dataset_defence.get(team_array[3]),defence_variables_for_average[4])),
    'NYK': offence_function(normalization(team_dataset_offence.get(team_array[4]),offence_variables_for_average[0]),
                            normalization(team_dataset_offence.get(team_array[4]),offence_variables_for_average[1]),
                            normalization(team_dataset_offence.get(team_array[4]),offence_variables_for_average[2]),
                            normalization(team_dataset_offence.get(team_array[4]),offence_variables_for_average[3]),
                            normalization(team_dataset_offence.get(team_array[4]),offence_variables_for_average[4])) +
           defence_function(normalization(team_dataset_defence.get(team_array[4]),defence_variables_for_average[0]),
                            normalization(team_dataset_defence.get(team_array[4]),defence_variables_for_average[1]),
                            normalization(team_dataset_defence.get(team_array[4]),defence_variables_for_average[2]),
                            normalization(team_dataset_defence.get(team_array[4]),defence_variables_for_average[3]),
                            normalization(team_dataset_defence.get(team_array[4]),defence_variables_for_average[4])),
    'MIN': offence_function(normalization(team_dataset_offence.get(team_array[5]),offence_variables_for_average[0]),
                            normalization(team_dataset_offence.get(team_array[5]),offence_variables_for_average[1]),
                            normalization(team_dataset_offence.get(team_array[5]),offence_variables_for_average[2]),
                            normalization(team_dataset_offence.get(team_array[5]),offence_variables_for_average[3]),
                            normalization(team_dataset_offence.get(team_array[5]),offence_variables_for_average[4])) +
           defence_function(normalization(team_dataset_defence.get(team_array[5]),defence_variables_for_average[0]),
                            normalization(team_dataset_defence.get(team_array[5]),defence_variables_for_average[1]),
                            normalization(team_dataset_defence.get(team_array[5]),defence_variables_for_average[2]),
                            normalization(team_dataset_defence.get(team_array[5]),defence_variables_for_average[3]),
                            normalization(team_dataset_defence.get(team_array[5]),defence_variables_for_average[4])),
    'OKC': offence_function(normalization(team_dataset_offence.get(team_array[6]),offence_variables_for_average[0]),
                            normalization(team_dataset_offence.get(team_array[6]),offence_variables_for_average[1]),
                            normalization(team_dataset_offence.get(team_array[6]),offence_variables_for_average[2]),
                            normalization(team_dataset_offence.get(team_array[6]),offence_variables_for_average[3]),
                            normalization(team_dataset_offence.get(team_array[6]),offence_variables_for_average[4])) +
           defence_function(normalization(team_dataset_defence.get(team_array[6]),defence_variables_for_average[0]),
                            normalization(team_dataset_defence.get(team_array[6]),defence_variables_for_average[1]),
                            normalization(team_dataset_defence.get(team_array[6]),defence_variables_for_average[2]),
                            normalization(team_dataset_defence.get(team_array[6]),defence_variables_for_average[3]),
                            normalization(team_dataset_defence.get(team_array[6]),defence_variables_for_average[4])),
    'DEN': offence_function(normalization(team_dataset_offence.get(team_array[7]),offence_variables_for_average[0]),
                            normalization(team_dataset_offence.get(team_array[7]),offence_variables_for_average[1]),
                            normalization(team_dataset_offence.get(team_array[7]),offence_variables_for_average[2]),
                            normalization(team_dataset_offence.get(team_array[7]),offence_variables_for_average[3]),
                            normalization(team_dataset_offence.get(team_array[7]),offence_variables_for_average[4])) +
           defence_function(normalization(team_dataset_defence.get(team_array[7]),defence_variables_for_average[0]),
                            normalization(team_dataset_defence.get(team_array[7]),defence_variables_for_average[1]),
                            normalization(team_dataset_defence.get(team_array[7]),defence_variables_for_average[2]),
                            normalization(team_dataset_defence.get(team_array[7]),defence_variables_for_average[3]),
                            normalization(team_dataset_defence.get(team_array[7]),defence_variables_for_average[4])),
    'POR': offence_function(normalization(team_dataset_offence.get(team_array[8]),offence_variables_for_average[0]),
                            normalization(team_dataset_offence.get(team_array[8]),offence_variables_for_average[1]),
                            normalization(team_dataset_offence.get(team_array[8]),offence_variables_for_average[2]),
                            normalization(team_dataset_offence.get(team_array[8]),offence_variables_for_average[3]),
                            normalization(team_dataset_offence.get(team_array[8]),offence_variables_for_average[4])) +
           defence_function(normalization(team_dataset_defence.get(team_array[8]),defence_variables_for_average[0]),
                            normalization(team_dataset_defence.get(team_array[8]),defence_variables_for_average[1]),
                            normalization(team_dataset_defence.get(team_array[8]),defence_variables_for_average[2]),
                            normalization(team_dataset_defence.get(team_array[8]),defence_variables_for_average[3]),
                            normalization(team_dataset_defence.get(team_array[8]),defence_variables_for_average[4])),
    'UTA': offence_function(normalization(team_dataset_offence.get(team_array[9]),offence_variables_for_average[0]),
                            normalization(team_dataset_offence.get(team_array[9]),offence_variables_for_average[1]),
                            normalization(team_dataset_offence.get(team_array[9]),offence_variables_for_average[2]),
                            normalization(team_dataset_offence.get(team_array[9]),offence_variables_for_average[3]),
                            normalization(team_dataset_offence.get(team_array[9]),offence_variables_for_average[4])) +
           defence_function(normalization(team_dataset_defence.get(team_array[9]),defence_variables_for_average[0]),
                            normalization(team_dataset_defence.get(team_array[9]),defence_variables_for_average[1]),
                            normalization(team_dataset_defence.get(team_array[9]),defence_variables_for_average[2]),
                            normalization(team_dataset_defence.get(team_array[9]),defence_variables_for_average[3]),
                            normalization(team_dataset_defence.get(team_array[9]),defence_variables_for_average[4])),
    'CHI': offence_function(normalization(team_dataset_offence.get(team_array[10]),offence_variables_for_average[0]),
                            normalization(team_dataset_offence.get(team_array[10]),offence_variables_for_average[1]),
                            normalization(team_dataset_offence.get(team_array[10]),offence_variables_for_average[2]),
                            normalization(team_dataset_offence.get(team_array[10]),offence_variables_for_average[3]),
                            normalization(team_dataset_offence.get(team_array[10]),offence_variables_for_average[4])) +
           defence_function(normalization(team_dataset_defence.get(team_array[10]),defence_variables_for_average[0]),
                            normalization(team_dataset_defence.get(team_array[10]),defence_variables_for_average[1]),
                            normalization(team_dataset_defence.get(team_array[10]),defence_variables_for_average[2]),
                            normalization(team_dataset_defence.get(team_array[10]),defence_variables_for_average[3]),
                            normalization(team_dataset_defence.get(team_array[10]),defence_variables_for_average[4])),
    'CLE': offence_function(normalization(team_dataset_offence.get(team_array[11]),offence_variables_for_average[0]),
                            normalization(team_dataset_offence.get(team_array[11]),offence_variables_for_average[1]),
                            normalization(team_dataset_offence.get(team_array[11]),offence_variables_for_average[2]),
                            normalization(team_dataset_offence.get(team_array[11]),offence_variables_for_average[3]),
                            normalization(team_dataset_offence.get(team_array[11]),offence_variables_for_average[4])) +
           defence_function(normalization(team_dataset_defence.get(team_array[11]),defence_variables_for_average[0]),
                            normalization(team_dataset_defence.get(team_array[11]),defence_variables_for_average[1]),
                            normalization(team_dataset_defence.get(team_array[11]),defence_variables_for_average[2]),
                            normalization(team_dataset_defence.get(team_array[11]),defence_variables_for_average[3]),
                            normalization(team_dataset_defence.get(team_array[11]),defence_variables_for_average[4])),
    'DET': offence_function(normalization(team_dataset_offence.get(team_array[12]),offence_variables_for_average[0]),
                            normalization(team_dataset_offence.get(team_array[12]),offence_variables_for_average[1]),
                            normalization(team_dataset_offence.get(team_array[12]),offence_variables_for_average[2]),
                            normalization(team_dataset_offence.get(team_array[12]),offence_variables_for_average[3]),
                            normalization(team_dataset_offence.get(team_array[12]),offence_variables_for_average[4])) +
           defence_function(normalization(team_dataset_defence.get(team_array[12]),defence_variables_for_average[0]),
                            normalization(team_dataset_defence.get(team_array[12]),defence_variables_for_average[1]),
                            normalization(team_dataset_defence.get(team_array[12]),defence_variables_for_average[2]),
                            normalization(team_dataset_defence.get(team_array[12]),defence_variables_for_average[3]),
                            normalization(team_dataset_defence.get(team_array[12]),defence_variables_for_average[4])),
    'IND': offence_function(normalization(team_dataset_offence.get(team_array[13]),offence_variables_for_average[0]),
                            normalization(team_dataset_offence.get(team_array[13]),offence_variables_for_average[1]),
                            normalization(team_dataset_offence.get(team_array[13]),offence_variables_for_average[2]),
                            normalization(team_dataset_offence.get(team_array[13]),offence_variables_for_average[3]),
                            normalization(team_dataset_offence.get(team_array[13]),offence_variables_for_average[4])) +
           defence_function(normalization(team_dataset_defence.get(team_array[13]),defence_variables_for_average[0]),
                            normalization(team_dataset_defence.get(team_array[13]),defence_variables_for_average[1]),
                            normalization(team_dataset_defence.get(team_array[13]),defence_variables_for_average[2]),
                            normalization(team_dataset_defence.get(team_array[13]),defence_variables_for_average[3]),
                            normalization(team_dataset_defence.get(team_array[13]),defence_variables_for_average[4])),
    'MIL': offence_function(normalization(team_dataset_offence.get(team_array[14]),offence_variables_for_average[0]),
                            normalization(team_dataset_offence.get(team_array[14]),offence_variables_for_average[1]),
                            normalization(team_dataset_offence.get(team_array[14]),offence_variables_for_average[2]),
                            normalization(team_dataset_offence.get(team_array[14]),offence_variables_for_average[3]),
                            normalization(team_dataset_offence.get(team_array[14]),offence_variables_for_average[4])) +
           defence_function(normalization(team_dataset_defence.get(team_array[14]),defence_variables_for_average[0]),
                            normalization(team_dataset_defence.get(team_array[14]),defence_variables_for_average[1]),
                            normalization(team_dataset_defence.get(team_array[14]),defence_variables_for_average[2]),
                            normalization(team_dataset_defence.get(team_array[14]),defence_variables_for_average[3]),
                            normalization(team_dataset_defence.get(team_array[14]),defence_variables_for_average[4])),
    'LAL': offence_function(normalization(team_dataset_offence.get(team_array[15]),offence_variables_for_average[0]),
                            normalization(team_dataset_offence.get(team_array[15]),offence_variables_for_average[1]),
                            normalization(team_dataset_offence.get(team_array[15]),offence_variables_for_average[2]),
                            normalization(team_dataset_offence.get(team_array[15]),offence_variables_for_average[3]),
                            normalization(team_dataset_offence.get(team_array[15]),offence_variables_for_average[4])) +
           defence_function(normalization(team_dataset_defence.get(team_array[15]),defence_variables_for_average[0]),
                            normalization(team_dataset_defence.get(team_array[15]),defence_variables_for_average[1]),
                            normalization(team_dataset_defence.get(team_array[15]),defence_variables_for_average[2]),
                            normalization(team_dataset_defence.get(team_array[15]),defence_variables_for_average[3]),
                            normalization(team_dataset_defence.get(team_array[15]),defence_variables_for_average[4])),
    'LAC': offence_function(normalization(team_dataset_offence.get(team_array[16]),offence_variables_for_average[0]),
                            normalization(team_dataset_offence.get(team_array[16]),offence_variables_for_average[1]),
                            normalization(team_dataset_offence.get(team_array[16]),offence_variables_for_average[2]),
                            normalization(team_dataset_offence.get(team_array[16]),offence_variables_for_average[3]),
                            normalization(team_dataset_offence.get(team_array[16]),offence_variables_for_average[4])) +
           defence_function(normalization(team_dataset_defence.get(team_array[16]),defence_variables_for_average[0]),
                            normalization(team_dataset_defence.get(team_array[16]),defence_variables_for_average[1]),
                            normalization(team_dataset_defence.get(team_array[16]),defence_variables_for_average[2]),
                            normalization(team_dataset_defence.get(team_array[16]),defence_variables_for_average[3]),
                            normalization(team_dataset_defence.get(team_array[16]),defence_variables_for_average[4])),
    'GSW': offence_function(normalization(team_dataset_offence.get(team_array[17]),offence_variables_for_average[0]),
                            normalization(team_dataset_offence.get(team_array[17]),offence_variables_for_average[1]),
                            normalization(team_dataset_offence.get(team_array[17]),offence_variables_for_average[2]),
                            normalization(team_dataset_offence.get(team_array[17]),offence_variables_for_average[3]),
                            normalization(team_dataset_offence.get(team_array[17]),offence_variables_for_average[4])) +
           defence_function(normalization(team_dataset_defence.get(team_array[17]),defence_variables_for_average[0]),
                            normalization(team_dataset_defence.get(team_array[17]),defence_variables_for_average[1]),
                            normalization(team_dataset_defence.get(team_array[17]),defence_variables_for_average[2]),
                            normalization(team_dataset_defence.get(team_array[17]),defence_variables_for_average[3]),
                            normalization(team_dataset_defence.get(team_array[17]),defence_variables_for_average[4])),
    'PHO': offence_function(normalization(team_dataset_offence.get(team_array[18]),offence_variables_for_average[0]),
                            normalization(team_dataset_offence.get(team_array[18]),offence_variables_for_average[1]),
                            normalization(team_dataset_offence.get(team_array[18]),offence_variables_for_average[2]),
                            normalization(team_dataset_offence.get(team_array[18]),offence_variables_for_average[3]),
                            normalization(team_dataset_offence.get(team_array[18]),offence_variables_for_average[4])) +
           defence_function(normalization(team_dataset_defence.get(team_array[18]),defence_variables_for_average[0]),
                            normalization(team_dataset_defence.get(team_array[18]),defence_variables_for_average[1]),
                            normalization(team_dataset_defence.get(team_array[18]),defence_variables_for_average[2]),
                            normalization(team_dataset_defence.get(team_array[18]),defence_variables_for_average[3]),
                            normalization(team_dataset_defence.get(team_array[18]),defence_variables_for_average[4])),
    'SAC': offence_function(normalization(team_dataset_offence.get(team_array[19]),offence_variables_for_average[0]),
                            normalization(team_dataset_offence.get(team_array[19]),offence_variables_for_average[1]),
                            normalization(team_dataset_offence.get(team_array[19]),offence_variables_for_average[2]),
                            normalization(team_dataset_offence.get(team_array[19]),offence_variables_for_average[3]),
                            normalization(team_dataset_offence.get(team_array[19]),offence_variables_for_average[4])) +
           defence_function(normalization(team_dataset_defence.get(team_array[19]),defence_variables_for_average[0]),
                            normalization(team_dataset_defence.get(team_array[19]),defence_variables_for_average[1]),
                            normalization(team_dataset_defence.get(team_array[19]),defence_variables_for_average[2]),
                            normalization(team_dataset_defence.get(team_array[19]),defence_variables_for_average[3]),
                            normalization(team_dataset_defence.get(team_array[19]),defence_variables_for_average[4])),
    'WAS': offence_function(normalization(team_dataset_offence.get(team_array[20]),offence_variables_for_average[0]),
                            normalization(team_dataset_offence.get(team_array[20]),offence_variables_for_average[1]),
                            normalization(team_dataset_offence.get(team_array[20]),offence_variables_for_average[2]),
                            normalization(team_dataset_offence.get(team_array[20]),offence_variables_for_average[3]),
                            normalization(team_dataset_offence.get(team_array[20]),offence_variables_for_average[4])) +
           defence_function(normalization(team_dataset_defence.get(team_array[20]),defence_variables_for_average[0]),
                            normalization(team_dataset_defence.get(team_array[20]),defence_variables_for_average[1]),
                            normalization(team_dataset_defence.get(team_array[20]),defence_variables_for_average[2]),
                            normalization(team_dataset_defence.get(team_array[20]),defence_variables_for_average[3]),
                            normalization(team_dataset_defence.get(team_array[20]),defence_variables_for_average[4])),
    'ATL': offence_function(normalization(team_dataset_offence.get(team_array[21]),offence_variables_for_average[0]),
                            normalization(team_dataset_offence.get(team_array[21]),offence_variables_for_average[1]),
                            normalization(team_dataset_offence.get(team_array[21]),offence_variables_for_average[2]),
                            normalization(team_dataset_offence.get(team_array[21]),offence_variables_for_average[3]),
                            normalization(team_dataset_offence.get(team_array[21]),offence_variables_for_average[4])) +
           defence_function(normalization(team_dataset_defence.get(team_array[21]),defence_variables_for_average[0]),
                            normalization(team_dataset_defence.get(team_array[21]),defence_variables_for_average[1]),
                            normalization(team_dataset_defence.get(team_array[21]),defence_variables_for_average[2]),
                            normalization(team_dataset_defence.get(team_array[21]),defence_variables_for_average[3]),
                            normalization(team_dataset_defence.get(team_array[21]),defence_variables_for_average[4])),
    'ORL': offence_function(normalization(team_dataset_offence.get(team_array[22]),offence_variables_for_average[0]),
                            normalization(team_dataset_offence.get(team_array[22]),offence_variables_for_average[1]),
                            normalization(team_dataset_offence.get(team_array[22]),offence_variables_for_average[2]),
                            normalization(team_dataset_offence.get(team_array[22]),offence_variables_for_average[3]),
                            normalization(team_dataset_offence.get(team_array[22]),offence_variables_for_average[4])) +
           defence_function(normalization(team_dataset_defence.get(team_array[22]),defence_variables_for_average[0]),
                            normalization(team_dataset_defence.get(team_array[22]),defence_variables_for_average[1]),
                            normalization(team_dataset_defence.get(team_array[22]),defence_variables_for_average[2]),
                            normalization(team_dataset_defence.get(team_array[22]),defence_variables_for_average[3]),
                            normalization(team_dataset_defence.get(team_array[22]),defence_variables_for_average[4])),
    'MIA': offence_function(normalization(team_dataset_offence.get(team_array[23]),offence_variables_for_average[0]),
                            normalization(team_dataset_offence.get(team_array[23]),offence_variables_for_average[1]),
                            normalization(team_dataset_offence.get(team_array[23]),offence_variables_for_average[2]),
                            normalization(team_dataset_offence.get(team_array[23]),offence_variables_for_average[3]),
                            normalization(team_dataset_offence.get(team_array[23]),offence_variables_for_average[4])) +
           defence_function(normalization(team_dataset_defence.get(team_array[23]),defence_variables_for_average[0]),
                            normalization(team_dataset_defence.get(team_array[23]),defence_variables_for_average[1]),
                            normalization(team_dataset_defence.get(team_array[23]),defence_variables_for_average[2]),
                            normalization(team_dataset_defence.get(team_array[23]),defence_variables_for_average[3]),
                            normalization(team_dataset_defence.get(team_array[23]),defence_variables_for_average[4])),
    'CHO': offence_function(normalization(team_dataset_offence.get(team_array[24]),offence_variables_for_average[0]),
                            normalization(team_dataset_offence.get(team_array[24]),offence_variables_for_average[1]),
                            normalization(team_dataset_offence.get(team_array[24]),offence_variables_for_average[2]),
                            normalization(team_dataset_offence.get(team_array[24]),offence_variables_for_average[3]),
                            normalization(team_dataset_offence.get(team_array[24]),offence_variables_for_average[4])) +
           defence_function(normalization(team_dataset_defence.get(team_array[24]),defence_variables_for_average[0]),
                            normalization(team_dataset_defence.get(team_array[24]),defence_variables_for_average[1]),
                            normalization(team_dataset_defence.get(team_array[24]),defence_variables_for_average[2]),
                            normalization(team_dataset_defence.get(team_array[24]),defence_variables_for_average[3]),
                            normalization(team_dataset_defence.get(team_array[24]),defence_variables_for_average[4])),
    'MEM': offence_function(normalization(team_dataset_offence.get(team_array[25]),offence_variables_for_average[0]),
                            normalization(team_dataset_offence.get(team_array[25]),offence_variables_for_average[1]),
                            normalization(team_dataset_offence.get(team_array[25]),offence_variables_for_average[2]),
                            normalization(team_dataset_offence.get(team_array[25]),offence_variables_for_average[3]),
                            normalization(team_dataset_offence.get(team_array[25]),offence_variables_for_average[4])) +
           defence_function(normalization(team_dataset_defence.get(team_array[25]),defence_variables_for_average[0]),
                            normalization(team_dataset_defence.get(team_array[25]),defence_variables_for_average[1]),
                            normalization(team_dataset_defence.get(team_array[25]),defence_variables_for_average[2]),
                            normalization(team_dataset_defence.get(team_array[25]),defence_variables_for_average[3]),
                            normalization(team_dataset_defence.get(team_array[25]),defence_variables_for_average[4])),
    'NOP': offence_function(normalization(team_dataset_offence.get(team_array[26]),offence_variables_for_average[0]),
                            normalization(team_dataset_offence.get(team_array[26]),offence_variables_for_average[1]),
                            normalization(team_dataset_offence.get(team_array[26]),offence_variables_for_average[2]),
                            normalization(team_dataset_offence.get(team_array[26]),offence_variables_for_average[3]),
                            normalization(team_dataset_offence.get(team_array[26]),offence_variables_for_average[4])) +
           defence_function(normalization(team_dataset_defence.get(team_array[26]),defence_variables_for_average[0]),
                            normalization(team_dataset_defence.get(team_array[26]),defence_variables_for_average[1]),
                            normalization(team_dataset_defence.get(team_array[26]),defence_variables_for_average[2]),
                            normalization(team_dataset_defence.get(team_array[26]),defence_variables_for_average[3]),
                            normalization(team_dataset_defence.get(team_array[26]),defence_variables_for_average[4])),
    'HOU': offence_function(normalization(team_dataset_offence.get(team_array[27]),offence_variables_for_average[0]),
                            normalization(team_dataset_offence.get(team_array[27]),offence_variables_for_average[1]),
                            normalization(team_dataset_offence.get(team_array[27]),offence_variables_for_average[2]),
                            normalization(team_dataset_offence.get(team_array[27]),offence_variables_for_average[3]),
                            normalization(team_dataset_offence.get(team_array[27]),offence_variables_for_average[4])) +
           defence_function(normalization(team_dataset_defence.get(team_array[27]),defence_variables_for_average[0]),
                            normalization(team_dataset_defence.get(team_array[27]),defence_variables_for_average[1]),
                            normalization(team_dataset_defence.get(team_array[27]),defence_variables_for_average[2]),
                            normalization(team_dataset_defence.get(team_array[27]),defence_variables_for_average[3]),
                            normalization(team_dataset_defence.get(team_array[27]),defence_variables_for_average[4])),
    'SAS': offence_function(normalization(team_dataset_offence.get(team_array[28]),offence_variables_for_average[0]),
                            normalization(team_dataset_offence.get(team_array[28]),offence_variables_for_average[1]),
                            normalization(team_dataset_offence.get(team_array[28]),offence_variables_for_average[2]),
                            normalization(team_dataset_offence.get(team_array[28]),offence_variables_for_average[3]),
                            normalization(team_dataset_offence.get(team_array[28]),offence_variables_for_average[4])) +
           defence_function(normalization(team_dataset_defence.get(team_array[28]), defence_variables_for_average[0]),
                            normalization(team_dataset_defence.get(team_array[28]),defence_variables_for_average[1]),
                            normalization(team_dataset_defence.get(team_array[28]),defence_variables_for_average[2]),
                            normalization(team_dataset_defence.get(team_array[28]),defence_variables_for_average[3]),
                            normalization(team_dataset_defence.get(team_array[28]),defence_variables_for_average[4])),
    'DAL': offence_function(normalization(team_dataset_offence.get(team_array[29]),offence_variables_for_average[0]),
                            normalization(team_dataset_offence.get(team_array[29]),offence_variables_for_average[1]),
                            normalization(team_dataset_offence.get(team_array[29]),offence_variables_for_average[2]),
                            normalization(team_dataset_offence.get(team_array[29]),offence_variables_for_average[3]),
                            normalization(team_dataset_offence.get(team_array[29]),offence_variables_for_average[4])) +
           defence_function(normalization(team_dataset_defence.get(team_array[29]),defence_variables_for_average[0]),
                            normalization(team_dataset_defence.get(team_array[29]),defence_variables_for_average[1]),
                            normalization(team_dataset_defence.get(team_array[29]),defence_variables_for_average[2]),
                            normalization(team_dataset_defence.get(team_array[29]),defence_variables_for_average[3]),
                            normalization(team_dataset_defence.get(team_array[29]),defence_variables_for_average[4]))
}