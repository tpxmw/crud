from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
app = FastAPI()
templates = Jinja2Templates(directory='templates')
@app.get('/')
def home():
    return {'hello': 'world'}



@app.get('/ping')
def ping(request: Request):
    return templates.TemplateResponse(
        request=request,
        name='ping.html'
    )




@app.get('/pong')
def pong(count: int):
    return {'result': count ** 3}

@app.post('/pong')
def pong_post(count: int = Form()):
    return {'result': count **2}