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
