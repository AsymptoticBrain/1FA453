#!/usr/bin/env python3
"""
Simple program that prints out a list of names using a for loop
"""

__author__ = "Timothy Johansson"
__version__ = "0.1.0"
__license__ = "MIT"


def hello_names(name_list):
    for name in name_list:
        print(f'Hello, {name}!')


if __name__ == "__main__":

    names = ["Alice", "Bob", "Charlotte"]

    hello_names(names)
