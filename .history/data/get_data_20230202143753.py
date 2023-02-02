import pandas as pd 
import numpy as np

from datasets import load_dataset
##were going to load Squad and diplo NLP
Squad = load_dataset("squad_v2")
Stack = load_dataset("flax-sentence-embeddings/stackexchange_title_best_voted_answer_jsonl")
Cour = load_dataset("Dipl0/last_minute")


#squad to df
squad_df = pd.DataFrame.from_dict(Squad['train'])
squad_df = squad_df[['title','context','answers']]

