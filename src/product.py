class Product:
    """Класс для представления товара."""
    name : str
    description : str
    price : float
    quantity : int

    def __init__(self, name, description, price, quantity):
        """Метод, который инициализирует экземпляры класса."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity