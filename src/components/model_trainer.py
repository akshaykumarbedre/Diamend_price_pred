from src.logger import logging
from src.exception import CustomException
from src.utils import evaluate_model
import pandas as pd
from dataclasses import dataclass
import os 
from src.utils import save_object
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression,Lasso,Ridge,ElasticNet
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
@dataclass
class model_train_config:
    model_plk_plat=os.path.join("artifacts","model.pkl")

class model_evaluate:
    def __init__(self):
        self.plk=model_train_config()

    def model_train(self,train_data,test_data):
        try:
            x_train=train_data.iloc[:,:-1]
            y_train=train_data.iloc[:,-1]
            x_test=test_data.iloc[:,:-1]
            y_test=test_data.iloc[:,-1]

            models={
                'LinearRegression':LinearRegression(),
                'Lasso':Lasso(),
                'Ridge':Ridge(),
                'Elasticnet':ElasticNet(),
                "DestionTree":DecisionTreeRegressor()
            }
            report=evaluate_model(x_train,y_train,x_test,y_test,models)
            logging.info(str(report))
            print(report)

            best_model_score=max(report.values())
            best_model_name=(list(report.keys())[list(report.values()).index(best_model_score)])
            print(best_model_name,best_model_score)

            save_object(self.plk.model_plk_plat, best_model_name)
        except Exception as e:
            print(e)
            logging.error("error occured in model trianling ")
            raise CustomException

