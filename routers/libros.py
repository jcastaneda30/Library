
from fastapi.routing import APIRouter

from typing import List
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import sys
sys.path.append("./")
from services.libros import LibrosService
from models.libros import Libro

libros_router = APIRouter()

@libros_router.get(path='/libros',tags=['libros'])
def get_libros() -> List[Libro]:
    instacia = LibrosService()
    result=instacia.get_libros()
    return JSONResponse(status_code=200,content=jsonable_encoder(result))

@libros_router.get(path='/libros/{name}',tags=['libros'])
def get_libros_names(name:str) -> Libro | dict:
    instacia = LibrosService()
    result=instacia.get_libros_name(name)
    return JSONResponse(status_code=200,content=jsonable_encoder(result)) if len(result)!=0 else \
        JSONResponse(status_code=404,content={'message':'No se encontro'})

@libros_router.post(path='/libros',tags=['libros'])
def post_libros(libro:Libro) -> str:
    instacia = LibrosService()
    instacia.post_libros(libro)
    return "Creacion exitosa"

@libros_router.put(path='/libros/{name}',tags=['libros'])
def put_libros(name:str,libro:Libro) -> str:
    instacia = LibrosService()
    libro = instacia.get_libros_name(name)
    if not libro:
        return JSONResponse(status_code=404,content={'message':'No se encontro'})
    instacia.put_libros(name,libro)
    return "Actualizacion exitosa"

@libros_router.delete(path='/libros/{name}',tags=['libros'])
def delete_libros(name:str) -> str:
    instacia = LibrosService()
    libro = instacia.get_libros_name(name)
    if not libro:
        return JSONResponse(status_code=404,content={'message':'No se encontro'})
    instacia.delete_libro_id(name)
    return "Eliminacion exitosa"






