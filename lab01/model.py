import validate

class Student:
    university_name = "МИСИС"
    def __init__(self, name, age, course, initial_grade=3.0):
        print(">> Вызван __init__: Создаем нового студента!")
        self._name = validate.validate_name(name)
        self._age = validate.validate_age(age)
        self._course = validate.validate_course(course)
        self._grade = validate.validate_grade(initial_grade)
        self._is_active = True 

    def __str__(self):
        status = "активен" if self._is_active else "не активен (отчислен)"
        return (f"Студент: {self._name}\n"
                f"  Возраст: {self._age}, Курс: {self._course}\n"
                f"  Средний балл: {self._grade:.2f}\n"
                f"  Статус: {status}\n"
                f"  Вуз: {Student.university_name}") 

    def __repr__(self):
        return (f"Student(name='{self._name}', age={self._age}, "
                f"course={self._course}, grade={self._grade})")

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return (self._name == other._name and
                self._age == other._age and
                self._course == other._course)

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, new_course):
        print(f">> Попытка перевести студента на курс {new_course}")
        if not self._is_active:
            raise Exception("Нельзя изменить курс для отчисленного студента!")
        self._course = validate.validate_course(new_course)
        print(">> Курс успешно изменен!")

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, new_grade):
        print(f">> Попытка выставить новую оценку: {new_grade}")
        if not self._is_active:
            raise Exception("Нельзя изменить оценку для отчисленного студента!")
        self._grade = validate.validate_grade(new_grade)
        print(">> Оценка успешно обновлена!")

    @property
    def is_active(self):
        return self._is_active

    def expel(self):
        if not self._is_active:
            print("Студент уже отчислен.")
            return
        print(f">> Студент {self._name} отчислен!")
        self._is_active = False

    def upgrade_course(self):
        if not self._is_active:
            raise Exception("Нельзя перевести на следующий курс отчисленного студента!")
        if self._course >= 6:
            raise Exception("Студент уже на последнем (6) курсе!")
        self.course = self._course + 1
        print(f"Поздравляем! {self._name} переведен на {self._course} курс.")

    def grant_scholarship(self):
        if not self._is_active:
            return False
        return self._grade > 4.0