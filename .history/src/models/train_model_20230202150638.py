import wandb
import logging
import pandas as pd
from simpletransformers.t5 import T5Model, T5Args
logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)

wandb.login()

import pandas as pd 

#get the data
df = pd.read_csv('../data/processed/Full_dataset.csv')
df.insert(0, "prefix", "QA")
#Last minute change to the data
df["target_text"] = df["target_text"].str.replace(r'<a href="(.+?)">(.+?)</a>', r'[\2](\1)')
df["target_text"] = df["target_text"].str.replace(r'&gt;', r'>')
df["target_text"] = df["target_text"].str.replace(r'&lt;', r'<')


#make model 

def make_model("t")
