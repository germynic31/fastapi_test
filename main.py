"""Run file with test views"""
from fastapi import FastAPI
import uvicorn

from items_views import router as items_router
from users.views import router as users_router


app = FastAPI()
app.include_router(items_router)
app.include_router(users_router)


@app.get('/')
def hello_index():
    """Return hello index."""
    return {'message': 'hello index'}


@app.get('/hello/')
def hello(name: str = 'World'):
    """Return string 'hello {name}'."""
    name = name.title()
    return {'message': f'hello {name}'}


@app.post('/calc/add/')
def add(a: int, b: int):
    """Calculator add."""
    return {'a': a, 'b': b, 'result': a + b}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
