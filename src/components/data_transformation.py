from src.logger import logging
from src.exception import CustomException
import pandas as pd
from dataclasses import dataclass
from sklearn.impute import SimpleImputer ## HAndling Missing Values
from sklearn.preprocessing import StandardScaler # HAndling Feature Scaling
from sklearn.preprocessing import OrdinalEncoder # Ordinal Encoding
## pipelines
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import os 
from src.utils import save_object

@dataclass
class proceess_config:
    pkl_file_path=os.path.join("artifacts","p.pkl")

class data_transform:
    def __init__(self):
        self.plk_file=proceess_config()

    def tranform(self,train_path,test_path):
        try:
            logging.info("data transform starts")
            train_ori=pd.read_csv(train_path)
            test_ori=pd.read_csv(test_path)
            
            obj=self.pre_proseser()
            train=train_ori.drop("id",axis=1)
            test=test_ori.drop("id",axis=1)

            train_data=obj.fit_transform(train.iloc[:,:-1])
            test_data=obj.transform(test.iloc[:,:-1])

            train_data=pd.DataFrame(train_data,columns=obj.get_feature_names_out())
            test_data=pd.DataFrame(test_data,columns=obj.get_feature_names_out())

            train_data['price']=train_ori['price']
            test_data['price']=test_ori['price']

            save_object(self.plk_file.pkl_file_path,obj)
            logging.info("saved pkl file of prepeoser")
          
            return train_data,test_data

        except Exception as e:
            logging.error('error in data trasformation')
            raise CustomException


    def pre_proseser(self):
        cut_categories = ['Fair', 'Good', 'Very Good','Premium','Ideal']
        color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
        clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']
        categorical_cols = ['cut', 'color','clarity']
        numerical_cols = ['carat', 'depth','table', 'x', 'y', 'z']

        num_pipeline=Pipeline(steps=[
        ('imputer',SimpleImputer(strategy='median')),
        ('scaler',StandardScaler())
        ]
        )

        # Categorigal Pipeline
        cat_pipeline=Pipeline(
            steps=[
            ('imputer',SimpleImputer(strategy='most_frequent')),
            ('ordinalencoder',OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories])),
            ('scaler',StandardScaler())
            ]

        )

        preprocessor=ColumnTransformer([
        ('num_pipeline',num_pipeline,numerical_cols),
        ('cat_pipeline',cat_pipeline,categorical_cols)
        ])
        return preprocessor


