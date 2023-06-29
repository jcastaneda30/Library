from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from routers.libros import libros_router
from routers.user import user_router
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.title = 'Library'
app.version = '0.0.1'

app.include_router(libros_router)
app.include_router(user_router)
templates = Jinja2Templates(directory="templates")

@app.get(path='/',tags=['home'])
def htmlProvitional(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})

