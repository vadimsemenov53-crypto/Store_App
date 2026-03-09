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
        if isinstance(other, Smartphone):
            return self.price * self.quantity + other.price * other.quantity

        raise TypeError(f'{other.__class__.__name__} не является объектом Smartphone')

if __name__ == '__main__':
    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                         "S23 Ultra", 256, "Серый")
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
