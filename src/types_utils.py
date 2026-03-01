from typing import TypedDict


class ProductDict(TypedDict):
    name: str
    description: str
    price: float
    quantity: int


class CategoryDict(TypedDict):
    name: str
    description: str
    products: list[ProductDict]
