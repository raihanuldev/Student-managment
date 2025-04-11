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
        
        # push student at db
        StudentDatabase.add_student(self)

    # enroll srudenrts
    def enroll_student(self):
        if not self.__is_enrolled:
            self.__is_enrolled = True
            print(f"✅ Student {self.__name} is now enrolled.")
        else:
            print(f"⚠️ Student {self.__name} is already enrolled.")
    
# Manual creation
student1 = Student("101", "Raihan Shorif", "CSE", True)
student2 = Student("102", "Shila Song", "EEE", False)
student3 = Student("103", "John Doe", "BBA", True)

