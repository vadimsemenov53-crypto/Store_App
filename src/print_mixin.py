from typing import Any


class PrintMixin:
    """Класс-миксин, для вывода в консоль информации о созданном объекте класса.
    (Пример: Product('Продукт1', 'Описание продукта', 1200, 10))"""

    def __init__(self) -> None:
        """Метод, при инициализации вызывает __repr__ и выводит в консоль информацию об объекте."""
        print(repr(self))

    def __repr__(self) -> str:
        obj: Any = self
        """Магический метод, возвращающий информацию об объекте класса."""
        return f"{obj.__class__.__name__} ({obj.name}, {obj.description}, {obj.price}, {obj.quantity})"
