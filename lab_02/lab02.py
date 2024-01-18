import csv
import os

def load_and_sort_data(file_name):
    try:
        with open(file_name, 'r') as file:
            reader = csv.DictReader(file)
            student_list = sorted([row for row in reader], key=lambda x: x['name'])
        print("Data loaded successfully from", file_name)
        return student_list
    except FileNotFoundError:
        print("File not found. Starting with an empty list.")
        return []

def save_data_to_csv(file_name, student_list):
    with open(file_name, 'w', newline='') as file:
        fieldnames = ["name", "phone", "specialty", "group"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(student_list)
        print("Data saved successfully to", file_name)

def print_all_list(student_list):
    for elem in student_list:
        str_for_print = "Student name is " + elem["name"] + ", Phone is " + elem["phone"] + \
                        ", Specialty is " + elem["specialty"] + ", Group is " + elem["group"]
        print(str_for_print)

def add_new_element(student_list):
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    specialty = input("Please enter specialty: ")
    group = input("Please enter group: ")
    new_item = {"name": name, "phone": phone, "specialty": specialty, "group": group}
    insert_position = 0
    for i, item in enumerate(student_list):
        if name > item["name"]:
            insert_position = i + 1
        else:
            break
    student_list.insert(insert_position, new_item)
    print("New element has been added")

def update_element(student_list):
    name = input("Please enter name to be updated: ")
    for item in student_list:
        if name == item["name"]:
            new_name = input("Enter the new name (or press Enter to keep the same): ")
            if new_name:
                item["name"] = new_name
                student_list.remove(item)
                insert_position = 0
                for i, existing_item in enumerate(student_list):
                    if new_name > existing_item["name"]:
                        insert_position = i + 1
                    else:
                        break
                student_list.insert(insert_position, item)
            print("Select field to update:")
            print("1. Phone")
            print("2. Specialty")
            print("3. Group")
            choice = input("Enter your choice (1/2/3): ")
            if choice == "1":
                item["phone"] = input("Enter new phone number: ")
            elif choice == "2":
                item["specialty"] = input("Enter new specialty value: ")
            elif choice == "3":
                item["group"] = input("Enter new group value: ")
            else:
                print("Invalid choice")
            print("Student information has been updated")
            return
    print("Student not found")

def delete_element(student_list):
    name = input("Please enter name to be deleted: ")
    for item in student_list:
        if name == item["name"]:
            student_list.remove(item)
            print("Student has been deleted")
            return
    print("Element not found")


def main():
    file_name = input("Enter CSV file name (e.g., lab-02/lab2.csv): ")
    file_path = os.path.join(os.path.dirname(__file__), file_name)

    student_list = load_and_sort_data(file_path)
    
    while True:
        choice = input("Please specify the action [C create, U update, D delete, P print, X exit]: ").lower()

        actions = {
            'c': lambda: add_new_element(student_list),
            'u': lambda: update_element(student_list),
            'd': lambda: delete_element(student_list),
            'p': lambda: print_all_list(student_list),
            'x': lambda: save_data_to_csv(file_name, student_list) or exit(0)
        }

        chosen_action = actions.get(choice, lambda: print("Wrong choice"))
        chosen_action()

if __name__ == "__main__":
    main()
    