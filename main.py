# Task 1: StudentDatabase class
class StudentDatabase:
    _student_list = []  # Private class attribute

    @classmethod
    def add_student(cls, student):
        cls._student_list.append(student)

# Task 2-5: Student class with required methods
class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self._student_id = student_id
        self._name = name
        self._department = department
        self._is_enrolled = is_enrolled

        StudentDatabase.add_student(self)

    # Task 4: Enroll student
    def enroll_student(self):
        if not self._is_enrolled:
            self._is_enrolled = True
            print(f"✅ Student {self._name} is now enrolled.")
        else:
            print(f"⚠️ Student {self._name} is already enrolled.")

    # Task 5: Drop student
    def drop_student(self):
        if self._is_enrolled:
            self._is_enrolled = False
            print(f"🛑 Student {self._name} has been dropped.")
        else:
            print(f"⚠️ Student {self._name} is already not enrolled.")


# Task 3: Manual
student1 = Student("101", "Raihan Shorif", "CSE", True)
student2 = Student("102", "Shila Song", "EEE", False)
student3 = Student("103", "John Doe", "BBA", True)


print("\n-- Test Enroll/Drop --")
student2.enroll_student()
student2.enroll_student()  

student3.drop_student()    
student3.drop_student()   
