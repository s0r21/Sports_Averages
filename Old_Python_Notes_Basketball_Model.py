# --- in the Basketball\dataset.py. This is the old model (removed FG, Pf & ToV
# @staticmethod
# def offence_function(FG, ThreeP, TwoP, FT, ORB):
#     final_result = (0.1 * FG) + (0.5 * ThreeP) + (0.25 * TwoP) + \
#                    + (0.1 * FT) + (0.05 * ORB)
#     return final_result
#
#
# @staticmethod
# def defence_function(Stl, Blk, Drb, Pf, Tov):
#     final_result = (0.2 * Stl) + (0.1 * Blk) + \
#                    (0.1 * Drb) - ((0.3 * Pf) + (0.3 * Tov))
#     return final_result