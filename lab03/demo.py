import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab01'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab02'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab03'))

from model import Student
from collection import StudentGroup 

from models import BachelorStudent, MasterStudent, PhDStudent


def print_separator(title=""):
    print("\n" + "=" * 60)
    if title:
        print(f"  {title}")
        print("=" * 60)


def demo():
    
    print_separator("ЛАБОРАТОРНАЯ РАБОТА №3")
    print("Наследование и полиморфизм")
    print("Базовый класс Student из ЛР-1")
    print("Коллекция StudentGroup из ЛР-2")

    print_separator("1. СОЗДАНИЕ ОБЪЕКТОВ ДОЧЕРНИХ КЛАССОВ")
    
    bachelor = BachelorStudent("Анна Петрова", 19, 2, 4.5, "Программирование")
    master = MasterStudent("Иван Сидоров", 23, 1, 4.8, "Искусственный интеллект")
    phd = PhDStudent("Мария Иванова", 26, 2, 4.9, "Машинное обучение", 3)
    
    print("Бакалавр:")
    print(bachelor)
    print("\nМагистр:")
    print(master)
    print("\nАспирант:")
    print(phd)

    print_separator("2. УНИКАЛЬНЫЕ МЕТОДЫ ДОЧЕРНИХ КЛАССОВ")
    
    print(bachelor.complete_practice())
    print(master.defend_thesis())
    print(phd.publish_article())
 
    print_separator("3. ПОЛИМОРФИЗМ — grant_scholarship()")
    
    students = [bachelor, master, phd]
    for s in students:
        print(f"{s.name} ({type(s).__name__}): стипендия? {s.grant_scholarship()}")

    print_separator("4. ПЕРЕОПРЕДЕЛЕНИЕ upgrade_course()")
    
    bachelor_4 = BachelorStudent("Петр Смирнов", 20, 4, 4.2, "Экономика")
    print(f"Бакалавр на 4 курсе: {bachelor_4.name}")
    try:
        bachelor_4.upgrade_course()
    except Exception as e:
        print(f"  Ошибка: {e}")

    print_separator("5. КОЛЛЕКЦИЯ ИЗ ЛР-2 С РАЗНЫМИ ТИПАМИ СТУДЕНТОВ")
    
    group = StudentGroup("Смешанная группа")
    group.add(bachelor)
    group.add(master)
    group.add(phd)
    
    print(group)
 
    print_separator("6. ФИЛЬТРАЦИЯ ПО ТИПУ (isinstance)")
    
    print("Бакалавры в группе:")
    for s in group:
        if isinstance(s, BachelorStudent):
            print(f"  - {s.name} ({s.specialization})")
    
    print("\nМагистры в группе:")
    for s in group:
        if isinstance(s, MasterStudent):
            print(f"  - {s.name} ({s.research_topic})")
    
    print("\nАспиранты в группе:")
    for s in group:
        if isinstance(s, PhDStudent):
            print(f"  - {s.name} ({s.research_area}, публикаций: {s.publications})")

    print_separator("7. ПОЛИМОРФИЗМ В КОЛЛЕКЦИИ")
    
    print("Стипендия для всех студентов (разное поведение в зависимости от типа):")
    for s in group:
        print(f"  {s.name} ({type(s).__name__}): {s.grant_scholarship()}")

    print_separator("8. ПРОВЕРКА ТИПОВ")
    
    print(f"Анна — бакалавр? {isinstance(bachelor, BachelorStudent)}")
    print(f"Анна — студент? {isinstance(bachelor, Student)}")
    print(f"Анна — магистр? {isinstance(bachelor, MasterStudent)}")
    print(f"Иван — студент? {isinstance(master, Student)}")

    print_separator("9. СРАВНЕНИЕ ПОВЕДЕНИЯ grant_scholarship()")
    
    print("При одинаковой оценке 4.5:")
    test_bachelor = BachelorStudent("Тест Бакалавр", 20, 2, 4.5, "Тест")
    test_master = MasterStudent("Тест Магистр", 22, 1, 4.5, "Тест")
    test_phd = PhDStudent("Тест Аспирант", 25, 2, 4.5, "Тест")
    
    print(f"  Бакалавр (оценка 4.5): {test_bachelor.grant_scholarship()}")
    print(f"  Магистр (оценка 4.5): {test_master.grant_scholarship()} (нужно >4.2)")
    print(f"  Аспирант (оценка 4.5): {test_phd.grant_scholarship()} (всегда)")


if __name__ == "__main__":
    demo()