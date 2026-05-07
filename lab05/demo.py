import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../lab03'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../lab05'))

from models import Student, BachelorStudent, MasterStudent, PhDStudent
from collection import StudentCollection
from strategies import (
    # Сортировка
    by_name, by_age, by_grade, by_course, by_name_then_grade,
    # Фильтры
    is_active_filter, is_high_achiever, is_first_course,
    # map
    to_string, extract_name, apply_grade_boost,
    # Фабрики
    make_grade_filter, make_course_filter, make_age_filter,
    # Callable-стратегии
    DiscountStrategy, BonusStrategy, RoundGradeStrategy
)


def print_separator(title: str = ""):
    print(f"\n{'=' * 60}")
    if title:
        print(f" {title} ".center(60, '='))
    print(f"{'=' * 60}")


def print_collection(collection: StudentCollection, title: str = ""):
    if title:
        print(f"\n--- {title} ---")
    print(collection)


def create_test_collection() -> StudentCollection:
    group = StudentCollection("ПИ-202")
    
    students = [
        BachelorStudent("Анна Петрова", 19, 2, 4.5, "Программирование", has_practice=True),
        BachelorStudent("Иван Сидоров", 18, 1, 3.8, "Экономика"),
        BachelorStudent("Мария Иванова", 20, 3, 4.9, "Программирование", has_practice=True),
        BachelorStudent("Петр Смирнов", 19, 2, 3.2, "Экономика"),
        MasterStudent("Елена Козлова", 21, 4, 4.7, "Искусственный интеллект"),
        BachelorStudent("Дмитрий Новиков", 18, 1, 4.1, "Программирование"),
        MasterStudent("Ольга Морозова", 22, 3, 4.3, "Биоинформатика"),
    ]
    
    for s in students:
        group.add(s)
    
    return group


# ========== СЦЕНАРИЙ 1: Цепочка операций ==========

def scenario_1():
    print_separator("СЦЕНАРИЙ 1: ЦЕПОЧКА ОПЕРАЦИЙ (filter → sort → apply)")
    
    group = create_test_collection()
    print_collection(group, "Исходная коллекция")
 
    result = (group
              .filter_by(is_active_filter)
              .sort_by(by_grade, reverse=True)
              .apply(lambda s: apply_grade_boost(s)))
    
    print_collection(result, "ШАГ 3: После применения бонуса")


# ========== СЦЕНАРИЙ 2: Замена стратегии ==========

def scenario_2():
    print_separator("СЦЕНАРИЙ 2: ЗАМЕНА СТРАТЕГИИ (разные ключи сортировки)")
    
    group = StudentCollection("Тестовая группа")
    group.add(BachelorStudent("Анна Петрова", 19, 2, 4.5, "IT"))
    group.add(BachelorStudent("Иван Сидоров", 18, 1, 3.8, "Экономика"))
    group.add(BachelorStudent("Мария Иванова", 20, 3, 4.9, "IT"))
    group.add(MasterStudent("Елена Козлова", 21, 4, 4.7, "AI"))
    
    print_collection(group, "Исходная коллекция")
    
    # Стратегия 1: по имени
    group.sort_by(by_name)
    print_collection(group, "Стратегия 1: by_name (по имени)")
    
    # Стратегия 2: по возрасту
    group.sort_by(by_age)
    print_collection(group, "Стратегия 2: by_age (по возрасту)")
    
    # Стратегия 3: по оценке (убывание)
    group.sort_by(by_grade, reverse=True)
    print_collection(group, "Стратегия 3: by_grade (по оценке, убывание)")


# ========== СЦЕНАРИЙ 3: Callable-объекты ==========

def scenario_3():
    print_separator("СЦЕНАРИЙ 3: CALLABLE-ОБЪЕКТ КАК СТРАТЕГИЯ")
    
    group = StudentCollection("Тестовая группа")
    group.add(BachelorStudent("Анна Петрова", 19, 2, 4.5, "IT"))
    group.add(BachelorStudent("Иван Сидоров", 18, 1, 3.8, "Экономика"))
    group.add(BachelorStudent("Мария Иванова", 20, 3, 4.9, "IT"))
    
    print_collection(group, "Исходные оценки")
    
    # Применение DiscountStrategy
    discount = DiscountStrategy(10)
    result = group.apply(discount)
    print_collection(result, f"После {discount}")
    
    # Восстанавливаем исходные оценки для следующего теста
    group = create_test_collection()
    
    # Применение BonusStrategy
    bonus = BonusStrategy(0.5)
    result = group.apply(bonus)
    print_collection(result, f"После {bonus}")


# ========== СЦЕНАРИЙ 4: map, filter, sorted ==========

def scenario_4():
    print_separator("СЦЕНАРИЙ 4: map, filter, sorted")
    
    group = create_test_collection()
    students = group.get_all()
    
    # filter - отличники
    high_achievers = list(filter(is_high_achiever, students))
    print("\n--- filter: отличники (балл > 4.5) ---")
    for s in high_achievers:
        print(f"  - {s.name}: {s.grade:.2f}")
    
    # map - имена студентов
    names = list(map(extract_name, students))
    print("\n--- map: имена студентов ---")
    print(f"  {', '.join(names)}")
    
    # sorted + lambda - сортировка по курсу, затем по имени
    sorted_students = sorted(students, key=lambda s: (s.course, s.name))
    print("\n--- sorted: по курсу, затем по имени ---")
    for s in sorted_students:
        print(f"  {s.course} курс: {s.name}")


# ========== СЦЕНАРИЙ 5: Фабрики функций ==========

def scenario_5():
    print_separator("СЦЕНАРИЙ 5: ФАБРИКИ ФУНКЦИЙ")
    
    group = create_test_collection()
    students = group.get_all()
    
    # Создаём фильтр через фабрику
    grade_filter = make_grade_filter(4.5)
    high_achievers = list(filter(grade_filter, students))
    print("\n--- Фильтр студентов с баллом >= 4.5 ---")
    for s in high_achievers:
        print(f"  - {s.name}: {s.grade:.2f}")
    
    # Фильтр по курсу
    course_filter = make_course_filter(1)
    first_course = list(filter(course_filter, students))
    print("\n--- Фильтр студентов 1 курса ---")
    for s in first_course:
        print(f"  - {s.name} (курс {s.course})")
    
    # Фильтр по возрасту
    age_filter = make_age_filter(19, 21)
    age_filtered = list(filter(age_filter, students))
    print("\n--- Фильтр студентов в возрасте 19-21 год ---")
    for s in age_filtered:
        print(f"  - {s.name} ({s.age} лет)")


# ========== СЦЕНАРИЙ 6: Lambda-выражения ==========

def scenario_6():
    print_separator("СЦЕНАРИЙ 6: LAMBDA-ВЫРАЖЕНИЯ")
    
    group = create_test_collection()
    students = group.get_all()
    
    # Сортировка через lambda
    sorted_by_name = sorted(students, key=lambda s: s.name)
    print("\n--- Сортировка по имени (lambda) ---")
    print(f"  {', '.join([s.name for s in sorted_by_name])}")
    
    # Фильтрация через lambda
    high_achievers = list(filter(lambda s: s.grade > 4.5, students))
    print(f"\n--- Фильтрация (балл > 4.5) через lambda ---")
    print(f"  Найдено: {len(high_achievers)} студентов")
    
    # map через lambda
    names = list(map(lambda s: f"{s.name} ({s.grade:.1f})", students))
    print("\n--- Преобразование через map + lambda ---")
    print(f"  {', '.join(names)}")


# ========== ЗАПУСК ==========

if __name__ == "__main__":
    scenario_1()
    scenario_2()
    scenario_3()
    scenario_4()
    scenario_5()
    scenario_6()
    
    print_separator("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")