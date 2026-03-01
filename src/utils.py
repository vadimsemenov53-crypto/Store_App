import json
import os
from json import JSONDecodeError
from typing import cast

from src.categoty import Category
from src.product import Product
from src.types_utils import CategoryDict

PATH = os.path.dirname(os.path.dirname(__file__))


def read_json(path_file: str | None = None) -> list[CategoryDict]:
    """Функция для чтения JSON файлов,
    принимает путь до файла, возвращает список словарей."""
    if not path_file:
        path_file = os.path.join(PATH, "data/products.json")

    try:
        with open(path_file, "r", encoding="utf-8") as file:
            data = cast(list[CategoryDict], json.load(file))
    except JSONDecodeError:
        return []

    return data


def create_obj_from_json(data_list: list[CategoryDict]) -> list[Category]:
    """Функция создания объектов класса из JSON-данных"""
    categories = []

    for category in data_list:
        products = [Product(**product) for product in category["products"]]

        categories.append(Category(name=category["name"], description=category["description"], products=products))

    return categories
