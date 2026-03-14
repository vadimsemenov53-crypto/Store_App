from abc import ABC, abstractmethod


class BaseModel(ABC):
    """Базовый класс для классов Order и Category, а так же их подклассов."""

    name: str
    description: str

    @abstractmethod
    def get_total_price(self) -> float:
        """Возвращает общую стоимость."""
        pass
