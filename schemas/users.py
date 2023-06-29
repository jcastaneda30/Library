from pydantic import BaseModel,Field
from typing import Optional

class User(BaseModel):
    name_user:str = Field(ax_length=500)
    token:str = Field(max_length=500)

    class Config:
        schema_extra = {
             "example":{
                  "name_user":"user name",
                  "token":"contraseña",
             }
        }