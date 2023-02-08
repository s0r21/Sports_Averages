import pandas as pd

from utils import *

# Injury Table
Injury = pd.read_html('https://www.basketball-reference.com/friv/injuries.fcgi#injuries')
time.sleep(t)
Injury_df = pd.DataFrame(Injury[0])
Injury_array = np.array(Injury_df['Player']).astype(str)

# CBS Schedule
string_split_array = [1,2,3,4,5,6,7,8,9]

class parameters:
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
    team_name_abbrevations = {
    'Celtics':'BOS',
    'Nets':'BRK',
    'Raptors':'TOR',
    'ers':'PHI',
    'Knicks':'NYK',
    'Timberwolves':'MIN',
    'Thunder':'OKC',
    'Nuggets':'DEN',
    'Trail Blazers':'POR',
    'Jazz':'UTA',
    'Bulls':'CHI',
    'Cavaliers':'CLE',
    'Pistons':'DET',
    'Pacers':'IND',
    'Bucks':'MIL',
    'Lakers':'LAL',
    'Clippers':'LAC',
    'Warriors':'GSW',
    'Suns':'PHO',
    'Kings':'SAC',
    'Wizards':'WAS',
    'Hawks':'ATL',
    'Magic':'ORL',
    'Heat':'MIA',
    'Hornets':'CHO',
    'Grizzlies':'MEM',
    'Pelicans':'NOP',
    'Rockets':'HOU',
    'Spurs':'SAS',
    'Mavericks':'DAL'
    }

class offence_defence_functions:
    @staticmethod
    def offence_dataset(df):
        df = df.loc[0:12, parameters.offence_variables_for_average]
        return df
    @staticmethod
    def defence_dataset(df):
        df = df.loc[0:12, parameters.defence_variables_for_average]
        return df
    @staticmethod
    def offence_function(FG, ThreeP, TwoP, FT, ORB):
        final_result = (0 * FG) + (0.5 * ThreeP) + (0.35 * TwoP) + \
                       + (0.1 * FT) + (0.05 * ORB)
        return final_result
    @staticmethod
    def defence_function(Stl, Blk, Drb, Pf, Tov):
        final_result = (0.15 * Stl) + (0.35 * Blk) + \
                       (0.5 * Drb) - ((0 * Pf) + (0 * Tov))
        return final_result
    @staticmethod
    def offence_defence_combo(team_number):
        total_team_score = offence_defence_functions.offence_function(
            normalization(team_dataset_offence.get(parameters.team_array[team_number]),
                          parameters.offence_variables_for_average[0]),
            normalization(team_dataset_offence.get(parameters.team_array[team_number]),
                          parameters.offence_variables_for_average[1]),
            normalization(team_dataset_offence.get(parameters.team_array[team_number]),
                          parameters.offence_variables_for_average[2]),
            normalization(team_dataset_offence.get(parameters.team_array[team_number]),
                          parameters.offence_variables_for_average[3]),
            normalization(team_dataset_offence.get(parameters.team_array[team_number]),
                          parameters.offence_variables_for_average[4])) + \
                           offence_defence_functions.defence_function(
                               normalization(team_dataset_defence.get(parameters.team_array[team_number]),
                                             parameters.defence_variables_for_average[0]),
                               normalization(team_dataset_defence.get(parameters.team_array[team_number]),
                                             parameters.defence_variables_for_average[1]),
                               normalization(team_dataset_defence.get(parameters.team_array[team_number]),
                                             parameters.defence_variables_for_average[2]),
                               normalization(team_dataset_defence.get(parameters.team_array[team_number]),
                                             parameters.defence_variables_for_average[3]),
                               normalization(team_dataset_defence.get(parameters.team_array[team_number]),
                                             parameters.defence_variables_for_average[4]))
        return total_team_score
class webscrape_functions:
    todays_date = date.today().strftime("%Y%m%d")
    random_date_for_testing = '20211013'
    Schedule = pd.read_html('https://www.cbssports.com/nba/scoreboard/' + todays_date + '/')
#    Schedule.pop(len(Schedule)-1)
    def webscrape_dataset_function(team_array, season_year):
        df = pd.read_html(
            'https://www.basketball-reference.com/teams/' + team_array + '/' + season_year + '.html#advanced')
        team_table_number = 1
        df = pd.DataFrame(df[team_table_number])
        df = injury_function(df)
        df = df.loc[0:12, ['FG', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB',
                           'DRB', 'STL', 'BLK', 'PF', 'TOV']].fillna(0)
        time.sleep(t)
        return df
    @staticmethod
    def concat_schedule_teams():
        todays_scheduled_teams = list()
        append_scheduled_teams = list()
        for i in range(0, len(webscrape_functions.Schedule)):
            if i % 1 == 0:
                todays_scheduled_teams.append(webscrape_functions.Schedule[i])
        for k in range(0, len(todays_scheduled_teams)):
            append_scheduled_teams.append(todays_scheduled_teams[k].T.iloc[0])
        todays_scheduled_teams_df = pd.DataFrame(append_scheduled_teams)
        todays_scheduled_teams_df.columns = ['Away', 'Home']
        todays_scheduled_teams_df['Home'] = todays_scheduled_teams_df.Home.str.replace(r'(\d+[.\d]*)','',regex = True).astype(str)
        todays_scheduled_teams_df['Home'] = todays_scheduled_teams_df['Home'].str.strip('-')
        todays_scheduled_teams_df['Away'] = todays_scheduled_teams_df['Away'].str.replace(r'(\d+[.\d]*)','',regex = True).astype(str)
        todays_scheduled_teams_df['Away'] = todays_scheduled_teams_df['Away'].str.strip('-')
        todays_scheduled_teams_df_away_no_numbers = pd.DataFrame(
            todays_scheduled_teams_df['Away']).reset_index(drop=True)
        todays_scheduled_teams_df_home_no_numbers = pd.DataFrame(
            todays_scheduled_teams_df['Home']).reset_index(drop=True)
        final_schedule_df = pd.merge(todays_scheduled_teams_df_away_no_numbers['Away'].map(parameters.team_name_abbrevations),
                                     todays_scheduled_teams_df_home_no_numbers['Home'].map(parameters.team_name_abbrevations),
                                     left_index=True, right_index=True)
        return final_schedule_df

def normalization(df,variable):
    variable_normalzied = float(np.sum(((df.loc[:, [variable]] - pd.DataFrame.mean(df.loc[:, [variable]])) /
                                        pd.DataFrame.std(df.loc[:, [variable]]))))
    return variable_normalzied
def injury_function(dataset):
    dataset = dataset[~dataset.isin(Injury_df)]
    dataset.dropna(subset=[('Unnamed: 1')], inplace = True)
    return dataset

todays_away_teams_df = webscrape_functions.concat_schedule_teams()['Away']
todays_home_teams_df = webscrape_functions.concat_schedule_teams()['Home']

team_dataset_offence = {
    'BOS': offence_defence_functions.offence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[0],season_year=parameters.season_year)),
    'BRK': offence_defence_functions.offence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[1],season_year=parameters.season_year)),
    'TOR': offence_defence_functions.offence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[2],season_year=parameters.season_year)),
    'PHI': offence_defence_functions.offence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[3],season_year=parameters.season_year)),
    'NYK': offence_defence_functions.offence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[4],season_year=parameters.season_year)),
    'MIN': offence_defence_functions.offence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[5],season_year=parameters.season_year)),
    'OKC': offence_defence_functions.offence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[6],season_year=parameters.season_year)),
    'DEN': offence_defence_functions.offence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[7],season_year=parameters.season_year)),
    'POR': offence_defence_functions.offence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[8],season_year=parameters.season_year)),
    'UTA': offence_defence_functions.offence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[9],season_year=parameters.season_year)),
    'CHI': offence_defence_functions.offence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[10],season_year=parameters.season_year)),
    'CLE': offence_defence_functions.offence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[11],season_year=parameters.season_year)),
    'DET': offence_defence_functions.offence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[12],season_year=parameters.season_year)),
    'IND': offence_defence_functions.offence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[13],season_year=parameters.season_year)),
    'MIL': offence_defence_functions.offence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[14],season_year=parameters.season_year)),
    'LAL': offence_defence_functions.offence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[15],season_year=parameters.season_year)),
    'LAC': offence_defence_functions.offence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[16],season_year=parameters.season_year)),
    'GSW': offence_defence_functions.offence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[17],season_year=parameters.season_year)),
    'PHO': offence_defence_functions.offence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[18],season_year=parameters.season_year)),
    'SAC': offence_defence_functions.offence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[19],season_year=parameters.season_year)),
    'WAS': offence_defence_functions.offence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[20],season_year=parameters.season_year)),
    'ATL': offence_defence_functions.offence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[21],season_year=parameters.season_year)),
    'ORL': offence_defence_functions.offence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[22],season_year=parameters.season_year)),
    'MIA': offence_defence_functions.offence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[23],season_year=parameters.season_year)),
    'CHO': offence_defence_functions.offence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[24],season_year=parameters.season_year)),
    'MEM': offence_defence_functions.offence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[25],season_year=parameters.season_year)),
    'NOP': offence_defence_functions.offence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[26],season_year=parameters.season_year)),
    'HOU': offence_defence_functions.offence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[27],season_year=parameters.season_year)),
    'SAS': offence_defence_functions.offence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[28],season_year=parameters.season_year)),
    'DAL': offence_defence_functions.offence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[29],season_year=parameters.season_year))
}
team_dataset_defence = {
    'BOS': offence_defence_functions.defence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[0],season_year=parameters.season_year)),
    'BRK': offence_defence_functions.defence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[1],season_year=parameters.season_year)),
    'TOR': offence_defence_functions.defence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[2],season_year=parameters.season_year)),
    'PHI': offence_defence_functions.defence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[3],season_year=parameters.season_year)),
    'NYK': offence_defence_functions.defence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[4],season_year=parameters.season_year)),
    'MIN': offence_defence_functions.defence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[5],season_year=parameters.season_year)),
    'OKC': offence_defence_functions.defence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[6],season_year=parameters.season_year)),
    'DEN': offence_defence_functions.defence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[7],season_year=parameters.season_year)),
    'POR': offence_defence_functions.defence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[8],season_year=parameters.season_year)),
    'UTA': offence_defence_functions.defence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[9],season_year=parameters.season_year)),
    'CHI': offence_defence_functions.defence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[10],season_year=parameters.season_year)),
    'CLE': offence_defence_functions.defence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[11],season_year=parameters.season_year)),
    'DET': offence_defence_functions.defence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[12],season_year=parameters.season_year)),
    'IND': offence_defence_functions.defence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[13],season_year=parameters.season_year)),
    'MIL': offence_defence_functions.defence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[14],season_year=parameters.season_year)),
    'LAL': offence_defence_functions.defence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[15],season_year=parameters.season_year)),
    'LAC': offence_defence_functions.defence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[16],season_year=parameters.season_year)),
    'GSW': offence_defence_functions.defence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[17],season_year=parameters.season_year)),
    'PHO': offence_defence_functions.defence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[18],season_year=parameters.season_year)),
    'SAC': offence_defence_functions.defence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[19],season_year=parameters.season_year)),
    'WAS': offence_defence_functions.defence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[20],season_year=parameters.season_year)),
    'ATL': offence_defence_functions.defence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[21],season_year=parameters.season_year)),
    'ORL': offence_defence_functions.defence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[22],season_year=parameters.season_year)),
    'MIA': offence_defence_functions.defence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[23],season_year=parameters.season_year)),
    'CHO': offence_defence_functions.defence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[24],season_year=parameters.season_year)),
    'MEM': offence_defence_functions.defence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[25],season_year=parameters.season_year)),
    'NOP': offence_defence_functions.defence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[26],season_year=parameters.season_year)),
    'HOU': offence_defence_functions.defence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[27],season_year=parameters.season_year)),
    'SAS': offence_defence_functions.defence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[28],season_year=parameters.season_year)),
    'DAL': offence_defence_functions.defence_dataset(webscrape_functions.webscrape_dataset_function(
        parameters.team_array[29],season_year=parameters.season_year))
}
team_final_result = {
    'BOS': offence_defence_functions.offence_defence_combo(0),
    'BRK': offence_defence_functions.offence_defence_combo(1),
    'TOR': offence_defence_functions.offence_defence_combo(2),
    'PHI': offence_defence_functions.offence_defence_combo(3),
    'NYK': offence_defence_functions.offence_defence_combo(4),
    'MIN': offence_defence_functions.offence_defence_combo(5),
    'OKC': offence_defence_functions.offence_defence_combo(6),
    'DEN': offence_defence_functions.offence_defence_combo(7),
    'POR': offence_defence_functions.offence_defence_combo(8),
    'UTA': offence_defence_functions.offence_defence_combo(9),
    'CHI': offence_defence_functions.offence_defence_combo(10),
    'CLE': offence_defence_functions.offence_defence_combo(11),
    'DET': offence_defence_functions.offence_defence_combo(12),
    'IND': offence_defence_functions.offence_defence_combo(13),
    'MIL': offence_defence_functions.offence_defence_combo(14),
    'LAL': offence_defence_functions.offence_defence_combo(15),
    'LAC': offence_defence_functions.offence_defence_combo(16),
    'GSW': offence_defence_functions.offence_defence_combo(17),
    'PHO': offence_defence_functions.offence_defence_combo(18),
    'SAC': offence_defence_functions.offence_defence_combo(19),
    'WAS': offence_defence_functions.offence_defence_combo(20),
    'ATL': offence_defence_functions.offence_defence_combo(21),
    'ORL': offence_defence_functions.offence_defence_combo(22),
    'MIA': offence_defence_functions.offence_defence_combo(23),
    'CHO': offence_defence_functions.offence_defence_combo(24),
    'MEM': offence_defence_functions.offence_defence_combo(25),
    'NOP': offence_defence_functions.offence_defence_combo(26),
    'HOU': offence_defence_functions.offence_defence_combo(27),
    'SAS': offence_defence_functions.offence_defence_combo(28),
    'DAL': offence_defence_functions.offence_defence_combo(29)
}