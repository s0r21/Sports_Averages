# Final Script for basket ball
from dataset import np, pd
from dataset import BOS_Offence_Weighted_Avg, BRK_Offence_Weighted_Avg, TOR_Offence_Weighted_Avg, PHI_Offence_Weighted_Avg, \
NYK_Offence_Weighted_Avg, MIN_Offence_Weighted_Avg, OKC_Offence_Weighted_Avg, DEN_Offence_Weighted_Avg, POR_Offence_Weighted_Avg, \
UTA_Offence_Weighted_Avg, CHI_Offence_Weighted_Avg, CLE_Offence_Weighted_Avg, DET_Offence_Weighted_Avg, IND_Offence_Weighted_Avg, \
MIL_Offence_Weighted_Avg, LAL_Offence_Weighted_Avg, LAC_Offence_Weighted_Avg, GSW_Offence_Weighted_Avg, PHO_Offence_Weighted_Avg, \
SAC_Offence_Weighted_Avg, WAS_Offence_Weighted_Avg, ATL_Offence_Weighted_Avg, ORL_Offence_Weighted_Avg, MIA_Offence_Weighted_Avg, \
CHO_Offence_Weighted_Avg, MEM_Offence_Weighted_Avg, NOP_Offence_Weighted_Avg, HOU_Offence_Weighted_Avg, SAS_Offence_Weighted_Avg, \
DAL_Offence_Weighted_Avg

from dataset import BOS_Defence_Weighted_Avg, BRK_Defence_Weighted_Avg, TOR_Defence_Weighted_Avg, PHI_Defence_Weighted_Avg, \
NYK_Defence_Weighted_Avg, MIN_Defence_Weighted_Avg, OKC_Defence_Weighted_Avg, DEN_Defence_Weighted_Avg, POR_Defence_Weighted_Avg, \
UTA_Defence_Weighted_Avg, CHI_Defence_Weighted_Avg, CLE_Defence_Weighted_Avg, DET_Defence_Weighted_Avg, IND_Defence_Weighted_Avg, \
MIL_Defence_Weighted_Avg, LAL_Defence_Weighted_Avg, LAC_Defence_Weighted_Avg, GSW_Defence_Weighted_Avg, PHO_Defence_Weighted_Avg, \
SAC_Defence_Weighted_Avg, WAS_Defence_Weighted_Avg, ATL_Defence_Weighted_Avg, ORL_Defence_Weighted_Avg, MIA_Defence_Weighted_Avg, \
CHO_Defence_Weighted_Avg, MEM_Defence_Weighted_Avg, NOP_Defence_Weighted_Avg, HOU_Defence_Weighted_Avg, SAS_Defence_Weighted_Avg, \
DAL_Defence_Weighted_Avg

print("Enter Team 1 here: ")
team_one_input = input()
print("Enter Team 2 here: ")
team_two_input = input()

def input_function_team_one(team_one_function_input):
    if team_one_function_input == 'BOS':
        x = BOS_Offence_Weighted_Avg + BOS_Defence_Weighted_Avg
    elif team_one_function_input == 'BRK':
        x = BRK_Offence_Weighted_Avg + BRK_Defence_Weighted_Avg
    elif team_one_function_input == 'TOR':
        x = TOR_Offence_Weighted_Avg + TOR_Defence_Weighted_Avg
    elif team_one_function_input == 'PHI':
        x = PHI_Offence_Weighted_Avg + PHI_Defence_Weighted_Avg
    elif team_one_function_input == 'NYK':
        x = NYK_Offence_Weighted_Avg + NYK_Defence_Weighted_Avg
    elif team_one_function_input == 'MIN':
        x = MIN_Offence_Weighted_Avg + MIN_Defence_Weighted_Avg
    elif team_one_function_input == 'OKC':
        x = OKC_Offence_Weighted_Avg + OKC_Defence_Weighted_Avg
    elif team_one_function_input == 'DEN':
        x = DEN_Offence_Weighted_Avg + DEN_Defence_Weighted_Avg
    elif team_one_function_input == 'POR':
        x = POR_Offence_Weighted_Avg + POR_Defence_Weighted_Avg
    elif team_one_function_input == 'UTA':
        x = UTA_Offence_Weighted_Avg + UTA_Defence_Weighted_Avg
    elif team_one_function_input == 'CHI':
        x = CHI_Offence_Weighted_Avg + CHI_Defence_Weighted_Avg
    elif team_one_function_input == 'CLE':
        x = CLE_Offence_Weighted_Avg + CLE_Defence_Weighted_Avg
    elif team_one_function_input == 'DET':
        x = DET_Offence_Weighted_Avg + DET_Defence_Weighted_Avg
    elif team_one_function_input == 'IND':
        x = IND_Offence_Weighted_Avg + IND_Defence_Weighted_Avg
    elif team_one_function_input == 'MIL':
        x = MIL_Offence_Weighted_Avg + MIL_Defence_Weighted_Avg
    elif team_one_function_input == 'LAL':
        x = LAL_Offence_Weighted_Avg + LAL_Defence_Weighted_Avg
    elif team_one_function_input == 'LAC':
        x = LAC_Offence_Weighted_Avg + LAC_Defence_Weighted_Avg
    elif team_one_function_input == 'GSW':
        x = GSW_Offence_Weighted_Avg + GSW_Defence_Weighted_Avg
    elif team_one_function_input == 'PHO':
        x = PHO_Offence_Weighted_Avg + PHO_Defence_Weighted_Avg
    elif team_one_function_input == 'SAC':
        x = SAC_Offence_Weighted_Avg + SAC_Defence_Weighted_Avg
    elif team_one_function_input == 'WSN':
        x = WAS_Offence_Weighted_Avg + WAS_Defence_Weighted_Avg
    elif team_one_function_input == 'ATL':
        x = ATL_Offence_Weighted_Avg + ATL_Defence_Weighted_Avg
    elif team_one_function_input == 'ORL':
        x = ORL_Offence_Weighted_Avg + ORL_Defence_Weighted_Avg
    elif team_one_function_input == 'MIA':
        x = MIA_Offence_Weighted_Avg + MIA_Defence_Weighted_Avg
    elif team_one_function_input == 'CHO':
        x = CHO_Offence_Weighted_Avg + CHO_Defence_Weighted_Avg
    elif team_one_function_input == 'MEM':
        x = MEM_Offence_Weighted_Avg + MEM_Defence_Weighted_Avg
    elif team_one_function_input == 'NOP':
        x = NOP_Offence_Weighted_Avg + NOP_Defence_Weighted_Avg
    elif team_one_function_input == 'HOU':
        x = HOU_Offence_Weighted_Avg + HOU_Defence_Weighted_Avg
    elif team_one_function_input == 'SAS':
        x = SAS_Offence_Weighted_Avg + SAS_Defence_Weighted_Avg
    elif team_one_function_input == 'DAL':
        x = DAL_Offence_Weighted_Avg + DAL_Defence_Weighted_Avg
    return x

def input_function_team_two(team_two_function_input):
    if team_two_function_input == 'BOS':
        x = BOS_Offence_Weighted_Avg + BOS_Defence_Weighted_Avg
    elif team_two_function_input == 'BRK':
        x = BRK_Offence_Weighted_Avg + BRK_Defence_Weighted_Avg
    elif team_two_function_input == 'TOR':
        x = TOR_Offence_Weighted_Avg + TOR_Defence_Weighted_Avg
    elif team_two_function_input == 'PHI':
        x = PHI_Offence_Weighted_Avg + PHI_Defence_Weighted_Avg
    elif team_two_function_input == 'NYK':
        x = NYK_Offence_Weighted_Avg + NYK_Defence_Weighted_Avg
    elif team_two_function_input == 'MIN':
        x = MIN_Offence_Weighted_Avg + MIN_Defence_Weighted_Avg
    elif team_two_function_input == 'OKC':
        x = OKC_Offence_Weighted_Avg + OKC_Defence_Weighted_Avg
    elif team_two_function_input == 'DEN':
        x = DEN_Offence_Weighted_Avg + DEN_Defence_Weighted_Avg
    elif team_two_function_input == 'POR':
        x = POR_Offence_Weighted_Avg + POR_Defence_Weighted_Avg
    elif team_two_function_input == 'UTA':
        x = UTA_Offence_Weighted_Avg + UTA_Defence_Weighted_Avg
    elif team_two_function_input == 'CHI':
        x = CHI_Offence_Weighted_Avg + CHI_Defence_Weighted_Avg
    elif team_two_function_input == 'CLE':
        x = CLE_Offence_Weighted_Avg + CLE_Defence_Weighted_Avg
    elif team_two_function_input == 'DET':
        x = DET_Offence_Weighted_Avg + DET_Defence_Weighted_Avg
    elif team_two_function_input == 'IND':
        x = IND_Offence_Weighted_Avg + IND_Defence_Weighted_Avg
    elif team_two_function_input == 'MIL':
        x = MIL_Offence_Weighted_Avg + MIL_Defence_Weighted_Avg
    elif team_two_function_input == 'LAL':
        x = LAL_Offence_Weighted_Avg + LAL_Defence_Weighted_Avg
    elif team_two_function_input == 'LAC':
        x = LAC_Offence_Weighted_Avg + LAC_Defence_Weighted_Avg
    elif team_two_function_input == 'GSW':
        x = GSW_Offence_Weighted_Avg + GSW_Defence_Weighted_Avg
    elif team_two_function_input == 'PHO':
        x = PHO_Offence_Weighted_Avg + PHO_Defence_Weighted_Avg
    elif team_two_function_input == 'SAC':
        x = SAC_Offence_Weighted_Avg + SAC_Defence_Weighted_Avg
    elif team_two_function_input == 'WSN':
        x = WAS_Offence_Weighted_Avg + WAS_Defence_Weighted_Avg
    elif team_two_function_input == 'ATL':
        x = ATL_Offence_Weighted_Avg + ATL_Defence_Weighted_Avg
    elif team_two_function_input == 'ORL':
        x = ORL_Offence_Weighted_Avg + ORL_Defence_Weighted_Avg
    elif team_two_function_input == 'MIA':
        x = MIA_Offence_Weighted_Avg + MIA_Defence_Weighted_Avg
    elif team_two_function_input == 'CHO':
        x = CHO_Offence_Weighted_Avg + CHO_Defence_Weighted_Avg
    elif team_two_function_input == 'MEM':
        x = MEM_Offence_Weighted_Avg + MEM_Defence_Weighted_Avg
    elif team_two_function_input == 'NOP':
        x = NOP_Offence_Weighted_Avg + NOP_Defence_Weighted_Avg
    elif team_two_function_input == 'HOU':
        x = HOU_Offence_Weighted_Avg + HOU_Defence_Weighted_Avg
    elif team_two_function_input == 'SAS':
        x = SAS_Offence_Weighted_Avg + SAS_Defence_Weighted_Avg
    elif team_two_function_input == 'DAL':
        x = DAL_Offence_Weighted_Avg + DAL_Defence_Weighted_Avg
    return x


def game_results(team_one_average_results, team_two_average_results):
    if team_one_average_results > team_two_average_results:
        results = team_one_input
    else:
        results = team_two_input
    print("The following team is going to win: " + results)

game_results(input_function_team_one(team_one_input),input_function_team_two(team_two_input))