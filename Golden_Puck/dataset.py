from packages import pd, np

def offence_function(goals, faceoff_wins, faceoff_loses):
    offence = 0.7 * ( np.sum(goals) + 0.3 * (np.sum(faceoff_wins) - np.sum(faceoff_loses)) )
    return offence

def defence_function(blocks, hits, goalie):
    defence = 0.1 * (np.sum(blocks)) + 0.1 * (np.sum(hits)) + 0.8 * (np.sum(goalie))
    return defence

def normalization_function(variable, mean, std):
    normalized_value = ( variable - mean ) / std
    return normalized_value

def injury_function(dataset, injury_array):
    dataset = dataset[~dataset.isin(injury_array)]
    dataset.dropna(subset=[('Unnamed: 1_level_0', 'Player')], inplace = True)
    return dataset

injury_table_number = 0
no_injury_table = None # in case a team has no injuries
offence_table_number = 4
goalie_table_number = 5
df_cutoff_value = 12

# Carolina Hurricanes
Carolina_df = pd.read_html('https://www.hockey-reference.com/teams/CAR/2022.html')

    # Accounting for injuries
Carolina_injury_df = pd.DataFrame(Carolina_df[injury_table_number])
Carolina_injury_array = np.array(Carolina_injury_df['Player']).astype(str)


    # Accounting for Offence
Carolina_offence_df = pd.DataFrame(Carolina_df[offence_table_number])
        # Injuries on Offence & Defence
Carolina_offence_df = injury_function(Carolina_offence_df, Carolina_injury_array)

Carolina_offence = Carolina_offence_df.loc[0:df_cutoff_value, [('Scoring', 'G'),
                                                  ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]

    # Accounting for Defence
Carolina_defence = Carolina_offence_df.loc[0:df_cutoff_value, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Carolina_goalie = pd.DataFrame(Carolina_df[goalie_table_number])
        # Goalie Injuries
Carolina_goalie = injury_function(Carolina_goalie, Carolina_injury_array)

Carolina_goalie = Carolina_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Florida Panthers
Florida_df = pd.read_html('https://www.hockey-reference.com/teams/FLA/2022.html')
Florida_offence_df = pd.DataFrame(Florida_df[offence_table_number])

    # Accounting for injuries
Florida_injury_df = pd.DataFrame(Florida_df[injury_table_number])
Florida_injury_array = np.array(Florida_injury_df['Player']).astype(str)

        # Injuries on Offence & Defence
Florida_offence_df = injury_function(Florida_offence_df, Florida_injury_array)

Florida_offence = Florida_offence_df.loc[0:df_cutoff_value, [('Scoring', 'G'),
                                                  ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Florida_defence = Florida_offence_df.loc[0:df_cutoff_value, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Florida_goalie = pd.DataFrame(Florida_df[goalie_table_number])
        # Goalie Injuries
Florida_goalie = injury_function(Florida_goalie, Florida_injury_array)

Florida_goalie = Florida_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Tampa Bay Lightning
Tampabay_df = pd.read_html('https://www.hockey-reference.com/teams/TBL/2022.html')
Tampabay_offence_df = pd.DataFrame(Tampabay_df[offence_table_number])

    # Accounting for injuries
Tampabay_injury_df = pd.DataFrame(Tampabay_df[injury_table_number])
Tampabay_injury_array = np.array(Tampabay_injury_df['Player']).astype(str)
        # Injuries on Offence & Defence
Tampabay_offence_df = injury_function(Tampabay_offence_df, Tampabay_injury_array)

Tampabay_offence = Tampabay_offence_df.loc[0:df_cutoff_value, [('Scoring', 'G'),
                                                  ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Tampabay_defence = Tampabay_offence_df.loc[0:df_cutoff_value, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Tampabay_goalie = pd.DataFrame(Tampabay_df[goalie_table_number])
        # Goalie Injuries
Tampabay_goalie = injury_function(Tampabay_goalie, Tampabay_injury_array)
Tampabay_goalie = Tampabay_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Nashville Predators
Nashville_df = pd.read_html('https://www.hockey-reference.com/teams/NSH/2022.html')
Nashville_offence_df = pd.DataFrame(Nashville_df[offence_table_number])

    # Accounting for injuries
Nashville_injury_df = pd.DataFrame(Nashville_df[injury_table_number])
Nashville_injury_array = np.array(Nashville_injury_df['Player']).astype(str)
        # Injuries on Offence & Defence
Nashville_offence_df = injury_function(Nashville_offence_df, Nashville_injury_array)

Nashville_offence = Nashville_offence_df.loc[0:df_cutoff_value, [('Scoring', 'G'),
                                                  ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Nashville_defence = Nashville_offence_df.loc[0:df_cutoff_value, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Nashville_goalie = pd.DataFrame(Nashville_df[goalie_table_number])
        # Goalie Injuries
Nashville_goalie = injury_function(Nashville_goalie, Nashville_injury_array)
Nashville_goalie = Nashville_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Dallas Stars
Dallas_df = pd.read_html('https://www.hockey-reference.com/teams/DAL/2022.html')
Dallas_offence_df = pd.DataFrame(Dallas_df[offence_table_number])

    # Accounting for injuries
Dallas_injury_df = pd.DataFrame(Dallas_df[injury_table_number])
Dallas_injury_array = np.array(Dallas_injury_df['Player']).astype(str)
        # Injuries on Offence & Defence
Dallas_offence_df = injury_function(Dallas_offence_df, Dallas_injury_array)

Dallas_offence = Dallas_offence_df.loc[0:df_cutoff_value, [('Scoring', 'G'),
                                                  ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Dallas_defence = Dallas_offence_df.loc[0:df_cutoff_value, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Dallas_goalie = pd.DataFrame(Dallas_df[goalie_table_number])
        # Goalie Injuries
Dallas_goalie = injury_function(Dallas_goalie, Dallas_injury_array)
Dallas_goalie = Dallas_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Chicago Blackhawks
Chicago_df = pd.read_html('https://www.hockey-reference.com/teams/CHI/2022.html')
Chicago_offence_df = pd.DataFrame(Chicago_df[offence_table_number])

    # Accounting for injuries
Chicago_injury_df = pd.DataFrame(Chicago_df[injury_table_number])
Chicago_injury_array = np.array(Chicago_injury_df['Player']).astype(str)
        # Injuries on Offence & Defence
Chicago_offence_df = injury_function(Chicago_offence_df, Chicago_injury_array)

Chicago_offence = Chicago_offence_df.loc[0:df_cutoff_value, [('Scoring', 'G'),
                                                  ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Chicago_defence = Chicago_offence_df.loc[0:df_cutoff_value, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Chicago_goalie = pd.DataFrame(Chicago_df[goalie_table_number])
        # Goalie Injuries
Chicago_goalie = injury_function(Chicago_goalie, Chicago_injury_array)
Chicago_goalie = Chicago_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Columbus Blue Jackets
Columbus_df = pd.read_html('https://www.hockey-reference.com/teams/CBJ/2022.html')
Columbus_offence_df = pd.DataFrame(Columbus_df[offence_table_number])

    # Accounting for injuries
Columbus_injury_df = pd.DataFrame(Columbus_df[injury_table_number])
Columbus_injury_array = np.array(Columbus_injury_df['Player']).astype(str)
        # Injuries on Offence & Defence
Columbus_offence_df = injury_function(Columbus_offence_df, Columbus_injury_array)

Columbus_offence = Columbus_offence_df.loc[0:df_cutoff_value, [('Scoring', 'G'),
                                                  ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Columbus_defence = Columbus_offence_df.loc[0:df_cutoff_value, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Columbus_goalie = pd.DataFrame(Columbus_df[goalie_table_number])
        # Goalie Injuries
Columbus_goalie = injury_function(Columbus_goalie, Columbus_injury_array)
Columbus_goalie = Columbus_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Detroit Redwings
Detroit_df = pd.read_html('https://www.hockey-reference.com/teams/DET/2022.html')
Detroit_offence_df = pd.DataFrame(Detroit_df[offence_table_number])

    # Accounting for injuries
Detroit_injury_df = pd.DataFrame(Detroit_df[injury_table_number])
Detroit_injury_array = np.array(Detroit_injury_df['Player']).astype(str)
        # Injuries on Offence & Defence
Detroit_offence_df = injury_function(Detroit_offence_df, Detroit_injury_array)

Detroit_offence = Detroit_offence_df.loc[0:df_cutoff_value, [('Scoring', 'G'),
                                                  ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Detroit_defence = Detroit_offence_df.loc[0:df_cutoff_value, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Detroit_goalie = pd.DataFrame(Detroit_df[goalie_table_number])
        # Goalie Injuries
Detroit_goalie = injury_function(Detroit_goalie, Detroit_injury_array)
Detroit_goalie = Detroit_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Pittsburgh Penguins
Pittsburgh_df = pd.read_html('https://www.hockey-reference.com/teams/PIT/2022.html')
Pittsburgh_offence_df = pd.DataFrame(Pittsburgh_df[offence_table_number])

    # Accounting for injuries
Pittsburgh_injury_df = pd.DataFrame(Pittsburgh_df[injury_table_number])
Pittsburgh_injury_array = np.array(Pittsburgh_injury_df['Player']).astype(str)
        # Injuries on Offence & Defence
Pittsburgh_offence_df = injury_function(Pittsburgh_offence_df, Pittsburgh_injury_array)

Pittsburgh_offence = Pittsburgh_offence_df.loc[0:df_cutoff_value, [('Scoring', 'G'),
                                                  ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Pittsburgh_defence = Pittsburgh_offence_df.loc[0:df_cutoff_value, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Pittsburgh_goalie = pd.DataFrame(Pittsburgh_df[goalie_table_number])
        # Goalie Injuries
Pittsburgh_goalie = injury_function(Pittsburgh_goalie, Pittsburgh_injury_array)
Pittsburgh_goalie = Pittsburgh_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Washington Capitals
Washington_df = pd.read_html('https://www.hockey-reference.com/teams/WSH/2022.html')
Washington_offence_df = pd.DataFrame(Washington_df[offence_table_number])

    # Accounting for injuries
Washington_injury_df = pd.DataFrame(Washington_df[injury_table_number])
Washington_injury_array = np.array(Washington_injury_df['Player']).astype(str)
        # Injuries on Offence & Defence
Washington_offence_df = injury_function(Washington_offence_df, Washington_injury_array)

Washington_offence = Washington_offence_df.loc[0:df_cutoff_value, [('Scoring', 'G'),
                                                  ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Washington_defence = Washington_offence_df.loc[0:df_cutoff_value, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Washington_goalie = pd.DataFrame(Washington_df[goalie_table_number])
        # Goalie Injuries
Washington_goalie = injury_function(Washington_goalie, Washington_injury_array)
Washington_goalie = Washington_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Boston Bruins
Boston_df = pd.read_html('https://www.hockey-reference.com/teams/BOS/2022.html')
Boston_offence_df = pd.DataFrame(Boston_df[offence_table_number])

    # Accounting for injuries
Boston_injury_df = pd.DataFrame(Boston_df[injury_table_number])
Boston_injury_array = np.array(Boston_injury_df['Player']).astype(str)
        # Injuries on Offence & Defence
Boston_offence_df = injury_function(Boston_offence_df, Boston_injury_array)

Boston_offence = Boston_offence_df.loc[0:df_cutoff_value, [('Scoring', 'G'),
                                                  ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Boston_defence = Boston_offence_df.loc[0:df_cutoff_value, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Boston_goalie = pd.DataFrame(Boston_df[goalie_table_number])
        # Goalie Injuries
Boston_goalie = injury_function(Boston_goalie, Boston_injury_array)

Boston_goalie = Boston_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# New York Islanders
NewyorkI_df = pd.read_html('https://www.hockey-reference.com/teams/NYI/2022.html')
NewyorkI_offence_df = pd.DataFrame(NewyorkI_df[3])

    # Accounting for injuries
# NewyorkI_injury_df = pd.DataFrame(NewyorkI_df[no_injury_table])
# NewyorkI_injury_array = np.array(NewyorkI_injury_df['Player']).astype(str)
        # Injuries on Offence & Defence
# NewyorkI_offence_df = injury_function(NewyorkI_offence_df, NewyorkI_injury_array)

NewyorkI_offence = NewyorkI_offence_df.loc[0:df_cutoff_value, [('Scoring', 'G'),
                                                  ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
NewyorkI_defence = NewyorkI_offence_df.loc[0:df_cutoff_value, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
NewyorkI_goalie = pd.DataFrame(NewyorkI_df[4])
        # Goalie Injuries
# NewyorkI_goalie = injury_function(NewyorkI_goalie, NewyorkI_injury_array)
NewyorkI_goalie = NewyorkI_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# New York Rangers
NewyorkR_df = pd.read_html('https://www.hockey-reference.com/teams/NYR/2022.html')
NewyorkR_offence_df = pd.DataFrame(NewyorkR_df[offence_table_number])

    # Accounting for injuries
NewyorkR_injury_df = pd.DataFrame(NewyorkR_df[injury_table_number])
NewyorkR_injury_array = np.array(NewyorkR_injury_df['Player']).astype(str)
        # Injuries on Offence & Defence
NewyorkR_offence_df = injury_function(NewyorkR_offence_df, NewyorkR_injury_array)

NewyorkR_offence = NewyorkR_offence_df.loc[0:df_cutoff_value, [('Scoring', 'G'),
                                                  ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
NewyorkR_defence = NewyorkR_offence_df.loc[0:df_cutoff_value, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
NewyorkR_goalie = pd.DataFrame(NewyorkR_df[goalie_table_number])
        # Goalie Injuries
NewyorkR_goalie = injury_function(NewyorkR_goalie, NewyorkR_injury_array)
NewyorkR_goalie = NewyorkR_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Philadelphia Flyers
Philadelphia_df = pd.read_html('https://www.hockey-reference.com/teams/PHI/2022.html')
Philadelphia_offence_df = pd.DataFrame(Philadelphia_df[offence_table_number])

    # Accounting for injuries
Philadelphia_injury_df = pd.DataFrame(Philadelphia_df[injury_table_number])
Philadelphia_injury_array = np.array(Philadelphia_injury_df['Player']).astype(str)
        # Injuries on Offence & Defence
Philadelphia_offence_df = injury_function(Philadelphia_offence_df, Philadelphia_injury_array)

Philadelphia_offence = Philadelphia_offence_df.loc[0:df_cutoff_value, [('Scoring', 'G'),
                                                  ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Philadelphia_defence = Philadelphia_offence_df.loc[0:df_cutoff_value, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Philadelphia_goalie = pd.DataFrame(Philadelphia_df[goalie_table_number])
        # Goalie Injuries
Philadelphia_goalie = injury_function(Philadelphia_goalie, Philadelphia_injury_array)
Philadelphia_goalie = Philadelphia_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# New Jersey Devils
Newjersey_df = pd.read_html('https://www.hockey-reference.com/teams/NJD/2022.html')
Newjersey_offence_df = pd.DataFrame(Newjersey_df[offence_table_number])

    # Accounting for injuries
Newjersey_injury_df = pd.DataFrame(Newjersey_df[injury_table_number])
Newjersey_injury_array = np.array(Newjersey_injury_df['Player']).astype(str)
        # Injuries on Offence & Defence
Newjersey_offence_df = injury_function(Newjersey_offence_df, Newjersey_injury_array)

Newjersey_offence = Newjersey_offence_df.loc[0:df_cutoff_value, [('Scoring', 'G'),
                                                  ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Newjersey_defence = Newjersey_offence_df.loc[0:df_cutoff_value, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Newjersey_goalie = pd.DataFrame(Newjersey_df[goalie_table_number])
        # Goalie Injuries
Newjersey_goalie = injury_function(Newjersey_goalie, Newjersey_injury_array)
Newjersey_goalie = Newjersey_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Buffalo Sabers
Buffalo_df = pd.read_html('https://www.hockey-reference.com/teams/BUF/2022.html')
Buffalo_offence_df = pd.DataFrame(Buffalo_df[offence_table_number])

    # Accounting for injuries
Buffalo_injury_df = pd.DataFrame(Buffalo_df[injury_table_number])
Buffalo_injury_array = np.array(Buffalo_injury_df['Player']).astype(str)
        # Injuries on Offence & Defence
Buffalo_offence_df = injury_function(Buffalo_offence_df, Buffalo_injury_array)

Buffalo_offence = Buffalo_offence_df.loc[0:df_cutoff_value, [('Scoring', 'G'),
                                                  ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Buffalo_defence = Buffalo_offence_df.loc[0:df_cutoff_value, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Buffalo_goalie = pd.DataFrame(Buffalo_df[goalie_table_number])
        # Goalie Injuries
Buffalo_goalie = injury_function(Buffalo_goalie, Buffalo_injury_array)
Buffalo_goalie = Buffalo_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Toronto Maple Leafs
Toronto_df = pd.read_html('https://www.hockey-reference.com/teams/TOR/2022.html')
Toronto_offence_df = pd.DataFrame(Toronto_df[offence_table_number])

    # Accounting for injuries
Toronto_injury_df = pd.DataFrame(Toronto_df[injury_table_number])
Toronto_injury_array = np.array(Toronto_injury_df['Player']).astype(str)
        # Injuries on Offence & Defence
Toronto_offence_df = injury_function(Toronto_offence_df, Toronto_injury_array)

Toronto_offence = Toronto_offence_df.loc[0:df_cutoff_value, [('Scoring', 'G'),
                                                  ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Toronto_defence = Toronto_offence_df.loc[0:df_cutoff_value, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Toronto_goalie = pd.DataFrame(Toronto_df[goalie_table_number])
        # Goalie Injuries
Toronto_goalie = injury_function(Toronto_goalie, Toronto_injury_array)
Toronto_goalie = Toronto_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Edmonton Oilers
Edmonton_df = pd.read_html('https://www.hockey-reference.com/teams/EDM/2022.html')
Edmonton_offence_df = pd.DataFrame(Edmonton_df[offence_table_number])

    # Accounting for injuries
Edmonton_injury_df = pd.DataFrame(Edmonton_df[injury_table_number])
Edmonton_injury_array = np.array(Edmonton_injury_df['Player']).astype(str)
        # Injuries on Offence & Defence
Edmonton_offence_df = injury_function(Edmonton_offence_df, Edmonton_injury_array)

Edmonton_offence = Edmonton_offence_df.loc[0:df_cutoff_value, [('Scoring', 'G'),
                                                  ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Edmonton_defence = Edmonton_offence_df.loc[0:df_cutoff_value, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Edmonton_goalie = pd.DataFrame(Edmonton_df[goalie_table_number])
        # Goalie Injuries
Edmonton_goalie = injury_function(Edmonton_goalie, Edmonton_injury_array)
Edmonton_goalie = Edmonton_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Winnipeg Jets
Winnipeg_df = pd.read_html('https://www.hockey-reference.com/teams/WPG/2022.html')
Winnipeg_offence_df = pd.DataFrame(Winnipeg_df[offence_table_number])

    # Accounting for injuries
Winnipeg_injury_df = pd.DataFrame(Winnipeg_df[injury_table_number])
Winnipeg_injury_array = np.array(Winnipeg_injury_df['Player']).astype(str)
        # Injuries on Offence & Defence
Winnipeg_offence_df = injury_function(Winnipeg_offence_df, Winnipeg_injury_array)

Winnipeg_offence = Winnipeg_offence_df.loc[0:df_cutoff_value, [('Scoring', 'G'),
                                                  ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Winnipeg_defence = Winnipeg_offence_df.loc[0:df_cutoff_value, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Winnipeg_goalie = pd.DataFrame(Winnipeg_df[goalie_table_number])
        # Goalie Injuries
Winnipeg_goalie = injury_function(Winnipeg_goalie, Winnipeg_injury_array)
Winnipeg_goalie = Winnipeg_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Montreal Canadiens
Montreal_df = pd.read_html('https://www.hockey-reference.com/teams/MTL/2022.html')
Montreal_offence_df = pd.DataFrame(Montreal_df[offence_table_number])

    # Accounting for injuries
Montreal_injury_df = pd.DataFrame(Montreal_df[injury_table_number])
Montreal_injury_array = np.array(Montreal_injury_df['Player']).astype(str)
        # Injuries on Offence & Defence
Montreal_offence_df = injury_function(Montreal_offence_df, Montreal_injury_array)

Montreal_offence = Montreal_offence_df.loc[0:df_cutoff_value, [('Scoring', 'G'),
                                                  ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Montreal_defence = Montreal_offence_df.loc[0:df_cutoff_value, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Montreal_goalie = pd.DataFrame(Montreal_df[goalie_table_number])
        # Goalie Injuries
Montreal_goalie = injury_function(Montreal_goalie, Montreal_injury_array)
Montreal_goalie = Montreal_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Calgary Flames
Calgary_df = pd.read_html('https://www.hockey-reference.com/teams/CGY/2022.html')
Calgary_offence_df = pd.DataFrame(Calgary_df[offence_table_number])

    # Accounting for injuries
Calgary_injury_df = pd.DataFrame(Calgary_df[injury_table_number])
Calgary_injury_array = np.array(Calgary_injury_df['Player']).astype(str)
        # Injuries on Offence & Defence
Calgary_offence_df = injury_function(Calgary_offence_df, Calgary_injury_array)

Calgary_offence = Calgary_offence_df.loc[0:df_cutoff_value, [('Scoring', 'G'),
                                                  ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Calgary_defence = Calgary_offence_df.loc[0:df_cutoff_value, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Calgary_goalie = pd.DataFrame(Calgary_df[goalie_table_number])
        # Goalie Injuries
Calgary_goalie = injury_function(Calgary_goalie, Calgary_injury_array)
Calgary_goalie = Calgary_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Ottawa Senators
Ottawa_df = pd.read_html('https://www.hockey-reference.com/teams/OTT/2022.html')
Ottawa_offence_df = pd.DataFrame(Ottawa_df[offence_table_number])

    # Accounting for injuries
Ottawa_injury_df = pd.DataFrame(Ottawa_df[injury_table_number])
Ottawa_injury_array = np.array(Ottawa_injury_df['Player']).astype(str)
        # Injuries on Offence & Defence
Ottawa_offence_df = injury_function(Ottawa_offence_df, Ottawa_injury_array)

Ottawa_offence = Ottawa_offence_df.loc[0:df_cutoff_value, [('Scoring', 'G'),
                                                  ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Ottawa_defence = Ottawa_offence_df.loc[0:df_cutoff_value, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Ottawa_goalie = pd.DataFrame(Ottawa_df[goalie_table_number])
        # Goalie Injuries
Ottawa_goalie = injury_function(Ottawa_goalie, Ottawa_injury_array)
Ottawa_goalie = Ottawa_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Vancouver Canucks
Vancouver_df = pd.read_html('https://www.hockey-reference.com/teams/VAN/2022.html')
Vancouver_offence_df = pd.DataFrame(Vancouver_df[offence_table_number])

    # Accounting for injuries
Vancouver_injury_df = pd.DataFrame(Vancouver_df[injury_table_number])
Vancouver_injury_array = np.array(Vancouver_injury_df['Player']).astype(str)
        # Injuries on Offence & Defence
Vancouver_offence_df = injury_function(Vancouver_offence_df, Vancouver_injury_array)

Vancouver_offence = Vancouver_offence_df.loc[0:df_cutoff_value, [('Scoring', 'G'),
                                                  ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Vancouver_defence = Vancouver_offence_df.loc[0:df_cutoff_value, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Vancouver_goalie = pd.DataFrame(Vancouver_df[goalie_table_number])
        # Goalie Injuries
Vancouver_goalie = injury_function(Vancouver_goalie, Vancouver_injury_array)
Vancouver_goalie = Vancouver_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Colorado Avalanche
Colorado_df = pd.read_html('https://www.hockey-reference.com/teams/COL/2022.html')
Colorado_offence_df = pd.DataFrame(Colorado_df[offence_table_number])

    # Accounting for injuries
Colorado_injury_df = pd.DataFrame(Colorado_df[injury_table_number])
Colorado_injury_array = np.array(Colorado_injury_df['Player']).astype(str)
        # Injuries on Offence & Defence
Colorado_offence_df = injury_function(Colorado_offence_df, Colorado_injury_array)

Colorado_offence = Colorado_offence_df.loc[0:df_cutoff_value, [('Scoring', 'G'),
                                                  ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Colorado_defence = Colorado_offence_df.loc[0:df_cutoff_value, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Colorado_goalie = pd.DataFrame(Colorado_df[goalie_table_number])
        # Goalie Injuries
Colorado_goalie = injury_function(Colorado_goalie, Colorado_injury_array)
Colorado_goalie = Colorado_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Vegas Golden Knights
Vegas_df = pd.read_html('https://www.hockey-reference.com/teams/VEG/2022.html')
Vegas_offence_df = pd.DataFrame(Vegas_df[offence_table_number])

    # Accounting for injuries
Vegas_injury_df = pd.DataFrame(Vegas_df[injury_table_number])
Vegas_injury_array = np.array(Vegas_injury_df['Player']).astype(str)
        # Injuries on Offence & Defence
Vegas_offence_df = injury_function(Vegas_offence_df, Vegas_injury_array)

Vegas_offence = Vegas_offence_df.loc[0:df_cutoff_value, [('Scoring', 'G'),
                                                  ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Vegas_defence = Vegas_offence_df.loc[0:df_cutoff_value, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Vegas_goalie = pd.DataFrame(Vegas_df[goalie_table_number])
        # Goalie Injuries
Vegas_goalie = injury_function(Vegas_goalie, Vegas_injury_array)
Vegas_goalie = Vegas_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Minnesota Wild
Minnesota_df = pd.read_html('https://www.hockey-reference.com/teams/MIN/2022.html')
Minnesota_offence_df = pd.DataFrame(Minnesota_df[offence_table_number])

    # Accounting for injuries
Minnesota_injury_df = pd.DataFrame(Minnesota_df[injury_table_number])
Minnesota_injury_array = np.array(Minnesota_injury_df['Player']).astype(str)
        # Injuries on Offence & Defence
Minnesota_offence_df = injury_function(Minnesota_offence_df, Minnesota_injury_array)

Minnesota_offence = Minnesota_offence_df.loc[0:df_cutoff_value, [('Scoring', 'G'),
                                                  ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Minnesota_defence = Minnesota_offence_df.loc[0:df_cutoff_value, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Minnesota_goalie = pd.DataFrame(Minnesota_df[goalie_table_number])
        # Goalie Injuries
Minnesota_goalie = injury_function(Minnesota_goalie, Minnesota_injury_array)
Minnesota_goalie = Minnesota_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# St. Louis Blues
Stlouis_df = pd.read_html('https://www.hockey-reference.com/teams/STL/2022.html')
Stlouis_offence_df = pd.DataFrame(Stlouis_df[offence_table_number])

    # Accounting for injuries
Stlouis_injury_df = pd.DataFrame(Stlouis_df[injury_table_number])
Stlouis_injury_array = np.array(Stlouis_injury_df['Player']).astype(str)
        # Injuries on Offence & Defence
Stlouis_offence_df = injury_function(Stlouis_offence_df, Stlouis_injury_array)

Stlouis_offence = Stlouis_offence_df.loc[0:df_cutoff_value, [('Scoring', 'G'),
                                                  ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Stlouis_defence = Stlouis_offence_df.loc[0:df_cutoff_value, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Stlouis_goalie = pd.DataFrame(Stlouis_df[goalie_table_number])
        # Goalie Injuries
Stlouis_goalie = injury_function(Stlouis_goalie, Stlouis_injury_array)
Stlouis_goalie = Stlouis_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Arizona Coyotes
Arizona_df = pd.read_html('https://www.hockey-reference.com/teams/ARI/2022.html')
Arizona_offence_df = pd.DataFrame(Arizona_df[offence_table_number])

    # Accounting for injuries
Arizona_injury_df = pd.DataFrame(Arizona_df[injury_table_number])
Arizona_injury_array = np.array(Arizona_injury_df['Player']).astype(str)
        # Injuries on Offence & Defence
Arizona_offence_df = injury_function(Arizona_offence_df, Arizona_injury_array)

Arizona_offence = Arizona_offence_df.loc[0:df_cutoff_value, [('Scoring', 'G'),
                                                  ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Arizona_defence = Arizona_offence_df.loc[0:df_cutoff_value, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Arizona_goalie = pd.DataFrame(Arizona_df[goalie_table_number])
        # Goalie Injuries
Arizona_goalie = injury_function(Arizona_goalie, Arizona_injury_array)
Arizona_goalie = Arizona_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# San Jose Sharks
Sanjose_df = pd.read_html('https://www.hockey-reference.com/teams/SJS/2022.html')
Sanjose_offence_df = pd.DataFrame(Sanjose_df[offence_table_number])

    # Accounting for injuries
Sanjose_injury_df = pd.DataFrame(Sanjose_df[injury_table_number])
Sanjose_injury_array = np.array(Sanjose_injury_df['Player']).astype(str)
        # Injuries on Offence & Defence
Sanjose_offence_df = injury_function(Sanjose_offence_df, Sanjose_injury_array)

Sanjose_offence = Sanjose_offence_df.loc[0:df_cutoff_value, [('Scoring', 'G'),
                                                  ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Sanjose_defence = Sanjose_offence_df.loc[0:df_cutoff_value, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Sanjose_goalie = pd.DataFrame(Sanjose_df[goalie_table_number])
        # Goalie Injuries
Sanjose_goalie = injury_function(Sanjose_goalie, Sanjose_injury_array)
Sanjose_goalie = Sanjose_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Los Angeles Kings
Losangeles_df = pd.read_html('https://www.hockey-reference.com/teams/LAK/2022.html')
Losangeles_offence_df = pd.DataFrame(Losangeles_df[offence_table_number])

    # Accounting for injuries
Losangeles_injury_df = pd.DataFrame(Losangeles_df[injury_table_number])
Losangeles_injury_array = np.array(Losangeles_injury_df['Player']).astype(str)
        # Injuries on Offence & Defence
Losangeles_offence_df = injury_function(Losangeles_offence_df, Losangeles_injury_array)

Losangeles_offence = Losangeles_offence_df.loc[0:df_cutoff_value, [('Scoring', 'G'),
                                                  ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Losangeles_defence = Losangeles_offence_df.loc[0:df_cutoff_value, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Losangeles_goalie = pd.DataFrame(Losangeles_df[goalie_table_number])
        # Goalie Injuries
Losangeles_goalie = injury_function(Losangeles_goalie, Losangeles_injury_array)
Losangeles_goalie = Losangeles_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Anaheim Ducks
Anaheim_df = pd.read_html('https://www.hockey-reference.com/teams/ANA/2022.html')
Anaheim_offence_df = pd.DataFrame(Anaheim_df[offence_table_number])

    # Accounting for injuries
Anaheim_injury_df = pd.DataFrame(Anaheim_df[injury_table_number])
Anaheim_injury_array = np.array(Anaheim_injury_df['Player']).astype(str)
        # Injuries on Offence & Defence
Anaheim_offence_df = injury_function(Anaheim_offence_df, Anaheim_injury_array)

Anaheim_offence = Anaheim_offence_df.loc[0:df_cutoff_value, [('Scoring', 'G'),
                                                  ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Anaheim_defence = Anaheim_offence_df.loc[0:df_cutoff_value, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Anaheim_goalie = pd.DataFrame(Anaheim_df[goalie_table_number])
        # Goalie Injuries
Anaheim_goalie = injury_function(Anaheim_goalie, Anaheim_injury_array)
Anaheim_goalie = Anaheim_goalie.loc[0:2, [('Goalie Stats', 'GA')]]

# Seattle Krakens
Seattle_df = pd.read_html('https://www.hockey-reference.com/teams/SEA/2022.html')
Seattle_offence_df = pd.DataFrame(Seattle_df[offence_table_number])

    # Accounting for injuries
Seattle_injury_df = pd.DataFrame(Seattle_df[injury_table_number])
Seattle_injury_array = np.array(Seattle_injury_df['Player']).astype(str)
        # Injuries on Offence & Defence
Seattle_offence_df = injury_function(Seattle_offence_df, Seattle_injury_array)

Seattle_offence = Seattle_offence_df.loc[0:df_cutoff_value, [('Scoring', 'G'),
                                                  ('Unnamed: 26_level_0', 'FOW'),
                                                  ('Unnamed: 27_level_0', 'FOL')]]
Seattle_defence = Seattle_offence_df.loc[0:df_cutoff_value, [('Unnamed: 24_level_0', 'BLK'), ('Unnamed: 25_level_0', 'HIT')]]
Seattle_goalie = pd.DataFrame(Seattle_df[goalie_table_number])
        # Goalie Injuries
Seattle_goalie = injury_function(Seattle_goalie, Seattle_injury_array)
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
Mean_Goals = np.mean(Full_offence_dataset[('Scoring', 'G')])
Mean_Faceoffwins = np.mean(Full_offence_dataset[('Unnamed: 26_level_0', 'FOW')])
Mean_Faceoffloses = np.mean(Full_offence_dataset[('Unnamed: 27_level_0', 'FOL')])
Mean_Blocks = np.mean(Full_defence_dataset[('Unnamed: 24_level_0', 'BLK')])
Mean_Hits = np.mean(Full_defence_dataset[('Unnamed: 25_level_0', 'HIT')])
Mean_Goalie = np.mean(Full_goalie_dataset[('Goalie Stats', 'GA')])

Std_Goals = np.std(Full_offence_dataset[('Scoring', 'G')])
Std_Faceoffwins = np.std(Full_offence_dataset[('Unnamed: 26_level_0', 'FOW')])
Std_Faceoffloses = np.std(Full_offence_dataset[('Unnamed: 27_level_0', 'FOL')])
Std_Blocks = np.std(Full_defence_dataset[('Unnamed: 24_level_0', 'BLK')])
Std_Hits = np.std(Full_defence_dataset[('Unnamed: 25_level_0', 'HIT')])
Std_Goalie = np.std(Full_goalie_dataset[('Goalie Stats', 'GA')])

# Final Normalized Averages

# Carolina Hurricanes
Carolina_final = offence_function(normalization_function(Carolina_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
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
Florida_final = offence_function(normalization_function(Florida_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
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
Tampabay_final = offence_function(normalization_function(Tampabay_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
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
Nashville_final = offence_function(normalization_function(Nashville_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
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
Dallas_final = offence_function(normalization_function(Dallas_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
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
Chicago_final = offence_function(normalization_function(Chicago_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
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
Columbus_final = offence_function(normalization_function(Columbus_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
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
Detroit_final = offence_function(normalization_function(Detroit_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
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
Pittsburgh_final = offence_function(normalization_function(Pittsburgh_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
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
Washington_final = offence_function(normalization_function(Washington_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
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
Boston_final = offence_function(normalization_function(Boston_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
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
NewyorkI_final = offence_function(normalization_function(NewyorkI_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
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
NewyorkR_final = offence_function(normalization_function(NewyorkR_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
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
Philadelphia_final = offence_function(normalization_function(Philadelphia_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
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
Newjersey_final = offence_function(normalization_function(Newjersey_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
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
Buffalo_final = offence_function(normalization_function(Buffalo_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
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
Toronto_final = offence_function(normalization_function(Toronto_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
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
Edmonton_final = offence_function(normalization_function(Edmonton_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
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
Winnipeg_final = offence_function(normalization_function(Winnipeg_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
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
Montreal_final = offence_function(normalization_function(Montreal_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
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
Calgary_final = offence_function(normalization_function(Calgary_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
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
Ottawa_final = offence_function(normalization_function(Ottawa_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
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
Vancouver_final = offence_function(normalization_function(Vancouver_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
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
Colorado_final = offence_function(normalization_function(Colorado_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
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
Vegas_final = offence_function(normalization_function(Vegas_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
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
Minnesota_final = offence_function(normalization_function(Minnesota_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
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
Stlouis_final = offence_function(normalization_function(Stlouis_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
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
Arizona_final = offence_function(normalization_function(Arizona_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
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
Sanjose_final = offence_function(normalization_function(Sanjose_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
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
Losangeles_final = offence_function(normalization_function(Losangeles_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
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
Anaheim_final = offence_function(normalization_function(Anaheim_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
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

Seattle_final = offence_function(normalization_function(Seattle_offence[('Scoring', 'G')], Mean_Goals, Std_Goals),
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