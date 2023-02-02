import wandb
import logging
import pandas as pd
from simpletransformers.t5 import T5Model, T5Args
logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)

wandb.login()

import pandas as pd 

#get the data
df = pd.read_csv('../data/processed/Full_dataset.csv')
df.insert(0, "prefix", "QA")
#Last minute change to the data
df["target_text"] = df["target_text"].str.replace(r'<a href="(.+?)">(.+?)</a>', r'[\2](\1)')
df["target_text"] = df["target_text"].str.replace(r'&gt;', r'>')
df["target_text"] = df["target_text"].str.replace(r'&lt;', r'<')





    
    
    
    
    
def make_model(type,name):
    model_args = T5Args()
    model_args.num_train_epochs = 1
    model_args.reprocess_input_data = True
    model_args.preprocess_inputs = False
    model_args.use_multiprocessing = False
    model_args.overwrite_output_dir = True
    model_args.max_length = 2048
    model_args.length_penalty =1.5
    model_args.fp16 = False
    model_args.top_p = 0.9
    model_args.top_k =  0
    model_args.num_return_sequences=  1
    model_args.num_beams = 4
    model_args.repetition_penalty = 2.5
    model_args.wandb_project = "FULL_QA"
    model = T5Model(type,name, args=model_args)
    return model


#train model
model = make_model("t5","t5-small")
model.train_model(df)

