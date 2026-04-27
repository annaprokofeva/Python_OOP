# lab04/demo.py

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../lab01'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../lab03'))

from models import BachelorStudent, MasterStudent, PhDStudent, Student
from interfaces import Printable, Comparable


# ------------------------------------------------------------
# Простая коллекция для демонстрации (встроена в demo.py)
# ------------------------------------------------------------
class StudentCollection:
    def __init__(self, name: str = "Группа"):
        self._name = name
        self._items = []

    def add(self, student):
        if not isinstance(student, (Student, BachelorStudent, MasterStudent, PhDStudent)):
            raise TypeError("Можно добавлять только Student или его наследников")
        self._items.append(student)

    def get_all(self):
        return self._items.copy()

    def sort_by_grade(self, reverse=False):
        self._items.sort(key=lambda s: s.grade, reverse=reverse)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, idx):
        return self._items[idx]

    def __str__(self):
        if not self._items:
            return f"{self._name}: пуста"
        res = f"{self._name} (всего: {len(self._items)} студентов):\n"
        res += "-" * 50 + "\n"
        for i, s in enumerate(self._items, 1):
            res += f"{i}. {s.name} (курс {s.course}, балл: {s.grade:.2f})\n"
        res += "-" * 50
        return res


# ------------------------------------------------------------
# Вспомогательные функции для работы с интерфейсами
# ------------------------------------------------------------
def filter_by_interface(collection, interface):
    """Фильтрация коллекции по интерфейсу"""
    new_coll = StudentCollection(f"{collection._name} (фильтр)")
    for item in collection:
        if isinstance(item, interface):
            new_coll.add(item)
    return new_coll


def print_all_printable(items):
    """Печать всех объектов, реализующих Printable"""
    for item in items:
        if isinstance(item, Printable):
            print(item.to_string())
        else:
            print(f"{item} — не реализует Printable")


def print_separator(title: str = ""):
    print(f"\n{'=' * 60}")
    if title:
        print(f" {title} ".center(60, '='))
    print(f"{'=' * 60}")


# ------------------------------------------------------------
# Сценарий 1: Вызов методов интерфейса
# ------------------------------------------------------------
def scenario_1():
    print_separator("СЦЕНАРИЙ 1: ВЫЗОВ МЕТОДОВ ИНТЕРФЕЙСА")

    students = [
        BachelorStudent("Анна Петрова", 19, 2, 4.5, "Программирование", has_practice=True),
        MasterStudent("Иван Сидоров", 23, 1, 4.8, "Искусственный интеллект"),
        PhDStudent("Мария Иванова", 26, 2, 4.9, "Машинное обучение", 3)
    ]

    for s in students:
        print(f"Тип: {type(s).__name__}")
        print(s.to_string())
        print(f"Стипендия: {s.grant_scholarship()}")
        print()


# ------------------------------------------------------------
# Сценарий 2: Полиморфная функция через интерфейс
# ------------------------------------------------------------
def scenario_2():
    print_separator("СЦЕНАРИЙ 2: ПОЛИМОРФНАЯ ФУНКЦИЯ")

    objects = [
        BachelorStudent("Петр Смирнов", 18, 1, 4.2, "Экономика"),
        MasterStudent("Елена Козлова", 22, 1, 4.5, "Биоинформатика"),
        PhDStudent("Дмитрий Новиков", 28, 2, 4.8, "Нейросети", 5),
        "Это просто строка"
    ]

    printable = [obj for obj in objects if isinstance(obj, Printable)]
    print("Только Printable объекты:")
    print_all_printable(printable)

    print("\nПроверка isinstance:")
    for obj in objects[:3]:
        print(f"{obj.name}: Printable? {isinstance(obj, Printable)}, Comparable? {isinstance(obj, Comparable)}")


# ------------------------------------------------------------
# Сценарий 3: Коллекция и фильтрация
# ------------------------------------------------------------
def scenario_3():
    print_separator("СЦЕНАРИЙ 3: КОЛЛЕКЦИЯ И ФИЛЬТРАЦИЯ")

    group = StudentCollection("ПИ-202")

    group.add(BachelorStudent("Анна Петрова", 19, 2, 4.5, "Программирование", has_practice=True))
    group.add(MasterStudent("Иван Сидоров", 23, 1, 4.8, "Искусственный интеллект"))
    group.add(PhDStudent("Мария Иванова", 26, 2, 4.9, "Машинное обучение", 3))
    group.add(BachelorStudent("Петр Смирнов", 18, 1, 3.2, "Экономика"))
    group.add(MasterStudent("Елена Козлова", 22, 1, 4.5, "Биоинформатика"))

    print("Исходная коллекция:")
    print(group)

    printable_coll = filter_by_interface(group, Printable)
    print("\nТолько Printable (все студенты):")
    print(printable_coll)

    print("\nСортировка по среднему баллу (Comparable):")
    group.sort_by_grade()
    print(group)

    # Сравнение двух студентов
    s1 = BachelorStudent("Студент1", 20, 2, 4.0, "Тест")
    s2 = BachelorStudent("Студент2", 20, 2, 4.5, "Тест")
    cmp = s1.compare_to(s2)
    print(f"\ns1.compare_to(s2) = {cmp} ({'меньше' if cmp < 0 else 'больше' if cmp > 0 else 'равно'})")


# ------------------------------------------------------------
# Запуск
# ------------------------------------------------------------
if __name__ == "__main__":
    scenario_1()
    scenario_2()
    scenario_3()