class ZeroProductQuantity(Exception):
    """Ошибка при добавлении товара с нулевым количеством."""

    def __init__(self, message: str):
        """Метод - конструктор, для формирования исключения."""
        super().__init__(message)
