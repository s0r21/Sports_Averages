# The Main Script File to analyze each team and provide the results of who will win

from packages import pd, np
from dataset import Carolina_final, Vegas_final, Calgary_final, Chicago_final, Colorado_final, Columbus_final, \
    Boston_final, Buffalo_final, Florida_final, Dallas_final, Detroit_final, Ottawa_final, Anaheim_final, Arizona_final,\
    Sanjose_final, Stlouis_final, Toronto_final, Tampabay_final, Edmonton_final, Montreal_final, Minnesota_final, \
    Winnipeg_final, Washington_final, Losangeles_final, Pittsburgh_final, Nashville_final, Newjersey_final, \
    Vancouver_final, Philadelphia_final, NewyorkI_final, NewyorkR_final, Seattle_final

print("Enter Team 1 here: ")
team_one_input = input()
print("Enter Team 2 here: ")
team_two_input = input()

def input_function_team_one(team_one_function_input):
    if team_one_function_input == "CAR":
        team_one_value = Carolina_final
    elif team_one_function_input == "LVK":
        team_one_value = Vegas_final
    elif team_one_function_input == "CAL":
        team_one_value = Calgary_final
    elif team_one_function_input == "CHI":
        team_one_value = Chicago_final
    elif team_one_function_input == "COL":
        team_one_value = Colorado_final
    elif team_one_function_input == "CBJ":
        team_one_value = Columbus_final
    elif team_one_function_input == "BOS":
        team_one_value = Boston_final
    elif team_one_function_input == "BUF":
        team_one_value = Buffalo_final
    elif team_one_function_input == "FLO":
        team_one_value = Florida_final
    elif team_one_function_input == "DAL":
        team_one_value = Dallas_final
    elif team_one_function_input == "DET":
        team_one_value = Detroit_final
    elif team_one_function_input == "OTT":
        team_one_value = Ottawa_final
    elif team_one_function_input == "ANA":
        team_one_value = Anaheim_final
    elif team_one_function_input == "ARI":
        team_one_value = Arizona_final
    elif team_one_function_input == "SJS":
        team_one_value = Sanjose_final
    elif team_one_function_input == "STL":
        team_one_value = Stlouis_final
    elif team_one_function_input == "TOR":
        team_one_value = Toronto_final
    elif team_one_function_input == "TBL":
        team_one_value = Tampabay_final
    elif team_one_function_input == "EDM":
        team_one_value = Edmonton_final
    elif team_one_function_input == "MTL":
        team_one_value = Montreal_final
    elif team_one_function_input == "MIN":
        team_one_value = Minnesota_final
    elif team_one_function_input == "WPG":
        team_one_value = Winnipeg_final
    elif team_one_function_input == "WSH":
        team_one_value = Washington_final
    elif team_one_function_input == "LAK":
        team_one_value = Losangeles_final
    elif team_one_function_input == "PIT":
        team_one_value = Pittsburgh_final
    elif team_one_function_input == "NSH":
        team_one_value = Nashville_final
    elif team_one_function_input == "NJD":
        team_one_value = Newjersey_final
    elif team_one_function_input == "VAN":
        team_one_value = Vancouver_final
    elif team_one_function_input == "PHI":
        team_one_value = Philadelphia_final
    elif team_one_function_input == "NYI":
        team_one_value = NewyorkI_final
    elif team_one_function_input == "NYR":
        team_one_value = NewyorkR_final
    elif team_one_function_input == "SEA":
        team_one_value = Seattle_final
    return team_one_value

def input_function_team_two(team_two_function_input):
    if team_two_function_input == "CAR":
        team_two_value = Carolina_final
    elif team_two_function_input == "LVK":
        team_two_value = Vegas_final
    elif team_two_function_input == "CAL":
        team_two_value = Calgary_final
    elif team_two_function_input == "CHI":
        team_two_value = Chicago_final
    elif team_two_function_input == "COL":
        team_two_value = Colorado_final
    elif team_two_function_input == "CBJ":
        team_two_value = Columbus_final
    elif team_two_function_input == "BOS":
        team_two_value = Boston_final
    elif team_two_function_input == "BUF":
        team_two_value = Buffalo_final
    elif team_two_function_input == "FLO":
        team_two_value = Florida_final
    elif team_two_function_input == "DAL":
        team_two_value = Dallas_final
    elif team_two_function_input == "DET":
        team_two_value = Detroit_final
    elif team_two_function_input == "OTT":
        team_two_value = Ottawa_final
    elif team_two_function_input == "ANA":
        team_two_value = Anaheim_final
    elif team_two_function_input == "ARI":
        team_two_value = Arizona_final
    elif team_two_function_input == "SJS":
        team_two_value = Sanjose_final
    elif team_two_function_input == "STL":
        team_two_value = Stlouis_final
    elif team_two_function_input == "TOR":
        team_two_value = Toronto_final
    elif team_two_function_input == "TBL":
        team_two_value = Tampabay_final
    elif team_two_function_input == "EDM":
        team_two_value = Edmonton_final
    elif team_two_function_input == "MTL":
        team_two_value = Montreal_final
    elif team_two_function_input == "MIN":
        team_two_value = Minnesota_final
    elif team_two_function_input == "WPG":
        team_two_value = Winnipeg_final
    elif team_two_function_input == "WSH":
        team_two_value = Washington_final
    elif team_two_function_input == "LAK":
        team_two_value = Losangeles_final
    elif team_two_function_input == "PIT":
        team_two_value = Pittsburgh_final
    elif team_two_function_input == "NSH":
        team_two_value = Nashville_final
    elif team_two_function_input == "NJD":
        team_two_value = Newjersey_final
    elif team_two_function_input == "VAN":
        team_two_value = Vancouver_final
    elif team_two_function_input == "PHI":
        team_two_value = Philadelphia_final
    elif team_two_function_input == "NYI":
        team_two_value = NewyorkI_final
    elif team_two_function_input == "NYR":
        team_two_value = NewyorkR_final
    elif team_two_function_input == "SEA":
        team_two_value = Seattle_final
    return team_two_value

def game_results(team_one_average_results, team_two_average_results):
    if team_one_average_results > team_two_average_results:
        results = team_one_input
    else: results = team_two_input
    print("The following team is going to win: " + results)

game_results(input_function_team_one(team_one_input), input_function_team_two((team_two_input)))
