import numpy as np
import matplotlib.pyplot as plt
import warnings

from test import test_data_path
from scipy.optimize import curve_fit
from data import ExcelLoader
from fitting import sigmoidal_dose_response_with_variable_slope


warnings.simplefilter("ignore")


'''
Restricting data to lowest and highest y-value
'''
def restrict_data(x_data, y_data):
    min_idx = np.argmin(y_data)
    return x_data[min_idx:], y_data[min_idx:]


def setup_plt():
    _, ax = plt.subplots()
    ax.set_xscale('Log')


def plot_data_and_fit(x_data, y_data, sd, fit_x_data, fit_y_data):
    plt.errorbar(x_data, y_data, sd, linestyle='None', marker='.')
    plt.plot(fit_x_data, fit_y_data)


if __name__ == "__main__":
    setup_plt()

    data = ExcelLoader(test_data_path()).load()
    x_data, y_data, sd = data.get(3)
    restricted_x_data, restricted_y_data = restrict_data(x_data, y_data)
    try:
        popt, pcov = curve_fit(sigmoidal_dose_response_with_variable_slope, restricted_x_data, restricted_y_data,
                               maxfev=10000)
        fitted_x = np.linspace(np.max(restricted_x_data), np.min(restricted_x_data), 1000)
        fitted_y = sigmoidal_dose_response_with_variable_slope(fitted_x, *popt)
        plot_data_and_fit(x_data, y_data, sd, fitted_x, fitted_y)
        plt.show()
    except TypeError:
        print("Couldn't fit data, because the problem is not constrained properly.")