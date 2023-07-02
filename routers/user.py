
from fastapi.routing import APIRouter

from typing import List
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import sys
sys.path.append("./")
from services.user import UsersService
from models.user import User

user_router = APIRouter()



@user_router.get(path='/users',tags=['users'])
def get_users_API() -> List[User]:
    instacia = UsersService()
    result=instacia.get_users()
    return JSONResponse(status_code=200,content=jsonable_encoder(result))

@user_router.post(path='/users/create',tags=['users'])
def post_users(User:User) -> str:
    instacia = UsersService()
    instacia.post_user(User)
    return "Creacion exitosa"

@user_router.post(path='/users',tags=['users'])
def login(user:User) -> str:
    instacia = UsersService()
    result=instacia.login(user.name,user.token)
    return "Login exitoso"

@user_router.put(path='/users/{name}',tags=['users'])
def put_users(name:str,User:User) -> str:
    instacia = UsersService()
    user = instacia.get_users_name(name)
    if not user:
        return JSONResponse(status_code=404,content={'message':'No se encontro'})
    instacia.put_users(name,User)
    return "Actualizacion exitosa"

@user_router.delete(path='/users/{name}',tags=['users'])
def delete_users(name:str) -> str:
    instacia = UsersService()
    User = instacia.get_users_name(name)
    if not User:
        return JSONResponse(status_code=404,content={'message':'No se encontro'})
    instacia.delete_user_name(name)
    return "Eliminacion exitosa"






