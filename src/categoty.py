class Category:
    """Класс для """
    name: str
    description: str
    products : list

    category_count = 0
    all_products_count = 0

    def __init__(self, name, description, products=None):
        """Метод, который инициализирует экземпляры класса."""
        self.name = name
        self.description = description
        self.products = products if products else []

        Category.category_count += 1
        Category.all_products_count += len(products) if products else 0