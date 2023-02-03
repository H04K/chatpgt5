import pandas as pd 
import numpy as np

from datasets import load_dataset
##were going to load Squad and diplo NLP


def main():
    dataset = load_dataset("Dipl0/QA_SMART_FULL_V0.1")
    df = pd.DataFrame.from_dict(dataset['train'])
    df.insert(0, 'prefix', 'QA: ') 
    df = df.dropna()
    df = df.astype(str)
    df.to_csv("dataset.csv",ignore)

if __name__ == '__main__':
    main()