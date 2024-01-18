# grouplist.py

from student import Student

class GroupList:
    def __init__(self):
        self.student_list = []

    def add_student(self, student):
        self.student_list.append(student)
        self.student_list.sort(key=lambda x: x.name)  # Sort the list by student names

    def delete_student(self, name):
        for student in self.student_list:
            if name == student.name:
                self.student_list.remove(student)
                return
        print("Student not found")

    def update_student(self, name, **kwargs):
        for student in self.student_list:
            if name == student.name:
                print("Select field to update:")
                print("1. Name")
                print("2. Phone")
                print("3. Specialty")
                print("4. Group")
                choice = input("Enter your choice (1/2/3/4): ")

                if choice == "1":
                    new_name = kwargs.get("new_name", input("Enter new name: "))
                    student.name = new_name
                elif choice == "2":
                    student.phone = kwargs.get("new_phone", input("Enter new phone number: "))
                elif choice == "3":
                    student.specialty = kwargs.get("new_specialty", input("Enter new specialty value: "))
                elif choice == "4":
                    student.group = kwargs.get("new_group", input("Enter new group value: "))
                else:
                    print("Invalid choice")
                self.student_list.sort(key=lambda x: x.name)
                print("Student information has been updated")
                return

        print("Student not found")

    def print_all_students(self):
        for student in self.student_list:
            print(f"Student name is {student.name}, Phone is {student.phone}, "
                  f"Specialty is {student.specialty}, Group is {student.group}")
            