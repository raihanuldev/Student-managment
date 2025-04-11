# Task-1-> create a student db;

class StudentDatabase:
    _student_list = [];  #eita private calss er attribute
    
    @classmethod
    def add_student(cls,student):
        cls._student_list.append(student) 
        
# create studebnt class
class Student:
    def __init__(self,student_id,name,department,is_enrolled):
        self.__student_id = student_id
        self._name = name
        self._department = department
        self._is_enrolled = is_enrolled
        