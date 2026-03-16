def validate_name(name):
    if not isinstance(name, str):
        raise TypeError(f"Имя должно быть строкой, получен {type(name).__name__}")
    if not name.strip():
        raise ValueError("Имя не может быть пустым или состоять только из пробелов")
    return name

def validate_age(age):
    if not isinstance(age, int):
        raise TypeError(f"Возраст должен быть целым числом, получен {type(age).__name__}")
    if age < 16 or age > 100:
        raise ValueError(f"Возраст должен быть от 16 до 100 лет, получен {age}")
    return age

def validate_grade(grade):
    if not isinstance(grade, (int, float)):
        raise TypeError(f"Оценка должна быть числом, получен {type(grade).__name__}")
    grade_float = float(grade)
    if grade_float < 2.0 or grade_float > 5.0:
        raise ValueError(f"Оценка должна быть от 2.0 до 5.0, получена {grade}")
    return grade_float

def validate_course(course):
    if not isinstance(course, int):
        raise TypeError(f"Курс должен быть целым числом, получен {type(course).__name__}")
    if course < 1 or course > 6:
        raise ValueError(f"Курс должен быть от 1 до 6, получен {course}")
    return course