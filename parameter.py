from fastapi import FastAPI,Header
from typing import Optional
from pydantic import BaseModel

app=FastAPI()

class item(BaseModel):
    name:str
    age:Optional[int]=Header(None)
    email:str
    
items=["banana","apple","orange"]

#Path parameter
@app.post("/user/{id}/post/{post_id}/")
def path_para(id:int,post_id:int):
    return{"data":{'id':id,"post_id":post_id}}

#query parameter
@app.post("/items/")
def query_para(limit:int,limits:int):
    return{"items":items[limit:limit+limits]}


#body request
@app.post("/user/")
def body_req(request:item):
    return{"data":{"name":request.name,"age":request.age,"email":request.email}}