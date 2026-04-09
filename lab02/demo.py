import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lab01'))

from collection import StudentGroup
from model import Student


def print_separator(title: str = ""):
    print("\n" + "=" * 60)
    if title:
        print(f"  {title}")
        print("=" * 60)


def demo():
    print_separator("ЛАБОРАТОРНАЯ РАБОТА №2")
    print("Класс коллекции StudentGroup")
    print_separator("1. СОЗДАНИЕ СТУДЕНТОВ И ГРУППЫ")
    
    students = [
        Student("Анна Петрова", 19, 2, 4.5),
        Student("Иван Сидоров", 18, 1, 3.8),
        Student("Мария Иванова", 20, 3, 4.9),
        Student("Петр Смирнов", 19, 2, 3.2),
        Student("Елена Козлова", 21, 4, 4.7),
        Student("Дмитрий Новиков", 18, 1, 4.1),
    ]
    
    print("Созданы студенты:")
    for s in students:
        print(f"  - {s.name}, {s.age} лет, курс {s.course}, балл {s.grade:.2f}")
    
    # Создаем группу
    group = StudentGroup("ПИ-202")
    print(f"\nСоздана группа: {group.name}")
    
    # Добавляем студентов
    print("\nДобавление студентов в группу:")
    for student in students:
        success = group.add(student)
        print(f"  Добавлен {student.name}: {'успешно' if success else 'уже есть'}")
    
    # Выводим группу
    print("\n" + str(group))
    
    print_separator("2. УДАЛЕНИЕ ЭЛЕМЕНТА")
    
    to_remove = students[3]
    print(f"Удаляем студента: {to_remove.name}")
    success = group.remove(to_remove)
    print(f"Результат: {'удален' if success else 'не найден'}")
    
    print("\nГруппа после удаления:")
    print(group)
    
    print_separator("3. ПОИСК СТУДЕНТОВ")
    
    print("Поиск по имени 'Анна Петрова':")
    found = group.find_by_name("Анна Петрова")
    for s in found:
        print(f"  Найден: {s.name}, курс {s.course}")
    
    print("\nПоиск студентов 1 курса:")
    found = group.find_by_course(1)
    for s in found:
        print(f"  {s.name} (курс {s.course})")
    
    print("\nПоиск студентов с оценкой выше 4.5:")
    found = group.find_by_grade(min_grade=4.5)
    for s in found:
        print(f"  {s.name} - {s.grade:.2f}")
    
    print_separator("4. ИТЕРАЦИЯ ПО КОЛЛЕКЦИИ")
    
    print(f"В группе {len(group)} студентов:")
    for i, student in enumerate(group, 1):
        print(f"  {i}. {student.name} (курс {student.course})")
    
    print_separator("5. ПРОВЕРКА НА ДУБЛИКАТЫ")
    
    duplicate = Student("Анна Петрова", 19, 2, 5.0)  
    print(f"Пытаемся добавить дубликат: {duplicate.name}")
    success = group.add(duplicate)
    print(f"Результат: {'добавлен' if success else 'НЕ ДОБАВЛЕН (дубликат)'}")
    
    print_separator("6. ИНДЕКСАЦИЯ КОЛЛЕКЦИИ")
    
    print("Доступ по индексу:")
    print(f"  group[0] = {group[0].name}")
    print(f"  group[1] = {group[1].name}")
    print(f"  group[2] = {group[2].name}")
    
    print("\nУдаление по индексу (group.remove_at(2)):")
    removed = group.remove_at(2)
    print(f"  Удален: {removed.name}")
    print(f"  Теперь в группе {len(group)} студентов")
    

    print_separator("7. СОРТИРОВКА")
    
    sort_group = StudentGroup("Для сортировки")
    for s in students[:5]: 
        sort_group.add(s)
    
    print("Исходная группа:")
    print(sort_group)
    
    print("Сортировка по имени (А-Я):")
    sort_group.sort_by_name()
    print(sort_group)
    
    print("Сортировка по оценке (по убыванию):")
    sort_group.sort_by_grade(reverse=True)
    print(sort_group)
    
    print_separator("8. ФИЛЬТРАЦИЯ КОЛЛЕКЦИИ")
    
    students[0].expel()
    
    print("Активные студенты:")
    active_group = group.filter_active()
    print(active_group)
    
    print("Стипендиаты (оценка > 4.0):")
    scholars = group.filter_scholarship()
    print(scholars)
    
    print_separator("9. СРЕЗЫ КОЛЛЕКЦИИ")
    
    print("Срез group[1:4]:")
    slice_group = group[1:4]
    print(slice_group)
    
    print_separator("10. СЦЕНАРИЙ: ПЕРЕВОД СТУДЕНТОВ НА СЛЕДУЮЩИЙ КУРС")
    
    current_group = StudentGroup("ПИ-202 (исходная)")
    for s in students[:4]:
        current_group.add(s)
    
    print("Исходная группа:")
    print(current_group)
    
    print("Переводим всех активных студентов на следующий курс:")
    for student in current_group:
        if student.is_active and student.course < 6:
            print(f"  {student.name}: курс {student.course} -> {student.course + 1}")
            student.course = student.course + 1
    
    print("\nГруппа после перевода:")
    print(current_group)
    
    print_separator("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")


if __name__ == "__main__":
    demo()