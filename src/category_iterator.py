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
