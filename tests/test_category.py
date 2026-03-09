import pytest

from src.categoty import Category


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
