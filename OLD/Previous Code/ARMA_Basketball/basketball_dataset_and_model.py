from packages import pd, np, ARIMA, warnings

warnings.filterwarnings('ignore', message='Non-invertible starting MA parameters found.')

season_year = '2022'
first_chosen_team = input('Please Select the First Team')
second_chosen_team = input('Please Select the Second Team')

# Normalization function & AR-MA function

def normalization(df):
    lagged_values = df['Tm'].apply(lambda x : float(x)).shift(1)
    regular_df = df['Tm'].apply(lambda x : float(x))
    normalized_df = np.log( regular_df / lagged_values )
    return pd.DataFrame( normalized_df )

# Redo the entire code below to only use this function.
def data_set_model(link):
    points_df = pd.read_html(link)
    main_df = pd.DataFrame(points_df[0])
    main_df = main_df[(main_df['Unnamed: 4'] == 'Box Score')]
    main_df = main_df.loc[:, ['Tm']].reset_index(drop=True)
    ARIMA_Model = ARIMA(main_df.loc[:, ['Tm']].astype(int), order=(1, 1, 1)) #Note: (AR,I,MA) & trend = constant
    ARIMA_fit = ARIMA_Model.fit()
    ARIMA_T_plus_one = int(ARIMA_fit.predict(len(main_df)+1))
    return ARIMA_T_plus_one

def selection_function(team_one_selected, team_two_selected):
    if NBA_teams[team_one_selected] > NBA_teams[team_two_selected]:
        print(team_one_selected + " is going to score more points")
    else: print(team_two_selected + " is going to score more points")

NBA_teams = {'BRK': data_set_model('https://www.basketball-reference.com/teams/BRK/' + season_year + '_games.html#games'),
             'PHI': data_set_model('https://www.basketball-reference.com/teams/PHI/' + season_year + '_games.html#games'),
             'BOS': data_set_model('https://www.basketball-reference.com/teams/BOS/' + season_year + '_games.html#games'),
             'TOR': data_set_model('https://www.basketball-reference.com/teams/TOR/' + season_year + '_games.html#games'),
             'NYK': data_set_model('https://www.basketball-reference.com/teams/NYK/' + season_year + '_games.html#games'),
             'UTA': data_set_model('https://www.basketball-reference.com/teams/UTA/' + season_year + '_games.html#games'),
             'DEN': data_set_model('https://www.basketball-reference.com/teams/DEN/' + season_year + '_games.html#games'),
             'MIN': data_set_model('https://www.basketball-reference.com/teams/MIN/' + season_year + '_games.html#games'),
             'POR': data_set_model('https://www.basketball-reference.com/teams/POR/' + season_year + '_games.html#games'),
             'OKC': data_set_model('https://www.basketball-reference.com/teams/OKC/' + season_year + '_games.html#games'),
             'CHI': data_set_model('https://www.basketball-reference.com/teams/CHI/' + season_year + '_games.html#games'),
             'MIL': data_set_model('https://www.basketball-reference.com/teams/MIL/' + season_year + '_games.html#games'),
             'CLE': data_set_model('https://www.basketball-reference.com/teams/CLE/' + season_year + '_games.html#games'),
             'IND': data_set_model('https://www.basketball-reference.com/teams/IND/' + season_year + '_games.html#games'),
             'DET': data_set_model('https://www.basketball-reference.com/teams/DET/' + season_year + '_games.html#games'),
             'GSW': data_set_model('https://www.basketball-reference.com/teams/GSW/' + season_year + '_games.html#games'),
             'PHO': data_set_model('https://www.basketball-reference.com/teams/PHO/' + season_year + '_games.html#games'),
             'LAC': data_set_model('https://www.basketball-reference.com/teams/LAC/' + season_year + '_games.html#games'),
             'LAL': data_set_model('https://www.basketball-reference.com/teams/LAL/' + season_year + '_games.html#games'),
             'SAC': data_set_model('https://www.basketball-reference.com/teams/SAC/' + season_year + '_games.html#games'),
             'WAS': data_set_model('https://www.basketball-reference.com/teams/WAS/' + season_year + '_games.html#games'),
             'MIA': data_set_model('https://www.basketball-reference.com/teams/MIA/' + season_year + '_games.html#games'),
             'CHO': data_set_model('https://www.basketball-reference.com/teams/CHO/' + season_year + '_games.html#games'),
             'ATL': data_set_model('https://www.basketball-reference.com/teams/ATL/' + season_year + '_games.html#games'),
             'ORL': data_set_model('https://www.basketball-reference.com/teams/ORL/' + season_year + '_games.html#games'),
             'MEM': data_set_model('https://www.basketball-reference.com/teams/MEM/' + season_year + '_games.html#games'),
             'DAL': data_set_model('https://www.basketball-reference.com/teams/DAL/' + season_year + '_games.html#games'),
             'SAS': data_set_model('https://www.basketball-reference.com/teams/SAS/' + season_year + '_games.html#games'),
             'HOU': data_set_model('https://www.basketball-reference.com/teams/HOU/' + season_year + '_games.html#games'),
             'NOP': data_set_model('https://www.basketball-reference.com/teams/NOP/' + season_year + '_games.html#games')
}

selection_function(first_chosen_team, second_chosen_team)