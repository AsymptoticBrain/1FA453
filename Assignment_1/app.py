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


def main():
    data = load_data_file()
    converted_data = convert_to_voltages(data)
    print(converted_data[0, 1:])
    create_plot(converted_data[0, 1:])


# load the data to a numpy array and returns it
def load_data_file():
    data = np.loadtxt(fname=DATA_PATH, delimiter=',')
    #print(data)

    return data


# Creates a new array with converted data from column [1:] and adds the first column of the original array again
def convert_to_voltages(data):
    converted_data = (data[0:, 1:]) / (2e-10 - 1) * 0.6
    updated_array = np.c_[data[0:, 0:1], converted_data]

    return updated_array


def create_plot(data):
    # Data for plotting
    t = np.arange( data.size)
    s = data

    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
           title='About as simple as it gets, folks')
    ax.grid()

    #fig.savefig("test.png")
    plt.show()


if __name__ == '__main__':
    main()
