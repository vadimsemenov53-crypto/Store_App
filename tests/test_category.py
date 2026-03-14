import pytest

from src.categoty import Category
from src.product import Product


def test_category_base(data_category):
    assert data_category.name == "Смартфоны"
    assert (
        data_category.description
        == "Средства не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert (
        data_category.products == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
    )

    assert Category.category_count == 1
    assert Category.product_count == 3


def test_category_add(data_category, data_cat_add_product):
    assert (
        data_category.products == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
    )
    assert Category.category_count == 1
    assert Category.product_count == 3

    data_category.add_product(data_cat_add_product)

    assert (
        data_category.products == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
        "Nokia, 1000.0 руб. Остаток: 1 шт."
    )
    assert Category.category_count == 1
    assert Category.product_count == 4


def test_category_add_error(data_category):
    with pytest.raises(TypeError, match="Можно добавлять только объекты Product или его наследников"):
        data_category.add_product({"name": "Iphone"})


def test_category_str(data_category, data_cat_add_product):
    assert str(data_category) == "Смартфоны, количество продуктов: 27 шт."

    data_category.add_product(data_cat_add_product)

    assert str(data_category) == "Смартфоны, количество продуктов: 28 шт."


def test_category_add_another(data_category, smartphone_obj_class_1, lawngrass_obj_class_1):
    assert (
        data_category.products == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
    )
    assert Category.category_count == 1
    assert Category.product_count == 3

    data_category.add_product(smartphone_obj_class_1)

    assert (
        data_category.products == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    )

    assert Category.category_count == 1
    assert Category.product_count == 4

    data_category.add_product(lawngrass_obj_class_1)

    assert (
        data_category.products == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Газонная трава, 500.0 руб. Остаток: 20 шт."
    )

    assert Category.category_count == 1
    assert Category.product_count == 5


def test_category_total_price(data_category):
    assert data_category.get_total_price() == 3014000.0


def test_category_avg_price_product(data_category):
    assert data_category.get_avg_price_products() == 140333.33


def test_category_avg_price_none_product():
    category = Category("test", "test", [])

    assert category.get_avg_price_products() == 0


def test_category_add_product_consol(capsys, data_category):
    product = Product("test", "test", 12000, 2)

    data_category.add_product(product)
    message = capsys.readouterr()

    assert message.out.strip().split("\n")[-3] == "Product (test, test, 12000, 2)"
    assert message.out.strip().split("\n")[-2] == "Товар добавлен успешно."
    assert message.out.strip().split("\n")[-1] == "Обработка добавления товара завершена."


def test_category_add_product_error(capsys, data_category):
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен."):
        Product("test", "test", 12000, 0)
