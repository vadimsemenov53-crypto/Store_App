from src.lawngrass_product import LawnGrass
from src.product import Product
from src.smartphone_product import Smartphone


def test_print_mixin_base(capsys):
    Product("Nokia", "Синий", 1000.0, 1)
    message_1 = capsys.readouterr()
    assert message_1.out.strip() == "Product (Nokia, Синий, 1000.0, 1)"

    Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    message_2 = capsys.readouterr()
    assert (
        message_2.out.strip() == "Smartphone (Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"
    )

    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    message_3 = capsys.readouterr()
    assert message_3.out.strip() == "LawnGrass (Газонная трава, Элитная трава для газона, 500.0, 20)"
