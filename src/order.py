from src.base_model import BaseModel
from src.product import Product
from src.exceptions import ZeroProductQuantity


class Order(BaseModel):
    """Класс для представления заказов."""

    name: str
    description: str
    product: Product
    quantity: int

    def __init__(self, name: str, description: str, product: Product, quantity: int):
        """Метод, который инициализирует экземпляры класса."""
        self.name = name
        self.description = description
        self.product = product

        try:
            if quantity == 0:
                raise ZeroProductQuantity('Нельзя оформить заказ с нулевым количеством товара.')

        except ZeroProductQuantity as e:
            print(f'{ZeroProductQuantity.__name__}: {e}')

        else:
            self.quantity = quantity
            print('Товар добавлена успешно.')

        finally:
            print('Обработка добавления товара прошла успешно.')

    def get_total_price(self) -> float:
        """Метод получение полной стоимости заказа с учетом количества."""
        return self.product.price * self.quantity
