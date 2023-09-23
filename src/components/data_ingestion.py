import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException
import os
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

@dataclass
class train_test_path_config:
    data_path=os.path.join("notebooks/data","gemstone.csv")
    train_path=os.path.join("artifacts","train.csv")
    test_path=os.path.join("artifacts","test.csv")

class data_ingestion:
    def __init__(self):
        self.data_ingestion_path=train_test_path_config()
        
    def ingest(self):
        try:
            logging.info("data inestion started")
            df=pd.read_csv(self.data_ingestion_path.data_path)

            train_data,test_data=train_test_split(df)

            train_data.to_csv(self.data_ingestion_path.train_path)
            test_data.to_csv(self.data_ingestion_path.test_path)

            logging.info("data ingestion is succfullty ")
            return self.data_ingestion_path.train_path,self.data_ingestion_path.test_path
        except Exception as e:
            logging.error(f"data ingeion is stop due to {e}")
            raise CustomException(e,sys)
    

         

