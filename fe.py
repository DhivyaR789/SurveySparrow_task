from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import xgboost as xgb
import tensorflow as tf
import pandas as pd

app = FastAPI()

loaded_model = xgb.XGBClassifier()

m1 = loaded_model.load_model('model1.json')
m2 = loaded_model.load_model('model2.json')
m3 = loaded_model.load_model('model3.json')

models = {
    'dataset1': m1,
    'dataset2': m2,
    'dataset3': m3
}

# Define input model with all possible fields
class PredictionInput(BaseModel):
    field1: float = None
    field2: float = None
    field3: float = None
    field4: float = None
    field5: float = None
    field6: float = None
    field7: float = None
    field8: float = None
    field9: float = None
    field10: float = None
    field11: float = None
    field12: float = None
    field13: float = None
    field14: float = None
    field15: float = None
    field16: float = None
    field17: float = None
    field18: float = None
    field19: float = None
    field20: float = None
    field21: float = None
    field22: float = None
    

# Define feature mappings and required fields
feature_mappings = {
    'dataset1': ['geography', 'age', 'balance', 'estimatedsalary'],
    'dataset2': ['preferredlogindevice', 'citytier', 'warehousetohome', 'gender','hourspendonapp', 'numberofdeviceregistered', 'preferedordercat',
       'satisfactionscore', 'maritalstatus', 'numberofaddress', 'complain',],
    'dataset3': ['accountweeks', 'custservcalls', 'daymins', 'daycalls', 'monthlycharge',
       'overagefee', 'roammins'] ,
}



def map_features(input_data: dict, dataset_key: str):
    expected_features = feature_mappings[dataset_key]
    input_df = pd.DataFrame([input_data], columns=expected_features)
    for feature in expected_features:
        if feature not in input_data:
            input_df[feature] = pd.NA
    return input_df

def identify_dataset(input_data: dict):
    fields_provided = {k: v for k, v in input_data.items() if v is not None}
    for dataset_key, fields in required_fields.items():
        if all(field in fields_provided for field in fields):
            return dataset_key
    return None

@app.post("/predict")
async def predict(input_data: PredictionInput):
    input_dict = input_data.dict()
    dataset_key = identify_dataset(input_dict)

    if dataset_key:
        required = required_fields.get(dataset_key, [])
        provided = [k for k, v in input_dict.items() if v is not None]
        missing_fields = [field for field in required if field not in provided]

        if missing_fields:
            return {"status": "incomplete", "missing_fields": missing_fields}

        input_df = map_features(input_dict, dataset_key)
        
        model = models.get(dataset_key)
        prediction = model.predict(input_df)[0]
        return {"status": "complete", "prediction": int(prediction)}
    
    else:
        return {"status": "error", "message": "Unable to identify the dataset based on provided input"}

@app.post("/update")
async def update_input(field: str, value: float):

    return {"status": "received", "field": field, "value": value}

