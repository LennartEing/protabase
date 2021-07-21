import numpy as np


'''
Dose response curve as described in: https://www.graphpad.com/guides/prism/latest/curve-fitting/reg_classic_dr_variable.htm
'''


def sigmoidal_dose_response_with_variable_slope(x_data, bottom, top, logec50, slope):
    numerator = top - bottom
    denominator = 1 + np.float_power(10, (logec50 - x_data) * slope, dtype=np.longdouble)
    return np.array(bottom + (numerator / denominator), dtype=np.float64)