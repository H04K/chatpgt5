# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')
    squad_df = pd.read_csv('data/raw/squad.csv')
    cour_df = pd.read_csv('data/raw/cour.csv')

    

    squad_df["target_text"] = squad_df["target_text"].apply(lambda x: get_element_between_brackets(x))
    squad_df["target_text"] = squad_df["target_text"].apply(lambda x: x.replace("'",""))

    merged_df = pd.concat([squad_df,cour_df],axis=0)
    merged_df = merged_df.sample(frac=1).reset_index(drop=True)

    merged_df.to_csv('data/processed/Full_dataset.csv',index=False)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
