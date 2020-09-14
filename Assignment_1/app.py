#!/usr/bin/env python3
"""
Assignment 1
"""

__author__ = "Timothy Johansson"
__version__ = "0.1.0"
__license__ = "MIT"

import numpy as np
import matplotlib.pyplot as plt

DATA_PATH = 'pulses.csv'
MEAN_NUMBER = 10


def main():
    data = load_data_file()
    converted_data = convert_to_voltages(data)
    print(converted_data[0, 1:])
    create_plot(converted_data[0, 0:])
    corrected_data = baseline_correction(converted_data[0:, 1:])
    print(corrected_data)


# load the data to a numpy array and returns it
def load_data_file():
    data = np.loadtxt(fname=DATA_PATH, delimiter=',')
    # print(data)

    return data


# Creates a new array with converted data from column [1:] and adds the first column of the original array again
def convert_to_voltages(data):
    converted_data = (data[0:, 1:]) / (2e-10 - 1) * 0.6
    updated_array = np.c_[data[0:, 0:1], converted_data]

    return updated_array


def create_plot(data):
    title = data[0]
    data_points = data[1:]

    fig, ax = plt.subplots()
    ax.plot(data_points)
    ax.set(ylabel='voltage (mV)',
           title=f'Neutron pulse for timestamp: {title} ')
    ax.grid()
    plt.show()

    # fig.savefig("plot.png")


def baseline_correction(data):
    corrected_array = []

    for row in data:
        mean = calculate_mean(row)
        corrected_row = row - mean
        corrected_array.append(corrected_row)

    corrected_array = np.asarray(corrected_array)
    return corrected_array


def calculate_mean(data):
    mean = np.sum(data[0:MEAN_NUMBER]) / MEAN_NUMBER

    return mean


if __name__ == '__main__':
    main()
