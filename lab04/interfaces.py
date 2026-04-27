# lab04/interfaces.py

from abc import ABC, abstractmethod


class Printable(ABC):
    """Интерфейс для получения строкового представления объекта"""
    
    @abstractmethod
    def to_string(self) -> str:
        """Вернуть строковое представление объекта"""
        pass


class Comparable(ABC):
    """Интерфейс для сравнения объектов"""
    
    @abstractmethod
    def compare_to(self, other) -> int:
        """
        Сравнить текущий объект с другим.
        
        Args:
            other: Другой объект для сравнения
            
        Returns:
            int: -1 если текущий меньше, 0 если равны, 1 если текущий больше
        """
        pass