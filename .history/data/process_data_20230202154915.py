import pandas as pd 
import numpy as np

#load data from raw 
squad_df = pd.read_csv('data/raw/squad.csv')
cour_df = pd.read_csv('data/raw/cour.csv')

def get_element_between_brackets(string):
    return string[string.find("[")+1:string.find("]")]


squad_df["target_text"] = squad_df["target_text"].apply(lambda x: get_element_between_brackets(x.astype(str)))
squad_df["target_text"] = squad_df["target_text"].apply(lambda x: x.replace("'",""))

merged_df = pd.concat([squad_df,cour_df],axis=0)
merged_df = merged_df.sample(frac=1).reset_index(drop=True)

merged_df.to_csv('data/processed/Full_dataset.csv',index=False)