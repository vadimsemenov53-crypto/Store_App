from abc import ABC, abstractmethod

class BaseProduct(ABC):
    """Базовый класс для класса Product и его подклассов"""

    @abstractmethod
    def __add__(self, other):
        """Магический метод сложения, который обязательно должен присутствовать
        в Product и его подклассах"""
        pass