import wandb
wandb.login()

import panfas 

#get the data
data = pd.read_csv('../data/processed/Full_dataset.csv')