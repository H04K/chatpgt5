import pandas as pd 
import numpy as np

#load data from raw 
squad_df = pd.read_csv('data/raw/squad.csv')
cour_df = pd.read_csv('data/raw/cour.csv')

#in squad_df, target_text is a list of dictionaries, we need to extract the text from the dictionary
    