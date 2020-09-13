#!/usr/bin/env python3
"""
Assignment 1
"""

__author__ = "Timothy Johansson"
__version__ = "0.1.0"
__license__ = "MIT"

import numpy as np

DATA = 'pulses.csv'


def main():
    question_1()


def question_1():
    data = np.loadtxt(fname=DATA, delimiter=',')
    print(data)


if __name__ == '__main__':
    main()
