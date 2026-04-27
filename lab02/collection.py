from typing import List, Optional, Callable
from model import Student

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab01'))

from model import Student


class StudentGroup:
    
    def __init__(self, name: str = "Группа"):
 
        self._name = name
        self._items: List[Student] = [] 
    
    def add(self, student: Student) -> bool:
      
        if not isinstance(student, Student):
            raise TypeError(f"Можно добавлять только Student, получен {type(student).__name__}")
        
        if student in self._items:
            return False 
        
        self._items.append(student)
        return True
    
    def remove(self, student: Student) -> bool:
    
        if student in self._items:
            self._items.remove(student)
            return True
        return False
    
    def get_all(self) -> List[Student]:
    
        return self._items.copy()
    
    
    def __len__(self) -> int:
   
        return len(self._items)
    
    def __iter__(self):
   
        return iter(self._items)
    
    def find_by_name(self, name: str) -> List[Student]:
      
        return [s for s in self._items if s.name == name]
    
    def find_by_age(self, age: int) -> List[Student]:
     
        return [s for s in self._items if s.age == age]
    
    def find_by_course(self, course: int) -> List[Student]:
       
        return [s for s in self._items if s.course == course]
    
    def find_by_grade(self, min_grade: float = 0, max_grade: float = 5.0) -> List[Student]:
        
        return [s for s in self._items if min_grade <= s.grade <= max_grade]
    
    
    def __getitem__(self, index: int) -> Student:
        
        if isinstance(index, slice):
            new_group = StudentGroup(f"{self._name}[срез]")
            for student in self._items[index]:
                new_group.add(student)
            return new_group
        return self._items[index]
    
    def remove_at(self, index: int) -> Optional[Student]:
    
        if 0 <= index < len(self._items):
            return self._items.pop(index)
        raise IndexError(f"Индекс {index} вне диапазона (0-{len(self._items)-1})")
    
    def sort(self, key: Callable[[Student], any], reverse: bool = False):
        self._items.sort(key=key, reverse=reverse)
    
    def sort_by_name(self, reverse: bool = False):
        self.sort(key=lambda s: s.name, reverse=reverse)
    
    def sort_by_age(self, reverse: bool = False):
        self.sort(key=lambda s: s.age, reverse=reverse)
    
    def sort_by_course(self, reverse: bool = False):
        self.sort(key=lambda s: s.course, reverse=reverse)
    
    def sort_by_grade(self, reverse: bool = False):
        self.sort(key=lambda s: s.grade, reverse=reverse)
    
    def filter_active(self) -> 'StudentGroup':
        new_group = StudentGroup(f"{self._name} (активные)")
        for student in self._items:
            if student.is_active:
                new_group.add(student)
        return new_group
    
    def filter_by_course(self, course: int) -> 'StudentGroup':
        new_group = StudentGroup(f"{self._name} (курс {course})")
        for student in self._items:
            if student.course == course:
                new_group.add(student)
        return new_group
    
    def filter_scholarship(self) -> 'StudentGroup':
        new_group = StudentGroup(f"{self._name} (стипендиаты)")
        for student in self._items:
            if student.grant_scholarship():
                new_group.add(student)
        return new_group
    

    
    def __str__(self) -> str:
        if len(self._items) == 0:
            return f"{self._name}: пуста"
        
        result = f"{self._name} (всего: {len(self._items)} студентов)\n"
        result += "-" * 40 + "\n"
        for i, student in enumerate(self._items, 1):
            result += f"{i}. {student.name} (курс {student.course}, балл: {student.grade:.2f})\n"
        result += "-" * 40
        return result
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def is_empty(self) -> bool:
        return len(self._items) == 0