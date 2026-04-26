import pytest

from src.lawngrass_product import LawnGrass
from src.product import Product


def test_lawngrass_product_base(lawngrass_obj_class_1):
    assert lawngrass_obj_class_1.name == "Газонная трава"
    assert lawngrass_obj_class_1.description == "Элитная трава для газона"
    assert lawngrass_obj_class_1.price == 500.0
    assert lawngrass_obj_class_1.quantity == 20
    assert lawngrass_obj_class_1.country == "Россия"
    assert lawngrass_obj_class_1.germination_period == "7 дней"
    assert lawngrass_obj_class_1.color == "Зеленый"

    assert len(lawngrass_obj_class_1.list_products) == 1
    assert lawngrass_obj_class_1.__str__() == "Газонная трава, 500.0 руб. Остаток: 20 шт."


def test_lawngrass_product_add(lawngrass_obj_class_1, lawngrass_obj_class_2):
    assert lawngrass_obj_class_1 + lawngrass_obj_class_2 == 16750.0


def test_lawngrass_product_add_error(lawngrass_obj_class_1, smartphone_obj_class_1):
    with pytest.raises(TypeError, match="int не является объектом LawnGrass"):
        lawngrass_obj_class_1 + 2

    with pytest.raises(TypeError, match="Smartphone не является объектом LawnGrass"):
        lawngrass_obj_class_1 + smartphone_obj_class_1


def test_lawngrass_product_none_quantity():
    Product.clear_products()

    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен."):
        LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 0, "США", "5 дней", "Темно-зеленый")
