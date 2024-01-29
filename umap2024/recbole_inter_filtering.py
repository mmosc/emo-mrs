import pandas as pd
from conf import RECBOLE_DATA_DIR
from dask import dataframe as dd
#%%
onion_items = pd.read_csv(f'{RECBOLE_DATA_DIR}/dataset/onion/onion.item', sep='\t')
track_ids = onion_items['item_id:token']
#%%
onion_inter = dd.read_csv(f'{RECBOLE_DATA_DIR}/dataset/onion/onion_timestamp.inter', sep='\t')
#%%
onion_inter = onion_inter[onion_inter['track_id:token'].isin(track_ids)]
#%%
onion_counts = onion_inter.groupby(['user_id:token', 'track_id:token']).size().to_frame('counts:float').reset_index()
#%%
onion_counts.columns = ['user_id:token', 'item_id:token', 'counts:float']
onion_counts.to_csv(f'{RECBOLE_DATA_DIR}/dataset/onion/onion.inter', sep='\t', index=None)
#%%
print('Done')
#%%
## Core filtering
onion_counts = pd.read_csv(f'{RECBOLE_DATA_DIR}/dataset/onion/onion_no_core.inter', sep='\t')

def k_core_filtering(lhs: pd.DataFrame, k: int) -> pd.DataFrame:
    """
    Performs core-filtering on the dataset.
    @param lhs: Pandas Dataframe containing the listening records. Has columns ["user", "item"]
    @param k: Threshold for performing the k-core filtering.
    @return: Filtered Dataframe
    """
    while True:
        start_number = len(lhs)

        # Item pass
        item_counts = lhs['item_id:token'].value_counts()
        item_above = set(item_counts[item_counts >= k].index)
        lhs = lhs[lhs['item_id:token'].isin(item_above)]
        print('Records after item pass: ', len(lhs))

        # User pass
        user_counts = lhs['user_id:token'].value_counts()
        user_above = set(user_counts[user_counts >= k].index)
        lhs = lhs[lhs['user_id:token'].isin(user_above)]
        print('Records after user pass: ', len(lhs))

        if len(lhs) == start_number:
            print('Exiting...')
            break
    return lhs
#%%
onion_core = k_core_filtering(onion_counts, k=5)
onion_core.to_csv(f'{RECBOLE_DATA_DIR}/dataset/onion/onion_core.inter', sep='\t', index=False)
