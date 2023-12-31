from jwt import decode, encode

def create_token(data: dict):
    token:str = encode(payload=data, key="my_secrete_key",algorithm="HS256")
    return token

def valite_toke(token:str) -> dict:
    data:dict= decode(token,key="my_secrete_key",algorithms=["HS256"])
    return data