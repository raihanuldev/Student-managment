# Task 1: Create the StudentDatabase class
class StudentDatabase:
    _student_list = []  # Initially, the student list is empty

    @classmethod
    def add_student(cls, student):
        """Add student to the student list"""
        cls._student_list.append(student)

    @classmethod
    def view_all_students(cls):
        """View all students in the database"""
        if not cls._student_list:
            print("⚠️ No students in the database.")
            return
        print("\n-- All Students --")
        for student in cls._student_list:
            student.view_student_info()

# Task 2: Create the Student class
class Student:
    def __init__(self, student_id, name, department, is_enrolled=False):
        """Initialize a new student object with the given details."""
        self._student_id = student_id  # Private attribute
        self._name = name  # Private attribute
        self._department = department  # Private attribute
        self._is_enrolled = is_enrolled  # Private attribute

        # Add student to the database
        StudentDatabase.add_student(self)

    # Task 4: Enroll student method (which means adding new student)
    def enroll_student(self):
        """Enroll the student if not already enrolled."""
        if not self._is_enrolled:
            self._is_enrolled = True
            print(f"✅ Student {self._name} is now enrolled.")
        else:
            print(f"⚠️ Student {self._name} is already enrolled.")

    # Task 5: Drop student method
    def drop_student(self):
        """Drop the student if they are enrolled."""
        if self._is_enrolled:
            self._is_enrolled = False
            print(f"🛑 Student {self._name} has been dropped.")
        else:
            print(f"⚠️ Student {self._name} is already not enrolled.")

    # Task 6: View student information
    def view_student_info(self):
        """View the student's information."""
        enrollment_status = "Enrolled" if self._is_enrolled else "Not Enrolled"
        print(f"Student ID: {self._student_id}")
        print(f"Name: {self._name}")
        print(f"Department: {self._department}")
        print(f"Enrollment Status: {enrollment_status}")
        print("-" * 30)

# Task 7: Menu System
def menu():
    while True:
        print("\n-- Menu --")
        print("1. View All Students")
        print("2. Add New Student")
        print("3. Drop Student")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            # View all students
            StudentDatabase.view_all_students()

        elif choice == "2":
            # Add new student: Ask for student details and add to the system
            student_id = input("Enter Student ID to add: ")
            # Check if the student already exists in the database
            existing_student = next((s for s in StudentDatabase._student_list if s._student_id == student_id), None)
            if existing_student:
                print("⚠️ Student with this ID already exists!")
            else:
                # Get additional student information
                name = input("Enter Student Name: ")
                department = input("Enter Department: ")
                # Create a new student and add to the database
                new_student = Student(student_id, name, department)
                print(f"✅ New student {name} successfully added!")

        elif choice == "3":
            # Drop student: Ask for student ID and drop if found
            student_id = input("Enter Student ID to drop: ")
            student = next((s for s in StudentDatabase._student_list if s._student_id == student_id), None)
            if student:
                student.drop_student()
            else:
                print("⚠️ Student not found!")

        elif choice == "4":
            # Exit the program
            print("Exiting the program...")
            break

        else:
            print("⚠️ Invalid choice! Please try again.")

# Run the menu system to interact with the program
menu()
