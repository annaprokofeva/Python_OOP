from model import Student

print("="*50)
print("ДЕМОНСТРАЦИЯ РАБОТЫ КЛАССА STUDENT")
print("="*50)

print("\n--- 1. Создание студента ---")
try:
    student_1 = Student("Анна Петрова", 19, 2, 4.5)
    print("Успешно создан:")
    print(student_1)
except Exception as e:
    print(f"Ошибка при создании: {e}")

print("\n" + "-"*50)

print("\n--- 2. Демонстрация __str__ и __repr__ ---")
student_2 = Student("Иван Сидоров", 18, 1)
print("Вызов print(student_2) -> __str__:")
print(student_2)
print("\nВызов repr(student_2) -> __repr__:")
print(repr(student_2))

print("\n" + "-"*50)

print("\n--- 3. Сравнение студентов (__eq__) ---")
student_3 = Student("Петр Иванов", 20, 3, 3.8)
student_4 = Student("Петр Иванов", 20, 3, 4.9)
student_5 = Student("Анна Петрова", 19, 2, 4.5)

print(f"student_3 == student_4? {'Да' if student_3 == student_4 else 'Нет'}")
print(f"(Ожидаем ДА, т.к. имя, возраст и курс совпадают)")
print(f"student_3 == student_5? {'Да' if student_3 == student_5 else 'Нет'}")
print(f"(Ожидаем НЕТ)")

print("\n" + "-"*50)

print("\n--- 4. Обработка ошибок при создании ---")
try:
    print("Пытаемся создать студента с возрастом 15 лет...")
    student_bad = Student("Олег", 15, 1)
except Exception as e:
    print(f"Перехвачена ошибка: {e}")

try:
    print("\nПытаемся создать студента с именем-пустышкой...")
    student_bad = Student("   ", 20, 2)
except Exception as e:
    print(f"Перехвачена ошибка: {e}")

print("\n" + "-"*50)

print("\n--- 5. Свойства и атрибут класса ---")
student_6 = Student("Мария", 20, 3, 4.2)
print("Создан студент Мария:")
print(f"Имя (геттер): {student_6.name}")
print(f"Курс (геттер): {student_6.course}")
print(f"Атрибут класса University: {Student.university_name}")
print(f"Доступ через экземпляр: {student_6.university_name}")

try:
    student_6.course = 4
    print(f"Новый курс Марии: {student_6.course}")
except Exception as e:
    print(f"Ошибка: {e}")

try:
    print("\nПытаемся перевести Марию на 7 курс...")
    student_6.course = 7
except Exception as e:
    print(f"Перехвачена ошибка: {e}")

print("\n" + "-"*50)

print("\n--- 6. Логические состояния и поведение ---")
student_7 = Student("Дмитрий", 18, 1, 3.5)
print("Создан студент Дмитрий:")
print(student_7)

print(f"\nМожет ли {student_7.name} получить стипендию? {'Да' if student_7.grant_scholarship() else 'Нет'}")

student_7.expel()
print("\nПосле отчисления:")
print(student_7)

try:
    print("\nПытаемся перевести отчисленного студента...")
    student_7.course = 2
except Exception as e:
    print(f"Перехвачена ошибка: {e}")

print("\n--- Работа с активным студентом ---")
student_8 = Student("Елена", 19, 5, 4.8)
print(student_8)
print(f"Может ли {student_8.name} получить стипендию? {'Да' if student_8.grant_scholarship() else 'Нет'}")

try:
    student_8.upgrade_course()
    student_8.upgrade_course()
except Exception as e:
    print(f"Перехвачена ошибка: {e}")

print("\n" + "="*50)
print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
print("="*50)