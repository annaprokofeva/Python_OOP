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

# lab01/validate.py (добавить в конец файла)

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