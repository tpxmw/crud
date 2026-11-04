from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
app = FastAPI()
templates = Jinja2Templates(directory='templates')

#가상 데이터
posts = {
    1: {'id': 1, 'title': 'a', 'content': 'b'},
    2: {'id': 2, 'title': 'c', 'content': 'd'},
}



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

#전체 게시물 출력
@app.get('/posts')
def post_list(request: Request):
    return templates.TemplateResponse(
        request=request,
        name='list.html',
        context = {'posts': list(posts.values())}
    )


#하나의 게시물 출력
@app.get('/posts/{post_if}')
def post_detail():
    pass