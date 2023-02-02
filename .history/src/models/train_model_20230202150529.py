import wandb
wandb.login()

import panda 

#get the data
data = pd.read_csv('../data/processed/Full_dataset.csv')