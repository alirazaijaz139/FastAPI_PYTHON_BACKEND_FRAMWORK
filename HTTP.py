from fastapi import FastAPI
from typing import Optional

app=FastAPI()

#GET METHOD
@app.get('/')
def get_show():
    return{"data":"this is a get function in HTTP METHOD"}

#POST METHOD
@app.post('/user/{id}')
def post_show(id:int):
    return{"data":f"this is post function id no{id}"}

# put METHOD
@app.put('/user/')
def replace(name:str,age:int):
    return{"data":{"name":name,"age":age}}

#patch method
@app.patch("/user/")
def update(name:str,age:Optional[int]=None):
    return{"data":{"name":name,"age":age}}

#Delete method
@app.delete("/user/")
def delete_all(name:str):
    return{"data":{name}}