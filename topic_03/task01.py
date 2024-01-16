def calculator():
    while True:
        # Запит на введення чисел та операції
        num1 = float(input("Введіть перше число: "))
        operation = input("Введіть операцію (+, -, *, /): ")
        num2 = float(input("Введіть друге число: "))
        
        # Виконання операції
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
                print("Помилка: ділення на нуль")
                continue
        else:
            print("Неправильна операція")
            continue
        
        print("Результат:", result)

        # Питання користувачу про продовження роботи
        continue_calculation = input("Бажаєте продовжити обчислення? (Так/Ні): ")
        if continue_calculation.lower() != 'так':
            break

# Виклик функції
calculator()