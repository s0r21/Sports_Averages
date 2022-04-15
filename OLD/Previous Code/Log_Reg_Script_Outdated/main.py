# This main one is going to be to run the model

from packages import np, pd, LogisticRegression
from data_prep import gamble_dataset

X = gamble_dataset[['Tm', 'Opp']]
y = gamble_dataset['W/L']

X_train = X[0:round(len(X)*0.8)]
y_train = y[0:round(len(X)*0.8)].astype('int')
X_test = X[0:round(len(X)*0.2)]
y_test = y[0:round(len(X)*0.2)].astype('int')

reg_model = LogisticRegression()
reg_model.fit(X_train, y_train)

y_prediction = reg_model.predict(X_test)
y_prediction = pd.DataFrame(y_prediction)
y_prediction = y_prediction.reset_index()

y_test = pd.DataFrame(y_test)
y_test = y_test.reset_index()

y_prediction = y_prediction.rename(columns={0 : "W/L_predict"})

y_test_reg = pd.DataFrame(np.transpose([y_test['W/L'], y_prediction['W/L_predict']]))
y_test_reg = y_test_reg.rename(columns={0 : "W/L_Actual",
                                        1 : "W/L_predict"})


y_test_reg.loc[y_test_reg['W/L_Actual'] == y_test_reg['W/L_predict'], 'Test'] = 1
y_test_reg.loc[y_test_reg['W/L_Actual'] != y_test_reg['W/L_predict'], 'Test'] = 0

percentage_chance = (np.sum(y_test_reg['Test']) / len(y_test)) * 100
print(percentage_chance)

print("Select Team 1: ")
team_one_selection = input()
print("Select Team 2: ")
team_two_selection = input()

def team_to_numbers(x):
    if x == 'LAA':
        team_selected = 1
    elif x == 'TEX':
        team_selected = 2
    elif x == 'LAD':
        team_selected = 3
    elif x == 'SEA':
        team_selected = 4
    elif x == 'CHW':
        team_selected = 5
    elif x == 'BOS':
        team_selected = 6
    elif x == 'HOU':
        team_selected = 7
    elif x == 'BAL':
        team_selected = 8
    elif x == 'NYY':
        team_selected = 9
    elif x == 'TOR':
        team_selected = 10
    elif x == 'ARI':
        team_selected = 11
    elif x == 'TBR':
        team_selected = 12
    elif x == 'KCR':
        team_selected = 13
    elif x == 'SDP':
        team_selected = 14
    elif x == 'DET':
        team_selected = 15
    elif x == 'CLE':
        team_selected = 16
    elif x == 'SFG':
        team_selected = 17
    elif x == 'MIN':
        team_selected = 18
    elif x == 'STL':
        team_selected = 19
    elif x == 'NYM':
        team_selected = 20
    elif x == 'MIL':
        team_selected = 21
    elif x == 'CIN':
        team_selected = 22
    elif x == 'CHC':
        team_selected = 23
    elif x == 'PIT':
        team_selected = 24
    elif x == 'PHI':
        team_selected = 25
    elif x == 'MIA':
        team_selected = 26
    elif x == 'ATL':
        team_selected = 27
    elif x == 'WSN':
        team_selected = 28
    elif x == 'COL':
        team_selected = 29
    elif x == 'OAK':
        team_selected = 30
    return team_selected

Team_one_chosen = team_to_numbers(team_one_selection)
Team_two_chosen = team_to_numbers(team_two_selection)

team_one_vs_team_two_values = np.transpose(pd.DataFrame([Team_one_chosen, Team_two_chosen]))

# t_plus_1_predict_data = pd.read_csv('C:/Users/t0ys0r/OneDrive/Desktop/Moneyball Predict CSV.csv')
t_plus_1_predict = reg_model.predict(team_one_vs_team_two_values)
print(t_plus_1_predict)

def winner_winner(x):
    if x == 1:
        print(team_one_selection + " is going to win")
    else: print(team_two_selection + " is going to win")

winner_winner(t_plus_1_predict)

# forward_test = pd.DataFrame(t_plus_1_predict)
# forward_test.columns = ['Team Prediction']

# forward_test.to_csv('Forward_test.csv')
