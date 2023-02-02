import pandas as pd 
import numpy as np

from datasets import load_dataset
##were going to load Squad and diplo NLP
Squad = load_dataset("squad_v2")
Cour = load_dataset("Dipl0/Cours_QA_MK_2")

def main()
    #squad to df
    squad_df = pd.DataFrame.from_dict(Squad['train'])
    squad_df = squad_df[['question','answers']]
    #merge title and context
    #rename title_context to input_text and answers to target_text
    squad_df.rename(columns={'question':'input_text','answers':'target_text'},inplace=True)
    #drop title and context
    #cour to df 
    cour_df = pd.DataFrame.from_dict(Cour['train'])
    def get_element_between_brackets(string):
        return string[string.find("[")+1:string.find("]")]


    squad_df["target_text"] = squad_df["target_text"].apply(lambda x: get_element_between_brackets(x))
    squad_df["target_text"] = squad_df["target_text"].apply(lambda x: x.replace("'",""))

    merged_df = pd.concat([squad_df,cour_df],axis=0)
    merged_df = merged_df.sample(frac=1).reset_index(drop=True)

    merged_df.to_csv('Full_dataset.csv',index=False)
    