from src.product import Product
from src.categoty import Category

class CategoryIterator:
    """Класс для итерации по товарам категории."""
    category_obj: "Category"
    index : int

    def __init__(self, category_obj: "Category"):
        """Метод, который инициализирует экземпляры класса."""
        self.category = category_obj
        self.index = 0

    def __iter__(self) -> "CategoryIterator":
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.category.product_list):
            item = self.category.product_list[self.index].name

            self.index += 1

            return item

        else:
            raise StopIteration


if __name__ == "__main__":
    product_1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product_2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product_3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    cat = Category(
        "Смартфоны",
        "Средства не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product_1, product_2, product_3],
    )

    res = CategoryIterator(cat)

    for i in res:
        print(i)