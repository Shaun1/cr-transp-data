import pytest

from .context import tools

import pandas


def test_load_xls():
    """Load the Excel file into a pandas DataFrame."""
    data = tools.clean_data.load_xls()
    assert isinstance(data, pandas.DataFrame)
    # also should work from top level
    data = tools.load_xls()
    assert isinstance(data, pandas.DataFrame)


def test_load_and_clean_data():
    """Load, clean, and return a pandas DataFrame."""
    data = tools.clean_data.load_and_clean_data()
    assert isinstance(data, pandas.DataFrame)
    # also should work from top level
    data = tools.load_and_clean_data()
    assert isinstance(data, pandas.DataFrame)
