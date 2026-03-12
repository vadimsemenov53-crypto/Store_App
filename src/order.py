from src.product import Product
from src.base_model import BaseModel

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
