operation = input("Введіть операцію (+, -, *, /): ")
num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))

# Використання оператора match для виконання операції
match operation:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num1 * num2
    case '/':
        # Перевірка на ділення на нуль
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Помилка: ділення на нуль"
    case _:
        result = "Неправильна операція"

print("Результат:", result)