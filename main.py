"""Run file with test views"""
from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn

from core.config import settings
from core.models import Base, db_helper
from api_v1 import router as router_v1
from items_views import router as items_router
from users.views import router as users_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """For lifespan on app"""
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router_v1, prefix=settings.api_v1_prefix)
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
