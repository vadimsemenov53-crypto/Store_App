import pytest

from src.categoty import Category
from src.product import Product


@pytest.fixture()
def first_product():
    return {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }


@pytest.fixture()
def second_product():
    return {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8}


@pytest.fixture()
def data_category():
    Category.category_count = 0
    Category.product_count = 0

    Product.clear_products()
    product_1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product_2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product_3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    return Category(
        "Смартфоны",
        "Средства не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product_1, product_2, product_3],
    )


@pytest.fixture()
def data_for_json_read():
    data = [
        {
            "name": "Смартфоны",
            "description": "Мобильные устройства",
            "products": [{"name": "iPhone", "description": "Apple phone", "price": 1000.0, "quantity": 5}],
        }
    ]
    return data


@pytest.fixture()
def data_new_product():
    return {"name": "Iphone 15", "description": "512GB", "price": 20033300.0, "quantity": 5}


@pytest.fixture()
def data_cat_add_product():
    Product.clear_products()
    return Product("Nokia", "Синий", 1000.0, 1)
