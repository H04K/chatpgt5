import wandb
wandb.login()

import pandas as pd 

#get the data
df = pd.read_csv('../data/processed/Full_dataset.csv')
df.insert(0, "prefix", "QA")
#Last minute change to the data
df["target_text"] = df["target_text"].str.replace(r'<a href="(.+?)">(.+?)</a>', r'[\2](\1)')
df["target_text"] = df["target_text"].str.replace(r'&gt;', r'>')
df["target_text"] = df["target_text"].str.replace(r'&lt;', r'<')
