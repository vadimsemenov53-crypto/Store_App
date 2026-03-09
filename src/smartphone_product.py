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

    def __add__(self, other: "Smartphone") -> float:
        """Метод сложения стоимости двух товаров, учитывая их количество."""
        if type(other) is Smartphone:
            return self.price * self.quantity + other.price * other.quantity

        raise TypeError(f'{other.__class__.__name__} не является объектом Smartphone')
