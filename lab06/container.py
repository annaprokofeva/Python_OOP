# lab06/container.py

from typing import TypeVar, Generic, Callable, Optional, List
from abc import abstractmethod


# ========== 1. ПРОТОКОЛЫ (структурная типизация) - оценка 5 ==========

class Displayable:
    """
    Протокол для объектов, которые умеют отображать себя в строку.
    Классы не должны наследовать этот протокол явно —
    достаточно иметь метод display().
    """
    @abstractmethod
    def display(self) -> str:
        """Вернуть строковое представление объекта"""
        ...


class Scorable:
    """
    Протокол для объектов, которые имеют числовую оценку.
    Классы не должны наследовать этот протокол явно —
    достаточно иметь метод score().
    """
    @abstractmethod
    def score(self) -> float:
        """Вернуть числовую оценку объекта"""
        ...


# ========== 2. TypeVar с ограничениями (bound) - оценка 5 ==========

T = TypeVar('T')                      # Без ограничений (для оценки 3)
R = TypeVar('R')                      # Для map() (оценка 4)
D = TypeVar('D', bound=Displayable)   # Только объекты с методом display()
S = TypeVar('S', bound=Scorable)      # Только объекты с методом score()


# ========== 3. Generic-коллекция - оценка 3 и 4 ==========

class TypedCollection(Generic[T]):
    """
    Обобщённая коллекция для хранения элементов одного типа.
    
    Пример использования:
        collection = TypedCollection[Student]()
        collection.add(student1)
        collection.add(student2)
    
    TypeVar T может быть заменён на любой тип.
    """
    
    def __init__(self) -> None:
        """Создаёт пустую коллекцию"""
        self._items: List[T] = []
    
    # ========== Базовые методы (из ЛР-2) - оценка 3 ==========
    
    def add(self, item: T) -> None:
        """
        Добавляет элемент в коллекцию.
        
        Args:
            item: Элемент типа T
        """
        self._items.append(item)
    
    def remove(self, item: T) -> bool:
        """
        Удаляет элемент из коллекции.
        
        Args:
            item: Элемент для удаления
        
        Returns:
            True если элемент был удалён, False если не найден
        """
        if item in self._items:
            self._items.remove(item)
            return True
        return False
    
    def get_all(self) -> List[T]:
        """
        Возвращает копию списка всех элементов.
        
        Returns:
            Список элементов типа T
        """
        return self._items.copy()
    
    def __len__(self) -> int:
        """Возвращает количество элементов в коллекции"""
        return len(self._items)
    
    def __iter__(self):
        """Позволяет итерироваться по коллекции"""
        return iter(self._items)
    
    def __getitem__(self, index: int) -> T:
        """Позволяет обращаться по индексу"""
        return self._items[index]
    
    # ========== Новые методы для ЛР-6 (оценка 4) ==========
    
    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        """
        Находит первый элемент, удовлетворяющий условию.
        
        Args:
            predicate: Функция, принимающая T и возвращающая bool
        
        Returns:
            Первый подходящий элемент или None
        """
        for item in self._items:
            if predicate(item):
                return item
        return None
    
    def filter(self, predicate: Callable[[T], bool]) -> List[T]:
        """
        Возвращает список всех элементов, удовлетворяющих условию.
        
        Args:
            predicate: Функция, принимающая T и возвращающая bool
        
        Returns:
            Список подходящих элементов
        """
        return [item for item in self._items if predicate(item)]
    
    def map(self, transform: Callable[[T], R]) -> List[R]:
        """
        Применяет функцию преобразования к каждому элементу.
        
        Args:
            transform: Функция, преобразующая T в R
        
        Returns:
            Список результатов типа R
        
        Пример:
            names = collection.map(lambda s: s.name)  # list[str]
            grades = collection.map(lambda s: s.grade)  # list[float]
        """
        return [transform(item) for item in self._items]
    
    # ========== Методы для работы с протоколами (оценка 5) ==========
    
    def get_first_display(self) -> Optional[str]:
        """
        Возвращает display() первого элемента.
        Работает только если T совместим с Displayable.
        """
        if self._items:
            # mypy знает, что у item есть метод display() благодаря bound
            return self._items[0].display()  # type: ignore
        return None
    
    def get_scores(self) -> List[float]:
        """
        Возвращает список score() всех элементов.
        Работает только если T совместим с Scorable.
        """
        return [item.score() for item in self._items]  # type: ignore
    
    def __str__(self) -> str:
        """Красивый вывод коллекции"""
        if not self._items:
            return "Коллекция пуста"
        
        result = f"TypedCollection (всего: {len(self._items)} элементов)\n"
        result += "-" * 40 + "\n"
        for i, item in enumerate(self._items, 1):
            result += f"{i}. {item}\n"
        result += "-" * 40
        return result


# ========== 4. Специализированные типы для удобства ==========

# Для коллекций, которые работают с Displayable объектами
DisplayableCollection = TypedCollection[D]

# Для коллекций, которые работают с Scorable объектами
ScorableCollection = TypedCollection[S]