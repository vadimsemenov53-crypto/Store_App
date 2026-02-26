import os
import json

from json import JSONDecodeError
from src.product import Product
from src.categoty import Category

PATH = os.path.dirname(os.path.dirname(__file__))

def read_json(path_file: str | None =None) -> list[dict]:
    """Функция для чтения JSON файлов,
    принимает путь до файла, возвращает список словарей."""
    if not path_file:
        path_file = os.path.join(PATH, 'data/products.json')

    try:
        with open(path_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except JSONDecodeError:
        raise JSONDecodeError

    return data


