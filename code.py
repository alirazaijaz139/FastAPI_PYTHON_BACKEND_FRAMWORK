from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel,EmailStr,Field
from typing import Optional

app=FastAPI()
class login(BaseModel):
    username:Optional[str]=Field(None,min_length=5,max_length=20)
    password:str = Field(min_length=8, max_length=20)
    useremail:EmailStr 
    
@app.post("/user/")
def login_bank(request:login):
    if request.username=="aliraza" and request.password=="123456789":
        return("login succesful")
    elif request.useremail=="HBL@gmail.com":
        return("bank HBL email")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
