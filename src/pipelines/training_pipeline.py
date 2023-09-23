from src.components.data_ingestion import data_ingestion
from src.components.data_transformation import data_transform
from src.components.model_trainer import model_evaluate

data_i=data_ingestion()
train_path,text_path=data_i.ingest()
print(train_path,text_path)

data_t=data_transform()
train_data,test_data=data_t.tranform(train_path,text_path)

model=model_evaluate()
model.model_train(train_data,test_data)