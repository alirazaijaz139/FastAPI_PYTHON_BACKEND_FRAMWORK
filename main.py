from fastapi import FastAPI,Header
from typing import Optional
from pydantic import BaseModel

app = FastAPI()




#Request body
class item(BaseModel):
    name:str
    age:int
    Born:Optional[int]=None
    
@app.post('/student')
def show(request:item):
    return{
        "Data":f"my name {request.name} is unique also age is {request.age}  unique and i born in {request.Born} ."
    }


#with optional
@app.get('/products')
def search(search: Optional[str] = None):
    if search:
        return {'message': f'searching for {search}'}
    return {'message': 'showing all products'}

#with optional
@app.get("/users")
def show(limit :Optional[int]=None ,name:Optional[str]=None):
    if name and limit:
        return {'name': name, 'limit': limit}
    elif name:
        return {'name': name}
    elif limit:
        return {'limit': limit}
    else:
        return {'message': 'no parameters provided'}
    

#without optional
@app.get("/user")
def show(limit :int ,name:str):
     return (name,limit)
   
    
#SIMPLE GET
@app.get('/')
def index():
    return {'data':{'name':'aliraza'}}


# SIMPLE GET WITH DETAIL
@app.get('/about')
def about():
    return {'data':'nameahmad'}


#path parameters
@app.get('/blog_list/{id}/comments')
def get_idcomments(id:int):
    return {'data':'ALIraza'}


#GET METHOD(HTTP)
@app.get('/users/{user_id}')
def show(user_id :int):
    return{'data': user_id}


#POST METHOD(HTTP)
@app.post('/user')
def show(name:str,age:int):
    return {"data":{name,age}}

#PUT METHOD(HTTP)
@app.put('/user/{id}')
def show_put(id:int,name:str):
    return{"data":{ id,name}}

#PATCH METHOD(HTTP)
@app.patch('/user/{id}')
def show_put(id:int,name:str =None):
    return{"data":{ id,name}}

#Delete METHOD(HTTP)
@app.delete('/user/{id}')
def show_D(id:int,name:str ):
    return{"data":{ id,name}}

#optional header
@app.get('/secure')
def token(x_api :   Optional[str]= Header(None)):
    return{"data": {x_api}}

from fastapi import Header
#header
@app.get("/securess")
def secure(x_api_key: Optional[str] = Header(None)):
    if x_api_key is None:
        return {"message": "No API key provided"}
    return {"message": "Key received", "key_prefix": x_api_key}
