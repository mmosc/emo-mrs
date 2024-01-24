import pandas as pd
from conf import DATA_DIR

song_majority = pd.read_csv(DATA_DIR + 'emma_percent.csv')
song_majority = song_majority.set_index('song_code')
onion_to_compare = pd.read_csv(DATA_DIR + 'onion_to_compare.csv')
onion_to_compare = onion_to_compare.set_index('song_code')
gems_9 = ['tend', 'joya', 'tran', 'peac', 'nost', 'wond', 'ener', 'sadn', 'tens']
song_majority = song_majority[gems_9]
onion_to_compare = onion_to_compare[gems_9]
song_majority.corrwith(onion_to_compare, axis=1, method='kendall').mean()
#%%

song_mean = pd.read_csv(DATA_DIR + 'emma_to_compare.csv')
song_mean = song_mean.set_index('song_code')
song_mean = song_mean[gems_9]
song_mean.corrwith(onion_to_compare, axis=1, method='kendall').mean()
# %%
song_mean.corrwith(song_majority, axis=1, method='kendall').mean()
# %%
# https://stats.stackexchange.com/questions/151476/statistical-significance-for-many-instances-of-kendall-tau-correlation
from scipy.stats import kendalltau
kendalltau(f.frequency_emma, f.frequency_user)