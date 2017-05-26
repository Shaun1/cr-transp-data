#!/usr/bin/env python
"""Tools for cleaning the raw CSV data."""

import os

import pandas

# shouldn't need to change, this is a direct dump from surveymonkey
RAW_DATA_FILENAME = "survey-raw-data.csv"

# some platform-independent path manipulation to get to the data/ directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
RAW_DATA_FILE = os.path.join(DATA_DIR, RAW_DATA_FILENAME)


def load_data():
    """Read csv data into a pandas DataFrame."""
    with open(RAW_DATA_FILE, "r") as f:
        raw_data = pandas.read_csv(f)
    return raw_data


def main():
    """Load data and run all cleaning steps."""
    raw_data = load_data()
    print repr(raw_data)


if __name__ == "__main__":
    main()
