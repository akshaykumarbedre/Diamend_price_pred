from src.utils import load_object
from src.logger import logging
from scr.exception import CustomException
import pandas as pd
import sys
class Predict:

    def predict(self,feature):
        try:
            pro=os.path.join("artifacts","p.pkl")
            model=os.path.join("artifacts","model.pkl")
            load_object(pro).transform(feature)
            pred=load_object(model).predict(feature)
            logging.info(f"predited succerly of data {str(feature),str(pred)}")
            return pred
        except Exception as e:
            logging.error('error in predi')
            raise CustomException(sys,e)

class Custem_data:
    def __init__(self,carat:float,depth:float,table:float,x:float,y:float,z:float,cut:str,color:str,clarity:str):        
        self.carat=carat
        self.depth=depth
        self.table=table
        self.x=x
        self.y=y
        self.z=z
        self.cut = cut
        self.color = color
        self.clarity = clarity

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'carat':[self.carat],
                'depth':[self.depth],
                'table':[self.table],
                'x':[self.x],
                'y':[self.y],
                'z':[self.z],
                'cut':[self.cut],
                'color':[self.color],
                'clarity':[self.clarity]
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise CustomException(e,sys)



