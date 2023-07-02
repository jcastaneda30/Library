from pydantic import BaseModel,Field
from typing import Optional

class User(BaseModel):
    name:str = Field(ax_length=500)
    token:str= Field(ax_length=50)
    class Config:
        schema_extra = {
             "example":{
                  "name":"Nombre del libro",
                  "token":"Contraseña del usuario"
             }
        }