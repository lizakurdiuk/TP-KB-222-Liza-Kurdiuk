from group import GroupList
from fim import FileManager
from student import Student
import os

def main():
    file_name = input("Enter CSV file name (e.g., lab-03/lab3.csv): ")
    file_path = os.path.join(os.path.dirname(__file__), file_name)

    # Додано перевірку існування файлу та вибір опції
    if os.path.exists(file_path):
        print(f"File '{file_name}' exists. Do you want to use existing data? (Y/N)")
        use_existing = input().lower() == 'y'
    else:
        print(f"File '{file_name}' does not exist. Do you want to create a new file? (Y/N)")
        use_existing = False

    group_list = GroupList()

    # Завантаження чи створення файлу в залежності від вибору користувача
    if use_existing:
        FileManager.load_and_sort_data(file_path, group_list)
    else:
        FileManager.save_data_to_csv(file_path, group_list)

    while True:
        choice = input("Please specify the action [C create, U update, D delete, P print, X exit]: ").lower()

        actions = {
            'c': lambda: group_list.add_student(Student(
                input("Please enter student name: "),
                input("Please enter student phone: "),
                input("Please enter specialty: "),
                input("Please enter group: ")
            )),
            'u': lambda: group_list.update_student(input("Please enter name to be updated: ")),
            'd': lambda: group_list.delete_student(input("Please enter name to be deleted: ")),
            'p': lambda: group_list.print_all_students(),
            'x': lambda: FileManager.save_data_to_csv(file_path, group_list) or exit(0)
        }

        chosen_action = actions.get(choice, lambda: print("Wrong choice"))
        chosen_action()

if __name__ == "__main__":
    main()
    