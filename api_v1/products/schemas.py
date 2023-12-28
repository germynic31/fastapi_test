from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    name: str
    description: str
    price: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductCreate):
    pass


class ProductUpdatePartial(ProductCreate):
    name: str or None = None
    description: str or None = None
    price: int or None = None


class Product(ProductBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
