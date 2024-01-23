import pandas as pd
from conf import DATA_DIR, ASSETS_DIR
from utils import compute_cohen_on_pandas_columns, compute_contingency_table
import matplotlib.pyplot as plt

onion_bin_to_compare = pd.read_csv(DATA_DIR + 'onion_bin_to_compare.csv')
emma_bin_to_compare = pd.read_csv(DATA_DIR + 'emma_bin_to_compare.csv')
emma_bin_majority = pd.read_csv(DATA_DIR + 'emma_bin_majority_to_compare.csv')

gems_9 = ['tend', 'joya', 'tran', 'peac', 'nost', 'wond', 'ener', 'sadn', 'tens']


rename_columns = {
    'tend': 'Tenderness',
    'peac': 'Peacefulness',
    'joya': 'Joyful Activation',
    'wond': 'Wonder',
    'ener': 'Power',
    'nost': 'Nostalgia',
    'tens': 'Tension',
    'sadn': 'Sadness',
    'tran': 'Transcendence',
}

f_emma = emma_bin_to_compare[gems_9]
f_emma = f_emma.sum() / len(f_emma)
f_emma.name = 'frequency_emma'

f_onion = onion_bin_to_compare[gems_9]
f_onion = f_onion.sum() / len(f_onion)
f_onion.name = 'frequency_user'

f_majority = emma_bin_majority[gems_9]
f_majority = f_majority.sum() / len(f_majority)
f_majority.name = 'frequency_majority'

f = pd.merge(f_emma, f_onion, left_index=True, right_index=True).sort_values(by='frequency_user', ascending=False)
f = pd.merge(f, f_majority, left_index=True, right_index=True)
f = f.rename(index=rename_columns)
#%%
plt.style.use('tableau-colorblind10')
ax = f.plot(y=['frequency_user', 'frequency_majority', 'frequency_emma'], use_index=True, kind='bar', legend=False)
ax.axhline(0.34854059357370615, linestyle='--', color='#006BA4', label='overall tags and sparsity')
ax.axhline(0.5847436840814324, linestyle='--', color='#FF800E', label='overall majority')
handles, labels = ax.get_legend_handles_labels()
labels = ['Tags', 'Majority', 'Tags', 'Majority', 'Sparsity']

# Slice list to remove first handle
plt.legend(handles = handles, labels = labels)
plt.subplots_adjust(bottom=0.30)
ax.figure.savefig(f'{ASSETS_DIR}frequencies.png', dpi=1000)
plt.show()
# %%
f.corr(method='kendall')
#
# %%