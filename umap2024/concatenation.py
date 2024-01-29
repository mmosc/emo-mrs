import pandas as pd
from conf import DATA_DIR
from conf import gems_9
from utils import convert_to_recbole

MAJORITY = True
if MAJORITY:
    emma_data = pd.read_csv(DATA_DIR + 'emma_bin_majority_to_compare.csv')
else:
    emma_data = pd.read_csv(DATA_DIR + 'emma_bin_to_compare.csv')
onion_bin = pd.read_csv(DATA_DIR + 'onion_bin_to_compare.csv')
onion_bin = onion_bin[['song_code'] + gems_9]
onion_columns = ['song_code'] + [gems + '_onion' for gems in gems_9]
onion_bin.columns = onion_columns
onion_bin
song_concat = emma_data.merge(onion_bin, left_on='song_code', right_on='song_code')
song_concat_recbole = convert_to_recbole(song_concat)
#%%
if MAJORITY:
    song_concat_recbole.to_csv(DATA_DIR + 'concat_majority.item', sep='\t', index=None)
else:
    song_concat_recbole.to_csv(DATA_DIR + 'concat_sparsity.item', sep='\t', index=None)