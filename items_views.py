"""Views for items"""
from typing import Annotated

from fastapi import APIRouter, Path


router = APIRouter(prefix='/items', tags=['Items'])


@router.get('/')
def list_items():
    """Return list of items."""
    return [
        'item_1',
        'item_2',
    ]


@router.get('/latest/')
def get_latest_item():
    """Return dict with info by latest update"""
    return {'item': {'id': '0', 'name': 'latest'}}


@router.get('/{item_id}/')
def get_item_by_id(item_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    """Return dict with info by id."""
    return {
        'item': {
            'id': item_id,
        },
    }
