import csv
from student import Student

class FileManager:
    @staticmethod
    def load_and_sort_data(file_name, group_list):
        try:
            with open(file_name, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student = Student(row["name"], row["phone"], row["specialty"], row["group"])
                    group_list.add_student(student)
            print("Data loaded successfully from", file_name)
        except FileNotFoundError:
            print("File not found. Starting with an empty list.")

    @staticmethod
    def save_data_to_csv(file_name, group_list):
        with open(file_name, 'w', newline='') as file:
            fieldnames = ["name", "phone", "specialty", "group"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for student in group_list.student_list:
                writer.writerow(vars(student))
            print("Data saved successfully to", file_name)
            