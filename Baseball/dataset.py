# This script is to import the data
from utils import *

year_selected = '2022' # Note: Make sure too adjust this as the new season starts.
Team_array = [
    'ARI',	'TBR',	'HOU',	'NYY',
    'CHW',	'BOS',	'OAK',	'SEA',
    'TOR',	'CLE',	'LAA',	'DET',
    'KCR',	'MIN',	'TEX',	'BAL',
    'SFG',	'LAD',	'MIL',	'CIN',
    'ATL',	'SDP',	'STL',	'PHI',
    'NYM',	'COL',	'WSN',	'CHC',
    'MIA',	'PIT'
]
team_abbrev = {
    'Arizona':'ARI', 'Minnesota':'MIN', 'Washington':'WSN',
    'Philadelphia':'PHI', 'N.Y. Yankees':'NYY', 'Oakland':'OAK',
    'San Francisco':'SFG', 'Tampa Bay':'TBR', 'L.A. Angels' : 'LAA',
    'Detroit':'DET', 'St. Louis':'STL', 'Chi. Cubs':'CHC',
    'Atlanta':'ATL', 'Houston':'HOU', 'Cincinnati':'CIN',
    'N.Y. Mets':'NYM', 'Boston':'BOS', 'Pittsburgh':'PIT',
    'Miami':'MIA', 'Baltimore':'BAL', 'Toronto':'TOR',
    'Cleveland':'CLE', 'Chi. White Sox':'CHW', 'Texas':'TEX',
    'Kansas City':'KCR', 'Milwaukee':'MIL', 'Colorado':'COL',
    'San Diego':'SDP', 'Seattle':'SEA', 'L.A. Dodgers':'LAD'
}

class offence_defence:
    def webscrape_link(team, season_year):
        Link = 'https://www.baseball-reference.com/teams/' + team + '/' + season_year + '.shtml#team_batting'
        return Link
    def batting_df(web_link):
        batting_link = pd.read_html(web_link)
        batting_Df = pd.DataFrame(batting_link[(len(batting_link) - 2)])
        batting_Df = batting_Df.loc[0:len(batting_Df), ['R', 'H', '2B', '3B', 'RBI', 'SB']]
        batting_Df = batting_Df.drop(labels=range(21, len(batting_Df)),
                                     axis=0)
        batting_Df = batting_Df.loc[(batting_Df['R'] != 'R')]
        batting_Df = batting_Df.dropna()
        return batting_Df
    def pitching_df(web_link):
        pitching_link = pd.read_html(web_link)
        pitching_Df = pd.DataFrame(pitching_link[(len(pitching_link) - 1)])
        pitching_Df = pitching_Df.loc[0:len(pitching_Df), ['R', 'H', 'ER', 'HR', 'BB', 'SO']]
        pitching_Df = pitching_Df.drop(labels=range(21, len(pitching_Df)),
                                       axis=0)
        pitching_Df = pitching_Df.loc[(pitching_Df['H'] != 'H')]
        pitching_Df = pitching_Df.dropna()
        return pitching_Df

class todays_games:
    todays_date = date.today().strftime("%Y%m%d")
    link_to_todays_games = pd.read_html('https://www.cbssports.com/mlb/schedule/' + todays_date)
    @staticmethod
    def home_teams():
        todays_home_teams_df = todays_games.link_to_todays_games[0]['Home'].map(team_abbrev)
        return todays_home_teams_df
    @staticmethod
    def away_teams():
        todays_away_teams_df = todays_games.link_to_todays_games[0]['Away'].map(team_abbrev)
        return todays_away_teams_df

class teams:
    class pitching:
        # Arizona = ARI
        ARI = offence_defence.pitching_df(web_link=offence_defence.webscrape_link(team=Team_array[0],
                                                                                  season_year=year_selected))
        # Tampa Bay = TBR
        TBR = offence_defence.pitching_df(web_link=offence_defence.webscrape_link(team=Team_array[1],
                                                                                  season_year=year_selected))
        # Houston = HOU
        HOU = offence_defence.pitching_df(web_link=offence_defence.webscrape_link(team=Team_array[2],
                                                                                  season_year=year_selected))
        # NY Yankees = NYY
        NYY = offence_defence.pitching_df(web_link=offence_defence.webscrape_link(team=Team_array[3],
                                                                                  season_year=year_selected))
        # Chicago White Sox = CHW
        CHW = offence_defence.pitching_df(web_link=offence_defence.webscrape_link(team=Team_array[4],
                                                                                  season_year=year_selected))
        # Boston = BOS
        BOS = offence_defence.pitching_df(web_link=offence_defence.webscrape_link(team=Team_array[5],
                                                                                  season_year=year_selected))
        # Oakland = OAK
        OAK = offence_defence.pitching_df(web_link=offence_defence.webscrape_link(team=Team_array[6],
                                                                                  season_year=year_selected))
        # Seattle = SEA
        SEA = offence_defence.pitching_df(web_link=offence_defence.webscrape_link(team=Team_array[7],
                                                                                  season_year=year_selected))
        # Toronto = TOR
        TOR = offence_defence.pitching_df(web_link=offence_defence.webscrape_link(team=Team_array[8],
                                                                                  season_year=year_selected))
        # Cleveland = CLE
        CLE = offence_defence.pitching_df(web_link=offence_defence.webscrape_link(team=Team_array[9],
                                                                                  season_year=year_selected))
        # LA Angels = LAA
        LAA = offence_defence.pitching_df(web_link=offence_defence.webscrape_link(team=Team_array[10],
                                                                                  season_year=year_selected))
        # Detroit = DET
        DET = offence_defence.pitching_df(web_link=offence_defence.webscrape_link(team=Team_array[11],
                                                                                  season_year=year_selected))
        # Kansas City = KCR
        KCR = offence_defence.pitching_df(web_link=offence_defence.webscrape_link(team=Team_array[12],
                                                                                  season_year=year_selected))
        # Minnesota = MIN
        MIN = offence_defence.pitching_df(web_link=offence_defence.webscrape_link(team=Team_array[13],
                                                                                  season_year=year_selected))
        # Texas = TEX
        TEX = offence_defence.pitching_df(web_link=offence_defence.webscrape_link(team=Team_array[14],
                                                                                  season_year=year_selected))
        # Baltimore = BAL
        BAL = offence_defence.pitching_df(web_link=offence_defence.webscrape_link(team=Team_array[15],
                                                                                  season_year=year_selected))
        # SF Giants = SFG
        SFG = offence_defence.pitching_df(web_link=offence_defence.webscrape_link(team=Team_array[16],
                                                                                  season_year=year_selected))
        # LA Dodgers = LAD
        LAD = offence_defence.pitching_df(web_link=offence_defence.webscrape_link(team=Team_array[17],
                                                                                  season_year=year_selected))
        # Milwauke = MIL
        MIL = offence_defence.pitching_df(web_link=offence_defence.webscrape_link(team=Team_array[18],
                                                                                  season_year=year_selected))
        # Cincinnati = CIN
        CIN = offence_defence.pitching_df(web_link=offence_defence.webscrape_link(team=Team_array[19],
                                                                                  season_year=year_selected))
        # Atlanta = ATL
        ATL = offence_defence.pitching_df(web_link=offence_defence.webscrape_link(team=Team_array[20],
                                                                                  season_year=year_selected))
        # San Diego = SDP
        SDP = offence_defence.pitching_df(web_link=offence_defence.webscrape_link(team=Team_array[21],
                                                                                  season_year=year_selected))
        # St. Louis
        STL = offence_defence.pitching_df(web_link=offence_defence.webscrape_link(team=Team_array[22],
                                                                                  season_year=year_selected))
        # Philadelphia = PHI
        PHI = offence_defence.pitching_df(web_link=offence_defence.webscrape_link(team=Team_array[23],
                                                                                  season_year=year_selected))
        # NY Mets = NYM
        NYM = offence_defence.pitching_df(web_link=offence_defence.webscrape_link(team=Team_array[24],
                                                                                  season_year=year_selected))
        # Colorado = COL
        COL = offence_defence.pitching_df(web_link=offence_defence.webscrape_link(team=Team_array[25],
                                                                                  season_year=year_selected))
        # Washington = WSN
        WSN = offence_defence.pitching_df(web_link=offence_defence.webscrape_link(team=Team_array[26],
                                                                                  season_year=year_selected))
        # Chicago Cubs = CHC
        CHC = offence_defence.pitching_df(web_link=offence_defence.webscrape_link(team=Team_array[27],
                                                                                  season_year=year_selected))
        # Miami = MIA
        MIA = offence_defence.pitching_df(web_link=offence_defence.webscrape_link(team=Team_array[28],
                                                                                  season_year=year_selected))
        # Pittsburgh = PIT
        PIT = offence_defence.pitching_df(web_link=offence_defence.webscrape_link(team=Team_array[29],
                                                                                  season_year=year_selected))
    class batting:
# Arizona = ARI
        ARI = offence_defence.batting_df(web_link=offence_defence.webscrape_link(team=Team_array[0],
                                                                                 season_year=year_selected))
# Tampa Bay = TBR
        TBR = offence_defence.batting_df(web_link=offence_defence.webscrape_link(team=Team_array[1],
                                                                                 season_year=year_selected))
# Houston = HOU
        HOU = offence_defence.batting_df(web_link=offence_defence.webscrape_link(team=Team_array[2],
                                                                                 season_year=year_selected))
# NY Yankees = NYY
        NYY = offence_defence.batting_df(web_link=offence_defence.webscrape_link(team=Team_array[3],
                                                                                 season_year=year_selected))
# Chicago White Sox = CHW
        CHW = offence_defence.batting_df(web_link=offence_defence.webscrape_link(team=Team_array[4],
                                                                                 season_year=year_selected))
# Boston = BOS
        BOS = offence_defence.batting_df(web_link=offence_defence.webscrape_link(team=Team_array[5],
                                                                                 season_year=year_selected))
# Oakland = OAK
        OAK = offence_defence.batting_df(web_link=offence_defence.webscrape_link(team=Team_array[6],
                                                                                 season_year=year_selected))
# Seattle = SEA
        SEA = offence_defence.batting_df(web_link=offence_defence.webscrape_link(team=Team_array[7],
                                                                                 season_year=year_selected))
# Toronto = TOR
        TOR = offence_defence.batting_df(web_link=offence_defence.webscrape_link(team=Team_array[8],
                                                                                 season_year=year_selected))
# Cleveland = CLE
        CLE = offence_defence.batting_df(web_link=offence_defence.webscrape_link(team=Team_array[9],
                                                                                 season_year=year_selected))
#LA Angels = LAA
        LAA = offence_defence.batting_df(web_link=offence_defence.webscrape_link(team=Team_array[10],
                                                                                 season_year=year_selected))
# Detroit = DET
        DET = offence_defence.batting_df(web_link=offence_defence.webscrape_link(team=Team_array[11],
                                                                                 season_year=year_selected))
# Kansas City = KCR
        KCR = offence_defence.batting_df(web_link=offence_defence.webscrape_link(team=Team_array[12],
                                                                                 season_year=year_selected))
# Minnesota = MIN
        MIN = offence_defence.batting_df(web_link=offence_defence.webscrape_link(team=Team_array[13],
                                                                                 season_year=year_selected))
# Texas = TEX
        TEX = offence_defence.batting_df(web_link=offence_defence.webscrape_link(team=Team_array[14],
                                                                                 season_year=year_selected))
# Baltimore = BAL
        BAL = offence_defence.batting_df(web_link=offence_defence.webscrape_link(team=Team_array[15],
                                                                                 season_year=year_selected))
# SF Giants = SFG
        SFG = offence_defence.batting_df(web_link=offence_defence.webscrape_link(team=Team_array[16],
                                                                                 season_year=year_selected))
# LA Dodgers = LAD
        LAD = offence_defence.batting_df(web_link=offence_defence.webscrape_link(team=Team_array[17],
                                                                                 season_year=year_selected))
# Milwauke = MIL
        MIL = offence_defence.batting_df(web_link=offence_defence.webscrape_link(team=Team_array[18],
                                                                                 season_year=year_selected))
# Cincinnati = CIN
        CIN = offence_defence.batting_df(web_link=offence_defence.webscrape_link(team=Team_array[19],
                                                                                 season_year=year_selected))
# Atlanta = ATL
        ATL = offence_defence.batting_df(web_link=offence_defence.webscrape_link(team=Team_array[20],
                                                                                 season_year=year_selected))
# San Diego = SDP
        SDP = offence_defence.batting_df(web_link=offence_defence.webscrape_link(team=Team_array[21],
                                                                                 season_year=year_selected))
# St. Louis
        STL = offence_defence.batting_df(web_link=offence_defence.webscrape_link(team=Team_array[22],
                                                                                 season_year=year_selected))
# Philadelphia = PHI
        PHI = offence_defence.batting_df(web_link=offence_defence.webscrape_link(team=Team_array[23],
                                                                                 season_year=year_selected))
# NY Mets = NYM
        NYM = offence_defence.batting_df(web_link=offence_defence.webscrape_link(team=Team_array[24],
                                                                                 season_year=year_selected))
# Colorado = COL
        COL = offence_defence.batting_df(web_link=offence_defence.webscrape_link(team=Team_array[25],
                                                                                 season_year=year_selected))
# Washington = WSN
        WSN = offence_defence.batting_df(web_link=offence_defence.webscrape_link(team=Team_array[26],
                                                                                 season_year=year_selected))
# Chicago Cubs = CHC
        CHC = offence_defence.batting_df(web_link=offence_defence.webscrape_link(team=Team_array[27],
                                                                                 season_year=year_selected))
# Miami = MIA
        MIA = offence_defence.batting_df(web_link=offence_defence.webscrape_link(team=Team_array[28],
                                                                                 season_year=year_selected))
# Pittsburgh = PIT
        PIT = offence_defence.batting_df(web_link=offence_defence.webscrape_link(team=Team_array[29],
                                                                                 season_year=year_selected))

todays_home_teams_df = todays_games.home_teams()
todays_away_teams_df = todays_games.away_teams()
