def find_insert_position(sorted_list, new_element):
    for i, element in enumerate(sorted_list):
        if new_element <= element:
            return i
    return len(sorted_list)

# Приклад використання
sorted_numbers = [1, 3, 5, 7, 9]
new_number = 6
position = find_insert_position(sorted_numbers, new_number)
print(f"Позиція для вставки {new_number} у відсортований список: {position}")
