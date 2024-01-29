import pandas as pd
from conf import DATA_DIR, gems_9
import scipy.stats as stats
#%%
########
# Kendall Tau
########

MAJORITY = True
EMMA_ONION = True
if EMMA_ONION:
    onion_to_compare = pd.read_csv(DATA_DIR + 'onion_to_compare.csv')
    if MAJORITY:
        emma_data = pd.read_csv(DATA_DIR + 'emma_percent.csv')
    else:
        emma_data = pd.read_csv(DATA_DIR + 'emma_to_compare.csv')
else:
    emma_data = pd.read_csv(DATA_DIR + 'emma_percent.csv')
    onion_to_compare = pd.read_csv(DATA_DIR + 'emma_to_compare.csv')

onion_to_compare = onion_to_compare.set_index('song_code')
onion_to_compare = onion_to_compare[gems_9]
emma_data = emma_data.set_index('song_code')
emma_data = emma_data[gems_9]

track_corr = emma_data.corrwith(onion_to_compare, axis=1, method='kendall')


ttest_results = stats.ttest_1samp(track_corr, 0)
ttest_results
print(f"Kendall tau for majority={MAJORITY}, emma_emma={EMMA_ONION}:\n"
      f" mu = {track_corr.mean():.3f}\n"
      f" 95% confidence interval: [{ttest_results.confidence_interval().low:.3f}; {ttest_results.confidence_interval().high:.3f}]\n"
      f" p-value: {ttest_results.pvalue:.2e}")
#ttest_results.confidence_interval()
# %%
