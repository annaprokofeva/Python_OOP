# lab06/demo.py

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../lab03'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../lab06'))

from models import Student, BachelorStudent, MasterStudent, PhDStudent
from container import TypedCollection, Displayable, Scorable


def print_separator(title: str = "") -> None:
    """Печатает красивый разделитель"""
    print(f"\n{'=' * 60}")
    if title:
        print(f" {title} ".center(60, '='))
    print(f"{'=' * 60}")


def create_students() -> list:
    """Создаёт список студентов для демонстрации"""
    return [
        BachelorStudent("Анна Петрова", 19, 2, 4.5, "Программирование", has_practice=True),
        BachelorStudent("Иван Сидоров", 18, 1, 3.8, "Экономика"),
        BachelorStudent("Мария Иванова", 20, 3, 4.9, "Программирование", has_practice=True),
        BachelorStudent("Петр Смирнов", 19, 2, 3.2, "Экономика"),
        MasterStudent("Елена Козлова", 21, 4, 4.7, "Искусственный интеллект"),
        BachelorStudent("Дмитрий Новиков", 18, 1, 4.1, "Программирование"),
        MasterStudent("Ольга Морозова", 22, 3, 4.3, "Биоинформатика"),
    ]


# ========== СЦЕНАРИЙ 1: Аннотации типов (оценка 3) ==========

def scenario_1() -> None:
    print_separator("СЦЕНАРИЙ 1: АННОТАЦИИ ТИПОВ")
    
    # Создаём студента с типизированной переменной
    student: Student = BachelorStudent("Анна Петрова", 19, 2, 4.5, "Программирование")
    
    # IDE и mypy знают типы
    name: str = student.name
    age: int = student.age
    grade: float = student.grade
    has_scholarship: bool = student.grant_scholarship()
    
    print(f"Студент: {name}")
    print(f"Возраст: {age}")
    print(f"Оценка: {grade}")
    print(f"Стипендия: {has_scholarship}")
    print(f"Тип name: {type(name).__name__}")
    print(f"Тип age: {type(age).__name__}")
    print(f"Тип grade: {type(grade).__name__}")
    print(f"Тип has_scholarship: {type(has_scholarship).__name__}")


# ========== СЦЕНАРИЙ 2: Generic-коллекция TypedCollection (оценка 3) ==========

def scenario_2() -> None:
    print_separator("СЦЕНАРИЙ 2: GENERIC-КОЛЛЕКЦИЯ TYPEDCOLLECTION")
    
    # Создаём типизированную коллекцию
    collection: TypedCollection[Student] = TypedCollection()
    
    students = create_students()
    
    # Добавляем студентов
    print("Добавление студентов в коллекцию:")
    for s in students[:5]:
        collection.add(s)
        print(f"  Добавлен: {s.name}")
    
    print(f"\nВ коллекции {len(collection)} студентов")
    
    # Получаем всех
    all_students = collection.get_all()
    print("\nВсе студенты в коллекции:")
    for s in all_students:
        print(f"  - {s.name} (курс {s.course}, балл: {s.grade:.2f})")


# ========== СЦЕНАРИЙ 3: find, filter, map (оценка 4) ==========

def scenario_3() -> None:
    print_separator("СЦЕНАРИЙ 3: FIND, FILTER, MAP")
    
    collection: TypedCollection[Student] = TypedCollection()
    for s in create_students():
        collection.add(s)
    
    # find() — найти студента по имени
    print("--- find() ---")
    found = collection.find(lambda s: s.name == "Мария Иванова")
    if found:
        print(f"Найден: {found.name} (оценка: {found.grade})")
    
    # find() — элемент не найден
    not_found = collection.find(lambda s: s.name == "Несуществующий Студент")
    print(f"Поиск несуществующего: {not_found}")
    
    # filter() — отфильтровать отличников
    print("\n--- filter() ---")
    high_achievers = collection.filter(lambda s: s.grade > 4.5)
    print(f"Отличники (балл > 4.5): {len(high_achievers)} студентов")
    for s in high_achievers:
        print(f"  - {s.name}: {s.grade:.2f}")
    
    # map() — преобразование в имена (str)
    print("\n--- map() → имена (str) ---")
    names: list[str] = collection.map(lambda s: s.name)
    print(f"Имена: {', '.join(names)}")
    print(f"Тип результата: {type(names[0]).__name__ if names else 'empty'}")
    
    # map() — преобразование в оценки (float)
    print("\n--- map() → оценки (float) ---")
    grades: list[float] = collection.map(lambda s: s.grade)
    print(f"Оценки: {grades}")
    print(f"Тип результата: {type(grades[0]).__name__ if grades else 'empty'}")
    
    # map() — демонстрация смены типа (Student → str)
    print("\n--- map() → информация о студентах (str) ---")
    info_list: list[str] = collection.map(lambda s: f"{s.name} (курс {s.course})")
    for info in info_list[:5]:
        print(f"  {info}")


# ========== СЦЕНАРИЙ 4: Протокол Displayable (оценка 5) ==========

def scenario_4() -> None:
    print_separator("СЦЕНАРИЙ 4: ПРОТОКОЛ DISPLAYABLE")
    
    # Создаём коллекцию, которая принимает только Displayable объекты
    # Python не проверяет это во время выполнения, но mypy/IDE подсветят ошибку
    collection: TypedCollection[Displayable] = TypedCollection()
    
    # Добавляем разные типы студентов (у всех есть метод display())
    students = create_students()
    collection.add(students[0])  # BachelorStudent
    collection.add(students[4])  # MasterStudent
    collection.add(students[6])  # MasterStudent (Ольга)
    
    print("Коллекция Displayable объектов:")
    print(f"Всего элементов: {len(collection)}")
    
    # Вызываем display() для каждого
    print("\nВызов display() для каждого объекта:")
    for item in collection:
        print(f"  {item.display()}")
    
    # Демонстрация, что объекты разных типов подходят под протокол
    print("\nПроверка: объекты разных типов в одной коллекции:")
    for item in collection:
        print(f"  Тип: {type(item).__name__}, display(): {item.display()}")


# ========== СЦЕНАРИЙ 5: Протокол Scorable (оценка 5) ==========

def scenario_5() -> None:
    print_separator("СЦЕНАРИЙ 5: ПРОТОКОЛ SCORABLE")
    
    # Создаём коллекцию, которая принимает только Scorable объекты
    collection: TypedCollection[Scorable] = TypedCollection()
    
    students = create_students()
    for s in students:
        collection.add(s)
    
    print(f"Коллекция Scorable объектов (всего: {len(collection)})")
    
    # Получаем все оценки через метод score()
    scores = [item.score() for item in collection]
    print(f"\nОценки всех студентов: {scores}")
    
    # Находим средний балл
    avg_score = sum(scores) / len(scores) if scores else 0
    print(f"Средний балл: {avg_score:.2f}")
    
    # Filtr по score
    high_scores = collection.filter(lambda s: s.score() > 4.5)
    print(f"\nСтуденты с оценкой > 4.5: {len(high_scores)}")
    for s in high_scores:
        print(f"  - {s.score():.2f}")


# ========== ЗАПУСК ==========

if __name__ == "__main__":
    print("ЛАБОРАТОРНАЯ РАБОТА №6")
    print("Generics и typing")
    
    scenario_1()
    scenario_2()
    scenario_3()
    scenario_4()
    scenario_5()
    
    print_separator("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")