from fastapi import UploadFile
import pandas as pd 
from pydantic import BaseModel,Field
import io

from db import DB


class Validation(BaseModel):
    name: str
    location:str
    danger_rate:int = Field(gt=1,lt=10)


def read_csv_file(file:UploadFile):
    df =pd.read_csv(io.BytesIO(file.file.read()))
    df = df.sort_values("danger_rate",ascending=False)
    return df

def validation_and_conversion(df:pd.DataFrame):
    df = df.sort_values(by=["danger_rate"],ascending=False).head(5)
    df = df.drop(columns=["last_seen","notes","age","group"], axis=1)

    all = []
    for row in range(5):
        try:
            Validation(name=df.iloc[row]["name"],location=df.iloc[row]["location"],danger_rate=int(df.iloc[row]["danger_rate"]))
            all.append(df.iloc[row].to_dict())
        except Exception:
            continue
    return {"count":len(all),"top":all}
    
def get_clear_data(data):
    return data["top"]




