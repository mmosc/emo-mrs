from recbole.quick_start import run
#%%

run(
    model='MultiVAE',
    dataset='onion',
    config_file_list=['/home/marta/jku/emotion-popularity/notebooks/psyias2024/recbole_data/model_config.yaml']
)
#%%
