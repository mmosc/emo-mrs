import pandas as pd
from conf import DATA_DIR, gems_9, RECBOLE_DATA_DIR
import numpy as np

emma_user_level = pd.read_csv(f'{DATA_DIR}/EMMA_total_prt.csv', low_memory=False)
emma_user_level[emma_user_level['gems_version'] == 'gems-9'].song_code.nunique()
emma_user_level = (emma_user_level[emma_user_level['gems_version'] == 'gems-9']
                   .drop(columns=[f'Gi_{k}' for k in range(1, 46)] + [f'Gs_{k}' for k in range(1, 46)] + ['gems_version', 'emo']))

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
song_majority_percent.to_csv(DATA_DIR + 'emma_percent.csv', index=True)
song_majority_bin.to_csv(DATA_DIR + 'emma_bin_majority_to_compare.csv', index=True)
#%%
song_majority_bin = song_majority_bin.reset_index()
song_majority_bin.columns = ['item_id:token'] + list(song_majority_bin.columns[1:])

index_to_gems_9 = {index: gems for index, gems in enumerate(gems_9)}
indices = [list(np.nonzero(x)[0].astype(int)) for x in song_majority_bin[gems_9].to_numpy()]
song_majority_bin['emotions:token_seq'] = indices
song_majority_bin_for_recbole = song_majority_bin[['item_id:token', 'emotions:token_seq']]
song_majority_bin_for_recbole
#%%
song_majority_bin_for_recbole.to_csv(f'{RECBOLE_DATA_DIR}/emma_majority.item', sep='\t', index=None)