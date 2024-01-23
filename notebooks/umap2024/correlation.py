import pandas as pd
from conf import DATA_DIR, ASSETS_DIR
from utils import compute_cohen_on_pandas_columns, compute_contingency_table
import matplotlib.pyplot as plt

onion_bin_to_compare = pd.read_csv(DATA_DIR + 'onion_bin_to_compare.csv')
emma_bin_to_compare = pd.read_csv(DATA_DIR + 'emma_bin_majority_to_compare.csv')

gems_9 = ['wond', 'tran', 'tend', 'nost', 'peac', 'joya', 'ener', 'sadn', 'tens']


for gems in gems_9:
    kappa = compute_cohen_on_pandas_columns(onion_bin_to_compare, emma_bin_to_compare, gems)
    print(f"{gems}\t{kappa = :.3f}")

kappa = compute_cohen_on_pandas_columns(onion_bin_to_compare, emma_bin_to_compare, gems_9)
print(f'Overall: {kappa = :.3f}')
#%%
