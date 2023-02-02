import pandas as pd 
import numpy as np

#load data from raw 
squad_df = pd.read_csv('data/raw/squad.csv')
cour_df = pd.read_csv('data/raw/cour.csv')

print(squad_df["target_text"]["text"][0])
# #merge the two dataframes
# df = pd.concat([squad_df,cour_df],axis=0)

# #save to csv in data/interim
# df.to_csv('data/interim/qa_cours.csv',index=False)