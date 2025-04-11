# Task-1-> create a student db;

class StudentDatabase:
    _student_list = [];  #eita private calss er attribute
    
    @classmethod
    def add_student(cls,student):
        cls._student_list.append(student) 
        