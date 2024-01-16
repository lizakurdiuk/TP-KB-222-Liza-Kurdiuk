def division(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        print("Помилка: Ділення на нуль")
        return None

# Виклик функції
result = division(10, 0)
if result is not None:
    print("Результат ділення:", result)