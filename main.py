"""test site on fastapi"""
from fastapi import FastAPI
from pydantic import EmailStr, BaseModel
import uvicorn


app = FastAPI()


class CreateUser(BaseModel):
    email: EmailStr


@app.get('/')
def hello_index():
    """Return hello index."""
    return {
        'message': 'hello index'
    }


@app.get('/hello/')
def hello(name: str = 'World'):
    """Return string 'hello {name}'."""
    name = name.title()
    return {'message': f'hello {name}'}


@app.post('/users/')
def create_user(user: CreateUser):
    """Return dict with message and email"""
    return {
        'message': 'success',
        'email': user.email,
    }


@app.post('/calc/add/')
def add(a: int, b: int):
    """Calculator add."""
    return {
        'a': a,
        'b': b,
        'result': a + b
    }


@app.get('/items/')
def list_items():
    """Return list of items."""
    return [
        'item_1',
        'item_2',
    ]


@app.get('/items/latest/')
def get_latest_item():
    """Return dict with info by latest update"""
    return {'item': {'id': '0', 'name': 'latest'}}


@app.get('/items/{item_id}/')
def get_item_by_id(item_id: int):
    """Return dict with info by id."""
    return {
        'item': {
            'id': item_id,
        },
    }


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
