from src.base_product import BaseProduct
from src.print_mixin import PrintMixin
from src.types_utils import ProductDict


class Product(PrintMixin, BaseProduct):
    """Класс для представления товара."""

    name: str
    description: str
    __price: float
    quantity: int

    __list_products: list["Product"] = []

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Метод, который инициализирует экземпляры класса."""
        self.name = name
        self.description = description
        self.__price = price

        if quantity <= 0:
            raise ValueError('Товар с нулевым количеством не может быть добавлен.')
        self.quantity = quantity

        self.__class__.__list_products.append(self)

        super().__init__()

    def __str__(self) -> str:
        """Метод, отображения продуктов."""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "BaseProduct") -> float:
        """Метод сложения стоимости двух товаров, учитывая их количество."""
        if type(other) is self.__class__:
            return self.__price * self.quantity + other.price * other.quantity

        raise TypeError(f"{other.__class__.__name__} не является объектом Product или того же подкласса.")

    @property
    def list_products(self) -> list["Product"]:
        """Метод вывода списка объектов"""
        return self.__class__.__list_products

    @classmethod
    def new_product(cls, dict_product: ProductDict) -> "Product":
        """Метод, который принимает на вход параметры товара в словаре
         и возвращать созданный объект класса Product
         Если товар с таким именем уже существует —
        увеличивает количество и выбирает более высокую цену."""
        for product in cls.__list_products:
            if product.name == dict_product["name"]:

                if dict_product["price"] > product.__price:
                    product.__price = dict_product["price"]

                product.quantity += dict_product["quantity"]

                return product

        return cls(**dict_product)

    @property
    def price(self) -> float:
        """Метод получения стоимости товара"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Метод изменения стоимости товара, при отрицательной цене"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            answer = (
                str(
                    input(
                        f"Новая цена: {new_price} < Старой: {self.__price}. Ставим новую цену?"
                        " y (значит yes) или n (значит no): "
                    )
                )
                .strip()
                .lower()
            )
            if answer == "y":
                self.__price = new_price
        else:
            self.__price = new_price

    @classmethod
    def clear_products(cls) -> None:
        """Метод для очистки списка товаров (для тестов)"""
        cls.__list_products.clear()
