import wandb
wandb.login()

import pandas as pd 

#get the data
data = pd.read_csv('../data/processed/Full_dataset.csv')
df.insert(0, "prefix", "QA")
display(df.head())