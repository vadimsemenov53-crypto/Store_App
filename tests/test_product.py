from unittest.mock import patch

from src.product import Product


def test_product_base(first_product, second_product):
    Product.clear_products()
    first = Product(**first_product)

    assert first.name == "Samsung Galaxy S23 Ultra"
    assert first.description == "256GB, Серый цвет, 200MP камера"
    assert first.price == 180000.0
    assert first.quantity == 5

    second = Product(**second_product)
    assert second.name == "Iphone 15"
    assert second.description == "512GB, Gray space"
    assert second.price == 210000.0
    assert second.quantity == 8


def test_product_property(first_product, second_product):
    Product.clear_products()
    first = Product(**first_product)
    second = Product(**second_product)

    assert len(first.list_products) == 2
    assert len(second.list_products) == 2


def test_product_new_product_clone(first_product, second_product, data_new_product):
    Product.clear_products()
    second = Product(**second_product)

    assert second.name == "Iphone 15"
    assert second.description == "512GB, Gray space"
    assert second.price == 210000.0
    assert second.quantity == 8
    assert len(second.list_products) == 1

    Product.new_product(data_new_product)

    assert second.name == "Iphone 15"
    assert second.description == "512GB, Gray space"
    assert second.price == 20033300.0
    assert second.quantity == 13
    assert len(second.list_products) == 1


def test_product_new_product(first_product, second_product):
    Product.clear_products()
    first = Product(**first_product)
    second = Product(**second_product)

    assert len(first.list_products) == 2
    assert len(second.list_products) == 2

    new_product = Product.new_product(
        {"name": "Iphone 17", "description": "512GB, Gray space", "price": 310000.0, "quantity": 5}
    )

    assert len(first.list_products) == 3

    assert new_product.name == "Iphone 17"
    assert new_product.description == "512GB, Gray space"
    assert new_product.price == 310000.0
    assert new_product.quantity == 5


def test_product_price(first_product):
    first = Product(**first_product)

    assert first.price == 180000.0


@patch("src.product.input")
def test_product_price_setter(mock_inp, capsys, first_product):
    mock_inp.return_value = "y"

    first = Product(**first_product)
    assert first.price == 180000.0

    first.price = 200000
    assert first.price == 200000

    first.price = 15000
    assert first.price == 15000

    first.price = 0
    message = capsys.readouterr()
    assert message.out == "Цена не должна быть нулевая или отрицательная\n"
