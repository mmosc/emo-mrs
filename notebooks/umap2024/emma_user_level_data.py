import pandas as pd
from conf import DATA_DIR
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

emma_user_level = pd.read_csv(f'{DATA_DIR}/EMMA_total_prt.csv', low_memory=False)
emma_user_level[emma_user_level['gems_version'] == 'gems-9'].song_code.nunique()
emma_user_level = (emma_user_level[emma_user_level['gems_version'] == 'gems-9']
                   .drop(columns=[f'Gi_{k}' for k in range(1, 46)] + [f'Gs_{k}' for k in range(1, 46)] + ['gems_version', 'emo']))
#%%
columns_i_dont_know = []
for column in emma_user_level.columns:
    if emma_user_level[column].isna().sum() != 0:
        columns_i_dont_know.append(column)
columns_i_dont_know
#%%
emma_user_level = emma_user_level.drop(columns=columns_i_dont_know)
#%%
gems_9 = ['tend', 'joya', 'tran', 'peac', 'nost', 'wond', 'ener', 'sadn', 'tens']

#%%
all_values = emma_user_level[gems_9].to_numpy().reshape((-1, ))
n, bins, patches = plt.hist(all_values, bins=100)
plt.show()
#%%
n, bins, patches = plt.hist(all_values[all_values!=0], bins=20)
plt.show()
#%%
ax = sns.violinplot(emma_user_level[gems_9], inner='quartile', color='white')
plt.show()
#%%
ax = sns.boxplot(emma_user_level[gems_9].replace({0:np.nan}), color='white')
plt.show()
#%%
### MAJORITY VOTING FOR THE EMOTIONS OF A TRACK
# How often was each track annotated?
apply_dict = {'PrtID': lambda x: x.nunique()}
for gems in gems_9:
    apply_dict[gems] = lambda x: x.astype(bool).sum(axis=0)

song_majority = emma_user_level.groupby('song_code').agg(apply_dict)
song_majority_percent = song_majority.copy()
song_majority_percent[gems_9] = (song_majority_percent[gems_9].T / song_majority_percent['PrtID']).T
song_majority_bin = song_majority_percent.copy()
song_majority_bin = song_majority_bin.drop(columns=['PrtID'])
song_majority_bin = (song_majority_bin[gems_9] >= 0.5) * 1
#%%
# Sparsity
song_majority_bin.to_numpy().sum() / (song_majority_bin.shape[0] * song_majority_bin.shape[1])
#%
#%%
song_majority_percent.to_csv(DATA_DIR + 'emma_percent.csv', index=True)
song_majority_bin.to_csv(DATA_DIR + 'emma_bin_majority_to_compare.csv', index=True)
#%%

gems_9
#%%

