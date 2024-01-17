list = [
    {"name": "Bob", "phone": "0631234567", "specialty": "125", "group": "kb-222"},
    {"name": "Emma", "phone": "0631234567", "specialty": "123", "group": "ce-123"},
    {"name": "Jon", "phone": "0631234567", "specialty": "121", "group": "se-211"},
    {"name": "Zak", "phone": "0631234567", "specialty": "112", "group": "st-202"}
]
def printAllList():
    for elem in list:
        strForPrint = "Student name is " + elem["name"] + ", Phone is " + elem["phone"] + \
                      ", Specialty is " + elem["specialty"] + ", Group is " + elem["group"]
        print(strForPrint)

def addNewElement():
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    specialty = input("Please enter specialty: ")
    group = input("Please enter group: ")
    newItem = {"name": name, "phone": phone, "specialty": specialty, "group": group}
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")

def deleteElement():
    name = input("Please enter name to be deleted: ")
    for item in list:
        if name == item["name"]:
            list.remove(item)
            print("Student has been deleted")
            return
    print("Element not found")

def updateElement():
    name = input("Please enter name to be updated: ")
    for item in list:
        if name == item["name"]:
            new_name = input("Enter the new name (or press Enter to keep the same): ")
            if new_name:
                item["name"] = new_name
                list.remove(item)
                insertPosition = 0
                for i, existing_item in enumerate(list):
                    if new_name > existing_item["name"]:
                        insertPosition = i + 1
                    else:
                        break
                list.insert(insertPosition, item)
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

def main():
    while True:
        choice = input("Please specify the action [C create, U update, D delete, P print, X exit]: ")
        if choice.lower() == "c":
            print("New element will be created:")
            addNewElement()
            printAllList()
        elif choice.lower() == "u":
            print("Existing element will be updated:")
            updateElement()
        elif choice.lower() == "d":
            print("Element will be deleted:")
            deleteElement()
        elif choice.lower() == "p":
            print("List will be printed:")
            printAllList()
        elif choice.lower() == "x":
            print("Exiting the program.")
            break
        else:
            print("Wrong choice")

if __name__ == "__main__":
    main()