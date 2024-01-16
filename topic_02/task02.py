operation = input("Введіть операцію (+, -, *, /): ")
num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))

# Умовний перехід для виконання операції
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    # Перевірка на ділення на нуль
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Помилка: ділення на нуль"
else:
    result = "Неправильна операція"

# Виведення результату
print("Результат:", result)