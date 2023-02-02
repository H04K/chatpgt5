import pandas as pd 
import numpy as np

#load data from raw 
squad_df = pd.read_csv('data/raw/squad.csv')
cour_df = pd.read_csv('data/raw/cour.csv')

#get element betxeen brackets in a string
def get_element_between_brackets(string):
    return string[string.find("[")+1:string.find("]")]
#convert the target_text column to a list of strings
squad_df["target_text"] = squad_df["target_text"].apply(lambda x: get_element_between_brackets(x))
#remove '
squad_df["target_text"] = squad_df["target_text"].apply(lambda x: x.replace("'",""))