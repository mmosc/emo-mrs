from recbole.quick_start import run

config_file_path = '<YOUR_CONFIG_FILE_PATH>'
#%%

run(
    model='DeepFM',
    dataset='onion',
    config_file_list=[config_file_path]
)
#%%
