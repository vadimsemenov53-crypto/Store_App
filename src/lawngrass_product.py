from src.product import Product


class LawnGrass(Product):
    """Подкласс (Product), для представления травы газонной."""

    country: str
    germination_period: str
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        """Метод, который инициализирует экземпляры класса."""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other: "Product") -> float:
        """Метод сложения стоимости двух товаров, учитывая их количество."""
        if type(other) is LawnGrass:
            return self.price * self.quantity + other.price * other.quantity

        raise TypeError(f"{other.__class__.__name__} не является объектом LawnGrass")
