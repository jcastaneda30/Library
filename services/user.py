#from schemas.users import user
import sys
import sys
sys.path.append("./")
from config.mongoDBconection import get_client
from fastapi.responses import JSONResponse
from middleware.jwt_bearer import JWTBearer
from utils.jwt_manager import create_token
class UsersService():
    user_id = None
    def __init__(self) -> None:
        self.db=get_client()
        
    #Metodos
    def login(self,name,password):
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaa")
        print(name,password)
        user = self.db.users.find_one({'name':name,'token':password})
        UsersService.userID=user
        print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        print(user)
        return user
    
    def get_users(self):
        users = self.db.users.find()
        print("--------------------")
        print(users)
        users_converted = []
        for user in users:
            user['_id'] = str(user['_id'])
            users_converted.append(user)
        return users_converted
    
    def get_users_name(self,name):
        result = self.db.users.find({'name': name})
        users = []
        for user in result:
            user['_id'] = str(user['_id'])
            users.append(user)
        return users
    
    def post_user(self,item):
        new_user = dict(item)
        self.db.users.insert_one(new_user)

    def put_users(self,name,item):
        item = dict(item)
        self.db.users.update_one({"name":name},{
            '$set':{'name':item['name'],
            'password':create_token(item['password'])}
        })

    def delete_user_name(self,name):
        self.db.users.delete_one({"name":name})


if __name__=="__main__":
    a = UsersService()
    print(a.get_users())