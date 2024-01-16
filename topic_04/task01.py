def calculator():
    try:
        num1 = float(input("Введіть перше число: "))
        operator = input("Введіть операцію (+, -, *, /): ")
        num2 = float(input("Введіть друге число: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        else:
            raise ValueError("Непідтримувана операція")

        print("Результат: ", result)

    except ValueError as ve:
        print(f"Помилка: {ve}")
    except ZeroDivisionError:
        print("Помилка: Ділення на нуль")
    except Exception as e:
        print(f"Невідома помилка: {e}")

calculator()