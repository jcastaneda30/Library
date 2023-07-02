#from schemas.libros import Libro
from .user import UsersService
import sys
sys.path.append("./")
from config.mongoDBconection import get_client
from fastapi.responses import JSONResponse
class LibrosService():
    user_id:str
    def __init__(self) -> None:
        self.db=get_client()
    #Metodos
    def get_libros(self):
        LibrosService.user_id = str(UsersService.user_id['_id'])
        libros = self.db.libros.find({'user_id':LibrosService.user_id})
        libros_converted = []
        for libro in libros:
            libro['_id'] = str(libro['_id'])
            libros_converted.append(libro)
        return libros_converted

    def get_libros_name(self,name):
        LibrosService.user_id = str(UsersService.user_id['_id'])
        result = self.db.libros.find({'name': name})
        libros = []
        for libro in result:
            libro['_id'] = str(libro['_id'])
            libros.append(libro)
        return libros
    
    def post_libros(self,item):
        LibrosService.user_id = str(UsersService.user_id['_id'])
        new_libro = dict(item)
        new_libro['user_id']=LibrosService.user_id
        self.db.libros.insert_one(new_libro)

    def put_libros(self,name,item):
        LibrosService.user_id = str(UsersService.user_id['_id'])
        item = dict(item)
        self.db.libros.update_one({"name":name},{
            '$set':{'name':item['name'],
            'overview':item['overview'],
            'category':item['category'],
            'chapter':item['chapter'],
            'link':item['link']}
        })

    def delete_libro_id(self,name):
        LibrosService.user_id = str(UsersService.user_id['_id'])
        libro = self.db.libros.find_one({'name':name})
        if libro['user_id']==LibrosService.user_id:
            self.db.libros.delete_one({"name":name})


if __name__=="__main__":
    a = LibrosService()
    print(a.get_libros())