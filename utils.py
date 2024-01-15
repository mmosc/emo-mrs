import pandas as pd
from sklearn.metrics import cohen_kappa_score
from typing import Union, List
import numpy as np


def compute_cohen_on_pandas_columns(onion_data: pd.DataFrame, emma_data: pd.DataFrame, gems: Union[str, List[str]]):
    """
    Compute cohen's kappa on two sets of data, selecting one or more columns of the dataframes.
    Each dataframe is assumed to be an indipendent "rater", and each entry in the matrix selected according
    to the "gems" (i.e., each song-emotion pair) is assumed to be a candidate to evaluate.

    :param onion_data:
    :param emma_data:
    :param gems:
    :return:
    """

    if isinstance(gems, str):
        gems = [gems]
    onion_data = onion_data[gems]
    emma_data = emma_data[gems]
    if isinstance(gems, list):
        onion_data = np.concatenate(onion_data.to_numpy())
        emma_data = np.concatenate(emma_data.to_numpy())
    kappa = cohen_kappa_score(onion_data, emma_data)
    return kappa


def compute_contingency_table(onion_data: pd.DataFrame, emma_data: pd.DataFrame, gems: Union[str, List[str]]):
    """
    Computes the contingency table over two dataframes storing binary data, over either a column (if gems is a string)
    or over several (if gems is a list of strings).

    :param onion_data:
    :param emma_data:
    :param gems:
    :return contingency: Contingency table as numpy array
    """

    pairs = list(zip(onion_data[gems].to_numpy().ravel(), emma_data[gems].to_numpy().ravel()))

    n_00 = 0
    n_01 = 0
    n_10 = 0
    n_11 = 0
    for tuple in pairs:
        if tuple == (0, 0):
            n_00 += 1
        elif tuple == (0, 1):
            n_01 += 1
        elif tuple == (1, 0):
            n_10 += 1
        elif tuple == (1, 1):
            n_11 += 1

    contingency = np.array([
        [n_00, n_01],
        [n_10, n_11]
    ])

    return contingency
