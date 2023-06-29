
from fastapi.routing import APIRouter

from typing import List
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import sys
sys.path.append("./")
from services.libros import LibrosService
from schemas.libros import Libro
libros_router = APIRouter()

@libros_router.get(path='/libros',tags=['libros'])
def getLibros() -> List[Libro]:
    instacia = LibrosService()
    result=instacia.get_libros()
    return JSONResponse(status_code=200,content=jsonable_encoder(result))


if __name__=="__main__":
    print(getLibros())