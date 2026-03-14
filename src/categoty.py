from src.base_model import BaseModel
from src.product import Product
from src.exceptions import ZeroProductQuantity


class Category(BaseModel):
    """Класс для представления категорий товаров."""

    name: str
    description: str
    __products: list[Product]

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list | None = None):
        """Метод, который инициализирует экземпляры класса."""
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self) -> str:
        """Метод, строкового отображения категорий и общего количества ее товаров"""
        count_all_products = 0

        for product in self.__products:
            count_all_products += product.quantity

        return f"{self.name}, количество продуктов: {count_all_products} шт."

    @property
    def product_list(self) -> list["Product"]:
        """Метод для вывода объектов __product"""
        return self.__products

    @property
    def products(self) -> str:
        """Метод просмотра товаров в виде строк"""
        list_products = []
        for item in self.__products:
            list_products.append(str(item))

        return "\n".join(list_products) if list_products else "Категорий нет."

    def add_product(self, product: Product) -> None:
        """Метод добавления товаров в категорию"""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты Product или его наследников.")

        try:
            if product.quantity == 0:
                raise ZeroProductQuantity('Нельзя добавить товар с нулевым количеством.')

        except ZeroProductQuantity as e:
            print(f'{ZeroProductQuantity.__name__}: {e}')

        else:
            self.__products.append(product)
            Category.product_count += 1
            print('Товар добавлена успешно.')

        finally:
            print('Обработка добавления товара прошла успешно.')

    def get_total_price(self) -> float:
        """Метод для получения общей стоимости всех товаров в категории."""
        return sum(item.price * item.quantity for item in self.__products)

    def get_avg_price_products(self) -> float:
        """Метод для получения средней стоимости товара в категории."""
        try:
            return round(sum(item.price for item in self.__products) / len(self.__products), 2)
        except ZeroDivisionError:
            return 0