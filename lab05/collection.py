import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../lab03'))
from models import Student, BachelorStudent, MasterStudent, PhDStudent


class StudentCollection:
    
    def __init__(self, name: str = "Группа"):
        self._name = name
        self._items: list = []
    
    def add(self, student: Student) -> bool:
        if not isinstance(student, (Student, BachelorStudent, MasterStudent, PhDStudent)):
            raise TypeError("Можно добавлять только Student или его наследников")
        if student in self._items:
            return False
        self._items.append(student)
        return True
    
    def remove(self, student: Student) -> bool:
        if student in self._items:
            self._items.remove(student)
            return True
        return False
    
    def get_all(self) -> list:
        return self._items.copy()
    
    def __len__(self) -> int:
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)
    
    def __getitem__(self, index):
        return self._items[index]
    
    def sort_by(self, key_func, reverse: bool = False) -> 'StudentCollection':
        self._items.sort(key=key_func, reverse=reverse)
        return self
    
    def filter_by(self, predicate) -> 'StudentCollection':
        new_collection = StudentCollection(f"{self._name} (фильтр)")
        for item in self._items:
            if predicate(item):
                new_collection.add(item)
        return new_collection
    
    def apply(self, func) -> 'StudentCollection':
        new_collection = StudentCollection(f"{self._name} (применено)")
        for item in self._items:
            result = func(item)
            new_collection.add(result)
        return new_collection

    
    def chain(self, filter_pred=None, sort_key=None, apply_func=None, reverse=False) -> 'StudentCollection':
        result = self
        
        # Фильтрация
        if filter_pred is not None:
            result = result.filter_by(filter_pred)
        
        # Создаём временную коллекцию для сортировки и применения
        temp_collection = StudentCollection(f"{self._name} (цепочка)")
        for item in result:
            temp_collection.add(item)
        
        # Сортировка
        if sort_key is not None:
            temp_collection.sort_by(sort_key, reverse)
        
        # Применение функции
        if apply_func is not None:
            final_collection = StudentCollection(f"{self._name} (результат)")
            for item in temp_collection:
                final_collection.add(apply_func(item))
            return final_collection
        
        return temp_collection
    
    def __str__(self) -> str:
        if not self._items:
            return f"{self._name}: пуста"
        
        result = f"{self._name} (всего: {len(self._items)} студентов)\n"
        result += "-" * 50 + "\n"
        for i, s in enumerate(self._items, 1):
            result += f"{i}. {s.name} (курс {s.course}, балл: {s.grade:.2f})\n"
        result += "-" * 50
        return result
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def is_empty(self) -> bool:
        return len(self._items) == 0