import wandb
import logging
import pandas as pd
from simpletransformers.t5 import T5Model, T5Args
logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)

wandb.login()

import pandas as pd 

from datasets import load_dataset


def make_model(type,name):
    model_args = T5Args()
    model_args.num_train_epochs = 1
    model_args.reprocess_input_data = True
    model_args.preprocess_inputs = False
    model_args.use_multiprocessing = False
    model_args.overwrite_output_dir = True
    model_args.save_steps = 5000
    model_args.max_length = 2048
    model_args.length_penalty =1.5
    model_args.fp16 = False
    model_args.top_p = 0.9
    model_args.top_k =  0
    model_args.num_return_sequences=  1
    model_args.num_beams = 4
    model_args.ev
    model_args.repetition_penalty = 2.5
    model_args.wandb_project = "FULL_QA"
    model = T5Model(type,name, args=model_args)
    return model


def main(): 
    dataset = load_dataset("Dipl0/QA_SMART_FULL_V0.1")
    df = pd.DataFrame.from_dict(dataset['train'])
    df.insert(0, 'prefix', 'QA: ') 
    df = df.dropna()
    df = df.astype(str)
    df.to_csv("dataset.csv",ignore_index=True,index=False)
    model = make_model("t5","t5-base")
    model.train_model("dataset.csv",wandb_name="FULL_QA")
    
    
if __name__ == '__main__':
    main()


    