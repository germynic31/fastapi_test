"""Views for users"""
from fastapi import APIRouter

from users.schemas import CreateUser
from users import crud


router = APIRouter(prefix='/users', tags=['Users'])


@router.post('/')
def create_user(user: CreateUser):
    """Return dict with message and email"""
    return crud.create_user(user)
