from src.product import Product

class Smartphone(Product):
    """Подкласс (Product), для представления смартфонов."""
    efficiency: float
    model: str
    memory: (int | float)
    color: str

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int | float, color: str):
        """Метод, который инициализирует экземпляры класса."""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
