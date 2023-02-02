import pandas as pd 
import numpy as np

from datasets import load_dataset
##were going to load Squad and diplo NLP
Squad = load_dataset("squad_v2")
Cour = load_dataset("Dipl0/Cours_QA_MK_2")


#squad to df
squad_df = pd.DataFrame.from_dict(Squad['train'])
squad_df = squad_df[['questions','answers']]
#merge title and context
#rename title_context to input_text and answers to target_text
squad_df.rename(columns={'questions':'input_text','answers':'target_text'},inplace=True)
#drop title and context
squad_df.drop(['title','context'],axis=1,inplace=True)
#cour to df 
cour_df = pd.DataFrame.from_dict(Cour['train'])


#save to csv in data/raw
squad_df.to_csv('data/raw/squad.csv',index=False)
cour_df.to_csv('data/raw/cour.csv',index=False)