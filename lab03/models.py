import sys

import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab01'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab02'))

from model import Student


class BachelorStudent(Student):
    
    def __init__(self, name, age, course, grade, specialization, has_practice=False):
        super().__init__(name, age, course, grade)
        self._specialization = specialization
        self._has_practice = has_practice
    
    @property
    def specialization(self):
        return self._specialization
    
    @property
    def has_practice(self):
        return self._has_practice
    
    def complete_practice(self):
        if not self._is_active:
            raise Exception("Отчисленный студент не может пройти практику")
        if self._has_practice:
            return "Практика уже пройдена"
        self._has_practice = True
        return f"{self._name} успешно прошел производственную практику!"
    
    def upgrade_course(self):
        if not self._is_active:
            raise Exception("Нельзя перевести отчисленного студента")
        if self._course >= 4:
            raise Exception("Бакалавр завершил обучение (4 курс). Пора выпускаться!")
        super().upgrade_course()  # Вызываем метод родителя
    
    def __str__(self):
        parent_str = super().__str__()
        practice_status = "Да" if self._has_practice else "Нет"
        return (f"{parent_str}\n"
                f"  Специализация: {self._specialization}\n"
                f"  Практика: {practice_status}")


class MasterStudent(Student):
    
    def __init__(self, name, age, course, grade, research_topic, has_thesis=False):
        super().__init__(name, age, course, grade)
        self._research_topic = research_topic
        self._has_thesis = has_thesis
    
    @property
    def research_topic(self):
        return self._research_topic
    
    @property
    def has_thesis(self):
        return self._has_thesis
    
    def defend_thesis(self):
        if not self._is_active:
            raise Exception("Отчисленный студент не может защищаться")
        if self._has_thesis:
            return "Диссертация уже защищена"
        self._has_thesis = True
        return f"{self._name} блестяще защитил диссертацию на тему '{self._research_topic}'!"
    
    def grant_scholarship(self):
        if not self._is_active:
            return False
        return self._grade > 4.2  # Более строгое требование
    
    def __str__(self):
        parent_str = super().__str__()
        thesis_status = "Да" if self._has_thesis else "Нет"
        return (f"{parent_str}\n"
                f"  Тема исследования: {self._research_topic}\n"
                f"  Диссертация: {thesis_status}")


class PhDStudent(Student):
    """Аспирант — есть область исследований и публикации"""
    
    def __init__(self, name, age, course, grade, research_area, publications=0):
        super().__init__(name, age, course, grade)
        self._research_area = research_area
        self._publications = publications
    
    @property
    def research_area(self):
        return self._research_area
    
    @property
    def publications(self):
        return self._publications
    
    def publish_article(self):
        """Опубликовать научную статью"""
        if not self._is_active:
            raise Exception("Отчисленный аспирант не может публиковаться")
        self._publications += 1
        return f"{self._name} опубликовал {self._publications}-ю статью в области '{self._research_area}'!"
    
    def grant_scholarship(self):
        """Аспиранты получают стипендию всегда (если активны)"""
        if not self._is_active:
            return False
        return True 
    
    def __str__(self):
        parent_str = super().__str__()
        return (f"{parent_str}\n"
                f"  Область исследований: {self._research_area}\n"
                f"  Публикаций: {self._publications}")