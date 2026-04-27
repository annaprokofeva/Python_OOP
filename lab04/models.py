# lab04/models.py

import sys
import os

# Добавляем пути к предыдущим лабораторным
sys.path.append(os.path.join(os.path.dirname(__file__), '../lab01'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../lab03'))

# Импортируем только существующие валидаторы из lab01
from validate import (
    validate_name,
    validate_age,
    validate_course,
    validate_grade
)

# Импортируем интерфейсы из текущей папки
from interfaces import Printable, Comparable


# ----- Вспомогательные валидаторы (так как их нет в lab01/validate.py) -----
def validate_specialization(specialization: str):
    """Проверяет специализацию бакалавра"""
    if not isinstance(specialization, str):
        raise TypeError(f"Специализация должна быть строкой, получен {type(specialization).__name__}")
    if not specialization.strip():
        raise ValueError("Специализация не может быть пустой")


def validate_topic(topic: str):
    """Проверяет тему исследования магистра"""
    if not isinstance(topic, str):
        raise TypeError(f"Тема исследования должна быть строкой, получен {type(topic).__name__}")
    if not topic.strip():
        raise ValueError("Тема исследования не может быть пустой")


def validate_area(area: str):
    """Проверяет область исследований аспиранта"""
    if not isinstance(area, str):
        raise TypeError(f"Область исследований должна быть строкой, получен {type(area).__name__}")
    if not area.strip():
        raise ValueError("Область исследований не может быть пустой")


# ------------------------------------------------------------
# Базовый класс Student
# ------------------------------------------------------------
class Student(Printable, Comparable):
    _next_id = 1000

    def __init__(self, name: str, age: int, course: int, grade: float = 3.0):
        validate_name(name)
        validate_age(age)
        validate_course(course)
        validate_grade(grade)

        self._student_id = str(Student._generate_id())
        self._name = name.strip()
        self._age = age
        self._course = course
        self._grade = float(grade)
        self._is_active = True

    @classmethod
    def _generate_id(cls):
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
    def name(self, new_name: str):
        validate_name(new_name)
        self._name = new_name.strip()

    @course.setter
    def course(self, new_course: int):
        validate_course(new_course)
        self._course = new_course

    @grade.setter
    def grade(self, new_grade: float):
        validate_grade(new_grade)
        self._grade = new_grade

    # ----- бизнес-методы -----
    def upgrade_course(self):
        if not self._is_active:
            raise ValueError("Нельзя перевести отчисленного студента")
        if self._course >= 6:
            raise ValueError("Студент уже на последнем курсе")
        self._course += 1

    def expel(self):
        if not self._is_active:
            raise ValueError("Студент уже отчислен")
        self._is_active = False

    def grant_scholarship(self) -> bool:
        if not self._is_active:
            return False
        return self._grade > 4.0

    # ----- магические методы -----
    def __str__(self):
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

    def __repr__(self):
        return f"Student(name='{self._name}', age={self._age}, course={self._course}, grade={self._grade})"

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return self._student_id == other._student_id

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._grade < other._grade

    # ----- реализация интерфейсов -----
    def to_string(self) -> str:
        return str(self)

    def compare_to(self, other) -> int:
        if not isinstance(other, Student):
            raise TypeError("Можно сравнивать только Student")
        if self._grade < other._grade:
            return -1
        elif self._grade > other._grade:
            return 1
        else:
            return 0


# ------------------------------------------------------------
# Бакалавр
# ------------------------------------------------------------
class BachelorStudent(Student):
    def __init__(self, name: str, age: int, course: int, grade: float = 3.0,
                 specialization: str = "Общая", has_practice: bool = False):
        super().__init__(name, age, course, grade)
        validate_specialization(specialization)
        self._specialization = specialization
        self._has_practice = has_practice

    @property
    def specialization(self) -> str:
        return self._specialization

    @property
    def has_practice(self) -> bool:
        return self._has_practice

    def complete_practice(self):
        if not self._is_active:
            raise ValueError("Отчисленный студент не может пройти практику")
        if self._has_practice:
            return "Практика уже пройдена"
        self._has_practice = True
        return f"{self._name} успешно прошёл практику!"

    def upgrade_course(self):
        if not self._is_active:
            raise ValueError("Нельзя перевести отчисленного студента")
        if self._course >= 4:
            raise ValueError("Бакалавр завершил обучение (4 курс). Пора выпускаться!")
        super().upgrade_course()

    def grant_scholarship(self) -> bool:
        if not self._is_active:
            return False
        return self._grade > 4.0

    def __str__(self):
        base = super().__str__()
        practice_status = "✅" if self._has_practice else "❌"
        return base + f"\n  Специализация: {self._specialization}, Практика: {practice_status}"


# ------------------------------------------------------------
# Магистр
# ------------------------------------------------------------
class MasterStudent(Student):
    def __init__(self, name: str, age: int, course: int, grade: float = 3.0,
                 research_topic: str = "Общая тема", has_thesis: bool = False):
        super().__init__(name, age, course, grade)
        validate_topic(research_topic)
        self._research_topic = research_topic
        self._has_thesis = has_thesis

    @property
    def research_topic(self) -> str:
        return self._research_topic

    @property
    def has_thesis(self) -> bool:
        return self._has_thesis

    def defend_thesis(self):
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

    def __str__(self):
        base = super().__str__()
        thesis_status = "✅" if self._has_thesis else "❌"
        return base + f"\n  Тема исследования: {self._research_topic}, Диссертация: {thesis_status}"


# ------------------------------------------------------------
# Аспирант
# ------------------------------------------------------------
class PhDStudent(Student):
    def __init__(self, name: str, age: int, course: int, grade: float = 3.0,
                 research_area: str = "Общая область", publications: int = 0):
        super().__init__(name, age, course, grade)
        validate_area(research_area)
        self._research_area = research_area
        self._publications = publications

    @property
    def research_area(self) -> str:
        return self._research_area

    @property
    def publications(self) -> int:
        return self._publications

    def publish_article(self):
        if not self._is_active:
            raise ValueError("Отчисленный аспирант не может публиковаться")
        self._publications += 1
        return f"{self._name} опубликовал {self._publications}-ю статью!"

    def grant_scholarship(self) -> bool:
        if not self._is_active:
            return False
        return True

    def __str__(self):
        base = super().__str__()
        return base + f"\n  Область исследований: {self._research_area}, Публикаций: {self._publications}"