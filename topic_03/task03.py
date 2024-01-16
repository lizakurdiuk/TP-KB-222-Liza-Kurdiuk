def dictionary_functions_test():
    # Створення словника
    my_dict = {'name': 'Liza', 'age': 19, 'city': 'Chernigiv'}

    my_dict['gender'] = 'Male'

    # Вивід словника
    print("Словник:", my_dict)

    # Пошук та вивід значення за ключем
    key_to_find = 'age'
    value = my_dict.get(key_to_find, 'Ключ не знайдено')
    print(f"{key_to_find}: {value}")

    # Видалення елемента за ключем
    key_to_remove = 'city'
    if key_to_remove in my_dict:
        del my_dict[key_to_remove]

    # Вивід оновленого словника
    print("Оновлений словник:", my_dict)

dictionary_functions_test()