#!/usr/bin/env python3
"""
Assignment 1
"""

__author__ = "Timothy Johansson"
__version__ = "0.1.0"
__license__ = "MIT"

import numpy as np
import matplotlib.pyplot as plt

# Path to the data
DATA_PATH = 'pulses.csv'
# Number of data points used for baseline correction
MEAN_NUMBER = 10
# Set to pick a pulse for graphing
PULSE = 200
# Number of bins for the histograms
BINS = 100


def main():
    # Question 1:
    data = load_data_file()

    # Question 2:
    converted_data, timestamp = convert_to_voltages(data)

    # Question 3:
    create_plot(converted_data[PULSE - 1], title=timestamp[PULSE - 1])

    # Question 4:
    corrected_data = baseline_correction(converted_data)

    # Question 5:
    create_plot(corrected_data[PULSE - 1], title=f'{timestamp[PULSE - 1]}_baseline')

    # Question 6:
    max_energy = calculate_max(corrected_data)
    tot_energy = calculate_total_energy(corrected_data)
    create_histogram_energy(max_energy, tot_energy)


# Load the data to a numpy array and returns it.
def load_data_file():
    data = np.loadtxt(fname=DATA_PATH, delimiter=',')
    print(data)

    return data


# Creates a new array with converted data and one for the time stamps.
def convert_to_voltages(data):
    converted_data = (data[0:, 1:]) / (2e10 - 1) * 0.6
    timestamps = data[0:, 0]

    return converted_data, timestamps


# Plots the deposited neutron pulse for a specific timestamp
def create_plot(data, title):
    title = title
    data_points = data

    fig, ax = plt.subplots()
    ax.plot(data_points)
    ax.set(ylabel='voltage (V)',
           title=f'Neutron pulse for timestamp: {title}')
    ax.grid()
    plt.show()

    fig.savefig(f'neutron_pulse_{title}.png')


# Calculates the mean of the first few elements and substracts this from the whole row
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


# Calculates the max voltage for each pulse and returns an array with all values
def calculate_max(data):
    max_value_array = []
    for row in data:
        max_value = np.min(row)
        max_value_array.append(max_value)

    max_value_array = np.asarray(max_value_array)

    return max_value_array


# Calculates total energy of each pulse and returns an array with all values
def calculate_total_energy(data):
    total_energy_array = []
    for row in data:
        total_energy = np.sum(row)
        total_energy_array.append(total_energy)

    total_energy_array = np.asarray(total_energy_array)

    return total_energy_array


# Graphs histograms for the max voltage and total energy
def create_histogram_energy(max_energy, total_energy):
    title = 'Histogram for max voltage'
    fig, ax = plt.subplots()
    ax.hist(max_energy, bins=BINS)
    ax.set(ylabel='# of pulses', xlabel='max voltage (V)',
           title=title)
    ax.grid()
    plt.show()

    fig.savefig(f'{title}.png')

    fig, ax = plt.subplots()
    ax.hist(total_energy, bins=BINS)
    ax.set(ylabel='# of pulses', xlabel='total energy',
           title=f'Histogram for total energy')
    ax.grid()
    plt.show()

    fig.savefig(f'{title}.png')


if __name__ == '__main__':
    main()
