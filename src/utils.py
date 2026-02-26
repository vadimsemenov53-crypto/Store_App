import os
import json

from json import JSONDecodeError
from src.product import Product
from src.categoty import Category
from src.types_utils import CategoryDict
from typing import cast

PATH = os.path.dirname(os.path.dirname(__file__))

def read_json(path_file: str | None =None) -> list[CategoryDict]:
    """Функция для чтения JSON файлов,
    принимает путь до файла, возвращает список словарей."""
    if not path_file:
        path_file = os.path.join(PATH, 'data/products.json')

    try:
        with open(path_file, 'r', encoding='utf-8') as file:
            data = cast(list[CategoryDict], json.load(file))
    except JSONDecodeError as error:
        return []

    return data

def create_obj_from_json(data_list: list[CategoryDict]) -> list[Category]:
    """Функция создания объектов класса из JSON-данных"""
    categories = []

    for category in data_list:
        products = [Product(**product) for product in category["products"]]

        category["products"] = products
        categories.append(Category(**category))

    return categories
