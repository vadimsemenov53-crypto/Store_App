from src.product import Product


class Category:
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

    @property
    def product(self) -> str:
        """Метод просмотра товаров в виде строк"""
        list_products = []
        for item in self.__products:
            list_products.append(f"{item.name}, {item.price} руб. Остаток: {item.quantity} шт.")

        return "\n".join(list_products) if list_products else "Категорий нет."

    def add_product(self, product: Product) -> None:
        """Метод добавления товаров в категорию"""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты Product")

        self.__products.append(product)
        Category.product_count += 1


if __name__ == "__main__":
    product_1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product_2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    cat_1 = Category("Смартфоны", "Улучшение жизни", [product_1, product_2])

    print(cat_1.name)
    print(cat_1.description)
    print(cat_1.product_count)

    product_3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    cat_1.add_product(product_3)
    print(cat_1.product_count)

    print(cat_1.product)
