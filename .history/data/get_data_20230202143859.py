import pandas as pd 
import numpy as np

from datasets import load_dataset
##were going to load Squad and diplo NLP
Squad = load_dataset("squad_v2")
Cour = load_dataset("Dipl0/Cours_QA_MK_2")


#squad to df
squad_df = pd.DataFrame.from_dict(Squad['train'])
squad_df = squad_df[['title','context','answers']]
#merge title and context
squad_df['title_context'] = squad_df['title'] + ' ' + squad_df['context']
#rename inp

#cour to df 
cour_df = pd.DataFrame.from_dict(Cour['train'])