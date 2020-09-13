#!/usr/bin/env python3
"""
Assignment 1
"""

__author__ = "Timothy Johansson"
__version__ = "0.1.0"
__license__ = "MIT"

import numpy as np

DATA_PATH = 'pulses.csv'


def main():
    data = load_data_file()
    convert_to_voltages(data)


def load_data_file():
    data = np.loadtxt(fname=DATA_PATH, delimiter=',')
    # print(data)

    return data


def convert_to_voltages(data):
    # print(data[0:3, 1:])
    converted_data = (data[0:, 1:]) * 2
    total = np.c_[data[0:, 0:1], converted_data]
    print(total)


if __name__ == '__main__':
    main()
