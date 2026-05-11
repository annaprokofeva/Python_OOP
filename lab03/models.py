# lab03/models.py

from typing import Optional
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../lab01'))
from validate import (
    validate_name, validate_age, validate_course, validate_grade,
    validate_specialization, validate_topic, validate_area
)


class Student:
    """Базовый класс студента"""
    
    _next_id: int = 1000
    
    def __init__(self, name: str, age: int, course: int, grade: float = 3.0) -> None:
        validate_name(name)
        validate_age(age)
        validate_course(course)
        validate_grade(grade)
        
        self._student_id: str = str(Student._generate_id())
        self._name: str = name.strip()
        self._age: int = age
        self._course: int = course
        self._grade: float = float(grade)
        self._is_active: bool = True
    
    @classmethod
    def _generate_id(cls) -> int:
        cls._next_id += 1
        return cls._next_id
    
    # ----- свойства -----
    @property
    def student_id(self) -> str:
        return self._student_id
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def age(self) -> int:
        return self._age
    
    @property
    def course(self) -> int:
        return self._course
    
    @property
    def grade(self) -> float:
        return self._grade
    
    @property
    def is_active(self) -> bool:
        return self._is_active
    
    @name.setter
    def name(self, new_name: str) -> None:
        validate_name(new_name)
        self._name = new_name.strip()
    
    @course.setter
    def course(self, new_course: int) -> None:
        validate_course(new_course)
        self._course = new_course
    
    @grade.setter
    def grade(self, new_grade: float) -> None:
        validate_grade(new_grade)
        self._grade = new_grade
    
    # ----- бизнес-методы -----
    def upgrade_course(self) -> None:
        if not self._is_active:
            raise ValueError("Нельзя перевести отчисленного студента")
        if self._course >= 6:
            raise ValueError("Студент уже на последнем курсе")
        self._course += 1
    
    def expel(self) -> None:
        if not self._is_active:
            raise ValueError("Студент уже отчислен")
        self._is_active = False
    
    def grant_scholarship(self) -> bool:
        if not self._is_active:
            return False
        return self._grade > 4.0
    
    # ----- методы для протоколов (ЛР-6) -----
    def display(self) -> str:
        """Возвращает строковое представление студента"""
        return f"{self._name} (курс {self._course}, балл: {self._grade:.2f})"
    
    def score(self) -> float:
        """Возвращает числовую оценку студента"""
        return self._grade
    
    # ----- магические методы -----
    def __str__(self) -> str:
        status = "✅ Активен" if self._is_active else "❌ Отчислен"
        return (f"┌────────────────────────────────────┐\n"
                f"│ Студент: {self._name:<27} │\n"
                f"├────────────────────────────────────┤\n"
                f"│ ID: {self._student_id:<30} │\n"
                f"│ Возраст: {self._age:<25} │\n"
                f"│ Курс: {self._course:<27} │\n"
                f"│ Средний балл: {self._grade:<20} │\n"
                f"│ Статус: {status:<26} │\n"
                f"└────────────────────────────────────┘")
    
    def __repr__(self) -> str:
        return f"Student(name='{self._name}', age={self._age}, course={self._course}, grade={self._grade})"
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Student):
            return False
        return self._student_id == other._student_id


class BachelorStudent(Student):
    """Бакалавр"""
    
    def __init__(self, name: str, age: int, course: int, grade: float = 3.0,
                 specialization: str = "Общая", has_practice: bool = False) -> None:
        super().__init__(name, age, course, grade)
        validate_specialization(specialization)
        self._specialization: str = specialization
        self._has_practice: bool = has_practice
    
    @property
    def specialization(self) -> str:
        return self._specialization
    
    @property
    def has_practice(self) -> bool:
        return self._has_practice
    
    def complete_practice(self) -> str:
        if not self._is_active:
            raise ValueError("Отчисленный студент не может пройти практику")
        if self._has_practice:
            return "Практика уже пройдена"
        self._has_practice = True
        return f"{self._name} успешно прошёл практику!"
    
    def upgrade_course(self) -> None:
        if not self._is_active:
            raise ValueError("Нельзя перевести отчисленного студента")
        if self._course >= 4:
            raise ValueError("Бакалавр завершил обучение (4 курс). Пора выпускаться!")
        super().upgrade_course()
    
    def grant_scholarship(self) -> bool:
        if not self._is_active:
            return False
        return self._grade > 4.0
    
    def display(self) -> str:
        return f"Бакалавр: {self._name} ({self._specialization}), балл: {self._grade:.2f}"
    
    def __str__(self) -> str:
        base = super().__str__()
        practice_status = "✅" if self._has_practice else "❌"
        return base + f"\n  Специализация: {self._specialization}, Практика: {practice_status}"


class MasterStudent(Student):
    """Магистр"""
    
    def __init__(self, name: str, age: int, course: int, grade: float = 3.0,
                 research_topic: str = "Общая тема", has_thesis: bool = False) -> None:
        super().__init__(name, age, course, grade)
        validate_topic(research_topic)
        self._research_topic: str = research_topic
        self._has_thesis: bool = has_thesis
    
    @property
    def research_topic(self) -> str:
        return self._research_topic
    
    @property
    def has_thesis(self) -> bool:
        return self._has_thesis
    
    def defend_thesis(self) -> str:
        if not self._is_active:
            raise ValueError("Отчисленный студент не может защищаться")
        if self._has_thesis:
            return "Диссертация уже защищена"
        self._has_thesis = True
        return f"{self._name} защитил диссертацию на тему '{self._research_topic}'!"
    
    def grant_scholarship(self) -> bool:
        if not self._is_active:
            return False
        return self._grade > 4.2
    
    def display(self) -> str:
        return f"Магистр: {self._name} (тема: {self._research_topic}), балл: {self._grade:.2f}"
    
    def __str__(self) -> str:
        base = super().__str__()
        thesis_status = "✅" if self._has_thesis else "❌"
        return base + f"\n  Тема исследования: {self._research_topic}, Диссертация: {thesis_status}"


class PhDStudent(Student):
    """Аспирант"""
    
    def __init__(self, name: str, age: int, course: int, grade: float = 3.0,
                 research_area: str = "Общая область", publications: int = 0) -> None:
        super().__init__(name, age, course, grade)
        validate_area(research_area)
        self._research_area: str = research_area
        self._publications: int = publications
    
    @property
    def research_area(self) -> str:
        return self._research_area
    
    @property
    def publications(self) -> int:
        return self._publications
    
    def publish_article(self) -> str:
        if not self._is_active:
            raise ValueError("Отчисленный аспирант не может публиковаться")
        self._publications += 1
        return f"{self._name} опубликовал {self._publications}-ю статью!"
    
    def grant_scholarship(self) -> bool:
        if not self._is_active:
            return False
        return True
    
    def display(self) -> str:
        return f"Аспирант: {self._name} (область: {self._research_area}), публикаций: {self._publications}"
    
    def __str__(self) -> str:
        base = super().__str__()
        return base + f"\n  Область исследований: {self._research_area}, Публикаций: {self._publications}"