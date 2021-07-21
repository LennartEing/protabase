import numpy as np


def test_data_path():
    return './ressources/data/test/data.xlsx'


'''
Just a method that produces some simple test data
'''


def test_data_1():
    return np.array([0.000610352, 0.002441406, 0.009765625, 0.0390625, 0.15625, 0.625, 2.5, 10]), \
           np.array([0.89, 0.81, 0.64, 0.48, 0.45, 0.50, 0.58, 0.70])


'''
Just a simple method that produces some more test data
'''


def test_data_2():
    return np.array([0.000610352, 0.002441406, 0.009765625, 0.0390625, 0.15625, 0.625, 2.5, 10]), \
           np.array([1, 0.83, 0.68, 0.52, 0.48, 0.59, 0.75, 0.62])