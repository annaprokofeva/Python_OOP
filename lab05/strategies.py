import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../lab03'))
from models import Student, BachelorStudent, MasterStudent, PhDStudent


def by_name(student: Student) -> str:
    return student.name


def by_age(student: Student) -> int:
    return student.age


def by_grade(student: Student) -> float:
    return student.grade


def by_course(student: Student) -> int:
    return student.course


def by_name_then_grade(student: Student) -> tuple:
    return (student.name, student.grade)


def by_course_then_grade(student: Student) -> tuple:
    return (student.course, student.grade)


def is_active_filter(student: Student) -> bool:
    return student.is_active


def is_high_achiever(student: Student) -> bool:
    return student.grade > 4.5


def is_first_course(student: Student) -> bool:
    return student.course == 1


def is_bachelor(student: Student) -> bool:
    return isinstance(student, BachelorStudent)


def is_master(student: Student) -> bool:
    return isinstance(student, MasterStudent)


def to_string(student: Student) -> str:
    return f"{student.name} (курс {student.course}, балл: {student.grade:.2f})"


def extract_name(student: Student) -> str:
    return student.name


def extract_grade(student: Student) -> float:
    return student.grade


def apply_grade_boost(student: Student) -> Student:
    student.grade = min(student.grade + 0.3, 5.0)
    return student


def apply_grade_penalty(student: Student) -> Student:
    student.grade = max(student.grade - 0.2, 2.0)
    return student


def make_grade_filter(min_grade: float):
    def filter_fn(student: Student) -> bool:
        return student.grade >= min_grade
    return filter_fn


def make_course_filter(course: int):
    def filter_fn(student: Student) -> bool:
        return student.course == course
    return filter_fn


def make_age_filter(min_age: int, max_age: int):
    def filter_fn(student: Student) -> bool:
        return min_age <= student.age <= max_age
    return filter_fn


def make_type_filter(class_type):
    def filter_fn(student: Student) -> bool:
        return isinstance(student, class_type)
    return filter_fn



class DiscountStrategy:
    def __init__(self, percent: float):
        self.percent = percent
    
    def __call__(self, student: Student) -> Student:
        new_grade = student.grade * (1 - self.percent / 100)
        student.grade = max(new_grade, 2.0) 
        return student
    
    def __str__(self):
        return f"DiscountStrategy({self.percent}%)"


class BonusStrategy:
    def __init__(self, bonus: float):
        self.bonus = bonus
    
    def __call__(self, student: Student) -> Student:
        student.grade = min(student.grade + self.bonus, 5.0)  # не выше 5.0
        return student
    
    def __str__(self):
        return f"BonusStrategy(+{self.bonus})"


class RoundGradeStrategy:
    def __call__(self, student: Student) -> Student:
        student.grade = round(student.grade)
        return student
    
    def __str__(self):
        return "RoundGradeStrategy()"


def apply_bonus_to_all(students, bonus: float):
    strategy = BonusStrategy(bonus)
    return [strategy(s) for s in students]