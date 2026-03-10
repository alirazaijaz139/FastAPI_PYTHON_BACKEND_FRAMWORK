from fastapi import FastAPI,status
from pydantic import BaseModel


app=FastAPI()

class stata(BaseModel):
    name:str
    email:str
    age:int
    
@app.post("/user",status_code=status.HTTP_200_OK)
def stat(request:stata):
    return{'data':request}