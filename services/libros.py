#from schemas.libros import Libro
import sys
import sys
sys.path.append("./")
from config.mongoDBconection import get_client
from fastapi.responses import JSONResponse
from bson.objectid import ObjectId
import pydantic
pydantic.json.ENCODERS_BY_TYPE[ObjectId]=str

class LibrosService():
    def __init__(self) -> None:
        self.db=get_client()
    #Metodos
    def get_libros(self):
        libros = self.db.libros.find()
        libros_converted = []
        for libro in libros:
            libro['_id'] = str(libro['_id'])
            libros_converted.append(libro)
        return libros_converted

    def get_libros_name(self,name):
        query = {'name':name}
        result = self.db.libros.find()
        result = self.db.libros.find({'name': name})
        libros = []

        for libro in result:
            libro['_id'] = str(libro['_id'])
            libros.append(libro)
        print(libros)
        return libros
    
    def post_libros(self,item):
        new_libro = dict(item)
        new_libro.pop("id", None)
        print(new_libro)
        self.db.libros.insert_one(new_libro)

    def put_libros(self,name,item):
        libro = (self.db.libros.find_one({'name':name}))
        if not libro:
            return JSONResponse(status_code=404,content={'message':'No se encontro'})
        item = dict(item)
        self.db.libros.update_one({"name":name},{
            '$set':{'name':item['name'],
            'overview':item['overview'],
            'category':item['category'],
            'chapter':item['chapter'],
            'link':item['link']}
        })

    def delete_libro_id(self,name):
        libro = (self.db.libros.find_one({'name':name}))
        if not libro:
            return JSONResponse(status_code=404,content={'message':'No se encontro'})
        self.db.libros.delete_one({"name":name})


if __name__=="__main__":
    a = LibrosService()
    print(a.get_libros())