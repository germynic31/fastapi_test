"""CRUD functions"""
from users.schemas import CreateUser


def create_user(user_in: CreateUser) -> dict:
    """Create a new user"""
    user = user_in.model_dump()
    return {
        'success': True,
        'user': user
    }