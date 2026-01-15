from fastapi import FastAPI,UploadFile ,File
import uvicorn
from db import DB
from models import get_clear_data, read_csv_file, validation_and_conversion

app = FastAPI()



@app.post("/top-threats")
def get_file_of_threats(file:UploadFile = File(...)):
    db = DB()
    df =read_csv_file(file)
    data = validation_and_conversion(df)
    get_clear_data(data)
    return data


if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)