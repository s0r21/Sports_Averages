# This page is strictly for the data preperation for the algo
import datetime

from packages import np, pd



data_set = [
# 2016 dataset
            pd.read_html('https://www.baseball-reference.com/teams/LAA/2016-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/TEX/2016-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/LAD/2016-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/SEA/2016-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/CHW/2016-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/BOS/2016-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/HOU/2016-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/BAL/2016-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/NYY/2016-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/TOR/2016-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/ARI/2016-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/TBR/2016-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/KCR/2016-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/SDP/2016-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/DET/2016-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/CLE/2016-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/SFG/2016-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/MIN/2016-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/STL/2016-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/NYM/2016-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/MIL/2016-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/CIN/2016-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/CHC/2016-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/PIT/2016-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/PHI/2016-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/MIA/2016-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/ATL/2016-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/WSN/2016-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/COL/2016-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/OAK/2016-schedule-scores.shtml#team_schedule'),

# 2017 dataset
            pd.read_html('https://www.baseball-reference.com/teams/LAA/2017-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/TEX/2017-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/LAD/2017-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/SEA/2017-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/CHW/2017-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/BOS/2017-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/HOU/2017-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/BAL/2017-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/NYY/2017-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/TOR/2017-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/ARI/2017-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/TBR/2017-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/KCR/2017-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/SDP/2017-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/DET/2017-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/CLE/2017-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/SFG/2017-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/MIN/2017-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/STL/2017-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/NYM/2017-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/MIL/2017-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/CIN/2017-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/CHC/2017-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/PIT/2017-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/PHI/2017-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/MIA/2017-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/ATL/2017-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/WSN/2017-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/COL/2017-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/OAK/2017-schedule-scores.shtml#team_schedule'),
# 2018 dataset
            pd.read_html('https://www.baseball-reference.com/teams/LAA/2018-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/TEX/2018-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/LAD/2018-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/SEA/2018-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/CHW/2018-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/BOS/2018-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/HOU/2018-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/BAL/2018-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/NYY/2018-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/TOR/2018-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/ARI/2018-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/TBR/2018-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/KCR/2018-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/SDP/2018-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/DET/2018-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/CLE/2018-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/SFG/2018-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/MIN/2018-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/STL/2018-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/NYM/2018-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/MIL/2018-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/CIN/2018-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/CHC/2018-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/PIT/2018-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/PHI/2018-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/MIA/2018-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/ATL/2018-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/WSN/2018-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/COL/2018-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/OAK/2018-schedule-scores.shtml#team_schedule'),
# 2019 dataset
            pd.read_html('https://www.baseball-reference.com/teams/LAA/2019-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/TEX/2019-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/LAD/2019-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/SEA/2019-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/CHW/2019-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/BOS/2019-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/HOU/2019-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/BAL/2019-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/NYY/2019-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/TOR/2019-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/ARI/2019-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/TBR/2019-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/KCR/2019-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/SDP/2019-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/DET/2019-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/CLE/2019-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/SFG/2019-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/MIN/2019-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/STL/2019-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/NYM/2019-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/MIL/2019-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/CIN/2019-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/CHC/2019-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/PIT/2019-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/PHI/2019-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/MIA/2019-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/ATL/2019-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/WSN/2019-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/COL/2019-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/OAK/2019-schedule-scores.shtml#team_schedule'),
# 2020 dataset
            pd.read_html('https://www.baseball-reference.com/teams/LAA/2020-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/TEX/2020-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/LAD/2020-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/SEA/2020-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/CHW/2020-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/BOS/2020-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/HOU/2020-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/BAL/2020-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/NYY/2020-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/TOR/2020-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/ARI/2020-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/TBR/2020-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/KCR/2020-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/SDP/2020-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/DET/2020-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/CLE/2020-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/SFG/2020-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/MIN/2020-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/STL/2020-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/NYM/2020-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/MIL/2020-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/CIN/2020-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/CHC/2020-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/PIT/2020-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/PHI/2020-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/MIA/2020-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/ATL/2020-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/WSN/2020-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/COL/2020-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/OAK/2020-schedule-scores.shtml#team_schedule'),
# 2021 dataset
            pd.read_html('https://www.baseball-reference.com/teams/LAA/2021-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/TEX/2021-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/LAD/2021-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/SEA/2021-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/CHW/2021-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/BOS/2021-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/HOU/2021-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/BAL/2021-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/NYY/2021-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/TOR/2021-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/ARI/2021-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/TBR/2021-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/KCR/2021-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/SDP/2021-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/DET/2021-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/CLE/2021-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/SFG/2021-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/MIN/2021-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/STL/2021-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/NYM/2021-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/MIL/2021-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/CIN/2021-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/CHC/2021-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/PIT/2021-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/PHI/2021-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/MIA/2021-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/ATL/2021-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/WSN/2021-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/COL/2021-schedule-scores.shtml#team_schedule'),
            pd.read_html('https://www.baseball-reference.com/teams/OAK/2021-schedule-scores.shtml#team_schedule')
]

df = pd.DataFrame(data_set[0][0]).append(data_set[1][0]).append(data_set[2][0]).append(data_set[3][0])\
    .append(data_set[4][0]).append(data_set[5][0]).append(data_set[6][0]).append(data_set[7][0]).append(data_set[8][0])\
    .append(data_set[9][0]).append(data_set[10][0]).append(data_set[11][0]).append(data_set[12][0]).append(data_set[13][0])\
    .append(data_set[14][0]).append(data_set[15][0]).append(data_set[16][0]).append(data_set[17][0]).append(data_set[18][0])\
    .append(data_set[19][0]).append(data_set[20][0]).append(data_set[21][0]).append(data_set[22][0]).append(data_set[23][0])\
    .append(data_set[24][0]).append(data_set[25][0]).append(data_set[26][0]).append(data_set[27][0]).append(data_set[28][0])\
    .append(data_set[29][0]).append(data_set[30][0]).append(data_set[31][0]).append(data_set[32][0]).append(data_set[33][0])\
    .append(data_set[34][0]).append(data_set[35][0]).append(data_set[36][0]).append(data_set[37][0]).append(data_set[38][0])\
    .append(data_set[39][0]).append(data_set[40][0]).append(data_set[41][0]).append(data_set[42][0]).append(data_set[43][0])\
    .append(data_set[44][0]).append(data_set[45][0]).append(data_set[46][0]).append(data_set[47][0]).append(data_set[48][0])\
    .append(data_set[49][0]).append(data_set[50][0]).append(data_set[51][0]).append(data_set[52][0]).append(data_set[53][0])\
    .append(data_set[54][0]).append(data_set[55][0]).append(data_set[56][0]).append(data_set[57][0]).append(data_set[58][0])\
    .append(data_set[59][0]).append(data_set[60][0]).append(data_set[61][0]).append(data_set[62][0]).append(data_set[63][0])\
    .append(data_set[64][0]).append(data_set[65][0]).append(data_set[66][0]).append(data_set[67][0]).append(data_set[68][0])\
    .append(data_set[69][0]).append(data_set[70][0]).append(data_set[71][0]).append(data_set[72][0]).append(data_set[73][0])\
    .append(data_set[74][0]).append(data_set[75][0]).append(data_set[76][0]).append(data_set[77][0]).append(data_set[78][0])\
    .append(data_set[79][0]).append(data_set[80][0]).append(data_set[81][0]).append(data_set[82][0]).append(data_set[83][0])\
    .append(data_set[84][0]).append(data_set[85][0]).append(data_set[86][0]).append(data_set[87][0]).append(data_set[88][0])\
    .append(data_set[89][0]).append(data_set[90][0]).append(data_set[91][0]).append(data_set[92][0]).append(data_set[93][0])\
    .append(data_set[94][0]).append(data_set[95][0]).append(data_set[96][0]).append(data_set[97][0]).append(data_set[98][0])\
    .append(data_set[99][0]).append(data_set[100][0]).append(data_set[101][0]).append(data_set[102][0]).append(data_set[103][0])\
    .append(data_set[104][0]).append(data_set[105][0]).append(data_set[106][0]).append(data_set[107][0]).append(data_set[108][0])\
    .append(data_set[109][0]).append(data_set[110][0]).append(data_set[111][0]).append(data_set[112][0]).append(data_set[113][0])\
    .append(data_set[114][0]).append(data_set[115][0]).append(data_set[116][0]).append(data_set[117][0]).append(data_set[118][0])\
    .append(data_set[119][0]).append(data_set[120][0]).append(data_set[121][0]).append(data_set[122][0]).append(data_set[123][0])\
    .append(data_set[124][0]).append(data_set[125][0]).append(data_set[126][0]).append(data_set[127][0]).append(data_set[128][0])\
    .append(data_set[129][0]).append(data_set[130][0]).append(data_set[131][0]).append(data_set[132][0]).append(data_set[133][0])\
    .append(data_set[134][0]).append(data_set[135][0]).append(data_set[136][0]).append(data_set[137][0]).append(data_set[138][0])\
    .append(data_set[139][0]).append(data_set[140][0]).append(data_set[141][0]).append(data_set[142][0]).append(data_set[143][0])\
    .append(data_set[144][0]).append(data_set[145][0]).append(data_set[146][0]).append(data_set[147][0]).append(data_set[148][0])\
    .append(data_set[149][0]).append(data_set[150][0]).append(data_set[151][0]).append(data_set[152][0]).append(data_set[153][0])\
    .append(data_set[154][0]).append(data_set[155][0]).append(data_set[156][0]).append(data_set[157][0]).append(data_set[158][0])\
    .append(data_set[159][0]).append(data_set[160][0]).append(data_set[161][0]).append(data_set[162][0]).append(data_set[163][0])\
    .append(data_set[164][0]).append(data_set[165][0]).append(data_set[166][0]).append(data_set[167][0]).append(data_set[168][0])\
    .append(data_set[169][0]).append(data_set[170][0]).append(data_set[171][0]).append(data_set[172][0]).append(data_set[173][0])\
    .append(data_set[174][0]).append(data_set[175][0]).append(data_set[176][0]).append(data_set[177][0]).append(data_set[178][0])\
    .append(data_set[179][0])

df['W/L'] = df['W/L'].replace(['L-wo', 'W-wo'], ['L', 'W'])
df = df[df.iloc[:, 0] != 'Gm#']


gamble_dataset = pd.DataFrame(df[['W/L', 'Tm', 'Opp']]) # NOTE: Input 'W/L' in the df[[]]
gamble_dataset['W/L'] = gamble_dataset['W/L'].replace(['L', 'W'], [0, 1])
gamble_dataset['Tm'] = gamble_dataset['Tm'].replace(['LAA', 'TEX', 'LAD', 'SEA', 'CHW', 'BOS', 'HOU', 'BAL', 'NYY',
                                                       'TOR', 'ARI', 'TBR', 'KCR', 'SDP', 'DET', 'CLE', 'SFG', 'MIN',
                                                       'STL', 'NYM', 'MIL', 'CIN', 'CHC', 'PIT', 'PHI', 'MIA', 'ATL',
                                                       'WSN', 'COL', 'OAK'],
                                                      [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,
                                                       26,27,28,29,30])
gamble_dataset['Opp'] = gamble_dataset['Opp'].replace(['LAA', 'TEX', 'LAD', 'SEA', 'CHW', 'BOS', 'HOU', 'BAL', 'NYY',
                                                       'TOR', 'ARI', 'TBR', 'KCR', 'SDP', 'DET', 'CLE', 'SFG', 'MIN',
                                                       'STL', 'NYM', 'MIL', 'CIN', 'CHC', 'PIT', 'PHI', 'MIA', 'ATL',
                                                       'WSN', 'COL', 'OAK'],
                                                      [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,
                                                       26,27,28,29,30])

gamble_dataset = gamble_dataset[(gamble_dataset['W/L'] == 1) | (gamble_dataset['W/L'] == 0)]
gamble_dataset = gamble_dataset.dropna()

