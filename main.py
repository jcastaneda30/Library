from fastapi import FastAPI, Request
from routers.libros import libros_router
from routers.user import user_router
from fastapi.templating import Jinja2Templates
from middleware.error_handler import ErrorHandler

app = FastAPI()
app.title = 'Library'
app.version = '0.0.1'

#app.add_middleware(ErrorHandler)
app.include_router(libros_router)
app.include_router(user_router)
templates = Jinja2Templates(directory="templates")

@app.get(path='/',tags=['home'])
def htmlProvitional(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})

