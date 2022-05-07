from utils import *

def offence_function(shots, goals, assists, penalties_in_minutes, faceoff_wins, faceoff_loses):
    offence = 0.5 * (np.sum((shots - goals))) + 0.2 * (np.sum(assists)) + 0.2 * ( np.sum(faceoff_wins) - np.sum(faceoff_loses) ) -\
              0.1 * (np.sum(penalties_in_minutes))
    return offence

def defence_function(blocks, hits, goalie):
    defence = 0.2 * (np.sum(blocks)) + 0.2 * (np.sum(hits)) + 0.6 * (np.sum(goalie))
    return defence

def normalization_function(variable, mean, std):
    normalized_value = ( variable - mean ) / std
    return normalized_value

offence_table_number = 4
goalie_table_number = 5

# Carolina Hurricanes
Carolina_df = pd.read_html('https://www.hockey-reference.com/teams/CAR/2022.html')
Carolina_offence_df = pd.DataFrame(Carolina_df[offence_table_number])
Carolina_offence = Carolina_offence_df.loc[0:16, [('Scoring', 'G'), ('Unnamed: 17_level_0', 'S'), ('Scoring', 'A'),
                                                  ('Scoring', 'PIM'), ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Carolina_defence = Carolina_offence_df.loc[0:16, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Carolina_goalie = pd.DataFrame(Carolina_df[goalie_table_number])
Carolina_goalie = Carolina_goalie.loc[0:2, [('Goalie Stats', 'GA')]]


# Florida Panthers
Florida_df = pd.read_html('https://www.hockey-reference.com/teams/FLA/2022.html')
Florida_offence_df = pd.DataFrame(Florida_df[offence_table_number])
Florida_offence = Florida_offence_df.loc[0:16, [('Scoring', 'G'), ('Unnamed: 17_level_0', 'S'), ('Scoring', 'A'),
                                                  ('Scoring', 'PIM'), ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Florida_defence = Florida_offence_df.loc[0:16, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Florida_goalie = pd.DataFrame(Florida_df[goalie_table_number])
Florida_goalie = Florida_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Tampa Bay Lightning
Tampabay_df = pd.read_html('https://www.hockey-reference.com/teams/TBL/2022.html')
Tampabay_offence_df = pd.DataFrame(Tampabay_df[offence_table_number])
Tampabay_offence = Tampabay_offence_df.loc[0:16, [('Scoring', 'G'), ('Unnamed: 17_level_0', 'S'), ('Scoring', 'A'),
                                                  ('Scoring', 'PIM'), ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Tampabay_defence = Tampabay_offence_df.loc[0:16, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Tampabay_goalie = pd.DataFrame(Tampabay_df[goalie_table_number])
Tampabay_goalie = Tampabay_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Nashville Predators
Nashville_df = pd.read_html('https://www.hockey-reference.com/teams/NSH/2022.html')
Nashville_offence_df = pd.DataFrame(Nashville_df[offence_table_number])
Nashville_offence = Nashville_offence_df.loc[0:16, [('Scoring', 'G'), ('Unnamed: 17_level_0', 'S'), ('Scoring', 'A'),
                                                  ('Scoring', 'PIM'), ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Nashville_defence = Nashville_offence_df.loc[0:16, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Nashville_goalie = pd.DataFrame(Nashville_df[goalie_table_number])
Nashville_goalie = Nashville_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Dallas Stars
Dallas_df = pd.read_html('https://www.hockey-reference.com/teams/DAL/2022.html')
Dallas_offence_df = pd.DataFrame(Dallas_df[offence_table_number])
Dallas_offence = Dallas_offence_df.loc[0:16, [('Scoring', 'G'), ('Unnamed: 17_level_0', 'S'), ('Scoring', 'A'),
                                                  ('Scoring', 'PIM'), ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Dallas_defence = Dallas_offence_df.loc[0:16, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Dallas_goalie = pd.DataFrame(Dallas_df[goalie_table_number])
Dallas_goalie = Dallas_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Chicago Blackhawks
Chicago_df = pd.read_html('https://www.hockey-reference.com/teams/CHI/2022.html')
Chicago_offence_df = pd.DataFrame(Chicago_df[offence_table_number])
Chicago_offence = Chicago_offence_df.loc[0:16, [('Scoring', 'G'), ('Unnamed: 17_level_0', 'S'), ('Scoring', 'A'),
                                                  ('Scoring', 'PIM'), ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Chicago_defence = Chicago_offence_df.loc[0:16, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Chicago_goalie = pd.DataFrame(Chicago_df[goalie_table_number])
Chicago_goalie = Chicago_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Columbus Blue Jackets
Columbus_df = pd.read_html('https://www.hockey-reference.com/teams/CBJ/2022.html')
Columbus_offence_df = pd.DataFrame(Columbus_df[offence_table_number])
Columbus_offence = Columbus_offence_df.loc[0:16, [('Scoring', 'G'), ('Unnamed: 17_level_0', 'S'), ('Scoring', 'A'),
                                                  ('Scoring', 'PIM'), ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Columbus_defence = Columbus_offence_df.loc[0:16, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Columbus_goalie = pd.DataFrame(Columbus_df[goalie_table_number])
Columbus_goalie = Columbus_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Detroit Redwings
Detroit_df = pd.read_html('https://www.hockey-reference.com/teams/DET/2022.html')
Detroit_offence_df = pd.DataFrame(Detroit_df[offence_table_number])
Detroit_offence = Detroit_offence_df.loc[0:16, [('Scoring', 'G'), ('Unnamed: 17_level_0', 'S'), ('Scoring', 'A'),
                                                  ('Scoring', 'PIM'), ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Detroit_defence = Detroit_offence_df.loc[0:16, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Detroit_goalie = pd.DataFrame(Detroit_df[goalie_table_number])
Detroit_goalie = Detroit_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Pittsburgh Penguins
Pittsburgh_df = pd.read_html('https://www.hockey-reference.com/teams/PIT/2022.html')
Pittsburgh_offence_df = pd.DataFrame(Pittsburgh_df[offence_table_number])
Pittsburgh_offence = Pittsburgh_offence_df.loc[0:16, [('Scoring', 'G'), ('Unnamed: 17_level_0', 'S'), ('Scoring', 'A'),
                                                  ('Scoring', 'PIM'), ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Pittsburgh_defence = Pittsburgh_offence_df.loc[0:16, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Pittsburgh_goalie = pd.DataFrame(Pittsburgh_df[goalie_table_number])
Pittsburgh_goalie = Pittsburgh_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Washington Capitals
Washington_df = pd.read_html('https://www.hockey-reference.com/teams/WSH/2022.html')
Washington_offence_df = pd.DataFrame(Washington_df[offence_table_number])
Washington_offence = Washington_offence_df.loc[0:16, [('Scoring', 'G'), ('Unnamed: 17_level_0', 'S'), ('Scoring', 'A'),
                                                  ('Scoring', 'PIM'), ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Washington_defence = Washington_offence_df.loc[0:16, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Washington_goalie = pd.DataFrame(Washington_df[goalie_table_number])
Washington_goalie = Washington_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Boston Bruins
Boston_df = pd.read_html('https://www.hockey-reference.com/teams/BOS/2022.html')
Boston_offence_df = pd.DataFrame(Boston_df[offence_table_number])
Boston_offence = Boston_offence_df.loc[0:16, [('Scoring', 'G'), ('Unnamed: 17_level_0', 'S'), ('Scoring', 'A'),
                                                  ('Scoring', 'PIM'), ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Boston_defence = Boston_offence_df.loc[0:16, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Boston_goalie = pd.DataFrame(Boston_df[goalie_table_number])
Boston_goalie = Boston_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# New York Islanders
NewyorkI_df = pd.read_html('https://www.hockey-reference.com/teams/NYI/2022.html')
NewyorkI_offence_df = pd.DataFrame(NewyorkI_df[offence_table_number])
NewyorkI_offence = NewyorkI_offence_df.loc[0:16, [('Scoring', 'G'), ('Unnamed: 17_level_0', 'S'), ('Scoring', 'A'),
                                                  ('Scoring', 'PIM'), ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
NewyorkI_defence = NewyorkI_offence_df.loc[0:16, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
NewyorkI_goalie = pd.DataFrame(NewyorkI_df[goalie_table_number])
NewyorkI_goalie = NewyorkI_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# New York Rangers
NewyorkR_df = pd.read_html('https://www.hockey-reference.com/teams/NYR/2022.html')
NewyorkR_offence_df = pd.DataFrame(NewyorkR_df[offence_table_number])
NewyorkR_offence = NewyorkR_offence_df.loc[0:16, [('Scoring', 'G'), ('Unnamed: 17_level_0', 'S'), ('Scoring', 'A'),
                                                  ('Scoring', 'PIM'), ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
NewyorkR_defence = NewyorkR_offence_df.loc[0:16, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
NewyorkR_goalie = pd.DataFrame(NewyorkR_df[goalie_table_number])
NewyorkR_goalie = NewyorkR_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Philadelphia Flyers
Philadelphia_df = pd.read_html('https://www.hockey-reference.com/teams/PHI/2022.html')
Philadelphia_offence_df = pd.DataFrame(Philadelphia_df[offence_table_number])
Philadelphia_offence = Philadelphia_offence_df.loc[0:16, [('Scoring', 'G'), ('Unnamed: 17_level_0', 'S'), ('Scoring', 'A'),
                                                  ('Scoring', 'PIM'), ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Philadelphia_defence = Philadelphia_offence_df.loc[0:16, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Philadelphia_goalie = pd.DataFrame(Philadelphia_df[goalie_table_number])
Philadelphia_goalie = Philadelphia_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# New Jersey Devils
Newjersey_df = pd.read_html('https://www.hockey-reference.com/teams/NJD/2022.html')
Newjersey_offence_df = pd.DataFrame(Newjersey_df[offence_table_number])
Newjersey_offence = Newjersey_offence_df.loc[0:16, [('Scoring', 'G'), ('Unnamed: 17_level_0', 'S'), ('Scoring', 'A'),
                                                  ('Scoring', 'PIM'), ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Newjersey_defence = Newjersey_offence_df.loc[0:16, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Newjersey_goalie = pd.DataFrame(Newjersey_df[goalie_table_number])
Newjersey_goalie = Newjersey_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Buffalo Sabers
Buffalo_df = pd.read_html('https://www.hockey-reference.com/teams/BUF/2022.html')
Buffalo_offence_df = pd.DataFrame(Buffalo_df[offence_table_number])
Buffalo_offence = Buffalo_offence_df.loc[0:16, [('Scoring', 'G'), ('Unnamed: 17_level_0', 'S'), ('Scoring', 'A'),
                                                  ('Scoring', 'PIM'), ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Buffalo_defence = Buffalo_offence_df.loc[0:16, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Buffalo_goalie = pd.DataFrame(Buffalo_df[goalie_table_number])
Buffalo_goalie = Buffalo_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Toronto Maple Leafs
Toronto_df = pd.read_html('https://www.hockey-reference.com/teams/TOR/2022.html')
Toronto_offence_df = pd.DataFrame(Toronto_df[offence_table_number])
Toronto_offence = Toronto_offence_df.loc[0:16, [('Scoring', 'G'), ('Unnamed: 17_level_0', 'S'), ('Scoring', 'A'),
                                                  ('Scoring', 'PIM'), ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Toronto_defence = Toronto_offence_df.loc[0:16, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Toronto_goalie = pd.DataFrame(Toronto_df[goalie_table_number])
Toronto_goalie = Toronto_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Edmonton Oilers
Edmonton_df = pd.read_html('https://www.hockey-reference.com/teams/EDM/2022.html')
Edmonton_offence_df = pd.DataFrame(Edmonton_df[offence_table_number])
Edmonton_offence = Edmonton_offence_df.loc[0:16, [('Scoring', 'G'), ('Unnamed: 17_level_0', 'S'), ('Scoring', 'A'),
                                                  ('Scoring', 'PIM'), ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Edmonton_defence = Edmonton_offence_df.loc[0:16, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Edmonton_goalie = pd.DataFrame(Edmonton_df[goalie_table_number])
Edmonton_goalie = Edmonton_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Winnipeg Jets
Winnipeg_df = pd.read_html('https://www.hockey-reference.com/teams/WPG/2022.html')
Winnipeg_offence_df = pd.DataFrame(Winnipeg_df[offence_table_number])
Winnipeg_offence = Winnipeg_offence_df.loc[0:16, [('Scoring', 'G'), ('Unnamed: 17_level_0', 'S'), ('Scoring', 'A'),
                                                  ('Scoring', 'PIM'), ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Winnipeg_defence = Winnipeg_offence_df.loc[0:16, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Winnipeg_goalie = pd.DataFrame(Winnipeg_df[goalie_table_number])
Winnipeg_goalie = Winnipeg_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Montreal Canadiens
Montreal_df = pd.read_html('https://www.hockey-reference.com/teams/MTL/2022.html')
Montreal_offence_df = pd.DataFrame(Montreal_df[offence_table_number])
Montreal_offence = Montreal_offence_df.loc[0:16, [('Scoring', 'G'), ('Unnamed: 17_level_0', 'S'), ('Scoring', 'A'),
                                                  ('Scoring', 'PIM'), ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Montreal_defence = Montreal_offence_df.loc[0:16, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Montreal_goalie = pd.DataFrame(Montreal_df[goalie_table_number])
Montreal_goalie = Montreal_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Calgary Flames
Calgary_df = pd.read_html('https://www.hockey-reference.com/teams/CGY/2022.html')
Calgary_offence_df = pd.DataFrame(Calgary_df[offence_table_number])
Calgary_offence = Calgary_offence_df.loc[0:16, [('Scoring', 'G'), ('Unnamed: 17_level_0', 'S'), ('Scoring', 'A'),
                                                  ('Scoring', 'PIM'), ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Calgary_defence = Calgary_offence_df.loc[0:16, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Calgary_goalie = pd.DataFrame(Calgary_df[goalie_table_number])
Calgary_goalie = Calgary_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Ottawa Senators
Ottawa_df = pd.read_html('https://www.hockey-reference.com/teams/OTT/2022.html')
Ottawa_offence_df = pd.DataFrame(Ottawa_df[offence_table_number])
Ottawa_offence = Ottawa_offence_df.loc[0:16, [('Scoring', 'G'), ('Unnamed: 17_level_0', 'S'), ('Scoring', 'A'),
                                                  ('Scoring', 'PIM'), ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Ottawa_defence = Ottawa_offence_df.loc[0:16, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Ottawa_goalie = pd.DataFrame(Ottawa_df[goalie_table_number])
Ottawa_goalie = Ottawa_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Vancouver Canucks
Vancouver_df = pd.read_html('https://www.hockey-reference.com/teams/VAN/2022.html')
Vancouver_offence_df = pd.DataFrame(Vancouver_df[offence_table_number])
Vancouver_offence = Vancouver_offence_df.loc[0:16, [('Scoring', 'G'), ('Unnamed: 17_level_0', 'S'), ('Scoring', 'A'),
                                                  ('Scoring', 'PIM'), ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Vancouver_defence = Vancouver_offence_df.loc[0:16, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Vancouver_goalie = pd.DataFrame(Vancouver_df[goalie_table_number])
Vancouver_goalie = Vancouver_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Colorado Avalanche
Colorado_df = pd.read_html('https://www.hockey-reference.com/teams/COL/2022.html')
Colorado_offence_df = pd.DataFrame(Colorado_df[offence_table_number])
Colorado_offence = Colorado_offence_df.loc[0:16, [('Scoring', 'G'), ('Unnamed: 17_level_0', 'S'), ('Scoring', 'A'),
                                                  ('Scoring', 'PIM'), ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Colorado_defence = Colorado_offence_df.loc[0:16, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Colorado_goalie = pd.DataFrame(Colorado_df[goalie_table_number])
Colorado_goalie = Colorado_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Vegas Golden Knights
Vegas_df = pd.read_html('https://www.hockey-reference.com/teams/VEG/2022.html')
Vegas_offence_df = pd.DataFrame(Vegas_df[offence_table_number])
Vegas_offence = Vegas_offence_df.loc[0:16, [('Scoring', 'G'), ('Unnamed: 17_level_0', 'S'), ('Scoring', 'A'),
                                                  ('Scoring', 'PIM'), ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Vegas_defence = Vegas_offence_df.loc[0:16, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Vegas_goalie = pd.DataFrame(Vegas_df[goalie_table_number])
Vegas_goalie = Vegas_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Minnesota Wild
Minnesota_df = pd.read_html('https://www.hockey-reference.com/teams/MIN/2022.html')
Minnesota_offence_df = pd.DataFrame(Minnesota_df[offence_table_number])
Minnesota_offence = Minnesota_offence_df.loc[0:16, [('Scoring', 'G'), ('Unnamed: 17_level_0', 'S'), ('Scoring', 'A'),
                                                  ('Scoring', 'PIM'), ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Minnesota_defence = Minnesota_offence_df.loc[0:16, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Minnesota_goalie = pd.DataFrame(Minnesota_df[goalie_table_number])
Minnesota_goalie = Minnesota_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# St. Louis Blues
Stlouis_df = pd.read_html('https://www.hockey-reference.com/teams/STL/2022.html')
Stlouis_offence_df = pd.DataFrame(Stlouis_df[offence_table_number])
Stlouis_offence = Stlouis_offence_df.loc[0:16, [('Scoring', 'G'), ('Unnamed: 17_level_0', 'S'), ('Scoring', 'A'),
                                                  ('Scoring', 'PIM'), ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Stlouis_defence = Stlouis_offence_df.loc[0:16, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Stlouis_goalie = pd.DataFrame(Stlouis_df[goalie_table_number])
Stlouis_goalie = Stlouis_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Arizona Coyotes
Arizona_df = pd.read_html('https://www.hockey-reference.com/teams/ARI/2022.html')
Arizona_offence_df = pd.DataFrame(Arizona_df[offence_table_number])
Arizona_offence = Arizona_offence_df.loc[0:16, [('Scoring', 'G'), ('Unnamed: 17_level_0', 'S'), ('Scoring', 'A'),
                                                  ('Scoring', 'PIM'), ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Arizona_defence = Arizona_offence_df.loc[0:16, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Arizona_goalie = pd.DataFrame(Arizona_df[goalie_table_number])
Arizona_goalie = Arizona_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# San Jose Sharks
Sanjose_df = pd.read_html('https://www.hockey-reference.com/teams/SJS/2022.html')
Sanjose_offence_df = pd.DataFrame(Sanjose_df[offence_table_number])
Sanjose_offence = Sanjose_offence_df.loc[0:16, [('Scoring', 'G'), ('Unnamed: 17_level_0', 'S'), ('Scoring', 'A'),
                                                  ('Scoring', 'PIM'), ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Sanjose_defence = Sanjose_offence_df.loc[0:16, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Sanjose_goalie = pd.DataFrame(Sanjose_df[goalie_table_number])
Sanjose_goalie = Sanjose_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Los Angeles Kings
Losangeles_df = pd.read_html('https://www.hockey-reference.com/teams/LAK/2022.html')
Losangeles_offence_df = pd.DataFrame(Losangeles_df[offence_table_number])
Losangeles_offence = Losangeles_offence_df.loc[0:16, [('Scoring', 'G'), ('Unnamed: 17_level_0', 'S'), ('Scoring', 'A'),
                                                  ('Scoring', 'PIM'), ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Losangeles_defence = Losangeles_offence_df.loc[0:16, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Losangeles_goalie = pd.DataFrame(Losangeles_df[goalie_table_number])
Losangeles_goalie = Losangeles_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Anaheim Ducks
Anaheim_df = pd.read_html('https://www.hockey-reference.com/teams/ANA/2022.html')
Anaheim_offence_df = pd.DataFrame(Anaheim_df[offence_table_number])
Anaheim_offence = Anaheim_offence_df.loc[0:16, [('Scoring', 'G'), ('Unnamed: 17_level_0', 'S'), ('Scoring', 'A'),
                                                  ('Unnamed: 9_level_0', 'PIM'), ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Anaheim_defence = Anaheim_offence_df.loc[0:16, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Anaheim_goalie = pd.DataFrame(Anaheim_df[goalie_table_number])
Anaheim_goalie = Anaheim_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Seattle Krakens
Seattle_df = pd.read_html('https://www.hockey-reference.com/teams/SEA/2022.html')
Seattle_offence_df = pd.DataFrame(Seattle_df[offence_table_number])
Seattle_offence = Seattle_offence_df.loc[0:16, [('Scoring', 'G'), ('Unnamed: 17_level_0', 'S'), ('Scoring', 'A'),
                                                  ('Scoring', 'PIM'), ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Seattle_defence = Seattle_offence_df.loc[0:16, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Seattle_goalie = pd.DataFrame(Seattle_df[goalie_table_number])
Seattle_goalie = Seattle_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Normalization of the data

#Giant dataset to append all the data into one.
Full_offence_dataset = Carolina_offence.append(Florida_offence).append(Tampabay_offence).append(Nashville_offence).\
    append(Dallas_offence).append(Chicago_offence).append(Columbus_offence).append(Detroit_offence).\
    append(Pittsburgh_offence).append(Washington_offence).append(Boston_offence).append(NewyorkI_offence).\
    append(NewyorkR_offence).append(Philadelphia_offence).append(Newjersey_offence).append(Buffalo_offence).\
    append(Toronto_offence).append(Edmonton_offence).append(Winnipeg_offence).append(Montreal_offence).\
    append(Calgary_offence).append(Ottawa_offence).append(Vancouver_offence).append(Colorado_offence).\
    append(Vegas_offence).append(Minnesota_offence).append(Stlouis_offence).append(Arizona_offence).\
    append(Sanjose_offence).append(Losangeles_offence).append(Anaheim_offence)

Full_defence_dataset = Carolina_defence.append(Florida_defence).append(Tampabay_defence).append(Nashville_defence).\
    append(Dallas_defence).append(Chicago_defence).append(Columbus_defence).append(Detroit_defence).\
    append(Pittsburgh_defence).append(Washington_defence).append(Boston_defence).append(NewyorkI_defence).\
    append(NewyorkR_defence).append(Philadelphia_defence).append(Newjersey_defence).append(Buffalo_defence).\
    append(Toronto_defence).append(Edmonton_defence).append(Winnipeg_defence).append(Montreal_defence).\
    append(Calgary_defence).append(Ottawa_defence).append(Vancouver_defence).append(Colorado_defence).\
    append(Vegas_defence).append(Minnesota_defence).append(Stlouis_defence).append(Arizona_defence).\
    append(Sanjose_defence).append(Losangeles_defence).append(Anaheim_defence)

Full_goalie_dataset = Carolina_goalie.append(Florida_goalie).append(Tampabay_goalie).append(Nashville_goalie).\
    append(Dallas_goalie).append(Chicago_goalie).append(Columbus_goalie).append(Detroit_goalie).\
    append(Pittsburgh_goalie).append(Washington_goalie).append(Boston_goalie).append(NewyorkI_goalie).\
    append(NewyorkR_goalie).append(Philadelphia_goalie).append(Newjersey_goalie).append(Buffalo_goalie).\
    append(Toronto_goalie).append(Edmonton_goalie).append(Winnipeg_goalie).append(Montreal_goalie).\
    append(Calgary_goalie).append(Ottawa_goalie).append(Vancouver_goalie).append(Colorado_goalie).\
    append(Vegas_goalie).append(Minnesota_goalie).append(Stlouis_goalie).append(Arizona_goalie).\
    append(Sanjose_goalie).append(Losangeles_goalie).append(Anaheim_goalie)


# Mean & Std / Varialbe for Standardization
Mean_Scoring = np.mean(Full_offence_dataset[('Unnamed: 17_level_0', 'S')])
Mean_Goals = np.mean(Full_offence_dataset[('Scoring', 'G')])
Mean_Assists = np.mean(Full_offence_dataset[('Scoring', 'A')])
Mean_Penalities = np.mean(Full_offence_dataset[('Scoring', 'PIM')])
Mean_Faceoffwins = np.mean(Full_offence_dataset[('Unnamed: 26_level_0', 'FOW')])
Mean_Faceoffloses = np.mean(Full_offence_dataset[('Unnamed: 27_level_0', 'FOL')])
Mean_Blocks = np.mean(Full_defence_dataset[('Unnamed: 24_level_0', 'BLK')])
Mean_Hits = np.mean(Full_defence_dataset[('Unnamed: 25_level_0', 'HIT')])
Mean_Goalie = np.mean(Full_goalie_dataset[('Goalie Stats', 'GA')])

Std_Scoring = np.std(Full_offence_dataset[('Unnamed: 17_level_0', 'S')])
Std_Goals = np.std(Full_offence_dataset[('Scoring', 'G')])
Std_Assists = np.std(Full_offence_dataset[('Scoring', 'A')])
Std_Penalities = np.std(Full_offence_dataset[('Scoring', 'PIM')])
Std_Faceoffwins = np.std(Full_offence_dataset[('Unnamed: 26_level_0', 'FOW')])
Std_Faceoffloses = np.std(Full_offence_dataset[('Unnamed: 27_level_0', 'FOL')])
Std_Blocks = np.std(Full_defence_dataset[('Unnamed: 24_level_0', 'BLK')])
Std_Hits = np.std(Full_defence_dataset[('Unnamed: 25_level_0', 'HIT')])
Std_Goalie = np.std(Full_goalie_dataset[('Goalie Stats', 'GA')])

# Final Normalized Averages

# Carolina Hurricanes
Carolina_final = offence_function(normalization_function(Carolina_offence[('Unnamed: 17_level_0', 'S')],Mean_Scoring,
                                                         Std_Scoring),
                                  normalization_function(Carolina_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
                                  normalization_function(Carolina_offence[('Scoring', 'A')], Mean_Assists, Std_Assists),
                                  normalization_function(Carolina_offence[('Scoring', 'PIM')], Mean_Penalities,
                                                         Std_Penalities),
                                  normalization_function(Carolina_offence[('Unnamed: 26_level_0', 'FOW')], Mean_Faceoffwins,
                                                         Std_Faceoffwins),
                                  normalization_function(Carolina_offence[('Unnamed: 27_level_0', 'FOL')],Mean_Faceoffloses,
                                                         Std_Faceoffloses)) + \
                 defence_function(normalization_function(Carolina_defence[('Unnamed: 24_level_0', 'BLK')], Mean_Blocks,
                                                         Std_Blocks),
                                  normalization_function(Carolina_defence[('Unnamed: 25_level_0', 'HIT')], Mean_Hits,
                                                         Std_Hits),
                                  normalization_function(Carolina_goalie[('Goalie Stats', 'GA')], Mean_Goalie,
                                                         Std_Goalie))
# Florida Panthers
Florida_final = offence_function(normalization_function(Florida_offence[('Unnamed: 17_level_0', 'S')],Mean_Scoring,
                                                         Std_Scoring),
                                  normalization_function(Florida_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
                                  normalization_function(Florida_offence[('Scoring', 'A')], Mean_Assists, Std_Assists),
                                  normalization_function(Florida_offence[('Scoring', 'PIM')], Mean_Penalities,
                                                         Std_Penalities),
                                  normalization_function(Florida_offence[('Unnamed: 26_level_0', 'FOW')], Mean_Faceoffwins,
                                                         Std_Faceoffwins),
                                  normalization_function(Florida_offence[('Unnamed: 27_level_0', 'FOL')],Mean_Faceoffloses,
                                                         Std_Faceoffloses)) + \
                 defence_function(normalization_function(Florida_defence[('Unnamed: 24_level_0', 'BLK')], Mean_Blocks,
                                                         Std_Blocks),
                                  normalization_function(Florida_defence[('Unnamed: 25_level_0', 'HIT')], Mean_Hits,
                                                         Std_Hits),
                                  normalization_function(Florida_goalie[('Goalie Stats', 'GA')], Mean_Goalie,
                                                         Std_Goalie))
#Tampabay Lightning
Tampabay_final = offence_function(normalization_function(Tampabay_offence[('Unnamed: 17_level_0', 'S')],Mean_Scoring,
                                                         Std_Scoring),
                                  normalization_function(Tampabay_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
                                  normalization_function(Tampabay_offence[('Scoring', 'A')], Mean_Assists, Std_Assists),
                                  normalization_function(Tampabay_offence[('Scoring', 'PIM')], Mean_Penalities,
                                                         Std_Penalities),
                                  normalization_function(Tampabay_offence[('Unnamed: 26_level_0', 'FOW')], Mean_Faceoffwins,
                                                         Std_Faceoffwins),
                                  normalization_function(Tampabay_offence[('Unnamed: 27_level_0', 'FOL')],Mean_Faceoffloses,
                                                         Std_Faceoffloses)) + \
                 defence_function(normalization_function(Tampabay_defence[('Unnamed: 24_level_0', 'BLK')], Mean_Blocks,
                                                         Std_Blocks),
                                  normalization_function(Tampabay_defence[('Unnamed: 25_level_0', 'HIT')], Mean_Hits,
                                                         Std_Hits),
                                  normalization_function(Tampabay_goalie[('Goalie Stats', 'GA')], Mean_Goalie,
                                                         Std_Goalie))
# Nashville Predators
Nashville_final = offence_function(normalization_function(Nashville_offence[('Unnamed: 17_level_0', 'S')],Mean_Scoring,
                                                         Std_Scoring),
                                  normalization_function(Nashville_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
                                  normalization_function(Nashville_offence[('Scoring', 'A')], Mean_Assists, Std_Assists),
                                  normalization_function(Nashville_offence[('Scoring', 'PIM')], Mean_Penalities,
                                                         Std_Penalities),
                                  normalization_function(Nashville_offence[('Unnamed: 26_level_0', 'FOW')], Mean_Faceoffwins,
                                                         Std_Faceoffwins),
                                  normalization_function(Nashville_offence[('Unnamed: 27_level_0', 'FOL')],Mean_Faceoffloses,
                                                         Std_Faceoffloses)) + \
                 defence_function(normalization_function(Nashville_defence[('Unnamed: 24_level_0', 'BLK')], Mean_Blocks,
                                                         Std_Blocks),
                                  normalization_function(Nashville_defence[('Unnamed: 25_level_0', 'HIT')], Mean_Hits,
                                                         Std_Hits),
                                  normalization_function(Nashville_goalie[('Goalie Stats', 'GA')], Mean_Goalie,
                                                         Std_Goalie))
# Dallas Stars
Dallas_final = offence_function(normalization_function(Dallas_offence[('Unnamed: 17_level_0', 'S')],Mean_Scoring,
                                                         Std_Scoring),
                                  normalization_function(Dallas_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
                                  normalization_function(Dallas_offence[('Scoring', 'A')], Mean_Assists, Std_Assists),
                                  normalization_function(Dallas_offence[('Scoring', 'PIM')], Mean_Penalities,
                                                         Std_Penalities),
                                  normalization_function(Dallas_offence[('Unnamed: 26_level_0', 'FOW')], Mean_Faceoffwins,
                                                         Std_Faceoffwins),
                                  normalization_function(Dallas_offence[('Unnamed: 27_level_0', 'FOL')],Mean_Faceoffloses,
                                                         Std_Faceoffloses)) + \
                 defence_function(normalization_function(Dallas_defence[('Unnamed: 24_level_0', 'BLK')], Mean_Blocks,
                                                         Std_Blocks),
                                  normalization_function(Dallas_defence[('Unnamed: 25_level_0', 'HIT')], Mean_Hits,
                                                         Std_Hits),
                                  normalization_function(Dallas_goalie[('Goalie Stats', 'GA')], Mean_Goalie,
                                                         Std_Goalie))
# Chicago Blackhawks
Chicago_final = offence_function(normalization_function(Chicago_offence[('Unnamed: 17_level_0', 'S')],Mean_Scoring,
                                                         Std_Scoring),
                                  normalization_function(Chicago_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
                                  normalization_function(Chicago_offence[('Scoring', 'A')], Mean_Assists, Std_Assists),
                                  normalization_function(Chicago_offence[('Scoring', 'PIM')], Mean_Penalities,
                                                         Std_Penalities),
                                  normalization_function(Chicago_offence[('Unnamed: 26_level_0', 'FOW')], Mean_Faceoffwins,
                                                         Std_Faceoffwins),
                                  normalization_function(Chicago_offence[('Unnamed: 27_level_0', 'FOL')],Mean_Faceoffloses,
                                                         Std_Faceoffloses)) + \
                 defence_function(normalization_function(Chicago_defence[('Unnamed: 24_level_0', 'BLK')], Mean_Blocks,
                                                         Std_Blocks),
                                  normalization_function(Chicago_defence[('Unnamed: 25_level_0', 'HIT')], Mean_Hits,
                                                         Std_Hits),
                                  normalization_function(Chicago_goalie[('Goalie Stats', 'GA')], Mean_Goalie,
                                                         Std_Goalie))
# Columbus Blue Jackets
Columbus_final = offence_function(normalization_function(Columbus_offence[('Unnamed: 17_level_0', 'S')],Mean_Scoring,
                                                         Std_Scoring),
                                  normalization_function(Columbus_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
                                  normalization_function(Columbus_offence[('Scoring', 'A')], Mean_Assists, Std_Assists),
                                  normalization_function(Columbus_offence[('Scoring', 'PIM')], Mean_Penalities,
                                                         Std_Penalities),
                                  normalization_function(Columbus_offence[('Unnamed: 26_level_0', 'FOW')], Mean_Faceoffwins,
                                                         Std_Faceoffwins),
                                  normalization_function(Columbus_offence[('Unnamed: 27_level_0', 'FOL')],Mean_Faceoffloses,
                                                         Std_Faceoffloses)) + \
                 defence_function(normalization_function(Columbus_defence[('Unnamed: 24_level_0', 'BLK')], Mean_Blocks,
                                                         Std_Blocks),
                                  normalization_function(Columbus_defence[('Unnamed: 25_level_0', 'HIT')], Mean_Hits,
                                                         Std_Hits),
                                  normalization_function(Columbus_goalie[('Goalie Stats', 'GA')], Mean_Goalie,
                                                         Std_Goalie))
# Detroit Redwings
Detroit_final = offence_function(normalization_function(Detroit_offence[('Unnamed: 17_level_0', 'S')],Mean_Scoring,
                                                         Std_Scoring),
                                  normalization_function(Detroit_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
                                  normalization_function(Detroit_offence[('Scoring', 'A')], Mean_Assists, Std_Assists),
                                  normalization_function(Detroit_offence[('Scoring', 'PIM')], Mean_Penalities,
                                                         Std_Penalities),
                                  normalization_function(Detroit_offence[('Unnamed: 26_level_0', 'FOW')], Mean_Faceoffwins,
                                                         Std_Faceoffwins),
                                  normalization_function(Detroit_offence[('Unnamed: 27_level_0', 'FOL')],Mean_Faceoffloses,
                                                         Std_Faceoffloses)) + \
                 defence_function(normalization_function(Detroit_defence[('Unnamed: 24_level_0', 'BLK')], Mean_Blocks,
                                                         Std_Blocks),
                                  normalization_function(Detroit_defence[('Unnamed: 25_level_0', 'HIT')], Mean_Hits,
                                                         Std_Hits),
                                  normalization_function(Detroit_goalie[('Goalie Stats', 'GA')], Mean_Goalie,
                                                         Std_Goalie))
# Pittsburgh Penguins
Pittsburgh_final = offence_function(normalization_function(Pittsburgh_offence[('Unnamed: 17_level_0', 'S')],Mean_Scoring,
                                                         Std_Scoring),
                                  normalization_function(Pittsburgh_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
                                  normalization_function(Pittsburgh_offence[('Scoring', 'A')], Mean_Assists, Std_Assists),
                                  normalization_function(Pittsburgh_offence[('Scoring', 'PIM')], Mean_Penalities,
                                                         Std_Penalities),
                                  normalization_function(Pittsburgh_offence[('Unnamed: 26_level_0', 'FOW')], Mean_Faceoffwins,
                                                         Std_Faceoffwins),
                                  normalization_function(Pittsburgh_offence[('Unnamed: 27_level_0', 'FOL')],Mean_Faceoffloses,
                                                         Std_Faceoffloses)) + \
                 defence_function(normalization_function(Pittsburgh_defence[('Unnamed: 24_level_0', 'BLK')], Mean_Blocks,
                                                         Std_Blocks),
                                  normalization_function(Pittsburgh_defence[('Unnamed: 25_level_0', 'HIT')], Mean_Hits,
                                                         Std_Hits),
                                  normalization_function(Pittsburgh_goalie[('Goalie Stats', 'GA')], Mean_Goalie,
                                                         Std_Goalie))
# Washington Capitals
Washington_final = offence_function(normalization_function(Washington_offence[('Unnamed: 17_level_0', 'S')],Mean_Scoring,
                                                         Std_Scoring),
                                  normalization_function(Washington_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
                                  normalization_function(Washington_offence[('Scoring', 'A')], Mean_Assists, Std_Assists),
                                  normalization_function(Washington_offence[('Scoring', 'PIM')], Mean_Penalities,
                                                         Std_Penalities),
                                  normalization_function(Washington_offence[('Unnamed: 26_level_0', 'FOW')], Mean_Faceoffwins,
                                                         Std_Faceoffwins),
                                  normalization_function(Washington_offence[('Unnamed: 27_level_0', 'FOL')],Mean_Faceoffloses,
                                                         Std_Faceoffloses)) + \
                 defence_function(normalization_function(Washington_defence[('Unnamed: 24_level_0', 'BLK')], Mean_Blocks,
                                                         Std_Blocks),
                                  normalization_function(Washington_defence[('Unnamed: 25_level_0', 'HIT')], Mean_Hits,
                                                         Std_Hits),
                                  normalization_function(Washington_goalie[('Goalie Stats', 'GA')], Mean_Goalie,
                                                         Std_Goalie))
# Boston Bruins
Boston_final = offence_function(normalization_function(Boston_offence[('Unnamed: 17_level_0', 'S')],Mean_Scoring,
                                                         Std_Scoring),
                                  normalization_function(Boston_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
                                  normalization_function(Boston_offence[('Scoring', 'A')], Mean_Assists, Std_Assists),
                                  normalization_function(Boston_offence[('Scoring', 'PIM')], Mean_Penalities,
                                                         Std_Penalities),
                                  normalization_function(Boston_offence[('Unnamed: 26_level_0', 'FOW')], Mean_Faceoffwins,
                                                         Std_Faceoffwins),
                                  normalization_function(Boston_offence[('Unnamed: 27_level_0', 'FOL')],Mean_Faceoffloses,
                                                         Std_Faceoffloses)) + \
                 defence_function(normalization_function(Boston_defence[('Unnamed: 24_level_0', 'BLK')], Mean_Blocks,
                                                         Std_Blocks),
                                  normalization_function(Boston_defence[('Unnamed: 25_level_0', 'HIT')], Mean_Hits,
                                                         Std_Hits),
                                  normalization_function(Boston_goalie[('Goalie Stats', 'GA')], Mean_Goalie,
                                                         Std_Goalie))
# New York Islanders
NewyorkI_final = offence_function(normalization_function(NewyorkI_offence[('Unnamed: 17_level_0', 'S')],Mean_Scoring,
                                                         Std_Scoring),
                                  normalization_function(NewyorkI_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
                                  normalization_function(NewyorkI_offence[('Scoring', 'A')], Mean_Assists, Std_Assists),
                                  normalization_function(NewyorkI_offence[('Scoring', 'PIM')], Mean_Penalities,
                                                         Std_Penalities),
                                  normalization_function(NewyorkI_offence[('Unnamed: 26_level_0', 'FOW')], Mean_Faceoffwins,
                                                         Std_Faceoffwins),
                                  normalization_function(NewyorkI_offence[('Unnamed: 27_level_0', 'FOL')],Mean_Faceoffloses,
                                                         Std_Faceoffloses)) + \
                 defence_function(normalization_function(NewyorkI_defence[('Unnamed: 24_level_0', 'BLK')], Mean_Blocks,
                                                         Std_Blocks),
                                  normalization_function(NewyorkI_defence[('Unnamed: 25_level_0', 'HIT')], Mean_Hits,
                                                         Std_Hits),
                                  normalization_function(NewyorkI_goalie[('Goalie Stats', 'GA')], Mean_Goalie,
                                                         Std_Goalie))
# New York Rangers
NewyorkR_final = offence_function(normalization_function(NewyorkR_offence[('Unnamed: 17_level_0', 'S')],Mean_Scoring,
                                                         Std_Scoring),
                                  normalization_function(NewyorkR_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
                                  normalization_function(NewyorkR_offence[('Scoring', 'A')], Mean_Assists, Std_Assists),
                                  normalization_function(NewyorkR_offence[('Scoring', 'PIM')], Mean_Penalities,
                                                         Std_Penalities),
                                  normalization_function(NewyorkR_offence[('Unnamed: 26_level_0', 'FOW')], Mean_Faceoffwins,
                                                         Std_Faceoffwins),
                                  normalization_function(NewyorkR_offence[('Unnamed: 27_level_0', 'FOL')],Mean_Faceoffloses,
                                                         Std_Faceoffloses)) + \
                 defence_function(normalization_function(NewyorkR_defence[('Unnamed: 24_level_0', 'BLK')], Mean_Blocks,
                                                         Std_Blocks),
                                  normalization_function(NewyorkR_defence[('Unnamed: 25_level_0', 'HIT')], Mean_Hits,
                                                         Std_Hits),
                                  normalization_function(NewyorkR_goalie[('Goalie Stats', 'GA')], Mean_Goalie,
                                                         Std_Goalie))
# Philadelphia Flyers
Philadelphia_final = offence_function(normalization_function(Philadelphia_offence[('Unnamed: 17_level_0', 'S')],Mean_Scoring,
                                                         Std_Scoring),
                                  normalization_function(Philadelphia_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
                                  normalization_function(Philadelphia_offence[('Scoring', 'A')], Mean_Assists, Std_Assists),
                                  normalization_function(Philadelphia_offence[('Scoring', 'PIM')], Mean_Penalities,
                                                         Std_Penalities),
                                  normalization_function(Philadelphia_offence[('Unnamed: 26_level_0', 'FOW')], Mean_Faceoffwins,
                                                         Std_Faceoffwins),
                                  normalization_function(Philadelphia_offence[('Unnamed: 27_level_0', 'FOL')],Mean_Faceoffloses,
                                                         Std_Faceoffloses)) + \
                 defence_function(normalization_function(Philadelphia_defence[('Unnamed: 24_level_0', 'BLK')], Mean_Blocks,
                                                         Std_Blocks),
                                  normalization_function(Philadelphia_defence[('Unnamed: 25_level_0', 'HIT')], Mean_Hits,
                                                         Std_Hits),
                                  normalization_function(Philadelphia_goalie[('Goalie Stats', 'GA')], Mean_Goalie,
                                                         Std_Goalie))
# New Jersey Devils
Newjersey_final = offence_function(normalization_function(Newjersey_offence[('Unnamed: 17_level_0', 'S')],Mean_Scoring,
                                                         Std_Scoring),
                                  normalization_function(Newjersey_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
                                  normalization_function(Newjersey_offence[('Scoring', 'A')], Mean_Assists, Std_Assists),
                                  normalization_function(Newjersey_offence[('Scoring', 'PIM')], Mean_Penalities,
                                                         Std_Penalities),
                                  normalization_function(Newjersey_offence[('Unnamed: 26_level_0', 'FOW')], Mean_Faceoffwins,
                                                         Std_Faceoffwins),
                                  normalization_function(Newjersey_offence[('Unnamed: 27_level_0', 'FOL')],Mean_Faceoffloses,
                                                         Std_Faceoffloses)) + \
                 defence_function(normalization_function(Newjersey_defence[('Unnamed: 24_level_0', 'BLK')], Mean_Blocks,
                                                         Std_Blocks),
                                  normalization_function(Newjersey_defence[('Unnamed: 25_level_0', 'HIT')], Mean_Hits,
                                                         Std_Hits),
                                  normalization_function(Newjersey_goalie[('Goalie Stats', 'GA')], Mean_Goalie,
                                                         Std_Goalie))
# Buffalo Sabers
Buffalo_final = offence_function(normalization_function(Buffalo_offence[('Unnamed: 17_level_0', 'S')],Mean_Scoring,
                                                         Std_Scoring),
                                  normalization_function(Buffalo_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
                                  normalization_function(Buffalo_offence[('Scoring', 'A')], Mean_Assists, Std_Assists),
                                  normalization_function(Buffalo_offence[('Scoring', 'PIM')], Mean_Penalities,
                                                         Std_Penalities),
                                  normalization_function(Buffalo_offence[('Unnamed: 26_level_0', 'FOW')], Mean_Faceoffwins,
                                                         Std_Faceoffwins),
                                  normalization_function(Buffalo_offence[('Unnamed: 27_level_0', 'FOL')],Mean_Faceoffloses,
                                                         Std_Faceoffloses)) + \
                 defence_function(normalization_function(Buffalo_defence[('Unnamed: 24_level_0', 'BLK')], Mean_Blocks,
                                                         Std_Blocks),
                                  normalization_function(Buffalo_defence[('Unnamed: 25_level_0', 'HIT')], Mean_Hits,
                                                         Std_Hits),
                                  normalization_function(Buffalo_goalie[('Goalie Stats', 'GA')], Mean_Goalie,
                                                         Std_Goalie))
# Toronto Maple Leafs
Toronto_final = offence_function(normalization_function(Toronto_offence[('Unnamed: 17_level_0', 'S')],Mean_Scoring,
                                                         Std_Scoring),
                                  normalization_function(Toronto_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
                                  normalization_function(Toronto_offence[('Scoring', 'A')], Mean_Assists, Std_Assists),
                                  normalization_function(Toronto_offence[('Scoring', 'PIM')], Mean_Penalities,
                                                         Std_Penalities),
                                  normalization_function(Toronto_offence[('Unnamed: 26_level_0', 'FOW')], Mean_Faceoffwins,
                                                         Std_Faceoffwins),
                                  normalization_function(Toronto_offence[('Unnamed: 27_level_0', 'FOL')],Mean_Faceoffloses,
                                                         Std_Faceoffloses)) + \
                 defence_function(normalization_function(Toronto_defence[('Unnamed: 24_level_0', 'BLK')], Mean_Blocks,
                                                         Std_Blocks),
                                  normalization_function(Toronto_defence[('Unnamed: 25_level_0', 'HIT')], Mean_Hits,
                                                         Std_Hits),
                                  normalization_function(Toronto_goalie[('Goalie Stats', 'GA')], Mean_Goalie,
                                                         Std_Goalie))
# Edmonton Oilers
Edmonton_final = offence_function(normalization_function(Edmonton_offence[('Unnamed: 17_level_0', 'S')],Mean_Scoring,
                                                         Std_Scoring),
                                  normalization_function(Edmonton_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
                                  normalization_function(Edmonton_offence[('Scoring', 'A')], Mean_Assists, Std_Assists),
                                  normalization_function(Edmonton_offence[('Scoring', 'PIM')], Mean_Penalities,
                                                         Std_Penalities),
                                  normalization_function(Edmonton_offence[('Unnamed: 26_level_0', 'FOW')], Mean_Faceoffwins,
                                                         Std_Faceoffwins),
                                  normalization_function(Edmonton_offence[('Unnamed: 27_level_0', 'FOL')],Mean_Faceoffloses,
                                                         Std_Faceoffloses)) + \
                 defence_function(normalization_function(Edmonton_defence[('Unnamed: 24_level_0', 'BLK')], Mean_Blocks,
                                                         Std_Blocks),
                                  normalization_function(Edmonton_defence[('Unnamed: 25_level_0', 'HIT')], Mean_Hits,
                                                         Std_Hits),
                                  normalization_function(Edmonton_goalie[('Goalie Stats', 'GA')], Mean_Goalie,
                                                         Std_Goalie))
# Winnipeg Jets
Winnipeg_final = offence_function(normalization_function(Winnipeg_offence[('Unnamed: 17_level_0', 'S')],Mean_Scoring,
                                                         Std_Scoring),
                                  normalization_function(Winnipeg_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
                                  normalization_function(Winnipeg_offence[('Scoring', 'A')], Mean_Assists, Std_Assists),
                                  normalization_function(Winnipeg_offence[('Scoring', 'PIM')], Mean_Penalities,
                                                         Std_Penalities),
                                  normalization_function(Winnipeg_offence[('Unnamed: 26_level_0', 'FOW')], Mean_Faceoffwins,
                                                         Std_Faceoffwins),
                                  normalization_function(Winnipeg_offence[('Unnamed: 27_level_0', 'FOL')],Mean_Faceoffloses,
                                                         Std_Faceoffloses)) + \
                 defence_function(normalization_function(Winnipeg_defence[('Unnamed: 24_level_0', 'BLK')], Mean_Blocks,
                                                         Std_Blocks),
                                  normalization_function(Winnipeg_defence[('Unnamed: 25_level_0', 'HIT')], Mean_Hits,
                                                         Std_Hits),
                                  normalization_function(Winnipeg_goalie[('Goalie Stats', 'GA')], Mean_Goalie,
                                                         Std_Goalie))
# Montreal Canedians
Montreal_final = offence_function(normalization_function(Montreal_offence[('Unnamed: 17_level_0', 'S')],Mean_Scoring,
                                                         Std_Scoring),
                                  normalization_function(Montreal_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
                                  normalization_function(Montreal_offence[('Scoring', 'A')], Mean_Assists, Std_Assists),
                                  normalization_function(Montreal_offence[('Scoring', 'PIM')], Mean_Penalities,
                                                         Std_Penalities),
                                  normalization_function(Montreal_offence[('Unnamed: 26_level_0', 'FOW')], Mean_Faceoffwins,
                                                         Std_Faceoffwins),
                                  normalization_function(Montreal_offence[('Unnamed: 27_level_0', 'FOL')],Mean_Faceoffloses,
                                                         Std_Faceoffloses)) + \
                 defence_function(normalization_function(Montreal_defence[('Unnamed: 24_level_0', 'BLK')], Mean_Blocks,
                                                         Std_Blocks),
                                  normalization_function(Montreal_defence[('Unnamed: 25_level_0', 'HIT')], Mean_Hits,
                                                         Std_Hits),
                                  normalization_function(Montreal_goalie[('Goalie Stats', 'GA')], Mean_Goalie,
                                                         Std_Goalie))
# Calgary Flames
Calgary_final = offence_function(normalization_function(Calgary_offence[('Unnamed: 17_level_0', 'S')],Mean_Scoring,
                                                         Std_Scoring),
                                  normalization_function(Calgary_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
                                  normalization_function(Calgary_offence[('Scoring', 'A')], Mean_Assists, Std_Assists),
                                  normalization_function(Calgary_offence[('Scoring', 'PIM')], Mean_Penalities,
                                                         Std_Penalities),
                                  normalization_function(Calgary_offence[('Unnamed: 26_level_0', 'FOW')], Mean_Faceoffwins,
                                                         Std_Faceoffwins),
                                  normalization_function(Calgary_offence[('Unnamed: 27_level_0', 'FOL')],Mean_Faceoffloses,
                                                         Std_Faceoffloses)) + \
                 defence_function(normalization_function(Calgary_defence[('Unnamed: 24_level_0', 'BLK')], Mean_Blocks,
                                                         Std_Blocks),
                                  normalization_function(Calgary_defence[('Unnamed: 25_level_0', 'HIT')], Mean_Hits,
                                                         Std_Hits),
                                  normalization_function(Calgary_goalie[('Goalie Stats', 'GA')], Mean_Goalie,
                                                         Std_Goalie))
# Ottawa Senators
Ottawa_final = offence_function(normalization_function(Ottawa_offence[('Unnamed: 17_level_0', 'S')],Mean_Scoring,
                                                         Std_Scoring),
                                  normalization_function(Ottawa_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
                                  normalization_function(Ottawa_offence[('Scoring', 'A')], Mean_Assists, Std_Assists),
                                  normalization_function(Ottawa_offence[('Scoring', 'PIM')], Mean_Penalities,
                                                         Std_Penalities),
                                  normalization_function(Ottawa_offence[('Unnamed: 26_level_0', 'FOW')], Mean_Faceoffwins,
                                                         Std_Faceoffwins),
                                  normalization_function(Ottawa_offence[('Unnamed: 27_level_0', 'FOL')],Mean_Faceoffloses,
                                                         Std_Faceoffloses)) + \
                 defence_function(normalization_function(Ottawa_defence[('Unnamed: 24_level_0', 'BLK')], Mean_Blocks,
                                                         Std_Blocks),
                                  normalization_function(Ottawa_defence[('Unnamed: 25_level_0', 'HIT')], Mean_Hits,
                                                         Std_Hits),
                                  normalization_function(Ottawa_goalie[('Goalie Stats', 'GA')], Mean_Goalie,
                                                         Std_Goalie))
# Vancouver Canucks
Vancouver_final = offence_function(normalization_function(Vancouver_offence[('Unnamed: 17_level_0', 'S')],Mean_Scoring,
                                                         Std_Scoring),
                                  normalization_function(Vancouver_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
                                  normalization_function(Vancouver_offence[('Scoring', 'A')], Mean_Assists, Std_Assists),
                                  normalization_function(Vancouver_offence[('Scoring', 'PIM')], Mean_Penalities,
                                                         Std_Penalities),
                                  normalization_function(Vancouver_offence[('Unnamed: 26_level_0', 'FOW')], Mean_Faceoffwins,
                                                         Std_Faceoffwins),
                                  normalization_function(Vancouver_offence[('Unnamed: 27_level_0', 'FOL')],Mean_Faceoffloses,
                                                         Std_Faceoffloses)) + \
                 defence_function(normalization_function(Vancouver_defence[('Unnamed: 24_level_0', 'BLK')], Mean_Blocks,
                                                         Std_Blocks),
                                  normalization_function(Vancouver_defence[('Unnamed: 25_level_0', 'HIT')], Mean_Hits,
                                                         Std_Hits),
                                  normalization_function(Vancouver_goalie[('Goalie Stats', 'GA')], Mean_Goalie,
                                                         Std_Goalie))
# Colorado Avalanche
Colorado_final = offence_function(normalization_function(Colorado_offence[('Unnamed: 17_level_0', 'S')],Mean_Scoring,
                                                         Std_Scoring),
                                  normalization_function(Colorado_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
                                  normalization_function(Colorado_offence[('Scoring', 'A')], Mean_Assists, Std_Assists),
                                  normalization_function(Colorado_offence[('Scoring', 'PIM')], Mean_Penalities,
                                                         Std_Penalities),
                                  normalization_function(Colorado_offence[('Unnamed: 26_level_0', 'FOW')], Mean_Faceoffwins,
                                                         Std_Faceoffwins),
                                  normalization_function(Colorado_offence[('Unnamed: 27_level_0', 'FOL')],Mean_Faceoffloses,
                                                         Std_Faceoffloses)) + \
                 defence_function(normalization_function(Colorado_defence[('Unnamed: 24_level_0', 'BLK')], Mean_Blocks,
                                                         Std_Blocks),
                                  normalization_function(Colorado_defence[('Unnamed: 25_level_0', 'HIT')], Mean_Hits,
                                                         Std_Hits),
                                  normalization_function(Colorado_goalie[('Goalie Stats', 'GA')], Mean_Goalie,
                                                         Std_Goalie))
# Los Vegas Knights
Vegas_final = offence_function(normalization_function(Vegas_offence[('Unnamed: 17_level_0', 'S')],Mean_Scoring,
                                                         Std_Scoring),
                                  normalization_function(Vegas_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
                                  normalization_function(Vegas_offence[('Scoring', 'A')], Mean_Assists, Std_Assists),
                                  normalization_function(Vegas_offence[('Scoring', 'PIM')], Mean_Penalities,
                                                         Std_Penalities),
                                  normalization_function(Vegas_offence[('Unnamed: 26_level_0', 'FOW')], Mean_Faceoffwins,
                                                         Std_Faceoffwins),
                                  normalization_function(Vegas_offence[('Unnamed: 27_level_0', 'FOL')],Mean_Faceoffloses,
                                                         Std_Faceoffloses)) + \
                 defence_function(normalization_function(Vegas_defence[('Unnamed: 24_level_0', 'BLK')], Mean_Blocks,
                                                         Std_Blocks),
                                  normalization_function(Vegas_defence[('Unnamed: 25_level_0', 'HIT')], Mean_Hits,
                                                         Std_Hits),
                                  normalization_function(Vegas_goalie[('Goalie Stats', 'GA')], Mean_Goalie,
                                                         Std_Goalie))
# Minnesota Wild
Minnesota_final = offence_function(normalization_function(Minnesota_offence[('Unnamed: 17_level_0', 'S')],Mean_Scoring,
                                                         Std_Scoring),
                                  normalization_function(Minnesota_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
                                  normalization_function(Minnesota_offence[('Scoring', 'A')], Mean_Assists, Std_Assists),
                                  normalization_function(Minnesota_offence[('Scoring', 'PIM')], Mean_Penalities,
                                                         Std_Penalities),
                                  normalization_function(Minnesota_offence[('Unnamed: 26_level_0', 'FOW')], Mean_Faceoffwins,
                                                         Std_Faceoffwins),
                                  normalization_function(Minnesota_offence[('Unnamed: 27_level_0', 'FOL')],Mean_Faceoffloses,
                                                         Std_Faceoffloses)) + \
                 defence_function(normalization_function(Minnesota_defence[('Unnamed: 24_level_0', 'BLK')], Mean_Blocks,
                                                         Std_Blocks),
                                  normalization_function(Minnesota_defence[('Unnamed: 25_level_0', 'HIT')], Mean_Hits,
                                                         Std_Hits),
                                  normalization_function(Minnesota_goalie[('Goalie Stats', 'GA')], Mean_Goalie,
                                                         Std_Goalie))
# St. Louis Blues
Stlouis_final = offence_function(normalization_function(Stlouis_offence[('Unnamed: 17_level_0', 'S')],Mean_Scoring,
                                                         Std_Scoring),
                                  normalization_function(Stlouis_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
                                  normalization_function(Stlouis_offence[('Scoring', 'A')], Mean_Assists, Std_Assists),
                                  normalization_function(Stlouis_offence[('Scoring', 'PIM')], Mean_Penalities,
                                                         Std_Penalities),
                                  normalization_function(Stlouis_offence[('Unnamed: 26_level_0', 'FOW')], Mean_Faceoffwins,
                                                         Std_Faceoffwins),
                                  normalization_function(Stlouis_offence[('Unnamed: 27_level_0', 'FOL')],Mean_Faceoffloses,
                                                         Std_Faceoffloses)) + \
                 defence_function(normalization_function(Stlouis_defence[('Unnamed: 24_level_0', 'BLK')], Mean_Blocks,
                                                         Std_Blocks),
                                  normalization_function(Stlouis_defence[('Unnamed: 25_level_0', 'HIT')], Mean_Hits,
                                                         Std_Hits),
                                  normalization_function(Stlouis_goalie[('Goalie Stats', 'GA')], Mean_Goalie,
                                                         Std_Goalie))
# Arizona Coyotes
Arizona_final = offence_function(normalization_function(Arizona_offence[('Unnamed: 17_level_0', 'S')],Mean_Scoring,
                                                         Std_Scoring),
                                  normalization_function(Arizona_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
                                  normalization_function(Arizona_offence[('Scoring', 'A')], Mean_Assists, Std_Assists),
                                  normalization_function(Arizona_offence[('Scoring', 'PIM')], Mean_Penalities,
                                                         Std_Penalities),
                                  normalization_function(Arizona_offence[('Unnamed: 26_level_0', 'FOW')], Mean_Faceoffwins,
                                                         Std_Faceoffwins),
                                  normalization_function(Arizona_offence[('Unnamed: 27_level_0', 'FOL')],Mean_Faceoffloses,
                                                         Std_Faceoffloses)) + \
                 defence_function(normalization_function(Arizona_defence[('Unnamed: 24_level_0', 'BLK')], Mean_Blocks,
                                                         Std_Blocks),
                                  normalization_function(Arizona_defence[('Unnamed: 25_level_0', 'HIT')], Mean_Hits,
                                                         Std_Hits),
                                  normalization_function(Arizona_goalie[('Goalie Stats', 'GA')], Mean_Goalie,
                                                         Std_Goalie))
# San Jose Sharks
Sanjose_final = offence_function(normalization_function(Sanjose_offence[('Unnamed: 17_level_0', 'S')],Mean_Scoring,
                                                         Std_Scoring),
                                  normalization_function(Sanjose_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
                                  normalization_function(Sanjose_offence[('Scoring', 'A')], Mean_Assists, Std_Assists),
                                  normalization_function(Sanjose_offence[('Scoring', 'PIM')], Mean_Penalities,
                                                         Std_Penalities),
                                  normalization_function(Sanjose_offence[('Unnamed: 26_level_0', 'FOW')], Mean_Faceoffwins,
                                                         Std_Faceoffwins),
                                  normalization_function(Sanjose_offence[('Unnamed: 27_level_0', 'FOL')],Mean_Faceoffloses,
                                                         Std_Faceoffloses)) + \
                 defence_function(normalization_function(Sanjose_defence[('Unnamed: 24_level_0', 'BLK')], Mean_Blocks,
                                                         Std_Blocks),
                                  normalization_function(Sanjose_defence[('Unnamed: 25_level_0', 'HIT')], Mean_Hits,
                                                         Std_Hits),
                                  normalization_function(Sanjose_goalie[('Goalie Stats', 'GA')], Mean_Goalie,
                                                         Std_Goalie))
# Los Angeles Kings
Losangeles_final = offence_function(normalization_function(Losangeles_offence[('Unnamed: 17_level_0', 'S')],Mean_Scoring,
                                                         Std_Scoring),
                                  normalization_function(Losangeles_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
                                  normalization_function(Losangeles_offence[('Scoring', 'A')], Mean_Assists, Std_Assists),
                                  normalization_function(Losangeles_offence[('Scoring', 'PIM')], Mean_Penalities,
                                                         Std_Penalities),
                                  normalization_function(Losangeles_offence[('Unnamed: 26_level_0', 'FOW')], Mean_Faceoffwins,
                                                         Std_Faceoffwins),
                                  normalization_function(Losangeles_offence[('Unnamed: 27_level_0', 'FOL')],Mean_Faceoffloses,
                                                         Std_Faceoffloses)) + \
                 defence_function(normalization_function(Losangeles_defence[('Unnamed: 24_level_0', 'BLK')], Mean_Blocks,
                                                         Std_Blocks),
                                  normalization_function(Losangeles_defence[('Unnamed: 25_level_0', 'HIT')], Mean_Hits,
                                                         Std_Hits),
                                  normalization_function(Losangeles_goalie[('Goalie Stats', 'GA')], Mean_Goalie,
                                                         Std_Goalie))
# Anaheim Ducks
Anaheim_final = offence_function(normalization_function(Anaheim_offence[('Unnamed: 17_level_0', 'S')],Mean_Scoring,
                                                         Std_Scoring),
                                  normalization_function(Anaheim_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
                                  normalization_function(Anaheim_offence[('Scoring', 'A')], Mean_Assists, Std_Assists),
                                  normalization_function(Anaheim_offence[('Unnamed: 9_level_0', 'PIM')], Mean_Penalities,
                                                         Std_Penalities),
                                  normalization_function(Anaheim_offence[('Unnamed: 26_level_0', 'FOW')], Mean_Faceoffwins,
                                                         Std_Faceoffwins),
                                  normalization_function(Anaheim_offence[('Unnamed: 27_level_0', 'FOL')], Mean_Faceoffloses,
                                                         Std_Faceoffloses)) + \
                 defence_function(normalization_function(Anaheim_defence[('Unnamed: 24_level_0', 'BLK')], Mean_Blocks,
                                                         Std_Blocks),
                                  normalization_function(Anaheim_defence[('Unnamed: 25_level_0', 'HIT')], Mean_Hits,
                                                         Std_Hits),
                                  normalization_function(Anaheim_goalie[('Goalie Stats', 'GA')], Mean_Goalie,
                                                         Std_Goalie))

Seattle_final = offence_function(normalization_function(Seattle_offence[('Unnamed: 17_level_0', 'S')],Mean_Scoring,
                                                         Std_Scoring),
                                  normalization_function(Seattle_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
                                  normalization_function(Seattle_offence[('Scoring', 'A')], Mean_Assists, Std_Assists),
                                  normalization_function(Seattle_offence[('Scoring', 'PIM')], Mean_Penalities,
                                                         Std_Penalities),
                                  normalization_function(Seattle_offence[('Unnamed: 26_level_0', 'FOW')], Mean_Faceoffwins,
                                                         Std_Faceoffwins),
                                  normalization_function(Seattle_offence[('Unnamed: 27_level_0', 'FOL')], Mean_Faceoffloses,
                                                         Std_Faceoffloses)) + \
                 defence_function(normalization_function(Seattle_defence[('Unnamed: 24_level_0', 'BLK')], Mean_Blocks,
                                                         Std_Blocks),
                                  normalization_function(Seattle_defence[('Unnamed: 25_level_0', 'HIT')], Mean_Hits,
                                                         Std_Hits),
                                  normalization_function(Seattle_goalie[('Goalie Stats', 'GA')], Mean_Goalie,
                                                         Std_Goalie))