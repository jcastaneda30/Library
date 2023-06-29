#from schemas.libros import Libro
import sys
import sys
sys.path.append("./")
from config.mongoDBconection import get_client
class LibrosService():
    def __init__(self) -> None:
        self.db=get_client()
    #Metodos
    def get_libros(self):
        return [x for x in self.db.libros.find()]

    # def get_movie(self,id):
    #     return self.db.query(MovieModel).filter(MovieModel.id==id).first()
    
    # def get_movies_by_category(self,category):
    #     return self.db.query(MovieModel).filter(MovieModel.category==category).all()
    
    # def create_movies(self, movies):
    #     for movie in movies:
    #         new_movie = MovieModel(**movie.dict())
    #         self.db.add(new_movie)
    #         self.db.commit()
    #     return "Se realizo con exito"
    
    # def uptdate_movie(self,id:int,movie:Movie):
    #     result = self.db.query(MovieModel).get(id)
    #     result.movie_title= movie.movie_title
    #     result.overview= movie.overview
    #     result.year= movie.year   
    #     result.rating= movie.rating   
    #     result.category= movie.category   
    #     self.db.commit()
    #     self.db.refresh(result)
    #     return "Realizado"
    
    # def delete_movies(self,id: int):
    #     self.db.query(MovieModel).filter(MovieModel.id==id).delete()
    #     return "Eliminacion adecuada"

if __name__=="__main__":
    a = LibrosService()
    print(a.get_libros())