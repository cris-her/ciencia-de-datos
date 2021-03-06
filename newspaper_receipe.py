import argparse
import logging
logging.basicConfig(level=logging.INFO)

from urllib.parse import urlparse

import  pandas as pd

logger = logging.getLogger(__name__)

def main(filename):
    logger.info('Starting cleaning process')

    df = _read_data(filename)
    newspaper_uid = _extract_newspaper_uid(filename)
    df = _add_newspaper_uid_column(df, newspaper_uid)
    df = _extract_host(df)
    
    return df

def _read_data(filename):
    logger.info(f'Reading file {filename}')

    return pd.read_csv(filename)

def _extract_newspaper_uid(filename):
    logger.info('Extracting newspaper uid')
    # Esto es muy especifico de nuestro data set periodico_fecha
    newspaper_uid = filename.split('_')[0]
    print(filename)
    print(filename.split('_')[0])

    logger.info(f'Newspaper uid detected {newspaper_uid}')
    return newspaper_uid

def _add_newspaper_uid_column(df, newspaper_uid):
    logger.info(f'Filling newspaper_uid column with {newspaper_uid}')
    df['newspaper_uid'] = newspaper_uid

    return df

def _extract_host(df):
    logger.info('Extracting host')
    df['host'] = df['url'].apply(lambda url: urlparse(url).netloc)

    return df


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', 
                        help='The path to the dirty data', 
                        type=str)
    arg = parser.parse_args()
    df = main(arg.filename)
    print(df)
