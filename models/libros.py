from pydantic import BaseModel,Field
from typing import Optional

class Libro(BaseModel):
    id: Optional[str]
    user_id:str
    name:str = Field(ax_length=500)
    overview:str = Field(max_length=500)
    category:str 
    chapter:str
    link:str
    class Config:
        schema_extra = {
             "example":{
                  "name":"Nombre del libro",
                  "overview":"Descripcion",
                  "user_id":"nada",
                    "category":"categorias", 
                    "chapter":"capitulo actual",
                    "link":"link hacia el libro"
             }
        }