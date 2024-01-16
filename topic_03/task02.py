def list_functions_test():
    # Створення списку
    my_list = [1, 2, 3, 4, 5]

    # Додавання елементу до списку
    my_list.append(6)

    # Вивід списку
    print("Список:", my_list)

    # Пошук та вивід індексу елементу
    element_to_find = 3
    index = my_list.index(element_to_find)
    print(f"Індекс елемента {element_to_find}: {index}")

    # Зміна значення елементу за індексом
    index_to_change = 2
    new_value = 10
    my_list[index_to_change] = new_value

    print("Оновлений список:", my_list)

list_functions_test()