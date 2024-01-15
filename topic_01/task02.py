# Рядок для тестування
test_string = "Python is awesome!"

# Довжина рядка
length = len(test_string)
print("Довжина рядка:", length)

# Рядок великими літерами
uppercase_string = test_string.upper()
print("Рядок у великих літерах:", uppercase_string)

# Рядок малими літерами
lowercase_string = test_string.lower()
print("Рядок у малих літерах:", lowercase_string)

# Чи починається рядок з певного префіксу
prefix = "Python"
starts_with_python = test_string.startswith(prefix)
print("Рядок починається з 'Python':", starts_with_python)

# Позицію підстроки у рядку
substring = "is"
position = test_string.find(substring)
print(f"Позиція підстроки '{substring}': {position}")