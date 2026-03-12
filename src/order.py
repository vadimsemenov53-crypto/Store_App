from src.product import Product
from src.base_model import BaseModel
from src.smartphone_product import Smartphone

class Order(BaseModel):
    """ Класс для представления заказов. """
    name: str
    description: str
    product: Product
    quantity: int

    def __init__(self, name, description, product: Product, quantity: int):
        """Метод, который инициализирует экземпляры класса."""
        self.name = name
        self.description = description
        self.product = product
        self.quantity = quantity

    def get_total_price(self) -> float:
        """ Метод получение полной стоимости заказа с учетом количества. """
        return self.product.price * self.quantity


if __name__ == '__main__':
    tel_1 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    order_1 = Order('Заказ 1', 'Покупка телефона', tel_1, 3)

    print(order_1.get_total_price())