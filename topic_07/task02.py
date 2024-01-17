class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def load_objects_from_file(filename):
    objects = []
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    name, age = parts
                    objects.append(MyClass(name, int(age)))
    except FileNotFoundError:
        print("error.")
        with open(filename, 'w') as file:
            pass
    return objects

def save_objects_to_file(filename, objects):
    with open(filename, 'w') as file:
        for obj in objects:
            file.write(f"{obj.name},{obj.age}\n")

def main():
    filename = "_input06.txt"
    objects = load_objects_from_file(filename)

    while True:
        print("Make a choice:")
        print("1. List objects")
        print("2. Add a new object")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            sorted_objects = sorted(objects, key=lambda x: x.age)  
            for obj in sorted_objects:
                print(f"{obj.name}, {obj.age}")

        elif choice == '2':
            name = input("Enter the name: ")
            age = int(input("Enter the age: "))
            new_object = MyClass(name, age)
            objects.append(new_object)
            save_objects_to_file(filename, objects)

        elif choice == '3':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()