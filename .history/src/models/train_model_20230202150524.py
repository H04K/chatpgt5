import wandb
wandb.login()

#get the data
data = pd.read_csv('../data/processed/Full_dataset.csv')