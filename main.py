from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
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



#사용자가 데이터 입력할 수 있는 페이지 제공
@app.get('/posts/new')
def post_new(request: Request):
    return templates.TemplateResponse(
        request=request,
        name='new.html'
    )


#사용자가 넘겨준 데이터를 저장 
@app.post('/posts/create')
def post_create(title: str = Form(), content: str = Form()):
    # return {'t': title, 'c': content}
    new_id = max(posts.keys()) + 1
    posts[new_id] = {'id' : 3, 'title': title, 'content': content}

    return RedirectResponse(f'/posts/{new_id}', status_code=303)

    
#하나의 게시물 출력
@app.get('/posts/{post_id}')
def post_detail(request: Request, post_id: int):
    post = posts[post_id]

    return templates.TemplateResponse(
        request=request,
        name='detail.html',
        context={'post':post}
    )

@app.get('/posts/{post_id}/edit')
def post_edit(request: Request, post_id: int):
    post = posts[post_id]

    return templates.TemplateResponse(
        request=request,
        name='edit.html',
        context={'post': post}
    )


@app.post('/posts/{post_id}/update')
def post_update(post_id: int, title: str = Form(), content: str = Form()):
    #기존 정보 착기
    old_post = posts[post_id]

    # 새로운 정보로 수정하기
    old_post['title'] = title
    old_post['content'] = content

    new_post = old_post
    # 전체 데이터에 적용시키기
    posts[post_id] = new_post

    return RedirectResponse(f'/posts/{post_id}', status_code = 303)