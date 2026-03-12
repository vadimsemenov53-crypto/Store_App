from abc import ABC, abstractmethod


class BaseProduct(ABC):
    price: float
    quantity: int
    """Базовый класс для класса Product и его подклассов"""

    @abstractmethod
    def __add__(self, other: "BaseProduct") -> float:
        """Магический метод сложения, который обязательно должен присутствовать
        в Product и его подклассах"""
        pass
