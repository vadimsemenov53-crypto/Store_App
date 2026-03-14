import pytest

from src.product import Product
from src.smartphone_product import Smartphone


def test_smartphone_product_base(smartphone_obj_class_1):
    assert smartphone_obj_class_1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone_obj_class_1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone_obj_class_1.price == 180000.0
    assert smartphone_obj_class_1.quantity == 5
    assert smartphone_obj_class_1.efficiency == 95.5
    assert smartphone_obj_class_1.model == "S23 Ultra"
    assert smartphone_obj_class_1.memory == 256
    assert smartphone_obj_class_1.color == "Серый"

    assert len(smartphone_obj_class_1.list_products) == 1
    assert smartphone_obj_class_1.__str__() == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_smartphone_product_add(smartphone_obj_class_1, smartphone_obj_class_2):
    assert smartphone_obj_class_1 + smartphone_obj_class_2 == 2580000.0


def test_smartphone_product_add_error(smartphone_obj_class_1, lawngrass_obj_class_1):
    with pytest.raises(TypeError, match="int не является объектом Smartphone"):
        smartphone_obj_class_1 + 2

    with pytest.raises(TypeError, match="LawnGrass не является объектом Smartphone"):
        smartphone_obj_class_1 + lawngrass_obj_class_1


def test_smartphone_product_none_quantity():
    Product.clear_products()

    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен."):
        Smartphone("Samsung Galaxy S23", "256GB", 180000.0, 0, 95.5, "S23 Ultra", 256, "Серый")
